# COMMAND_ROUTER - SUNO Workflow

## Commands
- `.plan`: `../WORKPLAN.md` 업데이트/보정
- `.run step=1`: I/O 스키마 고정
- `.run step=2`: 컨셉 모듈 규칙 확정
- `.run step=3`: 15트랙 블루프린트 확정
- `.run step=4`: Style Prompt 규칙 확정
- `.run step=5`: Lyrics/Instrumental 규칙 확정
- `.run step=6`: 품질 게이트 점검
- `.run step=7`: Export 포맷 완성
- `.review`: `QUALITY_GATE.md`로 pass/fail 판정
- `.validate-album file=<album_file.md> base=\"<style_prompt>\" mode=<VOCAL|INSTRUMENTAL> lyrics_template=<path|inline_text>`: 스타일+가사 구조/분량/복붙 포함 통합 검증
- `.log`: `../LOG.md`/`../STATE.md` 업데이트

## Routing Rule
- 사용자 요청이 자유 텍스트면 가장 가까운 명령으로 내부 매핑한다.
- 한 턴에는 명령 1개만 수행한다.
- `.review`가 fail이면 다음 step으로 진행하지 않고 fix 먼저 수행한다.
- `.validate-album`이 fail이면 `.run step=5`와 `.run step=6`을 반복해 통과할 때까지 수정한다.
