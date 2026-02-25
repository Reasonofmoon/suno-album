# Project RESONANCE Ops Workspace

This workspace operationalizes the `Project RESONANCE` directive for a two-agent pipeline:

- `COMPOSER`: Suno generation, curation, QA.
- `PUBLISHER`: long-form video build, metadata, upload ops, analytics.

## Directory Map

```text
resonance/
  composer/
    themes/
    prompts/
    qa/
    audio/
  publisher/
    videos/
    thumbnails/
    metadata/
    analytics/
    templates/
  shared/
    album_registry.yaml
    constants.yaml
    brand_guide.md
    content_calendar.yaml
  tools/
    new_album.ps1
    render_album_video.ps1
    render_flow_loops_3h.ps1
    build_chapters.py
  RESONANCE_SYNC.md
```

## Quick Start

1. Create a new album workspace package.

```powershell
pwsh .\tools\new_album.ps1 `
  -AlbumId T01_V01 `
  -Theme cafe_jazz `
  -Title "Cafe Jazz Vol.1 - Rainy Afternoon Sessions"
```

2. Fill prompt and theme docs:
- `composer/themes/composer_theme_cafe_jazz.md`
- `composer/prompts/composer_prompts_T01_V01.md`

3. Generate and QA tracks.
- Put approved audio files under `composer/audio/T01_V01/`.
- Fill `composer/qa/composer_qa_T01_V01.md`.

4. Prepare chapter metadata from CSV.

```powershell
python .\tools\build_chapters.py `
  --input .\composer\audio\T01_V01\manifest.csv `
  --output .\publisher\metadata\T01_V01_chapters.ffmeta `
  --youtube-output .\publisher\metadata\T01_V01_timestamps.txt
```

5. Render the long-form video.

```powershell
pwsh .\tools\render_album_video.ps1 `
  -TrackManifest .\composer\audio\T01_V01\manifest.csv `
  -BackgroundImage .\publisher\thumbnails\T01_V01_bg.jpg `
  -OutputVideo .\publisher\videos\T01_V01.mp4 `
  -CrossfadeSec 5 `
  -AddKenBurns
```

5b. Render a 3-hour Flow loop timeline (with optional album audio).

```powershell
pwsh .\tools\render_flow_loops_3h.ps1 `
  -LoopDir .\publisher\videos\T01_V01\loops `
  -AudioPath .\composer\audio\T01_V01\album_full.mp3 `
  -OutputVideo .\publisher\videos\T01_V01_flow_3h.mp4 `
  -TargetDurationSec 10800 `
  -SegmentSec 30 `
  -Shuffle
```

6. Finalize publishing docs:
- `publisher/metadata/publisher_video_T01_V01.md`
- `publisher/metadata/publisher_seo_T01_V01.md`

7. Append execution logs in `RESONANCE_SYNC.md` (append-only).

## Track Manifest CSV Format

`manifest.csv` requires these columns:

```csv
order,title,file,duration_sec
1,Rainy Afternoon,track01.mp3,495
2,Sunday Morning,track02.mp3,480
```

- `file` can be absolute or relative to the CSV directory.
- `duration_sec` should be integer seconds.

## Core Gates

- QA threshold: weighted score >= `4.0 / 5.0`.
- Audio target: integrated loudness around `-14 LUFS`.
- No abrupt volume spikes.
- No artist-name prompts.
- Instrumental-by-default for channel safety.

## Codex x Antigravity Merge Protocol

This project now operates with dual sync channels:

- `RESONANCE_SYNC.md`: album production ops between `COMPOSER` and `PUBLISHER`.
- `PROMETHEUS_SYNC.md`: Codex x Antigravity cross-agent collaboration logs.

Merge artifacts:

- `shared/joint_codex_antigravity_merge_2026-02-15.md`
- `shared/agent_merge_contract.yaml`

Working rules:

1. Keep `resonance/` as the canonical production workspace.
2. Use shared prefix naming for cross-agent artifacts:
   - `codex_*`, `ag_*`, `joint_*`
3. Append-only sync logs only; no in-place edits to past records.

## Antigravity REVIEW Intake

Review intake structure:

- Incoming review docs: `shared/reviews/incoming/`
- Review registry: `shared/reviews/review_registry.yaml`
- Review response template: `shared/reviews/ag_review_response_TEMPLATE.md`
- Intake script: `tools/ingest_ag_review.ps1`

Pull Antigravity `TYPE=REVIEW` lines into local workspace:

```powershell
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\ingest_ag_review.ps1
```

Dry run:

```powershell
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\ingest_ag_review.ps1 -DryRun
```

## Sync Auto-Detect (Codex)

Run mutual scanner to auto-detect pending SEQ messages for both agents:

```powershell
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\dual_boot_sync.ps1
```

Outputs:

- Auto ACK append to `RESONANCE_SYNC.md` for unacknowledged `EXPECTS_ACK:true` messages to `CODEX` and `ANTIGRAVITY`.
- Task digest files:
  - `shared/codex_inbox.md`
  - `shared/antigravity_inbox.md`

Dry run:

```powershell
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\dual_boot_sync.ps1 -DryRun
```

Optional continuous watcher:

```powershell
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\start_sync_watcher.ps1 -IntervalSec 20
```

Realtime file watcher with notifications + auto mutual boot on file change:

```powershell
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\watch_sync.ps1
```

Watcher options:

- Notification-only mode:
  - `powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\watch_sync.ps1 -NoAutoBoot`
- Keep auto boot but skip auto ACK writes:
  - `powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\watch_sync.ps1 -NoAutoAck`
- Silent mode:
  - `powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\watch_sync.ps1 -Silent`

## Agentation + MCP Quickstart

- Quickstart guide: `AGENTATION_MCP_QUICKSTART.md`
- Setup/build helper script:
  - `powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\setup_agentation_mcp.ps1 -AppPath C:\path\to\your-react-app`
