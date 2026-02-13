# OUTPUT_SCHEMA (Gemini 3.0 Pro × Suno v5) v1.1

이 문서는 Symphonic Storm 앨범 워크플로우의 출력 스키마/제약 정의다.

## 1) 공통 제약 (Hard)
- 트랙 수: 기본 15곡(원하면 8~20으로 변경 가능)
- 트랙 간 **mutually exclusive**: 같은 곡처럼 느껴지지 않게 “주요 차별점”을 곡마다 1개 이상 고정
- 트랙 간 일관성: 앨범 컨셉/키워드/정서 아크는 유지
- Suno v5 장르 프롬프트: 공백 포함 **800자 내외(최대 1000자 미만)**
- 가사: 라인 수 기준을 우선하며 **1,300~2,200자(가이드)**
- 가사 포맷: Global Style 태그 + 섹션 헤더(`[Intro]`, `[Verse 1]`, `[Hook]`, `[Verse 2]`, `[Bridge / Outro]`) 포함
- Hook: 2–3줄 micro chant
- Verse 2: 시작 메타태그에 “Switch to …” 패턴 반드시 포함(Chopper 구간 태그 추가 가능)
- Suno 메타태그: 각 섹션 시작에 1줄(필요 시 섹션 내부 상태 변화 지점에 추가 1줄)
- 금지: 실존 아티스트/곡/가사를 “그대로 모사·복제”하는 지시/표현(프롬프트/가사 모두)

## 1-1) 가사 글자 예산 (Section Budget)
- 기준: 공백 포함, 줄바꿈은 기본 제외(필요 시 포함 옵션)
- 총합 하드 범위: 1,300~2,200자
- 섹션 타깃(±10% 허용):
  - Intro: 140
  - Verse 1: 520
  - Hook: 140
  - Verse 2: 600
  - Bridge / Outro: 200
- 자동 체크 도구: `tools/lyrics_char_budget.py` (권장)

## 2) 앨범 청사진(BluePrint) 스키마
`.blueprint` 단계에서 반드시 아래 정보를 포함한다(가사는 금지).

- `album_working_title`: 작업용 제목(최종 제목은 `.finalize`에서 확정 가능)
- `logline`: 1문장 컨셉 문장
- `themes`: 5~9개 키워드
- `narrative_arc`: 4~6단계 감정/메시지 진행(예: 장엄한 분석→촉구→폭발→차갑게 정리)
- `sonic_palette`:
  - `bpm_range`: 220–240
  - `core_drums`: symphonic trap, ultra-fast hats, dense snares
  - `harmonic_language`: minor-key, dark orchestral + synth layers
  - `signature_motifs`: presto staccato strings, brass/timpani hits, short chant hook
  - `mix_notes`: dry vocal, tight low-end, wide strings
- `tracklist` (15개):
  - `no` (01~15)
  - `title`
  - `role_in_album`(이 곡이 앨범에서 하는 일)
  - `sub_theme`(컨셉의 하위 테마)
  - `primary_differentiator`(이 곡만의 핵심 차별점 1개)
  - `tempo_bpm`(220–240 정수)
  - `groove/beat_tag`(symphonic trap, double-time, triplet burst 등)
  - `hook_mode`(micro chant 2–3 lines)
  - `flow_palette`(regal legato/double → symphonic triplet → sextuplet rage)
  - `verse2_switch_tag`(예: "Switch to ultra-fast aggressive Korean chopper rap")
  - `avoid_repetition_note`(다른 곡과 겹치지 않기 위한 주의점)

## 3) 트랙 산출물 스키마
`.generate tracks=…`에서 각 트랙마다 아래를 출력한다.

- `track_title`
- `genre_prompt` (Suno v5 / 800자 내외)
- `lyrics` (1,300~2,200자 가이드, 라인 수 우선)

권장 추가(짧게):
- `micro-variation`(이번 곡에서 반복 모티프를 어떻게 변주했는지 1~2줄)
- `char_budget_check`(섹션별/총합 점검: OK/LOW/HIGH, 필요 시 `tools/lyrics_char_budget.py`로 검증)

## 4) 마크다운 Export 스키마(최종 파일 1개)
`.export` 결과는 아래 섹션 순서를 따른다.

1. 앨범 제목/한줄 소개
2. 컨셉/키워드/정서 아크/사운드 팔레트
3. 트랙리스트(표 또는 번호 목록)
4. 트랙별 섹션(01~15):
   - 장르 프롬프트(1줄~몇 줄)
   - 가사(코드블록)
5. 커버 이미지 생성 프롬프트(1~3안)
