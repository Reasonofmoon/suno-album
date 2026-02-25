# RESONANCE Agent Protocol v1.0

> 에이전트 간 자동 통신 + 충돌 방지 규약

## 1. 세션 시작 시 필수 행동 (BOOT SEQUENCE)

모든 에이전트는 세션 시작 시 반드시 다음을 수행:

```text
1. PROMETHEUS_SYNC.md 읽기 → PATH_REGISTRY로 경로 확인
2. RESONANCE_SYNC.md 읽기 → 마지막 메시지 확인
3. LOCK_REGISTRY 확인 → 현재 잠긴 파일 확인
4. 미응답 메시지에 ACK 응답
5. 자기 작업 시작 전 LOCK 획득
```

### Codex Trigger Mapping

Codex가 아래 사용자 문구를 받으면 BOOT SEQUENCE를 즉시 실행:

- Trigger: `RESONANCE_SYNC.md 읽어줘`
- Action: `tools/dual_boot_sync.ps1` 실행
  - pending `EXPECTS_ACK: true` for `CODEX` 자동 탐지/ACK
  - pending `EXPECTS_ACK: true` for `ANTIGRAVITY` 자동 탐지/ACK
  - `shared/codex_inbox.md` + `shared/antigravity_inbox.md` 동시 갱신

### Always-On File Watch Mode

실시간 자동 감지가 필요하면 watcher 실행:

- `tools/watch_sync.ps1` (기본: 변경 감지 시 `dual_boot_sync.ps1` 자동 실행)
- 결과: 알림 + 양측 미응답 ACK 자동 처리 + inbox 자동 갱신

## 2. 메시지 프로토콜

### 메시지 형식

```text
---
[SEQ:NNN] [YYYY-MM-DD HH:MM KST] [FROM->TO] [TYPE]
TYPE: REQUEST | ACK | DONE | BLOCKED | HANDOFF
WHAT: 한 줄 요약
DETAIL: 상세 내용 (선택)
EXPECTS_ACK: true | false
FILES_TOUCHED: 변경한 파일 목록 (절대경로)
---
```

### 시퀀스 번호 (SEQ)

- 메시지마다 순차 번호 부여 (001, 002, 003...)
- ACK 시 원본 SEQ 참조: `ACK_FOR: SEQ:005`
- **EXPECTS_ACK: true** 메시지는 상대방이 반드시 ACK 필요

### 자동 감지 규칙

각 에이전트는 세션 시작 시:

1. RESONANCE_SYNC.md에서 **자신에게 온 미응답 메시지** 검색
2. `EXPECTS_ACK: true`인 메시지에 즉시 ACK 응답
3. `TYPE: REQUEST`인 메시지는 작업 시작 전 처리

## 3. 파일 소유권 맵 (OWNERSHIP)

### 배타적 소유 (충돌 없음)

| 경로 | 소유자 | 설명 |
| --- | --- | --- |
| `composer/*` | ANTIGRAVITY | 프롬프트, 테마, QA, 오디오 |
| `publisher/*` | CODEX | 메타데이터, 썸네일, 영상 |
| `tools/*` | CODEX | 자동화 스크립트 |

### 공유 자원 (LOCK 필요)

| 경로 | 소유 | LOCK 필요 |
| --- | --- | --- |
| `shared/distribution_strategy.md` | 공유 | ✅ |
| `shared/brand_guide.md` | 공유 | ✅ |
| `shared/constants.yaml` | 공유 | ✅ |
| `shared/album_registry.yaml` | 공유 | ✅ |
| `shared/content_calendar.yaml` | 공유 | ✅ |
| `RESONANCE_SYNC.md` | 공유 | ❌ (append-only) |

## 4. LOCK 메커니즘

### LOCK 파일: `shared/.locks.yaml`

```yaml
# 현재 활성 잠금
locks:
  - file: "shared/distribution_strategy.md"
    owner: "ANTIGRAVITY"
    since: "2026-02-15 21:00 KST"
    reason: "전략 v3 업데이트"
  # 비어있으면 잠금 없음
```

### LOCK 규칙

1. **공유 파일 수정 전** → `.locks.yaml`에 잠금 등록
2. **수정 완료 후** → 잠금 해제 + SYNC에 DONE 메시지
3. **잠금 충돌 시** → SYNC에 BLOCKED 메시지 → 대기
4. **30분 초과 잠금** → 자동 만료 (stale lock)

### LOCK 획득 절차

```text
1. .locks.yaml 읽기
2. 대상 파일에 활성 잠금이 없는지 확인
3. 잠금이 없으면 → 자기 잠금 추가 + 작업 시작
4. 잠금이 있으면 → RESONANCE_SYNC에 BLOCKED 메시지 작성 → 대기
```

## 5. HANDOFF 패턴 (파이프라인 전달)

COMPOSER → PUBLISHER 작업 전달 시:

```text
[SEQ:NNN] [FROM: ANTIGRAVITY->CODEX] [TYPE: HANDOFF]
WHAT: T01_V01 오디오 완성, 영상 제작 요청
FILES_READY:
  - composer/audio/T01_V01/manifest.csv
  - composer/audio/T01_V01/*.mp3
PUBLISHER_TODO:
  - render_album_video.ps1 실행
  - build_chapters.py 실행
  - publisher_seo_T01_V01.md 작성
EXPECTS_ACK: true
```

## 6. 충돌 방지 요약

```text
                    ANTIGRAVITY              CODEX
                    ───────────              ─────
배타 영역:          composer/*               publisher/*, tools/*
공유 영역:          shared/* (LOCK 필요)     shared/* (LOCK 필요)
통신 채널:          RESONANCE_SYNC.md        RESONANCE_SYNC.md
                    (append-only, LOCK 불필요)
메시지:             SEQ 번호 + ACK 필수
세션 시작:          BOOT SEQUENCE 필수 실행
```
