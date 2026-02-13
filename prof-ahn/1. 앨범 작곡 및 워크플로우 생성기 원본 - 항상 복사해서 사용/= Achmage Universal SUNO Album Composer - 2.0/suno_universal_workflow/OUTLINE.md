# OUTLINE - SUNO 15-Track Workflow

## 1. Input Normalization
- 입력 필드 검증: `style_prompt`, `lyrics_input`, `concept_request`, `language`, `mode_hint`
- 모드 판정: `lyrics_input` 없음 -> `INSTRUMENTAL`, `lyrics_input` 있음 -> `VOCAL`
- `lyrics_input` 존재 시 가사 구조 블루프린트 추출(섹션 순서/섹션 수/섹션별 라인 수)
- 금지 조건 사전 정리: 직접 카피/직접 모사 요청 제거

## 2. Album Concept Builder
- 컨셉 모드 분기: `auto` 또는 `user`
- 산출물 생성:
- `Album Title`
- `Tagline`
- `Theme Sentence`
- `Theme Keywords (5~9)`
- `Sound Palette (3~7)`
- `Energy Curve (track 1~15)`

## 3. 15-Track Blueprint
- 각 트랙 필드:
- `Track No`
- `Track Title`
- `Intent (1 line)`
- `Energy (1~5)`
- `Variation Axis` (tempo/rhythm/instrument/vocal POV 중 최소 1개)

## 4. Track Generator
- 트랙별 `Style Prompt` 생성
- 앨범 공통 키워드 + 트랙 변주 키워드 결합
- 스타일 프롬프트 규격(강제):
- 입력 `style_prompt` 원문을 그대로 포함(보존)
- 출력은 한 줄(줄바꿈 금지), 공백 포함 1000자 미만
- `Identity/Mood/Instruments/Performance/Production` 정보를 모두 포함
- `Identity:`, `Mood:` 등의 라벨 금지 (내용만 압축)
- Instruments 문장은 `plays/provides/supports` 동사를 포함
- 모드별 출력:
- `VOCAL`: 입력 `lyrics_input` 블루프린트와 동일한 섹션 순서/섹션별 라인 수를 갖춘 신규 가사(verbatim 복붙 금지)
- `INSTRUMENTAL`: `Instrumental` 명시 + 보컬 부재 지시

## 5. Quality Gate
- 통일감 점검: 테마 키워드, 사운드 팔레트, 반복 모티프
- 다양성 점검: 템포/에너지/악기/리듬 분포
- 가사 점검: 모드 일관성(`VOCAL` 전곡 가사 / `INSTRUMENTAL` 전곡 Instrumental), 입력 가사 구조 준수, 분량 형식 준수, 템플릿 복붙 비율, 금지 조건 위반
- 스타일 프롬프트 점검: 원문 보존, 한 줄, 길이(<1000), 5요소 충족, 라벨 금지

## 6. Export
- 기본 포맷: Markdown
- 옵션 포맷: JSON
- 최종 패키지: `Album Concept` + `Tracklist 15` + `Copy/Paste blocks`
