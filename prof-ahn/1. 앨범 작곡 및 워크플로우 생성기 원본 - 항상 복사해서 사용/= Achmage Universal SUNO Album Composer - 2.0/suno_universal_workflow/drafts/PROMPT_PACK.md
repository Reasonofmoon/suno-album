# PROMPT_PACK - SUNO Universal 15-Track Composer

## Purpose
- 단일 SUNO 입력을 15트랙 컨셉 앨범 출력으로 확장한다.
- 트랙별 `Suno Style Prompt`를 `STYLE_PROMPT_SPEC.md` 규격으로 강제한다.

## INPUT
- `style_prompt`: 필수
- `lyrics_input`: 선택
- `concept_mode`: `auto` 또는 `user`
- `concept_request`: 선택
- `language`: 선택 (미입력 시 `lyrics_input` 언어를 우선, 없으면 한국어)
- `mode_hint`: 선택 (`instrumental`/`vocal`)

## MODE RESOLUTION
- `lyrics_input`이 비어 있으면 `INSTRUMENTAL` 강제.
- `lyrics_input`이 있으면 `VOCAL` 강제.
- `mode_hint`는 참고용이며 위 규칙을 뒤집을 수 없다.

## RULES
- 트랙 수는 반드시 15곡.
- 앨범 공통 키워드 3~5개를 고정하고, 각 트랙 변주 키워드 2~4개를 분리한다.
- `VOCAL` 가사는 신규 작성하고 입력 가사의 모티프/정서만 계승한다(입력 가사 verbatim 복붙 금지).
- `VOCAL`은 입력 `lyrics_input`에서 섹션 순서/섹션 개수/섹션별 라인 수를 추출해 15트랙 전부 동일하게 적용한다.
- `INSTRUMENTAL`은 15트랙 전부 `Lyrics: Instrumental`로 고정한다.
- 기존 상용곡 가사/후렴 직접 복제 금지.
- 특정 실존 아티스트 직접 모사 금지.

## STYLE PROMPT RULES (HARD)
- 상세 규격은 `STYLE_PROMPT_SPEC.md`를 우선 따른다.
- 각 트랙 `Suno Style Prompt`는 입력 `style_prompt` 원문을 1회 이상 그대로 포함한다.
- 각 트랙 `Suno Style Prompt`는 줄바꿈 없이 한 줄이어야 한다.
- 각 트랙 `Suno Style Prompt`는 공백 포함 1000자 미만이어야 한다.
- 각 트랙 `Suno Style Prompt`는 5요소(Identity/Mood/Instruments/Performance/Production)를 모두 포함한다.
- `Identity:`, `Mood:`, `Instruments:`, `Performance:`, `Production:` 라벨 문자열은 금지한다.
- Instruments 서술에는 `plays`/`provides`/`supports` 동사를 최소 3회 이상 사용한다.
- 기본 출력 키는 `Suno Style Prompt`이며 `[Genre Tag]`는 사용하지 않는다.

## LYRICS RULES (HARD)
- `lyrics_input` 없음: `INSTRUMENTAL` 고정, 전 트랙 `Lyrics: Instrumental`.
- `lyrics_input` 있음: `VOCAL` 고정, 전 트랙 완성 가사.
- `VOCAL`에서 트랙별 가사 섹션 시그니처는 입력 가사와 동일해야 한다.
- `VOCAL`에서 섹션별 라인 수는 입력 가사와 동일해야 한다(기본 허용 오차 0).
- `VOCAL`에서 트랙 가사 총 분량은 입력 가사 대비 유사 범위(기본 0.85~1.25 배수)를 유지한다.
- `VOCAL`에서 입력 가사 라인 재사용 비율은 기본 0.25 이하여야 한다.

## OUTPUT FORMAT (Markdown)
```markdown
# Album Concept
- Album Title:
- Tagline:
- Theme Sentence:
- Theme Keywords:
- Sound Palette:
- Energy Curve (1~15):

# Tracklist (15)
## Track 01
- Title:
- Intent:
- Energy:
- Variation Axis:
- Suno Style Prompt:
- Suno Style Prompt Char Count:
- Lyrics:

## Track 02
- Title:
- Intent:
- Energy:
- Variation Axis:
- Suno Style Prompt:
- Suno Style Prompt Char Count:
- Lyrics:

...

## Track 15
- Title:
- Intent:
- Energy:
- Variation Axis:
- Suno Style Prompt:
- Suno Style Prompt Char Count:
- Lyrics:
```
