# RESONANCE SYNC Watcher v1.0
# 사용법: .\tools\watch_sync.ps1
# 기능: RESONANCE_SYNC.md와 PROMETHEUS_SYNC.md 변경 감지 → Windows 알림
# 중지: Ctrl+C

param(
    [switch]$Silent,  # 소리 없이 알림만
    [switch]$NoAutoBoot, # 변경 감지 시 dual_boot_sync 자동 실행 비활성화
    [switch]$NoAutoAck   # AutoBoot 실행 시 ACK append 비활성화
)

$ErrorActionPreference = 'Stop'

# === 경로 계산 ===
$scriptRoot = Split-Path -Parent $PSCommandPath
$resonanceRoot = Split-Path -Parent $scriptRoot
$projectsRoot = Split-Path -Parent (Split-Path -Parent $resonanceRoot)
$dualBootScript = Join-Path $scriptRoot "dual_boot_sync.ps1"

# === 감시 대상 파일 ===
$watchFiles = @(
    @{
        Path = Join-Path $resonanceRoot "RESONANCE_SYNC.md"
        Name = "RESONANCE"
        Color = "Cyan"
    },
    @{
        Path = Join-Path $projectsRoot "memoglobe\PROMETHEUS_SYNC.md"
        Name = "PROMETHEUS"
        Color = "Yellow"
    }
)

# === 마지막 읽은 줄 수 기록 ===
$lastLineCount = @{}
foreach ($f in $watchFiles) {
    if (Test-Path $f.Path) {
        $lastLineCount[$f.Path] = (Get-Content $f.Path -Encoding UTF8).Count
    } else {
        $lastLineCount[$f.Path] = 0
    }
}

# === Windows Toast 알림 함수 ===
function Send-Toast {
    param([string]$Title, [string]$Message)
    try {
        [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
        [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom, ContentType = WindowsRuntime] | Out-Null

        $template = @"
<toast>
  <visual>
    <binding template="ToastGeneric">
      <text>$Title</text>
      <text>$Message</text>
    </binding>
  </visual>
  <audio silent="$($Silent.ToString().ToLower())" />
</toast>
"@
        $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
        $xml.LoadXml($template)
        $toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
        $appId = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe'
        [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($appId).Show($toast)
    }
    catch {
        # Toast 실패 시 콘솔만 출력 (비-Windows Terminal 환경 등)
    }
}

function Invoke-MutualBoot {
    if ($NoAutoBoot) {
        return
    }
    if (-not (Test-Path $dualBootScript)) {
        Write-Host "  ⚠️ dual_boot_sync.ps1 not found. Skipping auto boot." -ForegroundColor DarkYellow
        return
    }
    try {
        $args = @(
            "-NoLogo",
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-File", $dualBootScript
        )
        if ($NoAutoAck) {
            $args += "-NoAutoAck"
        }
        & powershell @args | Out-Null
    }
    catch {
        Write-Host "  ⚠️ Auto boot execution failed." -ForegroundColor DarkYellow
    }
}

# === SEQ 메시지 파서 ===
function Get-NewMessages {
    param([string]$FilePath, [int]$FromLine)
    
    $lines = Get-Content $FilePath -Encoding UTF8
    if ($lines.Count -le $FromLine) { return @() }
    
    $newLines = $lines[$FromLine..($lines.Count - 1)]
    $messages = @()
    $currentMsg = ""
    
    foreach ($line in $newLines) {
        if ($line -match '^\[SEQ:\d+\]') {
            if ($currentMsg) { $messages += $currentMsg }
            $currentMsg = $line
        }
        elseif ($line -match '^\[2026-') {
            if ($currentMsg) { $messages += $currentMsg }
            $currentMsg = $line
        }
        elseif ($currentMsg -and $line -notmatch '^---') {
            $currentMsg += " | $line"
        }
    }
    if ($currentMsg) { $messages += $currentMsg }
    
    return $messages
}

# === 메인 루프 ===
Clear-Host
Write-Host ""
Write-Host "  ╔══════════════════════════════════════════════╗" -ForegroundColor DarkCyan
Write-Host "  ║   🔭 RESONANCE SYNC WATCHER v1.0            ║" -ForegroundColor DarkCyan
Write-Host "  ║   Monitoring agent communication channels    ║" -ForegroundColor DarkCyan
Write-Host "  ╚══════════════════════════════════════════════╝" -ForegroundColor DarkCyan
Write-Host ""
Write-Host "  Watching:" -ForegroundColor Gray
foreach ($f in $watchFiles) {
    $status = if (Test-Path $f.Path) { "✅" } else { "❌" }
    Write-Host "    $status $($f.Name): $($f.Path)" -ForegroundColor $f.Color
}
Write-Host ""
Write-Host "  Press Ctrl+C to stop" -ForegroundColor DarkGray
Write-Host "  ─────────────────────────────────────────────" -ForegroundColor DarkGray
Write-Host ""
if (-not $NoAutoBoot) {
    Write-Host "  Auto Boot: ON (dual_boot_sync on each update)" -ForegroundColor DarkGreen
}
else {
    Write-Host "  Auto Boot: OFF (notification-only mode)" -ForegroundColor DarkYellow
}
Write-Host ""

$pollInterval = 3  # seconds

while ($true) {
    $changed = $false
    foreach ($f in $watchFiles) {
        if (-not (Test-Path $f.Path)) { continue }
        
        $currentLines = (Get-Content $f.Path -Encoding UTF8).Count
        $previousLines = $lastLineCount[$f.Path]
        
        if ($currentLines -gt $previousLines) {
            $changed = $true
            $newCount = $currentLines - $previousLines
            $timestamp = Get-Date -Format "HH:mm:ss"
            
            # 새 메시지 파싱
            $newMsgs = Get-NewMessages -FilePath $f.Path -FromLine $previousLines
            
            # 콘솔 알림
            Write-Host ""
            Write-Host "  ┌─ 📨 NEW MESSAGE ──────────────────────────" -ForegroundColor $f.Color
            Write-Host "  │ Channel: $($f.Name)" -ForegroundColor $f.Color
            Write-Host "  │ Time:    $timestamp" -ForegroundColor Gray
            Write-Host "  │ Lines:   +$newCount new lines" -ForegroundColor White
            
            foreach ($msg in $newMsgs) {
                $short = if ($msg.Length -gt 80) { $msg.Substring(0, 80) + "..." } else { $msg }
                Write-Host "  │ >> $short" -ForegroundColor White
            }
            
            Write-Host "  └─────────────────────────────────────────" -ForegroundColor $f.Color
            Write-Host ""
            
            # 비프음
            if (-not $Silent) {
                [Console]::Beep(800, 200)
                [Console]::Beep(1000, 200)
            }
            
            # Windows 토스트 알림
            $toastMsg = if ($newMsgs.Count -gt 0) {
                $newMsgs[0].Substring(0, [Math]::Min(100, $newMsgs[0].Length))
            } else {
                "+$newCount new lines"
            }
            Send-Toast -Title "🔔 $($f.Name) SYNC Update" -Message $toastMsg
            
            # 라인 카운트 업데이트
            $lastLineCount[$f.Path] = $currentLines
        }
    }

    if ($changed) {
        Invoke-MutualBoot
    }
    
    Start-Sleep -Seconds $pollInterval
}
