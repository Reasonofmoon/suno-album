# BRIEF

## Goal
김광석 스타일의 단일 곡 프롬프트를 앨범 단위로 확장하는 에이전트 워크플로우를 설계한다.

## Deliverables
- 앨범 단위 에이전트 워크플로우 문서(테마/컨셉/주제/작곡 구조/트랙 변주 포함).
- 길이 검수 프로세스(`browser_subagent` + textcount) 포함.
- 실행 모델: Gemini 3.0 Pro 명시.

## Constraints
- 앨범 테마/컨셉은 김광석 에이전트 map.MD 세계관과 일치해야 한다.
- 곡들은 앨범 테마로 이어지되 상호 차별성이 있어야 한다.
- 장르 프롬프트: 영어, 공백 포함 900~1000자(범위 밖이면 재생성). 스타일 전용 블록이며 가사 포함 금지.
- 가사: 한글, 공백 포함 4000~5000자(범위 밖이면 재생성).
- 길이 검수는 `universal_browser_control`의 `browser_subagent`로 https://textcount.sawoo.com/ 에서 수행.

## Assumptions
- 기존 단일 곡 프롬프트 형식은 `김광석 에이전트 map.MD`에 정의되어 있다.
- 브라우저 자동화는 `universal_browser_control.md`의 절차를 따른다.
