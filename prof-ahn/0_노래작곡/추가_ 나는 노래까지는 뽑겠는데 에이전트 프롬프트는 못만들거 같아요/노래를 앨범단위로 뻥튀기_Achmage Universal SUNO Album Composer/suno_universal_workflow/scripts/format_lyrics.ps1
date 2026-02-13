$path = 'C:\Users\82109\.gemini\antigravity\brain\3916a574-c53c-4e2d-a6aa-926777f8115b\Polite_Outsider_Album.md'
$content = Get-Content -LiteralPath $path -Raw
# Replace [Header] followed by newline with [Header] followed by 2 newlines
# We use regex to match [Anything] at start of line, followed by optional whitespace and a newline
$newContent = $content -replace '(?m)^(\[.+\])\s*(\r?\n)', '$1$2$2'
Set-Content -LiteralPath $path -Value $newContent -Encoding UTF8
Write-Host "Formatting complete."
