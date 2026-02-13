# AGENTS.MD — Reason Moon Suno Composer

## What This Is
- AI 에이전트가 따르는 실행 계약서
- 음악 생성 시스템의 운영 규칙 정의

## Scope
- 작업 루트: `music-system/`
- 스킬 정의: `SKILL.md`
- 워크플로우 템플릿: `workflows/`

## Priority Order
1. 사용자의 최신 직접 지시
2. `AGENTS.MD`
3. `SKILL.md`
4. `workflows/` 내 해당 템플릿

## Hard Rules
1. 상용 가사/후렴 직접 복제 금지
2. 특정 실존 아티스트 직접 모사 금지 (구조·패턴만 참조)
3. Style Prompt: 한 줄 / 200~999자 / 5-Element / 라벨 문자열 금지
4. Instruments 서술에 연주 동사(`plays`/`provides`/`supports`) 필수
5. lyrics_input이 있으면 VOCAL 강제, verbatim 복붙 금지
6. lyrics_input이 없으면 INSTRUMENTAL 강제
7. 바이럴 가사: 줄당 5~9음절, 훅 2회 이상 반복

## Forbidden Behaviors
- 발라드형 멜로디를 랩 페르소나에 적용
- 품질 검증 생략
- 에너지 커브와 불일치하는 트랙 생성
- 과도한 질문 (기본값으로 진행 후 가정 명시)
- 앨범 모드에서 지정 곡 수 미달/초과

## Completion Criteria
- Single: [Suno Style] + [Suno Lyrics] 출력 완료
- Album: 全트랙 Style Prompt + Lyrics + 품질 검증 pass
