# OUTPUT_SCHEMA (Gemini 3.0 Pro × Suno v5) v1.0

이 문서는 “앨범 단위” 결과물을 안정적으로 뽑기 위한 출력 스키마/제약 정의다.

## 1) 공통 제약 (Hard)
- 트랙 수: 기본 15곡(원하면 8~20으로 변경 가능)
- 트랙 간 **mutually exclusive**: 같은 곡처럼 느껴지지 않게 “주요 차별점”을 곡마다 1개 이상 고정
- 트랙 간 일관성: 앨범 컨셉/키워드/정서 아크는 유지
- Suno v5 장르 프롬프트: 공백 포함 **800자 내외(최대 1000자 미만)**
- 가사: 공백 포함 **4,000~5,000자(하드)**, 목표 5,000자
- 가사 포맷: 섹션 헤더(`[Intro]`, `[Verse 1]`, `[Hook]`, `[Verse 2]`, `[Bridge]`, `[Final Hook]`, `[Outro]`) 포함
- Suno 메타태그: 각 섹션 시작에 1줄(필요 시 섹션 내부 상태 변화 지점에 추가 1줄)
- 금지: 실존 아티스트/곡/가사를 “그대로 모사·복제”하는 지시/표현(프롬프트/가사 모두)

## 1-1) 가사 글자 예산 (Section Budget)
- 기준: 공백 포함, 줄바꿈은 기본 제외(필요 시 포함 옵션)
- 총합 하드 범위: 4,000~5,000자
- 섹션 타깃(±10% 허용):
  - Intro: 250
  - Verse 1: 1,200
  - Hook: 600
  - Verse 2: 1,500
  - Bridge: 600
  - Final Hook: 600
  - Outro: 250
- Final Hook을 생략하면 600자를 Verse 2/Hook/Outro 중 하나로 재분배(총합 범위 유지).
- 자동 체크 도구: `tools/lyrics_char_budget.py` (권장)

## 2) 앨범 청사진(BluePrint) 스키마
`.blueprint` 단계에서 반드시 아래 정보를 포함한다(가사는 금지).

- `album_working_title`: 작업용 제목(최종 제목은 `.finalize`에서 확정 가능)
- `logline`: 1문장 컨셉 문장
- `themes`: 5~9개 키워드
- `narrative_arc`: 4~6단계 감정/메시지 진행(예: 의심→각성→선언→충돌→결의→축복)
- `sonic_palette`:
  - `bpm_range`: 예) 152–182
  - `core_drums`: 킥/스네어/하이햇 질감, 그루브 성향
  - `harmonic_language`: 마이너/모달/코러스 등
  - `signature_motifs`: 반복될 모티프(피아노 리프/브라스 스탭/합창 샘플 등)
  - `mix_notes`: 보컬 전면/드라이/서브베이스 타이트 등
- `tracklist` (15개):
  - `no` (01~15)
  - `title`
  - `role_in_album`(이 곡이 앨범에서 하는 일)
  - `sub_theme`(컨셉의 하위 테마)
  - `primary_differentiator`(이 곡만의 핵심 차별점 1개)
  - `tempo_bpm`(정수)
  - `groove/beat_tag`(예: boom-bap×trap, drill, jersey club, DnB 등)
  - `hook_mode`(chant/rap hook/call&response 등)
  - `flow_palette`(double-time, triplet burst, swung 16th 등)
  - `avoid_repetition_note`(다른 곡과 겹치지 않기 위한 주의점)

## 3) 트랙 산출물 스키마
`.generate tracks=…`에서 각 트랙마다 아래를 출력한다.

- `track_title`
- `genre_prompt` (Suno v5 / 800자 내외)
- `lyrics` (4,000~5,000자)

권장 추가(짧게):
- `micro-variation`(이번 곡에서 반복 모티프를 어떻게 변주했는지 1~2줄)
- `char_budget_check`(Intro~Outro 섹션별/총합 점검: OK/LOW/HIGH, 필요 시 `tools/lyrics_char_budget.py`로 검증)

## 4) 마크다운 Export 스키마(최종 파일 1개)
`.export` 결과는 아래 섹션 순서를 따른다.

1. 앨범 제목/한줄 소개
2. 컨셉/키워드/정서 아크/사운드 팔레트
3. 트랙리스트(표 또는 번호 목록)
4. 트랙별 섹션(01~15):
   - 장르 프롬프트(1줄~몇 줄)
   - 가사(코드블록)
5. 커버 이미지 생성 프롬프트(1~3안)
