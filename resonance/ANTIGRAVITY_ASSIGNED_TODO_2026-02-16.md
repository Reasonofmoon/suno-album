# Antigravity Assigned TODO (One-Page)

Snapshot: 2026-02-16  
Scope: Antigravity -> Codex handoff/request + cross-agent pending items

## 1) Immediate Priority Board

| Priority | Task | Status | Evidence |
|---|---|---|---|
| P0 | `T01_V01` production render + `VIDEO_READY` 로그 | Pending | `shared/joint_codex_antigravity_merge_2026-02-15.md:80`, `RESONANCE_SYNC.md:15` |
| P0 | `publisher_video_T01_V01.md` Inputs 채우고 렌더 실행 준비 | In progress (template only) | `RESONANCE_SYNC.md:140`, `publisher/metadata/publisher_video_T01_V01.md` |
| P0 | `REVIEW` verdict를 `PROMETHEUS_SYNC.md`에 append (Antigravity action) | Pending | `PROMETHEUS_SYNC.md:22`, `shared/joint_codex_antigravity_merge_2026-02-15.md:77` |
| P1 | Shorts 파이프라인 설계(30-60s 하이라이트) | Pending | `RESONANCE_SYNC.md:149`, `RESONANCE_SYNC.md:225` |
| P1 | Distribution 실행 파일 `tools/prepare_distribution.ps1` 추가 | Pending (file missing) | `RESONANCE_SYNC.md:55` |
| P1 | Content ID/OAC 운영 문서 고도화 | Partially done (strategy exists) | `RESONANCE_SYNC.md:51-53`, `shared/distribution_strategy.md:85`, `shared/distribution_strategy.md:93` |
| P2 | MemoGlobe FE ownership ACK/constraint ACK 상태 정리 | Pending verification | `projects/memoglobe/MEMOGLOBE_SYNC.md:64`, `projects/memoglobe/MEMOGLOBE_SYNC.md:91` |

## 2) Confirmed Assigned Work (from Antigravity)

## A. Strategy Upgrade Handoff (Resonance)

- Source: `RESONANCE_SYNC.md:34`
- Antigravity assigned to Codex (`CODEX_ACTION_ITEMS`):
1. Content ID whitelist strategy design (`RESONANCE_SYNC.md:51`)
2. OAC checklist + timeline (`RESONANCE_SYNC.md:52`)
3. Distribution-vs-main-channel separation strategy (`RESONANCE_SYNC.md:53`)
4. Shorts pipeline design (`RESONANCE_SYNC.md:54`)
5. `tools/prepare_distribution.ps1` (`RESONANCE_SYNC.md:55`)
6. DistroKid account setup guide (`RESONANCE_SYNC.md:56`)

## B. T01 Kickoff Collaboration (Resonance)

- Source: `RESONANCE_SYNC.md:103`
- Codex publisher tasks:
1. `publisher/metadata/publisher_video_T01_V01.md` 작성/입력 완성 (`RESONANCE_SYNC.md:140`)
2. `publisher/thumbnails/T01_V01/` 썸네일 제작 (`RESONANCE_SYNC.md:142`)
3. `tools/render_album_video.ps1` 실행 (`RESONANCE_SYNC.md:144`)
4. `tools/build_chapters.py` 실행 (`RESONANCE_SYNC.md:145`)
5. `publisher/metadata/publisher_seo_T01_V01.md` 작성 (`RESONANCE_SYNC.md:146`)
6. Shorts 파이프라인 설계 (`RESONANCE_SYNC.md:149`)

## 3) Current Reality Check (Done vs Missing)

## Done / Exists

- `publisher/metadata/publisher_seo_T01_V01.md` exists and populated.
- Thumbnail directory exists: `publisher/thumbnails/T01_V01` (`RESONANCE_SYNC.md:320`).
- `composer/prompts/composer_prompts_T01_V01.md` exists (15-track prompt set declared done at `RESONANCE_SYNC.md:194`).

## Missing / Incomplete

- `REVIEW` verdict entry in `PROMETHEUS_SYNC.md` not found after request.
- `tools/prepare_distribution.ps1` missing.
- `publisher_video_T01_V01.md` still template-level (Inputs empty).
- `VIDEO_READY` completion log not found.
- Manifest path mismatch:
  - expected in sync doc: `audio/T01_V01/manifest.csv` (`RESONANCE_SYNC.md:136`)
  - actual file: `composer/audio/T01_V01/manifest.csv` (currently 1 row only)

## 4) Next 5 Actions (Execution Order)

1. `publisher/metadata/publisher_video_T01_V01.md` Inputs 채우기 (audio/background/chapter source 확정).
2. `composer/audio/T01_V01/manifest.csv`를 실제 15트랙 기준으로 확정하고 경로 기준 통일(`audio` vs `composer/audio`).
3. `tools/build_chapters.py` 실행하여 chapter metadata 생성, 이어 `tools/render_album_video.ps1` 실행.
4. 완료 후 `RESONANCE_SYNC.md`에 `TYPE: DONE` + `VIDEO_READY` append.
5. Antigravity에 `PROMETHEUS_SYNC.md` `TYPE=REVIEW` append 요청 재송신(또는 review ingest 경로 사용).

## 5) Cross-Project Pending (MemoGlobe)

- `ANTIGRAVITY please ACK ... take frontend ownership` 요청 존재 (`projects/memoglobe/MEMOGLOBE_SYNC.md:64`).
- `ACTION_REQUIRED: ACK this constraint` 존재 (`projects/memoglobe/MEMOGLOBE_SYNC.md:91`).
- Contract checklist still unchecked (`projects/memoglobe/docs/joint_phase1_contract_checklist.md:9`).

