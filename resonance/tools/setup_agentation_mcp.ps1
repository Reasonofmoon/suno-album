[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$AppPath,

    [switch]$SkipInstall,
    [switch]$SkipBuild
)

$ErrorActionPreference = "Stop"

function Assert-CommandExists {
    param([string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command not found: $Name"
    }
}

function Step {
    param([string]$Message)
    Write-Host ""
    Write-Host "==> $Message" -ForegroundColor Cyan
}

Assert-CommandExists "npm"

$appPathCandidate = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($AppPath)
if (-not (Test-Path $appPathCandidate)) {
    throw "AppPath does not exist: $AppPath"
}

$resolvedAppPath = Resolve-Path $appPathCandidate
$packageJson = Join-Path $resolvedAppPath "package.json"

if (-not (Test-Path $packageJson)) {
    throw "package.json not found under: $resolvedAppPath"
}

Step "Target app: $resolvedAppPath"

if (-not $SkipInstall) {
    Step "Installing Agentation into app"
    npm --prefix $resolvedAppPath install -D agentation

    Step "Installing agentation-mcp globally"
    npm install -g agentation-mcp
}

Step "Running MCP doctor"
agentation-mcp doctor

if (-not $SkipBuild) {
    Step "Running app build"
    npm --prefix $resolvedAppPath run build
}

Step "Done"
Write-Host "Next:"
Write-Host "1) Insert <Agentation /> in your React tree"
Write-Host "2) Start MCP server: agentation-mcp server"
Write-Host "3) If using endpoint mode: <Agentation endpoint=`"http://localhost:4747`" />"
