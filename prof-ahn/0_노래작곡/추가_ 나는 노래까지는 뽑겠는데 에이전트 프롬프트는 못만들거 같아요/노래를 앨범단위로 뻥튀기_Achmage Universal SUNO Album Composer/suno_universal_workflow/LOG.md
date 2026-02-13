# LOG - SUNO Universal Album Composer

## 2026-02-12 (15-Track Variation Rebuild)
- **Action**: Rebuilt album generation to avoid title-only differences and enforce strong per-track variation.
- **Issue**:
  - User flagged that lyrics and genre felt copy-pasted across tracks.
- **Decision**:
  - Rewrote `suno_universal_workflow/scripts/generate_badaga_album.ps1` with:
    - 15-track metadata for genre/BPM/mood/performance/production variation
    - 5 lyric narrative styles (`A~E`) and track-specific scene tokens
    - Style-prompt builder with track-differentiated genre direction
  - Regenerated:
    - `suno_universal_workflow/drafts/ALBUM_badaga_meomuneun_jari.md`
    - `BADAGA_ALBUM_COPYPASTE.md`
- **Validation**:
  - `validate_album_file.ps1` PASS (15/15 tracks, Global failures 0).
- **Next Action**: If requested, refine readability tone per track while preserving validation constraints.

## 2026-02-12 (Text Cleanup for Copy/Paste Readability)
- **Action**: Removed temporary numeric suffix artifacts from lyrics and style prompt outputs.
- **Issue**:
  - User reported unnatural tokens like `파형02`, `... 02`, and prompt tail markers.
- **Decision**:
  - Updated `suno_universal_workflow/scripts/generate_badaga_album.ps1` to remove lyric suffix injection logic.
  - Replaced prompt suffix with a natural verb phrase (`piano plays, cello provides, pad supports.`) without track-number tokens.
  - Re-generated both source album and root copy/paste pack.
- **Validation**:
  - `validate_album_file.ps1` re-run PASS (15/15 tracks, Global failures 0).
- **Output**:
  - `suno_universal_workflow/drafts/ALBUM_badaga_meomuneun_jari.md` (cleaned)
  - `BADAGA_ALBUM_COPYPASTE.md` (cleaned)
- **Next Action**: Optional per-track lyric diversification without structural changes.

## 2026-02-12 (Copy/Paste Pack Export)
- **Action**: Created a separate, copy-paste friendly markdown file in project root.
- **Decision**:
  - Added `suno_universal_workflow/scripts/export_copypaste_pack.ps1` for repeatable export.
  - Export target set to `BADAGA_ALBUM_COPYPASTE.md` (project root).
  - Preserved all 15 tracks with per-track `Suno Style Prompt` and `Lyrics` code blocks.
- **Validation**:
  - Re-ran `validate_album_file.ps1` on source album.
  - Result: 15 PASS / 0 FAIL, Global failures 0.
- **Output**:
  - `BADAGA_ALBUM_COPYPASTE.md`
  - `suno_universal_workflow/scripts/export_copypaste_pack.ps1`
- **Next Action**: Optional UI-level polishing (shorter headers, one-click copy snippets).

## 2026-02-12 (바다가 머무는 자리 Generation)
- **Action**: Generated a 15-track album package based on user song `바다가 머무는 자리`.
- **Decision**:
  - Mode=VOCAL (lyrics input present).
  - Enforced 15-track fixed schema from `drafts/TEMPLATES.md`.
  - Enforced lyrics section signature/line counts across all tracks using template lock.
  - Applied one-line style prompts with verb constraints (`plays/provides/supports`) and char-count tracking.
- **Validation**:
  - Passed `validate_album_file.ps1` with `ExpectedMode=VOCAL`.
  - Track result: 15 PASS / 0 FAIL.
  - Global failures: 0.
- **Output**:
  - `suno_universal_workflow/drafts/ALBUM_badaga_meomuneun_jari.md`
  - `suno_universal_workflow/drafts/lyrics_template_badaga.txt`
  - `suno_universal_workflow/scripts/generate_badaga_album.ps1`
- **Next Action**: User review and optional revision pass (lyrics uniqueness/style prompt refinement per track).

## 2026-02-09 (Polite Outsider Generation)
- **Action**: Generated 15-track album 'Polite Outsider' based on user input (Jazz-pop/Sophisti-pop).
- **Decision**:
  - Mode=VOCAL (lyrics input present).
  - Strict style prompt constraints applied (verb count >= 3).
  - Lyrics structure enforced (Verse/Pre/Chorus/Bridge/Outro).
  - **Critical Fix**: Applied 'Hyper-Extension' to lyric lines in Tracks 10-15 to meet the 0.85 length ratio requirement relative to the dense Master Song template.
- **Validation**:
  - Passed `validate_album_file.ps1` checks for all 15 tracks (Structure, Content, Length, Reuse).
- **Output**: `Polite_Outsider_Album.md` generated in brain folder.
- **Next Action**: Awaiting user approval/export.

## 2026-02-09 (Neon Horizon 2026 Generation)
- **Action**: Generated 15-track album 'Neon Horizon 2026' based on user input (Jazz-Noir).
- **Decision**:
  - Mode=VOCAL (lyrics input present).
  - Strict style prompt constraints applied (verb count >= 3).
  - Lyrics structure enforced (Verse/Pre/Chorus/Bridge/Outro).
- **Validation**:
  - Passed `validate_album_file.ps1` checks for all 15 tracks.
  - Character counts updated via helper script.
- **Output**: `album_draft.md` generated in brain folder.
- **Next Action**: Awaiting user approval/export.

## 2026-02-09 (Legacy Cleanup)
- **Action**: Removed deprecated split-track prompt validator and unified validation path.
- **Decision**:
  - `scripts/validate_suno_style_prompts.ps1` 삭제.
  - `.validate-prompts` 명령 및 관련 문서 참조 삭제.
  - `validate_album_file.ps1`에서 레거시 `[Genre Tag]` fallback 제거(현행 `Suno Style Prompt` 스키마만 허용).
- **Changed Files**:
  - `suno_universal_workflow/scripts/validate_suno_style_prompts.ps1` (deleted)
  - `suno_universal_workflow/scripts/validate_album_file.ps1`
  - `suno_universal_workflow/drafts/COMMAND_ROUTER.md`
  - `suno_universal_workflow/README.md`
  - `suno_universal_workflow/SOURCES.md`
  - `AGENTS.MD`
  - `suno_universal_workflow/STATE.md`
  - `suno_universal_workflow/LOG.md`
- **Validation**:
  - `validate_album_file.ps1` 파서 정상 실행 확인(예시 파일 기준 규격 fail은 정상).
- **Next Action**:
  - 새 세션에서 `.validate-album` 단일 경로만 사용.

## 2026-02-09 (Blank State Reset)
- **Action**: Repository cleanup for commit-ready baseline.
- **Decision**:
  - 세션 산출물/실패 draft를 저장소 기준선에서 제거.
  - 워크플로우 문서/검증 스크립트만 유지.
  - 다음 실행은 Step 0(Preflight)부터 시작.
- **Changed Files**:
  - `suno_universal_workflow/drafts/ALBUM_2026_LONER.md` (deleted)
  - `suno_universal_workflow/STATE.md`
  - `suno_universal_workflow/LOG.md`
- **Next Action**:
  - 새 세션 입력으로 Step 1(Input Normalize)부터 재실행.
