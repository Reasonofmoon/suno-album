[CmdletBinding()]
param(
    [string]$SyncPath,
    [int]$IntervalSec = 20,
    [switch]$NoAutoAck
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if ($IntervalSec -lt 5) {
    throw "IntervalSec must be >= 5."
}

$scriptRoot = Split-Path -Parent $PSCommandPath
$dualScript = Join-Path $scriptRoot "dual_boot_sync.ps1"

Write-Host ("Starting sync watcher. Interval: {0}s" -f $IntervalSec)
Write-Host "Press Ctrl+C to stop."

while ($true) {
    $args = @(
        "-NoLogo",
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $dualScript
    )
    if ($SyncPath) {
        $args += @("-SyncPath", $SyncPath)
    }
    if ($NoAutoAck) {
        $args += "-NoAutoAck"
    }

    & powershell @args
    if ($LASTEXITCODE -ne 0) {
        Write-Host "dual_boot_sync failed; retrying on next interval."
    }

    Start-Sleep -Seconds $IntervalSec
}
