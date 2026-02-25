[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern("^[A-Za-z0-9_]+$")]
    [string]$AlbumId,

    [Parameter(Mandatory = $true)]
    [ValidatePattern("^[a-z0-9_]+$")]
    [string]$Theme,

    [Parameter(Mandatory = $true)]
    [string]$Title,

    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$scriptRoot = Split-Path -Parent $PSCommandPath
$resonanceRoot = Split-Path -Parent $scriptRoot

function Ensure-Directory {
    param([string]$Path)
    if (Test-Path -LiteralPath $Path) {
        return
    }
    if ($DryRun) {
        Write-Host "[DRYRUN] mkdir $Path"
        return
    }
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
}

function Write-TextFile {
    param(
        [string]$Path,
        [string]$Content
    )
    if ($DryRun) {
        Write-Host "[DRYRUN] write $Path"
        return
    }
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    Set-Content -Path $Path -Value $Content -Encoding UTF8
}

function Create-FromTemplateIfMissing {
    param(
        [string]$TemplatePath,
        [string]$TargetPath,
        [hashtable]$Replacements
    )
    if (Test-Path -LiteralPath $TargetPath) {
        return
    }
    $content = Get-Content -Path $TemplatePath -Raw
    foreach ($key in $Replacements.Keys) {
        $content = $content.Replace($key, $Replacements[$key])
    }
    Write-TextFile -Path $TargetPath -Content $content
}

function Get-KstTimestamp {
    $tz = [System.TimeZoneInfo]::FindSystemTimeZoneById("Korea Standard Time")
    $kstNow = [System.TimeZoneInfo]::ConvertTimeFromUtc([DateTime]::UtcNow, $tz)
    return $kstNow.ToString("yyyy-MM-dd HH:mm")
}

$audioAlbumDir = Join-Path $resonanceRoot ("composer\audio\" + $AlbumId)
Ensure-Directory -Path $audioAlbumDir
Ensure-Directory -Path (Join-Path $resonanceRoot ("publisher\videos\" + $AlbumId))
Ensure-Directory -Path (Join-Path $resonanceRoot ("publisher\thumbnails\" + $AlbumId))

$themeTemplate = Join-Path $resonanceRoot "composer\themes\composer_theme_TEMPLATE.md"
$promptTemplate = Join-Path $resonanceRoot "composer\prompts\composer_prompts_TEMPLATE.md"
$qaTemplate = Join-Path $resonanceRoot "composer\qa\composer_qa_TEMPLATE.md"
$videoTemplate = Join-Path $resonanceRoot "publisher\templates\publisher_video_TEMPLATE.md"
$seoTemplate = Join-Path $resonanceRoot "publisher\templates\publisher_seo_TEMPLATE.md"

$themeDoc = Join-Path $resonanceRoot ("composer\themes\composer_theme_" + $Theme + ".md")
$promptDoc = Join-Path $resonanceRoot ("composer\prompts\composer_prompts_" + $AlbumId + ".md")
$qaDoc = Join-Path $resonanceRoot ("composer\qa\composer_qa_" + $AlbumId + ".md")
$videoDoc = Join-Path $resonanceRoot ("publisher\metadata\publisher_video_" + $AlbumId + ".md")
$seoDoc = Join-Path $resonanceRoot ("publisher\metadata\publisher_seo_" + $AlbumId + ".md")

Create-FromTemplateIfMissing -TemplatePath $themeTemplate -TargetPath $themeDoc -Replacements @{ "{theme_name}" = $Theme }
Create-FromTemplateIfMissing -TemplatePath $promptTemplate -TargetPath $promptDoc -Replacements @{ "{album_id}" = $AlbumId }
Create-FromTemplateIfMissing -TemplatePath $qaTemplate -TargetPath $qaDoc -Replacements @{ "{album_id}" = $AlbumId }
Create-FromTemplateIfMissing -TemplatePath $videoTemplate -TargetPath $videoDoc -Replacements @{ "{album_id}" = $AlbumId }
Create-FromTemplateIfMissing -TemplatePath $seoTemplate -TargetPath $seoDoc -Replacements @{ "{album_id}" = $AlbumId }

$manifestPath = Join-Path $audioAlbumDir "manifest.csv"
if (-not (Test-Path -LiteralPath $manifestPath)) {
    $manifest = @"
order,title,file,duration_sec
1,Track 01,track01.mp3,480
"@
    Write-TextFile -Path $manifestPath -Content $manifest
}

$registryPath = Join-Path $resonanceRoot "shared\album_registry.yaml"
$registry = Get-Content -Path $registryPath -Raw
$albumRegex = [regex]::Escape($AlbumId)
$existingAlbumPattern = "(?m)^\s*-\s*id:\s*`"" + $albumRegex + "`"\s*$"
if ($registry -notmatch $existingAlbumPattern) {
    $newEntry = @"
  - id: "$AlbumId"
    theme: "$Theme"
    title: "$Title"
    status: "draft"
    tracks: 0
    duration: "00:00:00"
    publish_date: null
    youtube_url: null
    analytics: null
    composer_qa_score: null
    notes: null
"@
    if ($registry -match "(?m)^albums:\s*\[\s*\]\s*$") {
        $updated = $registry -replace "(?m)^albums:\s*\[\s*\]\s*$", ("albums:`n" + $newEntry.TrimEnd())
    }
    else {
        $updated = $registry.TrimEnd() + "`n" + $newEntry
    }
    Write-TextFile -Path $registryPath -Content $updated
}

$syncPath = Join-Path $resonanceRoot "RESONANCE_SYNC.md"
$syncLine = "[" + (Get-KstTimestamp) + " KST] [STATUS] [SYSTEM->COMPOSER] [" + $AlbumId + "] Initialized package for theme '" + $Theme + "'."
if ($DryRun) {
    Write-Host "[DRYRUN] append sync line"
}
else {
    Add-Content -Path $syncPath -Value $syncLine -Encoding UTF8
}

Write-Host "Album package ready:"
Write-Host "  - $themeDoc"
Write-Host "  - $promptDoc"
Write-Host "  - $qaDoc"
Write-Host "  - $videoDoc"
Write-Host "  - $seoDoc"
Write-Host "  - $manifestPath"
