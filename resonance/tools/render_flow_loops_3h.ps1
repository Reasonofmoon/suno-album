[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$LoopDir,

    [Parameter(Mandatory = $true)]
    [string]$OutputVideo,

    [string]$AudioPath,
    [int]$TargetDurationSec = 10800,
    [int]$SegmentSec = 30,
    [int]$Width = 1920,
    [int]$Height = 1080,
    [int]$Fps = 30,
    [int]$Crf = 18,
    [switch]$Shuffle,
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

function Get-FullPath {
    param([string]$Path)
    return [System.IO.Path]::GetFullPath($Path)
}

function Invoke-FfmpegChecked {
    param([string[]]$Args)
    & ffmpeg @Args
    if ($LASTEXITCODE -ne 0) {
        throw "ffmpeg failed with exit code $LASTEXITCODE"
    }
}

Require-Command -Name "ffmpeg"
Require-Command -Name "ffprobe"

if ($TargetDurationSec -lt 300) {
    throw "TargetDurationSec must be >= 300."
}
if ($SegmentSec -lt 5) {
    throw "SegmentSec must be >= 5."
}

$loopDirFull = Get-FullPath -Path $LoopDir
if (-not (Test-Path -LiteralPath $loopDirFull)) {
    throw "LoopDir not found: $loopDirFull"
}

$outputFull = Get-FullPath -Path $OutputVideo
$outputDir = Split-Path -Parent $outputFull
if (-not (Test-Path -LiteralPath $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$audioFull = $null
if ($AudioPath) {
    $audioFull = Get-FullPath -Path $AudioPath
    if (-not (Test-Path -LiteralPath $audioFull)) {
        throw "AudioPath not found: $audioFull"
    }
}

$allowedExt = @(".mp4", ".mov", ".mkv", ".webm")
$clips = Get-ChildItem -Path $loopDirFull -File |
    Where-Object { $allowedExt -contains $_.Extension.ToLowerInvariant() } |
    Sort-Object Name

if (-not $clips -or $clips.Count -eq 0) {
    throw "No loop clips found in: $loopDirFull"
}

if ($Shuffle) {
    $clips = $clips | Sort-Object { Get-Random }
}

$tempDir = Join-Path $outputDir ("_tmp_flow_loops_" + [Guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $tempDir -Force | Out-Null

try {
    Write-Host "Preparing fixed-length loop segments..."
    $segmentFiles = @()
    $idx = 0
    foreach ($clip in $clips) {
        $idx += 1
        $segmentPath = Join-Path $tempDir ("segment_{0:D2}.mp4" -f $idx)

        $videoFilter = "fps=$Fps,scale=$Width:$Height:force_original_aspect_ratio=cover,crop=$Width:$Height,format=yuv420p"
        $args = @(
            "-y",
            "-stream_loop", "-1",
            "-i", $clip.FullName,
            "-t", $SegmentSec.ToString(),
            "-an",
            "-vf", $videoFilter,
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", $Crf.ToString(),
            "-pix_fmt", "yuv420p",
            $segmentPath
        )

        Invoke-FfmpegChecked -Args $args
        $segmentFiles += $segmentPath
    }

    $segmentCount = [int][Math]::Ceiling($TargetDurationSec / [double]$SegmentSec) + 1
    $concatListPath = Join-Path $tempDir "concat_list.txt"
    $concatLines = @()
    for ($i = 0; $i -lt $segmentCount; $i++) {
        $segment = $segmentFiles[$i % $segmentFiles.Count]
        $safePath = $segment.Replace("'", "'\''")
        $concatLines += "file '$safePath'"
    }
    Set-Content -Path $concatListPath -Value ($concatLines -join "`n") -Encoding UTF8

    $concatVideo = Join-Path $tempDir "video_concat.mp4"
    Write-Host "Concatenating segment timeline..."
    Invoke-FfmpegChecked -Args @(
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", $concatListPath,
        "-c", "copy",
        $concatVideo
    )

    if ($audioFull) {
        Write-Host "Muxing looped audio and trimming to target duration..."
        Invoke-FfmpegChecked -Args @(
            "-y",
            "-i", $concatVideo,
            "-stream_loop", "-1",
            "-i", $audioFull,
            "-t", $TargetDurationSec.ToString(),
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "320k",
            "-ar", "48000",
            "-movflags", "+faststart",
            $outputFull
        )
    }
    else {
        Write-Host "Exporting silent loop timeline and trimming to target duration..."
        Invoke-FfmpegChecked -Args @(
            "-y",
            "-i", $concatVideo,
            "-t", $TargetDurationSec.ToString(),
            "-c", "copy",
            "-movflags", "+faststart",
            $outputFull
        )
    }

    $duration = & ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $outputFull
    Write-Host ("Completed: {0}" -f $outputFull)
    Write-Host ("Duration(sec): {0}" -f $duration.Trim())
}
finally {
    if (-not $KeepTemp -and (Test-Path -LiteralPath $tempDir)) {
        Remove-Item -LiteralPath $tempDir -Recurse -Force
    }
}
