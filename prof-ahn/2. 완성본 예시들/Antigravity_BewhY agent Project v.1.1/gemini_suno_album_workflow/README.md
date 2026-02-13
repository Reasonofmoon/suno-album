# Gemini 3.0 Pro × Suno v5 — 앨범 프롬프트/가사 워크플로우 (v1.0)

이 폴더는 “앨범 단위(약 15곡)”로 **Suno v5 장르 프롬프트 + 가사**를 뽑고, 검토/재시도 후 **단일 MD 파일**로 정리하는 대화형 워크플로우다. 마지막에 **Gemini 내장 이미지 생성**으로 앨범 커버를 만들기 위한 프롬프트까지 포함한다.

## 핵심 파일
- `prompts/Gemini3_SUNO_Album_Agent.md`: Gemini에 그대로 붙여 넣는 “마스터 프롬프트”
- `OUTPUT_SCHEMA.md`: 길이/포맷/청사진(blueprint) 스키마
- `templates/ALBUM_PACK_TEMPLATE.md`: 최종 MD 파일 구조 템플릿
- `checklists/ALBUM_QUALITY_CHECKLIST.md`: 앨범/트랙 품질 체크리스트
- `reports/BewhY_Composition_Report_KR.md`: 참고용 분석 요약 보고서(기술/구조 관점)

## 이 저장소의 기존 자료(참고)
- `BewhY Lyric Analysis Framework.md`: 더 긴 분석 보고서(영문)
- `Achmage_BewhY_Rap_Agent_1.4.txt`: 1곡 단위 생성용 프롬프트(레퍼런스)

## Quick Start (Gemini UI 기준)
1. `prompts/Gemini3_SUNO_Album_Agent.md`를 Gemini 3.0 Pro에 붙여 넣는다.
2. Gemini가 `.init` 질문을 하면 답한다(모르면 “기본값으로 진행”이라고 답해도 됨).
3. `.blueprint` 결과(앨범 컨셉+15곡 트랙리스트)를 보고:
   - 통과: `APPROVE`
   - 수정: `REVISE: (수정 포인트)` 또는 `REJECT`(전면 재구성)
4. 통과되면 배치로 생성한다: 예) `.generate tracks=1-5` → `.generate tracks=6-10` → `.generate tracks=11-15`
5. 필요하면 `.review`로 품질 점검(pass/fail)과 수정 리스트를 받는다.
6. 앨범 제목을 확정하려면 `.finalize`를 실행한다.
7. 모든 트랙이 준비되면 `.export`로 **단일 MD 파일** 형태로 출력한다(길면 파트로 쪼개서 출력).
8. `.cover`로 커버 이미지 프롬프트를 받고, Gemini 이미지 생성 기능으로 1:1 앨범 커버를 만든다.

## 가사 글자 예산 체크
- 섹션별 예산(±10%)과 총합 4,000~5,000자 기준은 `OUTPUT_SCHEMA.md` 참고.
- 로컬 카운팅 도구: `tools/lyrics_char_budget.py`
- 사용 예: `python tools/lyrics_char_budget.py path\to\lyrics.txt`
- 줄바꿈 포함 카운트: `--include-newlines` 옵션

## Suno 사용 팁
- Suno의 스타일/장르 입력란에는 `Genre Prompt`를 붙여 넣고,
- 가사 입력란에는 `Lyrics`를 붙여 넣는다(섹션/메타태그 포함).

## 주의(중요)
- 이 워크플로우는 “특정 실존 아티스트를 그대로 흉내 내는” 지시를 포함하지 않도록 설계되어 있다. 결과물은 **완전히 새로운 오리지널**을 목표로 한다.
