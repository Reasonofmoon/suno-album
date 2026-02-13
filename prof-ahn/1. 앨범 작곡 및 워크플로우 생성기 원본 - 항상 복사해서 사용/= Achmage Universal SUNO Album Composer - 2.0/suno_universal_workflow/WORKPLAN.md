# WORKPLAN - SUNO Universal Album Composer

## Step 1 - I/O Schema Fix
### Output
- 입력 스키마 확정
- 출력 스키마 확정
- 스타일 프롬프트 하드 제약 확정(원문 보존, 5요소, 한 줄, 1000자 미만)

### Done Definition
- `instrumental`/`vocal` 입력이 모두 문서화되어 있다.
- 출력 필드와 형식이 고정되어 있다.
- `Suno Style Prompt` 제약이 스키마에 명시되어 있다.

## Step 2 - Concept Module
### Output
- 앨범 컨셉 생성 규칙
- `auto`/`user` 분기 규칙

### Done Definition
- 동일 입력에서 재현 가능한 컨셉 구조가 나온다.

## Step 3 - 15-Track Blueprint Rule
### Output
- 15트랙 에너지 커브 설계 규칙
- 트랙 메타 필드 템플릿

### Done Definition
- 어떤 입력에도 15트랙 구조가 누락 없이 생성된다.

## Step 4 - Style Prompt Rule
### Output
- 공통 키워드(고정) + 트랙 변주 키워드(가변) 결합 규칙
- 금지 요청 필터링 규칙
- 5요소 기반 작성 규칙(Identity/Mood/Instruments/Performance/Production)
- 라벨 금지 규칙(`Identity:` 등 금지, 내용만 작성)
- 한 줄 규칙(줄바꿈 금지) + 길이 규칙(공백 포함 <1000)
- 원문 보존 규칙(입력 `style_prompt` 그대로 포함)
- Instruments 동사 규칙(`plays/provides/supports`)

### Done Definition
- 트랙별 프롬프트가 통일감/차별성을 동시에 가진다.
- 모든 트랙의 프롬프트가 규격 검증을 통과한다.

## Step 5 - Lyrics or Instrumental Rule
### Output
- `lyrics_input` 기반 모드 강제 규칙 (`lyrics_input` 없음 -> `INSTRUMENTAL`, 있음 -> `VOCAL`)
- `VOCAL`용 가사 생성 규칙(입력 가사의 섹션 구조/섹션별 라인 수 템플릿 강제)
- `INSTRUMENTAL`용 출력 규칙(15트랙 전부 `Lyrics: Instrumental`)
- `VOCAL` 복붙 방지 규칙(입력 가사 verbatim 재사용 상한)

### Done Definition
- Mode A/Mode B 모두 출력 포맷이 흔들리지 않는다.
- `VOCAL`에서 15트랙 전부 구조 시그니처가 입력 가사와 일치한다.
- `VOCAL`에서 입력 가사 verbatim 복붙 트랙이 0개다.

## Step 6 - Quality Gate and Fix Loop
### Output
- Quick Gate 체크리스트
- Fail 시 수정 절차
- 스타일 프롬프트 자동 검증 절차(길이/한줄/원문 보존/5요소)
- 가사 구조/분량 자동 검증 절차(섹션 순서/섹션별 라인 수/총 분량)
- 가사 복붙 자동 검출 절차(템플릿 라인 재사용 비율)

### Done Definition
- 통일감/다양성/안전성 3축으로 pass/fail 판정이 가능하다.
- 스타일 프롬프트 구조 불량(짧은 프롬프트, 라벨 사용, 줄바꿈, 원문 손실)을 검출 가능하다.
- `lyrics_input` 기반 모드 위반(무단 Instrumental 혼입/무단 Vocal 생성)을 검출 가능하다.
- `VOCAL`에서 가사 구조 미준수와 과도한 템플릿 복제를 검출 가능하다.

## Step 7 - Export Pack
### Output
- Markdown 최종 템플릿
- JSON 옵션 템플릿

### Done Definition
- 사용자가 트랙별로 바로 복붙 가능하다.
