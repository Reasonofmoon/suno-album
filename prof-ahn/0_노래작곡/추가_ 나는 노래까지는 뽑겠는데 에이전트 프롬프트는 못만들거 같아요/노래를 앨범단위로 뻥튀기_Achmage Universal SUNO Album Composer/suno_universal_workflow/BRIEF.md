# BRIEF - SUNO Universal Album Composer Workflow

## Goal
- 사용자 입력(SUNO style prompt, 선택 가사, 컨셉 요청)을 받아 15트랙 앨범으로 확장 가능한 워크플로우를 제공한다.
- 각 트랙별 `Style Prompt`와 `Lyrics`(또는 `Instrumental`)를 재사용 가능한 포맷으로 출력한다.

## Target Users
- 단일 곡 아이디어를 앨범 단위로 확장하고 싶은 SUNO 사용자
- 컨셉 앨범(테마/서사/무드)을 빠르게 설계하려는 크리에이터

## Input Modes
- Mode A: `instrumental` (`lyrics_input` 없음, style prompt만 입력)
- Mode B: `vocal` (`lyrics_input` 있음, style prompt + lyrics 입력)
- Concept Mode 1: `auto` (AI가 앨범 컨셉 제안)
- Concept Mode 2: `user` (사용자 컨셉 우선 반영)

## Core Constraints
- 출력 트랙 수는 정확히 15곡이다.
- `lyrics_input`이 비어 있으면 모드는 `INSTRUMENTAL` 고정이며, 15트랙 모두 `Lyrics: Instrumental`이어야 한다.
- `lyrics_input`이 있으면 모드는 `VOCAL` 고정이며, 15트랙 모두 완성 가사를 가져야 한다.
- `VOCAL`에서는 입력 가사의 섹션 순서/섹션 개수/섹션별 라인 수를 15트랙 전부 동일하게 유지한다.
- `VOCAL`에서는 입력 가사의 verbatim 복붙을 금지하고 모티프/정서만 계승한다.
- 앨범 통일감(핵심 키워드/사운드 팔레트)과 트랙 변주(에너지/템포/악기/시점)를 동시에 유지한다.
- 트랙별 `Suno Style Prompt`는 입력 `style_prompt` 원문을 최소 1회 **그대로 보존**한 뒤 확장한다.
- 트랙별 `Suno Style Prompt`는 반드시 **한 줄**로 작성하고 줄바꿈/엔터를 포함하지 않는다.
- 트랙별 `Suno Style Prompt`는 공백 포함 **1000자 미만**이어야 하며, 5요소(Identity/Mood/Instruments/Performance/Production)를 모두 포함해야 한다.
- 트랙별 `Suno Style Prompt` 안에는 `Identity:`, `Mood:` 같은 라벨을 쓰지 않고 내용만 압축해 작성한다.
- Instruments 파트는 명사 나열이 아니라 `plays/provides/supports` 같은 연주 동사와 함께 작성한다.
- 기존 상용곡 가사/후렴의 직접 복제는 금지한다.
- 특정 실존 아티스트를 직접 모사하지 않고 속성 기반으로 묘사한다.

## Success Criteria
- 입력이 Mode A/Mode B 어느 쪽이어도 동일한 출력 구조를 유지한다.
- 앨범 컨셉, 15트랙 블루프린트, 트랙별 생성물(Style Prompt + Lyrics/Instrumental)이 한 번에 생성된다.
- 모든 트랙의 `Suno Style Prompt`가 위 규격(원문 보존, 5요소 확장, 한 줄, 1000자 미만, 라벨 금지)을 통과한다.
- `VOCAL`에서 모든 트랙 가사가 입력 가사의 구조/분량 형식을 통과하고, 템플릿 verbatim 복붙이 검출되지 않는다.
- 결과물을 SUNO에 복붙하기 쉬운 Markdown 구조로 제공한다.
