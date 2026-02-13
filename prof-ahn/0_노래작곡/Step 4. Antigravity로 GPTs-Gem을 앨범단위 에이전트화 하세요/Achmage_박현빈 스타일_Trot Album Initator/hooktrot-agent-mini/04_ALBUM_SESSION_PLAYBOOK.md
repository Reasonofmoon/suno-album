# 04_ALBUM_SESSION_PLAYBOOK.md
Version: v0.1

목적
- HookTrot 에이전트를 앨범 단위로 운영할 때 필요한 최소 실행 절차를 한 문서로 제공한다.

## 1) 세션 시작
명령:
- `.album.init 6 여름밤 행사장 네오트로트`

반드시 생성/출력할 것:
- `ALBUM_STATE`
- `Tracklist Plan`
- `TRACKLOG_COLLECTION`

## 2) 트랙 생성 루프
명령:
- `.album.next` 또는 `.album.track T03`

반드시 포함:
- Track 완제품 (Title + Style Prompt + Full Lyrics + TRACKLOG)
- Updated `ALBUM_STATE`
- Updated `TRACKLOG_COLLECTION`

## 3) 품질 루프
명령:
- `.qa` (트랙 단위)
- `.album.qa` (앨범 단위)

통과 기준:
- 트랙: Q-Score >= 24 and 필수축 통과
- 앨범: Q-GATE 5 통과

## 4) 완료 조건
아래 모두 충족 시 완료:
- 모든 트랙 `qa_pass` 또는 `locked`
- 앨범 QA 최종 판정 `ALBUM PASS`
- 최종 `TRACKLOG_COLLECTION` 확정

## 5) 권장 파일 운영
- `ALBUM_STATE.md`: 현재 앨범 상태 스냅샷
- `TRACKLOG_COLLECTION.md`: 트랙 DNA 기록
- 필요 시 `appendix/state_board.md` 규약 적용
