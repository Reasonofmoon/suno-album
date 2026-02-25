[CmdletBinding()]
param(
    [string]$SourcePrometheusSync = "C:\Users\sound\.gemini\antigravity\knowledge\project_resonance\artifacts\PROMETHEUS_SYNC.md",
    [string]$LocalPrometheusSync,
    [string]$ReviewRegistryPath,
    [string]$ReviewIncomingDir,
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-Sha256Hex {
    param([string]$Text)
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ($sha.ComputeHash($bytes) | ForEach-Object { $_.ToString("x2") }) -join ""
    }
    finally {
        $sha.Dispose()
    }
}

function Get-KstNowString {
    $tz = [System.TimeZoneInfo]::FindSystemTimeZoneById("Korea Standard Time")
    $kst = [System.TimeZoneInfo]::ConvertTimeFromUtc([DateTime]::UtcNow, $tz)
    return $kst.ToString("yyyy-MM-dd HH:mm")
}

function Ensure-File {
    param([string]$Path, [string]$DefaultContent = "")
    if (Test-Path -LiteralPath $Path) {
        return
    }
    if ($DryRun) {
        Write-Host "[DRYRUN] create file $Path"
        return
    }
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    Set-Content -Path $Path -Value $DefaultContent -Encoding UTF8
}

$scriptRoot = Split-Path -Parent $PSCommandPath
$resonanceRoot = Split-Path -Parent $scriptRoot

if (-not $LocalPrometheusSync) {
    $LocalPrometheusSync = Join-Path $resonanceRoot "PROMETHEUS_SYNC.md"
}
if (-not $ReviewRegistryPath) {
    $ReviewRegistryPath = Join-Path $resonanceRoot "shared\reviews\review_registry.yaml"
}
if (-not $ReviewIncomingDir) {
    $ReviewIncomingDir = Join-Path $resonanceRoot "shared\reviews\incoming"
}

if (-not (Test-Path -LiteralPath $SourcePrometheusSync)) {
    throw "Source sync file not found: $SourcePrometheusSync"
}

Ensure-File -Path $LocalPrometheusSync -DefaultContent "# PROMETHEUS_SYNC`n"
Ensure-File -Path $ReviewRegistryPath -DefaultContent "reviews: []`n"
if (-not (Test-Path -LiteralPath $ReviewIncomingDir) -and -not $DryRun) {
    New-Item -ItemType Directory -Path $ReviewIncomingDir -Force | Out-Null
}

$sourceLines = Get-Content -Path $SourcePrometheusSync
$localRaw = Get-Content -Path $LocalPrometheusSync -Raw

$candidateLines = $sourceLines | Where-Object {
    $_ -match "\[ANTIGRAVITY\].*TYPE=REVIEW"
}

$newLines = @()
foreach ($line in $candidateLines) {
    if ($localRaw -notlike ("*" + $line + "*")) {
        $newLines += $line
    }
}

if ($newLines.Count -eq 0) {
    Write-Host "No new Antigravity REVIEW lines found."
    exit 0
}

$kstNow = Get-KstNowString
$batchStamp = (Get-Date).ToString("yyyyMMdd_HHmmss")
$idx = 0

foreach ($line in $newLines) {
    $idx++
    $reviewId = "ag_review_" + $batchStamp + "_" + $idx.ToString("00")
    $lineHash = Get-Sha256Hex -Text $line
    $fileName = $reviewId + ".md"
    $incomingPath = Join-Path $ReviewIncomingDir $fileName
    $relativeIncoming = $incomingPath.Substring($resonanceRoot.Length + 1).Replace("\", "/")

    $target = ""
    $summary = ""
    if ($line -match "TARGET=(?<target>.+?)\s+SUMMARY=(?<summary>.+)$") {
        $target = $Matches["target"]
        $summary = $Matches["summary"]
    }

    $reviewDoc = @"
# $reviewId

## Imported Metadata

- Source Agent: `ANTIGRAVITY`
- Imported At (KST): `$kstNow`
- Source Sync Path: `$SourcePrometheusSync`
- Source Sync Hash: `$lineHash`

## Parsed Fields

- Target: $target
- Summary: $summary

## Raw Sync Line

```text
$line
```

## Action Status

- Verdict Mapping: `PENDING`
- Owner: `CODEX`
- Status: `OPEN`
"@

    if ($DryRun) {
        Write-Host "[DRYRUN] write $incomingPath"
    }
    else {
        Set-Content -Path $incomingPath -Value $reviewDoc -Encoding UTF8
    }

    $registryEntry = @"
  - id: "$reviewId"
    source_agent: "ANTIGRAVITY"
    imported_at_kst: "$kstNow"
    source_sync_path: "$SourcePrometheusSync"
    source_sync_hash: "$lineHash"
    status: "imported"
    review_file: "$relativeIncoming"
"@

    if ($DryRun) {
        Write-Host "[DRYRUN] append registry entry for $reviewId"
    }
    else {
        Add-Content -Path $ReviewRegistryPath -Value $registryEntry -Encoding UTF8
    }

    if ($DryRun) {
        Write-Host "[DRYRUN] append line to local sync"
    }
    else {
        Add-Content -Path $LocalPrometheusSync -Value $line -Encoding UTF8
    }
}

$summaryLine = "[" + $kstNow + " KST] [CODEX] TYPE=STATUS TARGET=REVIEW_INTAKE SUMMARY=Imported " + $newLines.Count + " new ANTIGRAVITY REVIEW entries."
if ($DryRun) {
    Write-Host "[DRYRUN] append summary line"
}
else {
    Add-Content -Path $LocalPrometheusSync -Value $summaryLine -Encoding UTF8
}

Write-Host ("Imported REVIEW entries: " + $newLines.Count)
