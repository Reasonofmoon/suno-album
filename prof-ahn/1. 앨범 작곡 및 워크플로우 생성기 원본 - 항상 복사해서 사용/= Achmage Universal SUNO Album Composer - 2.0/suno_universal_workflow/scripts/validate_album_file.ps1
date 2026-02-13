param(
    [Parameter(Mandatory = $true)]
    [string]$AlbumFilePath,

    [Parameter(Mandatory = $true)]
    [string]$BasePrompt,

    [Alias("MinLength")]
    [int]$MinPromptLength = 450,

    [Alias("MaxLength")]
    [int]$MaxPromptLength = 999,

    [ValidateSet("AUTO", "VOCAL", "INSTRUMENTAL")]
    [string]$ExpectedMode = "AUTO",

    [string]$LyricsTemplateFilePath = "",

    [string]$LyricsTemplateText = "",

    [int]$ExpectedTrackCount = 15,

    [int]$MinInstrumentVerbCount = 3,

    [double]$MinLyricsLengthRatio = 0.85,

    [double]$MaxLyricsLengthRatio = 1.25,

    [double]$MaxTemplateLineReuseRatio = 0.25,

    [int]$AllowedSectionLineDelta = 0
)

$ErrorActionPreference = "Stop"

function Get-SingleLineField {
    param(
        [Parameter(Mandatory = $true)][string]$Block,
        [Parameter(Mandatory = $true)][string]$FieldName
    )

    $fieldPattern = [regex]::Escape($FieldName)
    $match = [regex]::Match(
        $Block,
        "(?mi)^\s*-\s*(?:\*\*)?$fieldPattern(?:\*\*)?\s*:\s*(.+)$"
    )
    if ($match.Success) {
        return $match.Groups[1].Value.Trim()
    }
    return $null
}

function Get-StylePromptData {
    param([Parameter(Mandatory = $true)][string]$Block)

    $styleMatch = [regex]::Match(
        $Block,
        '(?ms)^\s*-\s*(?:\*\*)?Suno Style Prompt(?:\*\*)?\s*:\s*(.+?)(?=^\s*-\s*(?:\*\*)?Suno Style Prompt Char Count(?:\*\*)?\s*:|^\s*-\s*(?:\*\*)?Lyrics(?:\*\*)?\s*:|^##\s*Track\b|\z)'
    )
    if ($styleMatch.Success) {
        return [pscustomobject]@{
            Prompt = $styleMatch.Groups[1].Value.Trim()
        }
    }

    return $null
}

function Get-LyricsField {
    param([Parameter(Mandatory = $true)][string]$Block)

    $lyricsMatch = [regex]::Match(
        $Block,
        '(?ms)^\s*-\s*(?:\*\*)?Lyrics(?:\*\*)?\s*:\s*(.+?)(?=^##\s*Track\b|\z)'
    )
    if ($lyricsMatch.Success) {
        return $lyricsMatch.Groups[1].Value.Trim()
    }
    return $null
}

function Normalize-Header {
    param([Parameter(Mandatory = $true)][string]$Text)

    $value = $Text.ToLowerInvariant()
    $value = $value -replace '[^a-z0-9\uAC00-\uD7A3\-\s]', ''
    $value = $value -replace '\s+', ' '
    return $value.Trim()
}

function Normalize-Line {
    param([Parameter(Mandatory = $true)][string]$Text)

    $value = $Text.ToLowerInvariant()
    $value = $value -replace '[^a-z0-9\uAC00-\uD7A3\s]', ''
    $value = $value -replace '\s+', ' '
    return $value.Trim()
}

function Normalize-Block {
    param([Parameter(Mandatory = $true)][string]$Text)

    $value = $Text.ToLowerInvariant()
    $value = $value -replace '[^a-z0-9\uAC00-\uD7A3\s]', ''
    $value = $value -replace '\s+', ' '
    return $value.Trim()
}

function Get-LyricsBlueprint {
    param([Parameter(Mandatory = $true)][string]$LyricsText)

    $lines = $LyricsText -split '\r?\n'
    $sections = New-Object System.Collections.Generic.List[object]
    $currentHeaderRaw = $null
    $currentHeaderNorm = $null
    $currentLines = New-Object System.Collections.Generic.List[string]

    foreach ($rawLine in $lines) {
        $trimmed = $rawLine.Trim()

        if ($trimmed -match '^\[(.+?)\](?:\s*\(.*\))?\s*$') {
            if ($null -ne $currentHeaderRaw) {
                $sectionLines = @($currentLines.ToArray())
                $sections.Add([pscustomobject]@{
                    HeaderRaw  = $currentHeaderRaw
                    HeaderNorm = $currentHeaderNorm
                    Lines      = $sectionLines
                    LineCount  = $sectionLines.Count
                    CharCount  = (($sectionLines -join " ").Length)
                })
            }
            $currentHeaderRaw = $matches[1].Trim()
            $currentHeaderNorm = Normalize-Header -Text $currentHeaderRaw
            $currentLines = New-Object System.Collections.Generic.List[string]
            continue
        }

        if ($null -eq $currentHeaderRaw) {
            continue
        }
        if ($trimmed.Length -eq 0) {
            continue
        }
        $currentLines.Add($trimmed)
    }

    if ($null -ne $currentHeaderRaw) {
        $sectionLines = @($currentLines.ToArray())
        $sections.Add([pscustomobject]@{
            HeaderRaw  = $currentHeaderRaw
            HeaderNorm = $currentHeaderNorm
            Lines      = $sectionLines
            LineCount  = $sectionLines.Count
            CharCount  = (($sectionLines -join " ").Length)
        })
    }

    if ($sections.Count -eq 0) {
        return $null
    }

    $allLines = New-Object System.Collections.Generic.List[string]
    foreach ($section in $sections) {
        foreach ($line in $section.Lines) {
            $allLines.Add($line)
        }
    }

    $normalizedLines = @(
        $allLines.ToArray() |
            ForEach-Object { Normalize-Line -Text $_ } |
            Where-Object { $_.Length -gt 0 }
    )

    return [pscustomobject]@{
        Sections        = @($sections.ToArray())
        Signature       = (($sections | ForEach-Object { $_.HeaderNorm }) -join " > ")
        TotalLineCount  = $allLines.Count
        TotalCharCount  = (($allLines.ToArray() -join " ").Length)
        NormalizedLines = $normalizedLines
        NormalizedBlock = Normalize-Block -Text ($LyricsText -replace '^\s*-\s*(?:\*\*)?Lyrics(?:\*\*)?\s*:\s*', '')
    }
}

if (-not (Test-Path -LiteralPath $AlbumFilePath)) {
    Write-Error "Album file does not exist: $AlbumFilePath"
}

$content = Get-Content -Raw -Encoding utf8 $AlbumFilePath

$globalFailures = New-Object System.Collections.Generic.List[string]

$requiredAlbumFields = @(
    "Album Title",
    "Tagline",
    "Theme Sentence",
    "Theme Keywords",
    "Sound Palette",
    "Energy Curve"
)
foreach ($field in $requiredAlbumFields) {
    if (-not (Get-SingleLineField -Block $content -FieldName $field)) {
        $globalFailures.Add("Album concept field missing: $field")
    }
}

$trackMatches = [regex]::Matches(
    $content,
    '(?ms)^##\s*Track\s*0?(\d{1,2})\b.*?(?=^##\s*Track\s*0?\d{1,2}\b|\z)'
)

$trackBlocks = @()
foreach ($match in $trackMatches) {
    $trackBlocks += [pscustomobject]@{
        TrackNo = [int]$match.Groups[1].Value
        Block   = $match.Value
    }
}

if ($trackBlocks.Count -ne $ExpectedTrackCount) {
    $globalFailures.Add("Track count mismatch: expected $ExpectedTrackCount, found $($trackBlocks.Count)")
}

for ($i = 0; $i -lt $trackBlocks.Count; $i++) {
    $expectedNo = $i + 1
    if ($trackBlocks[$i].TrackNo -ne $expectedNo) {
        $globalFailures.Add("Track numbering mismatch at index ${expectedNo}: found Track $($trackBlocks[$i].TrackNo)")
    }
}

$trackData = New-Object System.Collections.Generic.List[object]
foreach ($track in $trackBlocks) {
    $reasons = New-Object System.Collections.Generic.List[string]
    $block = $track.Block

    $title = Get-SingleLineField -Block $block -FieldName "Title"
    $intent = Get-SingleLineField -Block $block -FieldName "Intent"
    $energyText = Get-SingleLineField -Block $block -FieldName "Energy"
    $variationAxis = Get-SingleLineField -Block $block -FieldName "Variation Axis"
    $declaredCharCountText = Get-SingleLineField -Block $block -FieldName "Suno Style Prompt Char Count"
    $styleData = Get-StylePromptData -Block $block
    $lyrics = Get-LyricsField -Block $block

    if ([string]::IsNullOrWhiteSpace($title)) { $reasons.Add("Title missing") }
    if ([string]::IsNullOrWhiteSpace($intent)) { $reasons.Add("Intent missing") }
    if ([string]::IsNullOrWhiteSpace($variationAxis)) { $reasons.Add("Variation Axis missing") }

    $energyValue = $null
    if ([string]::IsNullOrWhiteSpace($energyText)) {
        $reasons.Add("Energy missing")
    } else {
        $energyMatch = [regex]::Match($energyText, '\d+')
        if (-not $energyMatch.Success) {
            $reasons.Add("Energy value is not numeric")
        } else {
            $energyValue = [int]$energyMatch.Value
            if ($energyValue -lt 1 -or $energyValue -gt 5) {
                $reasons.Add("Energy out of range (1~5): $energyValue")
            }
        }
    }

    $prompt = $null
    $promptLength = 0
    if ($null -eq $styleData) {
        $reasons.Add("Suno Style Prompt not found")
    } else {
        $prompt = $styleData.Prompt
        $promptLength = $prompt.Length
        if ($promptLength -lt $MinPromptLength) {
            $reasons.Add("Prompt too short (< $MinPromptLength, actual $promptLength)")
        }
        if ($promptLength -gt $MaxPromptLength) {
            $reasons.Add("Prompt too long (> $MaxPromptLength, actual $promptLength)")
        }
        if ($prompt -match "[`r`n]") {
            $reasons.Add("Prompt contains newline")
        }
        if (-not $prompt.Contains($BasePrompt)) {
            $reasons.Add("Base prompt not preserved verbatim")
        }
        if ($prompt -match '(?i)\b(identity|mood|instruments|performance|production)\s*:') {
            $reasons.Add("Prompt contains forbidden labels")
        }

        $verbCount = [regex]::Matches($prompt, '(?i)\b(plays|provides|supports)\b').Count
        if ($verbCount -lt $MinInstrumentVerbCount) {
            $reasons.Add("Instrument verbs too few ($verbCount < $MinInstrumentVerbCount)")
        }

        if (-not ($prompt -match '(?i)\b(\d{2,3}\s?bpm|tempo|mid-tempo|uptempo|down-tempo)\b')) {
            $reasons.Add("Prompt missing tempo info")
        }
        if (-not ($prompt -match '(?i)\b(texture|delivery|register|range|phrasing|whisper|breathy|punch|chest|falsetto|head voice|dynamic|spoken|call and response)\b')) {
            $reasons.Add("Prompt missing performance details")
        }
        if (-not ($prompt -match '(?i)\b(space|reverb|mix|saturation|lofi|lo-fi|clarity|mic|stage|stereo|plate|room)\b')) {
            $reasons.Add("Prompt missing production details")
        }
    }

    $declaredCharCount = $null
    if ([string]::IsNullOrWhiteSpace($declaredCharCountText)) {
        $reasons.Add("Suno Style Prompt Char Count missing")
    } elseif (-not [int]::TryParse($declaredCharCountText, [ref]$declaredCharCount)) {
        $reasons.Add("Suno Style Prompt Char Count is not an integer")
    } elseif ($null -ne $prompt -and $declaredCharCount -ne $promptLength) {
        $reasons.Add("Suno Style Prompt Char Count mismatch (declared $declaredCharCount, actual $promptLength)")
    }

    $lyricsPresent = -not [string]::IsNullOrWhiteSpace($lyrics)
    if (-not $lyricsPresent) {
        $reasons.Add("Lyrics missing")
    }
    $isInstrumental = $false
    if ($lyricsPresent -and ($lyrics.Trim() -match '^(?i)instrumental$')) {
        $isInstrumental = $true
    }

    $trackData.Add([pscustomobject]@{
        TrackNo         = $track.TrackNo
        Reasons         = $reasons
        PromptLength    = $promptLength
        LyricsPresent   = $lyricsPresent
        IsInstrumental  = $isInstrumental
        Lyrics          = $lyrics
        LyricsBlueprint = $null
    })
}

$instrumentalCount = ($trackData | Where-Object { $_.IsInstrumental }).Count
$vocalCount = ($trackData | Where-Object { $_.LyricsPresent -and -not $_.IsInstrumental }).Count

$inferredMode = "UNKNOWN"
if ($trackData.Count -gt 0) {
    if ($instrumentalCount -eq $trackData.Count) {
        $inferredMode = "INSTRUMENTAL"
    } elseif ($vocalCount -eq $trackData.Count) {
        $inferredMode = "VOCAL"
    } else {
        $inferredMode = "MIXED"
        $globalFailures.Add("Mixed mode detected: instrumental=$instrumentalCount, vocal=$vocalCount")
    }
}

if ($ExpectedMode -ne "AUTO" -and $inferredMode -ne $ExpectedMode) {
    $globalFailures.Add("Expected mode $ExpectedMode but inferred mode is $inferredMode")
}

$modeForValidation = $ExpectedMode
if ($modeForValidation -eq "AUTO") {
    $modeForValidation = $inferredMode
}

$lyricsTemplateBlueprint = $null
$lyricsTemplateLineSet = [System.Collections.Generic.HashSet[string]]::new()

if ($modeForValidation -eq "VOCAL") {
    $templateTextToUse = $LyricsTemplateText
    $templateSource = "LyricsTemplateText"

    if ([string]::IsNullOrWhiteSpace($templateTextToUse)) {
        if ([string]::IsNullOrWhiteSpace($LyricsTemplateFilePath)) {
            $globalFailures.Add("LyricsTemplateFilePath or LyricsTemplateText is required for VOCAL mode validation")
        } elseif (-not (Test-Path -LiteralPath $LyricsTemplateFilePath)) {
            $globalFailures.Add("Lyrics template file does not exist: $LyricsTemplateFilePath")
        } else {
            $templateTextToUse = Get-Content -Raw -Encoding utf8 $LyricsTemplateFilePath
            $templateSource = $LyricsTemplateFilePath
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($templateTextToUse)) {
        $lyricsTemplateBlueprint = Get-LyricsBlueprint -LyricsText $templateTextToUse
        if ($null -eq $lyricsTemplateBlueprint) {
            $globalFailures.Add("Failed to parse lyrics template structure from: $templateSource")
        } else {
            foreach ($line in $lyricsTemplateBlueprint.NormalizedLines) {
                if ($line.Length -gt 0) {
                    [void]$lyricsTemplateLineSet.Add($line)
                }
            }
        }
    }
}

foreach ($track in $trackData) {
    if ($modeForValidation -eq "INSTRUMENTAL") {
        if (-not $track.IsInstrumental) {
            $track.Reasons.Add("Lyrics must be exactly Instrumental in INSTRUMENTAL mode")
        }
        continue
    }

    if ($modeForValidation -ne "VOCAL") {
        continue
    }

    if ($track.IsInstrumental) {
        $track.Reasons.Add("Instrumental lyrics are forbidden in VOCAL mode")
        continue
    }

    if (-not $track.LyricsPresent) {
        $track.Reasons.Add("Lyrics missing in VOCAL mode")
        continue
    }

    $trackBlueprint = Get-LyricsBlueprint -LyricsText $track.Lyrics
    $track.LyricsBlueprint = $trackBlueprint

    if ($null -eq $trackBlueprint) {
        $track.Reasons.Add("Lyrics section structure not detected")
        continue
    }

    if ($null -eq $lyricsTemplateBlueprint) {
        continue
    }

    if ($trackBlueprint.Signature -ne $lyricsTemplateBlueprint.Signature) {
        $track.Reasons.Add("Lyrics section signature mismatch")
    }

    if ($trackBlueprint.Sections.Count -ne $lyricsTemplateBlueprint.Sections.Count) {
        $track.Reasons.Add("Lyrics section count mismatch")
    } else {
        for ($i = 0; $i -lt $lyricsTemplateBlueprint.Sections.Count; $i++) {
            $expectedSection = $lyricsTemplateBlueprint.Sections[$i]
            $actualSection = $trackBlueprint.Sections[$i]
            if ($actualSection.HeaderNorm -ne $expectedSection.HeaderNorm) {
                $track.Reasons.Add("Lyrics section order mismatch at position $($i + 1)")
                break
            }

            $lineDelta = [math]::Abs($actualSection.LineCount - $expectedSection.LineCount)
            if ($lineDelta -gt $AllowedSectionLineDelta) {
                $track.Reasons.Add(
                    "Lyrics line-count mismatch in section '$($actualSection.HeaderRaw)' (expected $($expectedSection.LineCount), actual $($actualSection.LineCount), allowed delta $AllowedSectionLineDelta)"
                )
            }
        }
    }

    if ($lyricsTemplateBlueprint.TotalCharCount -gt 0) {
        $lengthRatio = [double]$trackBlueprint.TotalCharCount / [double]$lyricsTemplateBlueprint.TotalCharCount
        if ($lengthRatio -lt $MinLyricsLengthRatio -or $lengthRatio -gt $MaxLyricsLengthRatio) {
            $track.Reasons.Add(
                "Lyrics total length ratio out of range (ratio $([math]::Round($lengthRatio, 3)); allowed $MinLyricsLengthRatio~$MaxLyricsLengthRatio)"
            )
        }
    }

    if ($trackBlueprint.NormalizedBlock -eq $lyricsTemplateBlueprint.NormalizedBlock) {
        $track.Reasons.Add("Lyrics copied verbatim from template")
    }

    $normalizedTrackLines = @($trackBlueprint.NormalizedLines | Where-Object { $_.Length -gt 0 })
    if ($normalizedTrackLines.Count -gt 0 -and $lyricsTemplateLineSet.Count -gt 0) {
        $reusedLineCount = 0
        foreach ($line in $normalizedTrackLines) {
            if ($lyricsTemplateLineSet.Contains($line)) {
                $reusedLineCount++
            }
        }

        $reuseRatio = [double]$reusedLineCount / [double]$normalizedTrackLines.Count
        if ($reuseRatio -gt $MaxTemplateLineReuseRatio) {
            $track.Reasons.Add(
                "Template line reuse ratio too high ($([math]::Round($reuseRatio, 3)) > $MaxTemplateLineReuseRatio)"
            )
        }
    }
}

$results = @()
foreach ($track in ($trackData | Sort-Object TrackNo)) {
    $status = if ($track.Reasons.Count -eq 0) { "PASS" } else { "FAIL" }
    $results += [pscustomobject]@{
        Track   = $track.TrackNo
        Result  = $status
        Length  = $track.PromptLength
        Lyrics  = if ($track.IsInstrumental) { "Instrumental" } elseif ($track.LyricsPresent) { "Vocal" } else { "Missing" }
        Reasons = ($track.Reasons -join "; ")
    }
}

$results | Format-Table -AutoSize

if ($globalFailures.Count -gt 0) {
    Write-Host ""
    Write-Host "Global validation failures:"
    foreach ($reason in $globalFailures) {
        Write-Host "- $reason"
    }
}

$trackFailCount = ($results | Where-Object { $_.Result -eq "FAIL" }).Count
$totalFailCount = $trackFailCount + $globalFailures.Count

Write-Host ""
Write-Host "Inferred mode: $inferredMode"
Write-Host "Expected mode: $ExpectedMode"
Write-Host "Tracks failed: $trackFailCount"
Write-Host "Global failures: $($globalFailures.Count)"

if ($totalFailCount -gt 0) {
    Write-Host "Validation FAILED."
    exit 1
}

Write-Host "Validation PASSED."
exit 0
