# STATE - suno_universal_workflow

## Goal
- SUNO 입력(장르/스타일 프롬프트 + 선택 가사)을 15트랙 앨범 출력으로 확장하는 재사용 워크플로우를 안정적으로 유지한다.
- 새 세션에서도 동일 규칙으로 재현 가능하도록 blank state를 유지한다.

## Deliverables
- [x] `drafts/PROMPT_PACK.md` 확정본
- [x] `drafts/TEMPLATES.md` 확정본
- [x] `drafts/QUALITY_GATE.md` 확정본
- [x] `scripts/validate_album_file.ps1` 통합 검증기(스타일 프롬프트 + 모드 + 가사 구조/분량/복붙)
- [x] 레거시 검증 스크립트/명령 정리(`validate_suno_style_prompts.ps1`, `.validate-prompts` 제거)
- [x] 세션 산출물 정리(커밋용 blank state)

## Constraints
- Must:
  - 15트랙 고정
  - `lyrics_input` 없음 -> 전 트랙 `INSTRUMENTAL`
  - `lyrics_input` 있음 -> 전 트랙 `VOCAL` + 섹션 구조/분량 형식 고정
- Must NOT:
  - 상용 가사 복제
  - 특정 아티스트 직접 모사
- Format/Style:
  - Markdown 우선, JSON 옵션

## Current Step
- step_id: 8
- step_name: State and Log Sync
- done_definition: 작업 이력을 기록하고 다음 입력을 대기한다.

## Next Step
- step_id: 0
- step_name: Preflight (Next Session)
- action: 새 사용자 입력 대기

## Open Questions
- 없음 (앨범 '바다가 머무는 자리' 생성 완료)

## Risks
- risk: `VOCAL` 생성 시 구조 준수는 통과해도 의미 변주가 약해질 수 있음
- mitigation: Variation Axis 분산 + 라인 재사용 상한(기본 0.25) 유지

## Recent Decisions
- 2026-02-12: 사용자 피드백 반영해 15트랙 가사/장르 변주를 전면 재구성(트랙별 장르/BPM/무드 분화).
- 2026-02-12: `generate_badaga_album.ps1`를 스타일 기반(5개 가사 서술 스타일 + 트랙별 토큰) 생성기로 교체.
- 2026-02-12: 변주본 기준 `validate_album_file.ps1` 재검증 PASS (15/15 PASS, Global Fail 0).
- 2026-02-12: 가사 내 임시 꼬리표(`파형02`, `... 02`) 제거 후 앨범/복붙 정리본 재생성.
- 2026-02-12: 스타일 프롬프트 임시 꼬리표(`tide01`) 제거, 자연 문장(`piano plays, cello provides, pad supports.`)으로 치환.
- 2026-02-12: 수정본 기준 통합 검증 PASS 유지 (`validate_album_file.ps1`, 15/15 PASS).
- 2026-02-12: 프로젝트 루트에 복붙 전용 정리본 `BADAGA_ALBUM_COPYPASTE.md` 생성.
- 2026-02-12: 정리본 자동 생성 스크립트 `scripts/export_copypaste_pack.ps1` 추가.
- 2026-02-12: 원본 앨범 재검증 PASS 유지 (`validate_album_file.ps1`, 15/15 PASS).
- 2026-02-12: 앨범 '바다가 머무는 자리' 생성 완료 (Mode: VOCAL, 15 Tracks).
- 2026-02-12: `lyrics_template_badaga.txt` 기준 섹션 시그니처/라인 수 고정 검증 통과.
- 2026-02-12: 통합 검증기 `validate_album_file.ps1` PASS (15/15 트랙, Global Fail 0).
- 2026-02-09: 앨범 'Polite Outsider' 생성 완료 (Mode: VOCAL, 15 Tracks, Hyper-Extended Lyrics).
- 2026-02-09: 앨범 'Neon Horizon 2026' 생성 완료 (Mode: VOCAL, 15 Tracks).
- 2026-02-09: 스타일 프롬프트 동사 제약(plays/provides/supports) 강제 적용 및 검증 통과.
- 2026-02-09: `lyrics_input` 기반 모드 강제 규칙 확정 (`없음=INSTRUMENTAL`, `있음=VOCAL`).
- 2026-02-09: `VOCAL` 전 트랙 가사 구조/라인 수/분량 형식 검증을 `validate_album_file.ps1`에 내장.

## Current Files of Truth
- `AGENTS.MD`
- `README.md`
- `WORKPLAN.md`
- `OUTLINE.md`
- `LOG.md`
- `SOURCES.md`
- `drafts/TEMPLATES.md`
- `drafts/PROMPT_PACK.md`
- `drafts/QUALITY_GATE.md`
- `drafts/COMMAND_ROUTER.md`
- `scripts/validate_album_file.ps1`
