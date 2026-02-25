[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$TrackManifest,

    [Parameter(Mandatory = $true)]
    [string]$BackgroundImage,

    [Parameter(Mandatory = $true)]
    [string]$OutputVideo,

    [double]$CrossfadeSec = 5,
    [double]$TargetLufs = -14,
    [int]$Width = 1920,
    [int]$Height = 1080,
    [int]$Fps = 30,
    [int]$Crf = 18,
    [switch]$AddKenBurns,
    [switch]$KeepTemp
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Require-Command {
    param([string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command not found: $Name"
    }
}

function Resolve-PathSafe {
    param(
        [string]$Path,
        [string]$RelativeBase
    )
    if ([System.IO.Path]::IsPathRooted($Path)) {
        return [System.IO.Path]::GetFullPath($Path)
    }
    return [System.IO.Path]::GetFullPath((Join-Path $RelativeBase $Path))
}

function Invoke-FfmpegChecked {
    param([string[]]$Args)
    & ffmpeg @Args
    if ($LASTEXITCODE -ne 0) {
        throw "ffmpeg failed with exit code $LASTEXITCODE"
    }
}

Require-Command -Name "ffmpeg"

$manifestFull = [System.IO.Path]::GetFullPath($TrackManifest)
if (-not (Test-Path -LiteralPath $manifestFull)) {
    throw "Track manifest not found: $manifestFull"
}

$manifestDir = Split-Path -Parent $manifestFull
$rows = Import-Csv -Path $manifestFull
if (-not $rows -or $rows.Count -eq 0) {
    throw "Manifest is empty: $manifestFull"
}

$tracks = @()
foreach ($row in $rows) {
    if (-not $row.file) {
        throw "Manifest row missing 'file' value."
    }
    $trackPath = Resolve-PathSafe -Path $row.file -RelativeBase $manifestDir
    if (-not (Test-Path -LiteralPath $trackPath)) {
        throw "Track file not found: $trackPath"
    }
    $tracks += $trackPath
}

$bgFull = [System.IO.Path]::GetFullPath($BackgroundImage)
if (-not (Test-Path -LiteralPath $bgFull)) {
    throw "Background image not found: $bgFull"
}

$outputFull = [System.IO.Path]::GetFullPath($OutputVideo)
$outputDir = Split-Path -Parent $outputFull
if (-not (Test-Path -LiteralPath $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$tempDir = Join-Path $outputDir ("_tmp_" + [Guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $tempDir -Force | Out-Null

try {
    $mergedWav = Join-Path $tempDir "album_merged.wav"
    $normM4a = Join-Path $tempDir "album_norm.m4a"

    $inputArgs = @()
    for ($i = 0; $i -lt $tracks.Count; $i++) {
        $inputArgs += "-i"
        $inputArgs += $tracks[$i]
    }

    $prepFilters = @()
    for ($i = 0; $i -lt $tracks.Count; $i++) {
        $prepFilters += "[" + $i + ":a]aresample=48000,asetpts=N/SR/TB[a" + $i + "]"
    }

    $chainFilters = @()
    if ($tracks.Count -eq 1) {
        $finalLabel = "[a0]"
    }
    else {
        $chainFilters += "[a0][a1]acrossfade=d=$CrossfadeSec:c1=tri:c2=tri[xf1]"
        for ($i = 2; $i -lt $tracks.Count; $i++) {
            $prev = "xf" + ($i - 1)
            $next = "xf" + $i
            $chainFilters += "[" + $prev + "][a" + $i + "]acrossfade=d=$CrossfadeSec:c1=tri:c2=tri[" + $next + "]"
        }
        $finalLabel = "[xf" + ($tracks.Count - 1) + "]"
    }

    $filterComplex = ($prepFilters + $chainFilters) -join ";"
    $mergeArgs = @(
        "-y"
    ) + $inputArgs + @(
        "-filter_complex", $filterComplex,
        "-map", $finalLabel,
        "-c:a", "pcm_s16le",
        $mergedWav
    )
    Invoke-FfmpegChecked -Args $mergeArgs

    $normArgs = @(
        "-y",
        "-i", $mergedWav,
        "-af", "loudnorm=I=$TargetLufs:TP=-1.5:LRA=11",
        "-ar", "48000",
        "-c:a", "aac",
        "-b:a", "320k",
        $normM4a
    )
    Invoke-FfmpegChecked -Args $normArgs

    $videoFilter = if ($AddKenBurns) {
        "zoompan=z='min(zoom+0.00008,1.12)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)',fps=$Fps,scale=$Width:$Height,format=yuv420p"
    }
    else {
        "fps=$Fps,scale=$Width:$Height,format=yuv420p"
    }

    $videoArgs = @(
        "-y",
        "-loop", "1",
        "-framerate", $Fps.ToString(),
        "-i", $bgFull,
        "-i", $normM4a,
        "-vf", $videoFilter,
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", $Crf.ToString(),
        "-c:a", "aac",
        "-b:a", "320k",
        "-shortest",
        "-movflags", "+faststart",
        $outputFull
    )
    Invoke-FfmpegChecked -Args $videoArgs

    Write-Host "Video render complete: $outputFull"
}
finally {
    if (-not $KeepTemp -and (Test-Path -LiteralPath $tempDir)) {
        Remove-Item -LiteralPath $tempDir -Recurse -Force
    }
}
