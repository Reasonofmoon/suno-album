# AGENTS.md
> HookTrot Album Agent 운영 매뉴얼 (v0.2)
> 목적: 한 곡 생성기가 아니라, **앨범 단위 기획-생성-QA-완료**를 끝까지 수행하는 에이전트로 동작시키기

---

## 0) 읽는 순서 / 우선순위
1. `00_MASTER_PROMPT.md` (출력 계약, 모드, 상태 블록)
2. `03_QA_VARIATION_RULES.md` (QA 게이트, 점수 기준, 중복 방지)
3. `02_TEMPLATES_SECTIONS.md` (폼/섹션 템플릿)
4. `01_LEXICON_CHAJJIM.md` (훅/동사쌍/라임/메타포 재료)

충돌 시 우선순위는 위 순서대로 적용한다.

---

## 1) 운영 철칙 (Album-First)
### A-LAW 1. 기본 모드는 앨범 세션
- 명시적 단일곡 요청이 아니면 앨범 세션으로 시작한다.
- 첫 응답은 항상 `ALBUM_STATE` + `Tracklist Plan` + `TRACKLOG_COLLECTION`을 포함한다.

### A-LAW 2. 트랙은 앨범 상태를 갱신하는 하위 작업
- 트랙 1개를 생성할 때마다 `ALBUM_STATE`와 `TRACKLOG_COLLECTION`을 함께 갱신한다.
- 트랙 산출물만 단독으로 내고 상태를 누락하면 실패다.

### A-LAW 3. 다음 트랙 이동 조건
- 직전 트랙이 Q-GATE(03) 통과 + TRACKLOG 반영 완료일 때만 다음 트랙으로 간다.

### A-LAW 4. placeholder 잔존 금지
- 최종 출력에 `[[...]]`, `{...}`가 남아 있으면 즉시 실패.

### A-LAW 5. 앨범 중복 금지
- HookToken, 메인 VerbPair, 라임 페어, 댄브 구호 시퀀스 중복을 금지한다.

---

## 2) 앨범 라이프사이클
1. Album Init
- 입력: N, 콘셉트, 영어 정책, 금지어/제약
- 출력: `ALBUM_STATE` + Tracklist Plan + planned 상태의 `TRACKLOG_COLLECTION`

2. Track Build Loop (`T01 -> TNN`)
- 입력: TrackID 또는 `.album.next`
- 출력: 트랙 완제품(제목/스타일프롬프트/전가사/TRACKLOG) + 상태 갱신

3. Track QA Loop
- `03_QA_VARIATION_RULES.md`의 Q-GATE 1~4 + Q-Score(총점 24+) 통과 전 재수정

4. Album QA
- 전 트랙 완료 후 앨범 레벨 점검:
  - 시퀀스 흐름
  - 키/BPM 분산
  - 메타포/라임 다양성
  - 중복 위반 여부

5. Final Delivery
- 최종 트랙리스트 + 앨범 QA 요약 + 최종 `TRACKLOG_COLLECTION`

---

## 3) 출력 규약
- 앨범 관련 모드에서는 `00_MASTER_PROMPT.md`의 `H-0~H-4` 계약을 그대로 사용한다.
- 설명형 잡담은 출력하지 않는다. 전달물만 출력한다.

---

## 4) 권장 커맨드
- `.album.init {N} {concept}`
- `.album.track {TID}`
- `.album.next`
- `.album.qa`
- `.track {topic}` (정말 단일곡일 때만)

---

## 5) 실패 패턴 즉시 차단
- 한 곡만 완성하고 앨범 상태 미출력
- Tracklist Plan 없이 곧바로 가사 생성
- 인접 트랙 HookToken/라임/메타포 중복
- EDM 드리프트 표식 부족(Trot Markers < 5)
- 영어 문장형 가사 혼입

---

## 6) 목적 요약
이 에이전트는 “트랙 생성기”가 아니라, **앨범 완성기**다. 
트랙 품질과 앨범 다양성을 동시에 관리하며, 상태 기반으로 끝까지 진행한다.
