[CmdletBinding()]
param(
    [string]$SyncPath,
    [switch]$NoAutoAck,
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$scriptRoot = Split-Path -Parent $PSCommandPath
if (-not $SyncPath) {
    $SyncPath = Join-Path (Split-Path -Parent $scriptRoot) "RESONANCE_SYNC.md"
}

$commonArgs = @(
    "-NoLogo",
    "-NoProfile",
    "-ExecutionPolicy", "Bypass",
    "-File", (Join-Path $scriptRoot "boot_sync.ps1"),
    "-SyncPath", $SyncPath
)
if ($NoAutoAck) {
    $commonArgs += "-NoAutoAck"
}
if ($DryRun) {
    $commonArgs += "-DryRun"
}

Write-Host "Running mutual sync scan for CODEX..."
& powershell @($commonArgs + @("-AgentName", "CODEX"))
if ($LASTEXITCODE -ne 0) {
    throw "boot_sync for CODEX failed."
}

Write-Host "Running mutual sync scan for ANTIGRAVITY..."
& powershell @($commonArgs + @("-AgentName", "ANTIGRAVITY"))
if ($LASTEXITCODE -ne 0) {
    throw "boot_sync for ANTIGRAVITY failed."
}

Write-Host "Mutual sync scan completed."
