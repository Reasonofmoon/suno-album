# STYLE_PROMPT_SPEC

## Objective
- 트랙별 `Suno Style Prompt`를 짧은 태그 수준이 아닌 실제 생성 제어가 가능한 밀도로 작성한다.
- 입력 원문 스타일 프롬프트의 정체성을 잃지 않고, 트랙별 변주를 안전하게 확장한다.

## Hard Format Contract
1. 입력 `style_prompt` 원문을 프롬프트 안에 **verbatim**으로 보존한다.
2. 프롬프트는 반드시 **한 줄**이다. 줄바꿈/엔터 금지.
3. 프롬프트 길이는 공백 포함 **450~999자**.
4. 아래 5요소를 모두 포함한다:
- Identity
- Mood
- Instruments
- Performance
- Production
5. `Identity:`, `Mood:` 같은 라벨 문구는 쓰지 않는다. 내용만 작성한다.

## 5-Element Content Contract (라벨 없이 포함)
- Identity:
- 보컬 성별/편성 + 장르 정체성을 1문장으로 포함
- Mood:
- 템포(BPM/tempo) + 정서 + (선택) 조성/모드
- Instruments:
- 악기 나열 금지, 연주 동사를 반드시 포함
- 권장 동사: `plays`, `provides`, `supports`
- Performance:
- 보컬 텍스처, 전달 방식, 음역/레인지, 프레이징 묘사
- Production:
- 공간감, 리버브 양, 믹스 배치, 새츄레이션/로파이/클린 성향

## Compression Rules
- 콜론 라벨을 빼고 쉼표/세미콜론으로 정보 밀도를 높인다.
- 동일 의미 반복을 줄이고 수식어를 기능어로 치환한다.
- 트랙 변주어는 2~4개만 넣고 나머지는 앨범 공통 어휘를 유지한다.

## Suggested Clause Order
1. 입력 원문 스타일 프롬프트 verbatim
2. 트랙별 mood/energy 변주
3. 악기 연주 동사 구문
4. 보컬 수행 디테일
5. 프로덕션 디테일

## Required Keywords (at least one per line)
- Instruments verbs: `plays` or `provides` or `supports`
- Performance cues: `texture`, `delivery`, `register`, `range`, `phrasing` 중 1개 이상
- Production cues: `space`, `reverb`, `mix`, `saturation`, `clarity`, `mic` 중 1개 이상

## Non-Compliant Example
- `Female solo vocal, Jazz-Funk, high energy, wide stage.`  
문제: 너무 짧음, 원문 보존 없음, 5요소 누락, 동사 기반 악기 묘사 없음.

## Compliant Example (single line)
- `Female solo vocal / Space-noir Latin Jazz × Hard Bop × Jazz-Funk, 138 BPM, 4/4 hard swing, C minor w/ Dorian color. Minimalist arrangement: bongo + upright bass vamp, brushy drums, sparse muted-trumpet hits, tight sax unison riffs. Whisper-to-punch dynamics, stop-time breaks, wide stage but intimate mics, warm vintage tone with modern clarity, New Year city-loner resolve with anxious hope, bongo plays clipped heartbeat syncopation, upright bass provides a tense looping vamp, brush drums support hard-swing lift, muted trumpet provides short neon cuts, sax unison supports sharp stop-time pivots, vocal texture moves from breathy whisper to focused chest register, delivery stays restrained then decisive, phrasing lands late then snaps on accents, intimate front-center mix with medium plate reverb, low tape saturation, clear transient edges.`
