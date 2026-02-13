# SUNO Universal Workflow

## What This Folder Contains
- `BRIEF.md`: 목표/제약/성공 기준
- `OUTLINE.md`: 모듈 구조
- `WORKPLAN.md`: 실행 단계
- `SOURCES.md`: 참고 링크 및 내부 참조
- `LOG.md`: 변경 이력
- `STATE.md`: 현재 상태 보드
- `drafts/*`: 실사용 프롬프트/템플릿/예시
- `scripts/validate_album_file.ps1`: 단일 앨범 파일 통합 검증(스타일 프롬프트 + 모드 + 가사 구조/분량/복붙)

## Run Order
1. `WORKPLAN.md` Step 1부터 순서대로 실행
2. `drafts/TEMPLATES.md`의 입력 스키마로 요청 정규화
3. `drafts/STYLE_PROMPT_SPEC.md` + `drafts/PROMPT_PACK.md` 규칙으로 출력 생성
4. `scripts/validate_album_file.ps1`로 앨범 단위 자동 검증
5. `drafts/QUALITY_GATE.md`로 점검 후 `WORKPLAN.md` Step 6 완료 처리
6. `LOG.md`, `STATE.md` 업데이트

## Minimum Command Pattern
- `.plan`: WORKPLAN 보정
- `.run step=N`: 해당 단계 수행
- `.validate-album file=<album_file.md> base=\"<style_prompt>\" mode=<VOCAL|INSTRUMENTAL> lyrics_template=<path|inline_text>`: 통합 하드 규격 검사
- `.review`: `drafts/QUALITY_GATE.md` 기준 점검
- `.log`: 변경 기록
