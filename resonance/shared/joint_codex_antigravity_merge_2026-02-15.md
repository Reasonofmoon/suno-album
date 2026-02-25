# joint_codex_antigravity_merge_2026-02-15

## Context

- Date: `2026-02-15`
- Protocol: `prometheus-developer-agent` (Multi-agent merge)
- Objective: Share completed work between Codex and Antigravity, then merge into one operating baseline for `Project RESONANCE`.

## Source A - Codex Contributions (this session)

Workspace implemented under `projects/suno-album/resonance`:

- Ops structure:
  - `composer/`, `publisher/`, `shared/`, `tools/`
- Shared controls:
  - `shared/constants.yaml`
  - `shared/album_registry.yaml`
  - `shared/content_calendar.yaml`
  - `shared/brand_guide.md`
- Automation:
  - `tools/new_album.ps1`
  - `tools/render_album_video.ps1`
  - `tools/build_chapters.py`
- Bootstrapped album package:
  - `T01_V01` docs + `manifest.csv`

## Source B - Antigravity Contributions (imported references)

### B1) Existing Suno production assets in repo

- `music-system/AGENTS.MD`
- `music-system/SKILL.md`
- `music-system/specs/STYLE_PROMPT_SPEC.md`
- `music-system/workflows/concept_album.md`
- `music-system/workflows/single_viral_track.md`

Merged key rules:

- One-line high-density style prompt standard.
- 5-element prompt composition (Identity/Mood/Instruments/Performance/Production).
- Instrument verb requirements (`plays`, `provides`, `supports`).
- Album energy-curve and quality-gate workflow.

### B2) Antigravity global memory references

- `C:/Users/sound/.gemini/antigravity/brain/6899bfa1-6ef4-4dc0-ad88-5cb67cc4476d/task.md`
  - "Project RESONANCE Setup" checklist existed but incomplete.
- `C:/Users/sound/.gemini/antigravity/brain/85812cf5-c109-4c6f-9b4a-42d6f9e63e2a/suno_status_report.md`
  - Historical Suno album production status and integration notes.
- `C:/Users/sound/.gemini/antigravity/skills/moon--prometheus-developer-agent/SKILL.md`
  - Cross-agent sync and merge governance protocol.

## Merge Decisions

1. Canonical workspace remains `resonance/`.
2. Keep dual sync channels:
   - `RESONANCE_SYNC.md` for album production ops.
   - `PROMETHEUS_SYNC.md` for Codex<->Antigravity governance.
3. Apply Antigravity 5-element prompt compliance to RESONANCE templates.
4. Use prefix naming for cross-agent shared artifacts:
   - `codex_*`, `ag_*`, `joint_*`.
5. Background-music channel default remains instrumental-first.

## Concrete Changes Applied

- Updated:
  - `composer/prompts/composer_prompts_TEMPLATE.md`
  - `composer/qa/composer_qa_TEMPLATE.md`
  - `README.md`
- Added:
  - `PROMETHEUS_SYNC.md`
  - `shared/agent_merge_contract.yaml`
  - `shared/joint_codex_antigravity_merge_2026-02-15.md` (this file)

## Open Items (Post-Merge)

- [ ] Antigravity to append `REVIEW` verdict in `PROMETHEUS_SYNC.md`.
- [ ] Fill `T01_V01` prompt pack using new one-line 5-element format.
- [ ] Generate first real `T01_V01` chapter metadata from completed manifest.
- [ ] Render first production-ready long-form video and log `VIDEO_READY`.
