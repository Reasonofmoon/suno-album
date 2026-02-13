# TEMPLATES

## Input Schema
| Field | Type | Required | Description |
|---|---|---|---|
| style_prompt | string | Yes | SUNO 스타일/장르 프롬프트 원문 |
| lyrics_input | string | No | 기존 가사 또는 메모 |
| concept_mode | enum(auto,user) | Yes | 컨셉 생성 방식 |
| concept_request | string | No | 사용자 지정 테마/키워드/금지요소 |
| language | string | No | 가사 언어 |
| mode_hint | enum(instrumental,vocal) | No | 사용자가 강제 지정할 모드 |
| style_prompt_lock | boolean | No | 기본값 `true`, 원문 style_prompt verbatim 보존 여부 |
| lyrics_structure_lock | boolean | No | 기본값 `true`(lyrics_input 존재 시), 샘플 가사 구조/분량 형식 강제 여부 |
| lyrics_reuse_max_ratio | number(0~1) | No | 기본값 `0.25`, 샘플 가사 라인 verbatim 재사용 허용 상한 |

## Input JSON Example
```json
{
  "style_prompt": "cinematic synthwave, neon night drive, analog bass, wide pads",
  "lyrics_input": "",
  "concept_mode": "auto",
  "concept_request": "도시의 심야 감정선, 희망으로 끝나는 흐름",
  "language": "ko",
  "mode_hint": "instrumental",
  "style_prompt_lock": true,
  "lyrics_structure_lock": true,
  "lyrics_reuse_max_ratio": 0.25
}
```

## Style Prompt Hard Spec
- 상세 규격: `STYLE_PROMPT_SPEC.md`
- 한 줄(줄바꿈 없음), 공백 포함 450~999자(하드 범위)
- 입력 `style_prompt` 원문 verbatim 포함
- 라벨 문자열(`Identity:` 등) 금지
- 5요소(Identity/Mood/Instruments/Performance/Production) 모두 포함

## Lyrics Policy Hard Spec
- `lyrics_input`이 비어 있으면 모드는 `INSTRUMENTAL` 고정, 15트랙 전부 `Lyrics: Instrumental`.
- `lyrics_input`이 있으면 모드는 `VOCAL` 고정, 15트랙 전부 완성 가사.
- `VOCAL`에서는 `lyrics_input`에서 추출한 섹션 순서/섹션 개수/섹션별 라인 수를 모든 트랙에 동일 적용.
- `VOCAL`에서는 `lyrics_input`의 verbatim 복붙 금지, 트랙별 템플릿 라인 재사용 비율은 기본 `<= 0.25`.

## Output Schema
| Section | Field | Description |
|---|---|---|
| Album Concept | Album Title | 앨범 제목 |
| Album Concept | Tagline | 한 줄 태그라인 |
| Album Concept | Theme Sentence | 컨셉 한 문장 |
| Album Concept | Theme Keywords | 핵심 키워드 목록 |
| Album Concept | Sound Palette | 사운드 재료 |
| Album Concept | Energy Curve | 1~15 에너지 설계 |
| Track n | Title | 트랙 제목 |
| Track n | Intent | 트랙 역할/장면 |
| Track n | Energy | 1~5 |
| Track n | Variation Axis | 변주 축 |
| Track n | Suno Style Prompt | SUNO 입력 프롬프트 |
| Track n | Suno Style Prompt Char Count | 공백 포함 길이(정수) |
| Track n | Lyrics | 가사 또는 Instrumental 표기 |

## Output JSON Example (축약)
```json
{
  "album_concept": {
    "album_title": "Midnight Transit",
    "tagline": "도시의 어둠을 통과해 새벽으로",
    "theme_sentence": "고요한 불안에서 점진적 해방으로 이동하는 심야 여정",
    "theme_keywords": ["neon", "asphalt", "pulse", "haze", "dawn"],
    "sound_palette": ["analog bass", "wide pads", "tight drums", "soft arps"],
    "energy_curve": [1,2,2,3,3,4,4,5,5,4,4,3,2,2,1]
  },
  "tracks": [
    {
      "track_no": 1,
      "title": "Cold Station",
      "intent": "정적과 잔향으로 시작하는 도입부",
      "energy": 1,
      "variation_axis": "sparse drums",
      "suno_style_prompt": "cinematic synthwave, neon night drive, analog bass, wide pads, female solo vocal with restrained determination, 112 BPM mid-tempo with hopeful tension, bongo plays clipped syncopation, upright bass provides steady pulse, brushed snare supports swing lift, muted trumpet provides short answer phrases, vocal texture shifts from breathy low register to focused mid range, delivery starts intimate then firm, phrasing delays then locks on downbeat, narrow room space with medium plate reverb, vocal front-center mix, low tape saturation, warm tone with clear transients",
      "suno_style_prompt_char_count": 753,
      "lyrics": "Instrumental"
    }
  ]
}
```
