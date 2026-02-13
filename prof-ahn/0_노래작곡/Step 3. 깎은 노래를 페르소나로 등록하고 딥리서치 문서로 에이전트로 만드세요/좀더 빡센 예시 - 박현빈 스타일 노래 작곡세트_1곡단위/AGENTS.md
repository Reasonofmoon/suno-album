# AGENTS.md
> 앨범 단위 “찰진 고반복 훅송 네오-트로트(댄스트로트)”를 **4개 모듈(00~03)**로 공용 운영하기 위한 **강제 워크플로우 운영 매뉴얼**  
> 목표: (1) SUNO Style Prompt 대충 작성 방지 (2) 가사 몇 줄 쓰고 다음 트랙 넘어가는 사고 방지 (3) EDM 드리프트/인트로 과다/영어 번역 가사 혼입 방지 (4) 앨범 단위 변주/중복 관리

---

## 0) 반드시 읽는 순서 & 우선순위(충돌 해결 규칙)

### 0-1. 파일 의존성(반드시 참조)
- **00_MASTER_PROMPT.md**: 출력 계약(ABSOLUTE), SUNO 스타일 프롬프트 패키저, 기본값, 수리(Repair) 규칙  
  - 링크: `./00_MASTER_PROMPT.md`
- **01_LEXICON_CHAJJIM.md**: 찰짐 사전(훅토큰/동사쌍/라임 패밀리/트리거 태그), TRACKLOG 템플릿  
  - 링크: `./01_LEXICON_CHAJJIM.md`
- **02_TEMPLATES_SECTIONS.md**: 섹션 태그 규격, FORM 라이브러리(바 수/진입속도), 섹션별 가사 템플릿  
  - 링크: `./02_TEMPLATES_SECTIONS.md`
- **03_QA_VARIATION_RULES.md**: QA 게이트/점수표/통과 기준, 앨범 내 중복 방지/변주 법칙, EDM 드리프트 방지 표식  
  - 링크: `./03_QA_VARIATION_RULES.md`

### 0-2. 우선순위(충돌 시 이 순서로 “상위 규칙” 적용)
1) **00_MASTER_PROMPT.md의 [O] OUTPUT CONTRACT** (출력 형식/순서/필수 항목)  
2) **03_QA_VARIATION_RULES.md의 [Q-GATE] & [V-LAW]** (통과/실패 판정)  
3) **02_TEMPLATES_SECTIONS.md의 FORM/섹션 템플릿** (구조/분량/문장 규칙)  
4) **01_LEXICON_CHAJJIM.md의 어휘/조합 사전** (찰짐 재료 선택)

> ⚠️ 태그 문법 충돌 처리:  
> - 최종 출력은 **00의 섹션 태그(고정 리스트)**를 “반드시” 지킨다.  
> - 02의 5단 태그(`[SECTION | FUNCTION | VOCAL MODE | ENERGY | NOTE]`)는 **내부 설계/초안용**으로만 쓰고, 최종 출력에서는 **00의 고정 섹션 태그로 변환(축약) 후 제출**한다.  
> - (원한다면) 사용자 지시가 명시적으로 있을 때만 02 태그 포맷을 최종 출력에 사용한다.

---

## 1) 에이전트 운영 철칙(FAIL-FAST / NO-SLOPPY)

### [A-LAW 1] “트랙 1곡 = 완제품 1개”
- 트랙은 반드시 아래 4개를 **한 번에** 완성해야 한다(부분 제출 금지).
  1) Title  
  2) SUNO Style Prompt(1줄, <1000 chars)  
  3) Song Structure Tags + **Full Lyrics**(전 섹션)  
  4) TRACKLOG(필수 필드 전부 채움)

### [A-LAW 2] “다음 트랙으로 넘어가기 전, 현재 트랙 QA 통과”
- 03의 QA 기준을 통과하기 전에는 다음 트랙으로 이동 불가.
- “대충”/“일단 넘어가자”/“이 정도면 됨” 금지.

### [A-LAW 3] “placeholder 금지”
- 최종 출력에 `[[LIKE_2]]`, `{BPM}`, `{KEY}` 같은 플레이스홀더가 남아 있으면 **즉시 실패**.
- 플레이스홀더는 초안 단계에서만 사용 가능. 최종 제출 전 100% 치환.

### [A-LAW 4] “영어 번역 가사 혼입은 즉시 실패”
- 가사 본문에 영어 문장/설명형 영어 라인/로마자 가사 등장 시 즉시 FAIL.  
- 허용 정책은 00의 `{ENGLISH_POLICY}`를 따르며, 기본은 **“1단어 구호만”**이다.  
- 앨범 운영 기본값 권장: **NO ENGLISH VOCAL**(가능하면 ‘핫/헤이’ 한글 표기).

---

## 2) 앨범 제작 워크플로우(강제 루프)

### 2-1. AlbumSpec 작성(트랙 생성 전에 반드시)
앨범을 “즉흥 생성”하면 중복/드리프트가 발생한다. 먼저 다음 스펙을 고정한다.

**AlbumSpec(필수)**
- N(트랙 수)
- 공통 코어: Neo-Trot/Dance-Trot, 136~142 BPM 범위(기본 140), 4/4, “disco-gogo + subtle trot shuffle overlay”
- 보컬: 남성 하이테너 트롯(퍼커시브 자음/짧은 꺾기/클린 비브라토)
- 영어 정책: Default(1단어 구호만) 또는 NO ENGLISH(가사 내 영어 0)
- 앨범 톤: 행사/떼창/단체구호 중심(“빵빵/찰짐/반복”)

**Album Variation Matrix(필수)**
- 각 트랙별로 아래를 “겹치지 않게” 배치:
  - HookToken(01)
  - VerbPairA/B(01)
  - RhymeFamilyVerse(01)
  - MetaphorDomain(01)
  - Dance Break 구호 세트(03: 매 트랙 새로 구성)
  - 리프 주역 악기 비중(03: 브라스 중심/브라스+아코디언/기타 궁짝 강조 등)

> 결과물: **Tracklist Plan**(00의 Album Pack 형식에 맞춘 요약표)

---

## 3) 트랙 생성 파이프라인(곡 1개를 찍어내는 “강제 절차”)

### Step 1) 재료 선택(LEXICON 기반)
01에서 다음을 고른다(중복 체크 포함):
- HookToken 1개(2음절 권장)
- VerbPairA 1개 + VerbPairB 1개(서로 다르게)
- RhymeFamilyVerse 1개(RF-EO / RF-YEO 등)
- TriggerSet 1개(태그/원샷/라스트히트 기능 고려)
- MetaphorDomain 1개(heat/fire, neon/electric, speed/engine, sweet/liquor, crowd/festival 등)

**선택 규칙(강제)**
- HookToken은 후렴에서 **고반복** 가능한 발음이어야 한다(02~03의 “찰짐” 기준).
- VerbPair는 “서술형+축약형” 반복이 가능해야 한다(예: `번진다 번져`처럼).
- RhymeFamily는 Verse의 “끝소리 라임 1쌍(커플렛)”을 안정적으로 만들 수 있어야 한다.
- TriggerTag는 **편곡 빈칸**을 만들기 위한 장치(후렴 말미/댄브 구호/라스트히트)에만 쓴다. 남발 금지.

### Step 2) FORM 선택(02 기반)
02의 FORM 라이브러리 중 1개를 고르고, “후렴 진입 속도”를 고정한다.
- 기본 권장: **FORM_01 Hook-first Festival Standard**
- 모델이 인트로 늘어지면: **FORM_02 Ultra-Short Intro → Chorus Rush**

**공통 불변(강제)**
- Intro ≤ 4 bars
- Hook(리프/구호) ≤ 첫 2 bars 안에 등장
- Chorus(체감) ≤ 0:12 전후 도착
- Dance Break 4~8 bars, **지시어/구호만**
- Outro는 “딱/원샷/라스트히트”로 짧게 종료

### Step 3) SUNO Style Prompt 작성(00 기반: PACKAGER 사용)
00의 “1-line, under 1000 chars” 규칙을 그대로 적용한다.

**Style Prompt 필수 체크(모두 들어가야 통과)**
- `Neo-Trot / Dance-Trot` 명시
- `BPM`, `4/4`, `Key` 명시
- 리듬/그루브: `disco-gogo four-on-the-floor + subtle trot shuffle overlay`
- 악기 앵커 6종: `TR-909 kick`, `snare+clap on 2&4`, `16th hats`, `tom fills every 8 bars`, `gung-jjak palm-muted guitar`, `layered synth brass hook + call/response`, `synth-accordion color`
- 보컬 앵커: `male Korean trot high-tenor`, `percussive consonants`, `quick kkeokki`, `clean vibrato`
- 편곡 제약: `intro max 4 bars`, `hook within first 2 bars`, `chorus by ~0:12`, `no long breakdowns`, `final chorus double-hook`, `hard last hit`
- 언어 제약: `Korean lyrics only` + (NO ENGLISH 선택 시) `no English words`

**금지어(EDM 드리프트 유발)**
- `drop`, `rave`, `big room`, `dubstep`, `festival EDM` 등(00/03 기준)

### Step 4) 가사 작성(02 기반 + 01 찰짐 재료 적용)
- 02 템플릿을 사용하되, 최종 제출은 00 섹션 태그로 출력한다.
- 핵심은 “후렴 단순/고반복” + “벌스 찰짐(라임/자음/대구)” + “섹션 대비(밀도 대비)”.

#### [LYRICS MINIMUM RULES] (대충 몇 줄 방지용 강제 최소치)
아래를 만족하지 않으면 **즉시 FAIL**:
- 섹션 누락 0개(00의 고정 섹션 10개 모두 존재)
- 전체 가사(빈 줄 제외) **최소 40줄 이상**
- Chorus는 최소 4줄 구조를 갖고, 동일 훅을 반복(가변 최소화)
- Verse 1/2는 각각 **최소 6줄**
- Pre-Chorus는 **정확히 4줄**(짧고 반복적)
- Dance Break는 **최소 4줄**, 문장형 서사 금지(지시어/구호만)
- Bridge는 “선언형/양보형” 중심으로 **최소 4줄**
- Final Chorus는 “더블 훅”이 체감되도록 **최소 8줄(후렴 4줄×2)** 권장

#### [찰짐 구성 4대 축] (앨범 공통 코어)
1) **2~3음절 반복 훅**: HookToken을 후렴 전면에 고정  
2) **끝소리 라임 + 자음 타격**: Verse에 라임 커플렛 1쌍 이상 + 파열음(ㅂ/ㄷ/ㄱ/ㅌ/ㅋ/ㅍ) 밀도  
3) **TriggerTag로 빈칸 설계**: (딱!)/(와!)/(핫!) 등은 “편곡 슬롯”에만 배치  
4) **벌스/훅 대비(밀도 대비)**: Verse는 말하듯/리듬 타이트, Chorus는 떼창/고음/풀스택

---

## 4) QA 강제 게이트(03 기반): “통과 전까지 수정 루프”

### 4-1. Q-GATE 1: 형태 검사(하나라도 실패하면 즉시 수정)
- 섹션 10개 전부 존재(Intro/Chorus/Verse1/Pre/Chorus/Verse2/Dance Break/Bridge/Final Chorus/Outro)
- Intro 4 bars 초과 금지 + Hook 2 bars 이내 등장(구호/리프)
- 영어 문장/영어 설명 라인/로마자 가사 혼입 금지  
  - 허용 정책은 00에 따름(기본 1단어 구호만)
- 훅 라인 1줄당 10~16음절 내외 유지(너무 길면 따라부르기 실패)

### 4-2. Q-Score(총 30점) 통과 기준(03 기준)
- **총점 ≥ 24**
- 필수 축 최소점:
  - Hook Adhesion ≥ 4
  - Chajjim Index ≥ 4
  - Trot Identity ≥ 4
  - Section Contrast ≥ 3
  - Lyric Naturalness ≥ 3
  - Album Uniqueness ≥ 3

### 4-3. EDM 드리프트 방지(Trot Markers)
- 아래 표식 중 **최소 5개**가 곡에 명확히 존재해야 한다(4개 이하면 EDM으로 기움):
  1) 고고 베이스(옥타브 바운스 + 오프비트 5도/8도 팝)  
  2) 팔뮤트 기타 궁짝  
  3) 브라스 리프가 메인 멜로디 리드  
  4) 콜 앤 리스폰스(보컬 끝에 악기 답가/구호)  
  5) 벌스 말하듯 리드미컬한 트로트 프레이징  
  6) 훅에서 고음 벨트 + 짧은 꺾기 + 클린 비브라토  
  7) 펜타토닉 중심 멜로디 감각  
  8) 8마디 전환마다 탐/필/심벌로 경계 선명

---

## 5) 앨범 중복 방지 운영(Tracklog Collection 기반)

### 5-1. TRACKLOG는 “곡의 DNA 바코드”
각 트랙 출력 끝에 반드시 아래를 채운다(00/01 기준):
- HookToken
- VerbPairA
- VerbPairB
- RhymeFamilyVerse
- MetaphorDomain
- Key
- BPM
- (권장) TriggerSet / DanceBreakShouts / LeadRiffBias 메모

### 5-2. 앨범 내 중복 금지(03 기준 강화 운영)
- 같은 HookToken “코어(중심 2음절)”를 연속 트랙에 배치 금지(피로도 상승)
- 같은 라임 페어(끝소리 커플렛) 재사용 금지
- Dance Break 지시 구호 세트는 **매 트랙 새로 구성**
- 리프 주역 악기 비중은 트랙마다 바꿔서 “같은 곡 복제” 인상을 차단  
  - 단, 브라스 콜앤리스폰스 기능은 사라지면 안 됨

---

## 6) 실패 유형별 “즉시 수리” 플레이북(00/03 기반)

### 6-1. “SUNO Style Prompt가 대충이다” (가장 흔한 찐빠)
**증상**
- BPM/Key 빠짐, Neo-Trot 명시 없음, 악기 앵커 누락, “신나는 댄스곡” 같은 추상어만 존재

**수리**
- 00의 Default Style Prompt Template(변수 치환)로 재작성  
- 체크리스트(3-3) 항목이 모두 들어갈 때까지 반복

### 6-2. “가사가 몇 줄만 나오고 끝남” (가장 치명적인 찐빠)
**증상**
- Verse 2/Dance Break/Bridge/Final Chorus 생략
- 후렴만 반복하고 곡이 끝남

**수리**
- 4-1 형태 검사 통과할 때까지 섹션을 강제로 채움  
- [LYRICS MINIMUM RULES]의 줄수/섹션 최소치를 만족할 때까지 추가 작성  
- Bridge는 “문장 최소화”로 채우고, Final Chorus는 더블훅으로 확장

### 6-3. “EDM처럼 들림”
**증상**
- 브라스 훅이 약하고 신스 리드/빌드업/드롭 중심, 트로트 표식 부족

**수리**
- Style Prompt에서 `disco-gogo`, `gung-jjak`, `synth-accordion`, `pentatonic trot hook`를 전면에 올림  
- 03의 Trot Markers를 최소 5개 충족하도록 악기/보컬/편곡 문장 보강  
- 금지어(드롭/레이브 등) 제거

### 6-4. “인트로가 너무 길어짐”
**수리**
- Style Prompt에 **반드시** 다음 문장 포함:
  - `intro max 4 bars, hook within first 2 bars, chorus by ~0:12, keep groove continuous (no long build-ups)`
- 가사에서도 Intro를 구호 1~3줄로 줄이고, 바로 Hook/Chorus로 진입

### 6-5. “번역체/딱딱함/입에 안 붙음”
**수리**
- Verse는 “짧은 구어체 + 리듬 타격 자음”으로 재작성  
- 라임 커플렛 1쌍을 Verse에 강제 삽입  
- 동사쌍(한다/해, 번진다/번져 등) 반복을 Chorus와 Verse에 분배  
- 의미 설명 줄이고 “상황-반응-과장”으로 재배치

### 6-6. “앨범인데 다 같은 곡”
**수리**
- Tracklog Collection을 보고 중복 요소(HookToken/라임/구호/도메인)를 교체  
- 변주 축(03: 악기 비중/댄브 구호/메타포)을 최소 2개 이상 바꾼 뒤 재생성

---

## 7) 앨범 생성 출력 운영 규약(사용자에게 제출할 때)

### 7-1. Album Pack 제출 순서(00의 O-2 준수)
1) Tracklist Plan (N tracks)  
2) Track 1 완제품(O-1 전부)  
3) (선택) Track 1 QA 요약(사용자가 원할 때만)  
4) TRACKLOG COLLECTION 업데이트  
5) 다음 트랙으로 이동(단, 반드시 “직전 트랙 QA 통과” 후)

### 7-2. “사용자 지시가 없을 때” 기본 운영값(00의 DEFAULTS 준수)
- BPM=140
- KEY=F# minor
- RhymeFamilyVerse=RF-EO 또는 RF-YEO
- MetaphorDomain=heat/fire(트랙 1 기본)
- English Policy: 1단어 구호만(또는 NO ENGLISH로 고정)

---

## 8) 이 문서의 목적(한 줄 요약)
**“대충 생성”을 구조적으로 봉쇄하고, ‘찰짐/고반복/트로트 정체성/앨범 변주’가 동시에 유지되는 생산 라인을 만든다.**

---
(EOF)
