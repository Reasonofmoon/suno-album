param(
    [string]$InputPath = "suno_universal_workflow/drafts/ALBUM_badaga_meomuneun_jari.md",
    [string]$OutputPath = "BADAGA_ALBUM_COPYPASTE.md"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $InputPath)) {
    throw "Input file not found: $InputPath"
}

$content = Get-Content -Raw -Encoding utf8 $InputPath

function Get-AlbumField {
    param(
        [string]$Text,
        [string]$FieldName
    )
    $pattern = "(?mi)^\s*-\s*" + [regex]::Escape($FieldName) + "\s*:\s*(.+)$"
    $m = [regex]::Match($Text, $pattern)
    if ($m.Success) { return $m.Groups[1].Value.Trim() }
    return ""
}

function Get-TrackField {
    param(
        [string]$Block,
        [string]$FieldName
    )
    $pattern = "(?mi)^\s*-\s*" + [regex]::Escape($FieldName) + "\s*:\s*(.+)$"
    $m = [regex]::Match($Block, $pattern)
    if ($m.Success) { return $m.Groups[1].Value.Trim() }
    return ""
}

$albumTitle = Get-AlbumField -Text $content -FieldName "Album Title"
$tagline = Get-AlbumField -Text $content -FieldName "Tagline"
$themeSentence = Get-AlbumField -Text $content -FieldName "Theme Sentence"
$themeKeywords = Get-AlbumField -Text $content -FieldName "Theme Keywords"
$soundPalette = Get-AlbumField -Text $content -FieldName "Sound Palette"
$energyCurve = Get-AlbumField -Text $content -FieldName "Energy Curve"

$trackMatches = [regex]::Matches(
    $content,
    "(?ms)^##\s*Track\s*0?(\d{1,2})\b.*?(?=^##\s*Track\s*0?\d{1,2}\b|\z)"
)

$tracks = New-Object System.Collections.Generic.List[object]
foreach ($match in $trackMatches) {
    $block = $match.Value
    $trackNo = [int]$match.Groups[1].Value
    $title = Get-TrackField -Block $block -FieldName "Title"
    $intent = Get-TrackField -Block $block -FieldName "Intent"
    $energy = Get-TrackField -Block $block -FieldName "Energy"
    $variationAxis = Get-TrackField -Block $block -FieldName "Variation Axis"
    $charCount = Get-TrackField -Block $block -FieldName "Suno Style Prompt Char Count"

    $styleMatch = [regex]::Match(
        $block,
        "(?ms)^\s*-\s*Suno Style Prompt\s*:\s*(.+?)(?=^\s*-\s*Suno Style Prompt Char Count\s*:)"
    )
    $stylePrompt = ""
    if ($styleMatch.Success) {
        $stylePrompt = $styleMatch.Groups[1].Value.Trim()
    }

    $lyricsMatch = [regex]::Match(
        $block,
        "(?ms)^\s*-\s*Lyrics\s*:\s*(.+?)\s*\z"
    )
    $lyrics = ""
    if ($lyricsMatch.Success) {
        $lyrics = $lyricsMatch.Groups[1].Value.Trim()
    }

    $tracks.Add([pscustomobject]@{
        TrackNo = $trackNo
        Title = $title
        Intent = $intent
        Energy = $energy
        VariationAxis = $variationAxis
        CharCount = $charCount
        StylePrompt = $stylePrompt
        Lyrics = $lyrics
    })
}

$tracks = $tracks | Sort-Object TrackNo

$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine("# $albumTitle - SUNO Copy/Paste Pack")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Source: $InputPath")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## Album Concept")
[void]$sb.AppendLine("- Album Title: $albumTitle")
[void]$sb.AppendLine("- Tagline: $tagline")
[void]$sb.AppendLine("- Theme Sentence: $themeSentence")
[void]$sb.AppendLine("- Theme Keywords: $themeKeywords")
[void]$sb.AppendLine("- Sound Palette: $soundPalette")
[void]$sb.AppendLine("- Energy Curve: $energyCurve")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## Quick Track Index")
foreach ($track in $tracks) {
    $trackNo = "{0:D2}" -f $track.TrackNo
    [void]$sb.AppendLine("$trackNo. $($track.Title)")
}
[void]$sb.AppendLine("")

foreach ($track in $tracks) {
    $trackNo = "{0:D2}" -f $track.TrackNo
    [void]$sb.AppendLine("---")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("## Track $trackNo - $($track.Title)")
    [void]$sb.AppendLine("- Intent: $($track.Intent)")
    [void]$sb.AppendLine("- Energy: $($track.Energy)")
    [void]$sb.AppendLine("- Variation Axis: $($track.VariationAxis)")
    [void]$sb.AppendLine("- Suno Style Prompt Char Count: $($track.CharCount)")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("### Suno Style Prompt (Copy)")
    [void]$sb.AppendLine('```text')
    [void]$sb.AppendLine($track.StylePrompt)
    [void]$sb.AppendLine('```')
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("### Lyrics (Copy)")
    [void]$sb.AppendLine('```text')
    [void]$sb.AppendLine($track.Lyrics)
    [void]$sb.AppendLine('```')
    [void]$sb.AppendLine("")
}

Set-Content -LiteralPath $OutputPath -Value $sb.ToString() -Encoding utf8
Write-Host "Created: $OutputPath"
