# AGENTS.MD

## What This Is
- `AGENTS.MD`는 이 폴더에서 동작하는 AI 에이전트용 운영 규칙 파일이다.
- 사람용 설명이 아니라, 에이전트가 따라야 하는 **실행 계약서**다.

## Scope
- 작업 루트: 프로젝트 루트
- SUNO 전용 워크플로우 루트: `suno_universal_workflow/`

## Priority Order (Conflict Resolution)
1. 사용자의 최신 직접 지시
2. `AGENTS.MD`
3. `suno_universal_workflow/STATE.md`
4. `suno_universal_workflow/WORKPLAN.md`
5. `suno_universal_workflow/BRIEF.md`
6. `suno_universal_workflow/OUTLINE.md`
7. `suno_universal_workflow/drafts/TEMPLATES.md`
8. `suno_universal_workflow/drafts/STYLE_PROMPT_SPEC.md`
9. `suno_universal_workflow/drafts/PROMPT_PACK.md`
10. `suno_universal_workflow/drafts/QUALITY_GATE.md`

## Required Read Order (Start Here Every Time)
1. `AGENTS.MD`
2. `suno_universal_workflow/STATE.md`
3. `suno_universal_workflow/WORKPLAN.md`
4. `suno_universal_workflow/BRIEF.md`
5. `suno_universal_workflow/OUTLINE.md`
6. `suno_universal_workflow/drafts/TEMPLATES.md`
7. `suno_universal_workflow/drafts/STYLE_PROMPT_SPEC.md`
8. `suno_universal_workflow/drafts/PROMPT_PACK.md`
9. `suno_universal_workflow/drafts/QUALITY_GATE.md`
10. `suno_universal_workflow/drafts/COMMAND_ROUTER.md`
11. `suno_universal_workflow/LOG.md`

## Reference-Only Documents
- 아래 문서는 운영 지시가 아니라 배경/템플릿/대화 기록이다.
- 실행 경로 추론의 기준으로 사용하지 않는다.
- `ACHMAGE_Workflow_README.md`
- `appendix/state_board.md`
- `appendix/command_router.md`
- `appendix/quality_writing.md`
- `appendix/quality_research.md`
- `appendix/quality_coding.md`

## Hard Rules
1. 트랙 수는 항상 15곡 고정이다.
2. 모드(`VOCAL`/`INSTRUMENTAL`) 확정 전에 트랙 생성을 시작하지 않는다.
3. 출력 포맷은 `suno_universal_workflow/drafts/TEMPLATES.md` Output Schema를 강제한다.
4. 트랙별 `Suno Style Prompt`는 입력 `style_prompt` 원문을 verbatim으로 보존해야 한다.
5. 트랙별 `Suno Style Prompt`는 한 줄이며 공백 포함 1000자 미만이어야 한다.
6. 트랙별 `Suno Style Prompt`는 라벨(`Identity:` 등) 없이 5요소(Identity/Mood/Instruments/Performance/Production)를 포함해야 한다.
7. Instruments 파트는 명사 나열 금지, `plays/provides/supports` 동사를 포함해야 한다.
8. `lyrics_input`이 비어 있으면 모드는 반드시 `INSTRUMENTAL`이며 15트랙 전부 `Lyrics: Instrumental`이어야 한다.
9. `lyrics_input`이 있으면 모드는 반드시 `VOCAL`이며 15트랙 전부 완성 가사를 포함해야 한다(`Instrumental` 혼입 금지).
10. `VOCAL`에서 모든 트랙 가사는 입력 `lyrics_input`의 섹션 순서/섹션 개수/섹션별 라인 수 구조를 동일하게 따라야 하고, 총 분량도 템플릿 배수 범위를 벗어나면 실패 처리한다.
11. `VOCAL`에서 입력 `lyrics_input` 가사를 트랙 본문에 verbatim 복붙하면 실패 처리한다(모티프 계승만 허용).
12. 품질 점검(`suno_universal_workflow/drafts/QUALITY_GATE.md`) 없이 완료 처리하지 않는다.
13. 완료 시 `suno_universal_workflow/STATE.md`와 `suno_universal_workflow/LOG.md`를 반드시 갱신한다.
14. 상용 가사/후렴 직접 복제 금지, 특정 실존 아티스트 직접 모사 금지.

## Default Rules (Use When Input Is Missing)
- `concept_mode` 누락: `auto`
- `language` 누락: `lyrics_input` 언어 우선, 없으면 `ko`
- `lyrics_input` 존재: `VOCAL` 강제 (전 트랙 가사 생성)
- `lyrics_input` 없음: `INSTRUMENTAL` 강제 (전 트랙 `Lyrics: Instrumental`)
- `lyrics_input` 없음 + `mode_hint=vocal`: 입력 불충분으로 간주, `INSTRUMENTAL` 유지 후 보완요청 메모를 남긴다.

## Step-by-Step Workflow (Do Not Skip)
### Step 0 - Preflight
- Read: `suno_universal_workflow/STATE.md`, `suno_universal_workflow/WORKPLAN.md`
- Check:
- 현재 `Current Step`과 실제 수행 단계가 일치하는지 확인
- 파일 누락 여부 확인

### Step 1 - Input Normalize
- Read: `suno_universal_workflow/drafts/TEMPLATES.md`
- Action:
- 입력을 Input Schema 형태로 재구성
- 누락값은 `Default Rules`로 채움
- `lyrics_input`이 있으면 섹션 시그니처(순서/개수)와 섹션별 라인 수를 추출해 `lyrics_structure_blueprint`를 만든다.
- Output:
- 정규화된 입력 블록 1개

### Step 2 - Mode Resolve
- Read: `suno_universal_workflow/drafts/PROMPT_PACK.md`
- Action:
- `lyrics_input` 존재 여부로 `VOCAL`/`INSTRUMENTAL`를 단일 결정한다(애매 모드 금지).
- Output:
- mode 결정값 + 근거 1줄

### Step 3 - Album Concept Build
- Read: `suno_universal_workflow/OUTLINE.md`
- Action:
- 아래 6개 필드를 반드시 생성
- Output Contract:
- `Album Title`
- `Tagline`
- `Theme Sentence`
- `Theme Keywords`
- `Sound Palette`
- `Energy Curve (1~15)`

### Step 4 - 15-Track Blueprint
- Read: `suno_universal_workflow/WORKPLAN.md`
- Action:
- Track 01~Track 15 전부 생성
- Output Contract (per track):
- `Title`
- `Intent`
- `Energy (1~5)`
- `Variation Axis`

### Step 5 - Track Generation
- Read: `suno_universal_workflow/drafts/STYLE_PROMPT_SPEC.md`, `suno_universal_workflow/drafts/PROMPT_PACK.md`
- Action:
- 각 트랙에 `Suno Style Prompt` 생성
- 모드별 처리:
- `VOCAL`: 신규 가사 생성 + `lyrics_structure_blueprint`와 동일한 섹션 구조/라인 수 강제 + 입력 가사 verbatim 복붙 금지
- `INSTRUMENTAL`: `Lyrics: Instrumental` 고정
- Output Contract (per track):
- `Suno Style Prompt`
- `Suno Style Prompt Char Count`
- `Lyrics`

### Step 6 - Quality Gate
- Read: `suno_universal_workflow/drafts/QUALITY_GATE.md`
- Action:
- Quick/Diversity/Lyrics Gate 검사
- Style Prompt Gate(원문 보존/한줄/길이/5요소/라벨 금지) 검사
- `suno_universal_workflow/scripts/validate_album_file.ps1`로 자동 검증(모드/스타일프롬프트/가사구조/가사분량/복붙 검출 포함)
- Rule:
- fail 1개라도 있으면 Step 5로 되돌아가 수정
- pass 전에는 완료 금지

### Step 7 - Export
- Read: `suno_universal_workflow/drafts/TEMPLATES.md`
- Action:
- Markdown 기본 출력
- 필요 시 JSON 옵션 출력
- Check:
- 필드 누락 없음
- 트랙 수 15 유지

### Step 8 - State and Log Sync
- Write: `suno_universal_workflow/STATE.md`
- `Current Step`, `Next Step`, `Recent Decisions` 갱신
- Write: `suno_universal_workflow/LOG.md`
- 날짜, 작업, 결정, 변경 파일, 다음 액션 기록

## File Update Matrix
- 규칙 변경:
- `suno_universal_workflow/drafts/PROMPT_PACK.md`
- 스타일 프롬프트 규격 변경:
- `suno_universal_workflow/drafts/STYLE_PROMPT_SPEC.md`
- 스키마 변경:
- `suno_universal_workflow/drafts/TEMPLATES.md`
- 품질 기준 변경:
- `suno_universal_workflow/drafts/QUALITY_GATE.md`
- 자동 검증 규칙 변경:
- `suno_universal_workflow/scripts/validate_album_file.ps1`
- 단계 계획 변경:
- `suno_universal_workflow/WORKPLAN.md`
- 상태/이력 기록:
- `suno_universal_workflow/STATE.md`
- `suno_universal_workflow/LOG.md`

## Forbidden Behaviors
- 15트랙 미만/초과 생성
- 모드 확정 생략
- 원문 `style_prompt` 보존 누락
- 줄바꿈 포함 프롬프트 작성
- 1000자 이상 프롬프트 작성
- `Identity:` 같은 라벨 문자열 사용
- `lyrics_input` 없음 상태에서 `VOCAL` 생성
- `lyrics_input` 있음 상태에서 `Instrumental` 트랙 혼입
- `lyrics_input` 섹션 구조(순서/개수/라인 수) 미준수
- `lyrics_input` 가사 verbatim 복붙
- 품질 게이트 생략
- `suno_universal_workflow/STATE.md`/`suno_universal_workflow/LOG.md` 미갱신
- 경로를 임의 추정하여 잘못된 파일 수정
- 카피/직접 모사 금지 규칙 위반

## Completion Criteria
- 15트랙 전체 출력 완료
- 품질 게이트 pass
- `VOCAL`이면 15트랙 전부 샘플 가사 구조/분량 검증 pass
- `INSTRUMENTAL`이면 15트랙 전부 `Lyrics: Instrumental` 검증 pass
- `suno_universal_workflow/STATE.md` 최신화
- `suno_universal_workflow/LOG.md` 최신화
- 출력이 `suno_universal_workflow/drafts/TEMPLATES.md` 스키마와 일치
