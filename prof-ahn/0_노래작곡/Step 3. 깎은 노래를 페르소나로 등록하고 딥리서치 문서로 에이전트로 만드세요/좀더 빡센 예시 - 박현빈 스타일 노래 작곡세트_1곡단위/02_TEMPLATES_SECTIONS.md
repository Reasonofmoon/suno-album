# 02_TEMPLATES_SECTIONS.md

****************************************
[DOC] PURPOSE / 사용 목적
****************************************

이 문서는 “찰진 고반복 훅송 네오-트로트(댄스트로트/일렉트로-트로트 하이브리드)”를 안정적으로 찍어내기 위한 섹션(Section) 템플릿 모음이다.

목표는 3가지다.

1) 훅은 단순하고 따라부르기 쉬운데, 전체 곡은 촘촘하고 빵빵하게 들리게 만들기  
2) “인트로 길어짐, EDM으로 기울어짐, 가사 번역체/영어 섞임” 같은 실패를 구조적으로 차단하기  
3) 앨범 단위로 여러 곡을 뽑아도 ‘같은 엔진에서 나온 일관성’은 유지하면서, 훅/벌스/브릿지에서 ‘베리에이션’이 나게 만들기

****************************************
[0] SECTION TAG 규격 (출력에 붙일 태그 문법)
****************************************

[태그 1줄 규칙]
- 모든 섹션은 반드시 1줄 태그로 시작한다.
- 태그는 대괄호 한 쌍으로만 감싼다.
- 태그 안에는 “섹션명 | 기능 | 보컬 모드 | 에너지 | 추가 힌트” 순서를 유지한다.
- 추가 힌트는 선택 항목이며, 붙일 경우에도 짧게 2~6단어로 제한한다.

[표준 태그 포맷]
[SECTION | FUNCTION | VOCAL MODE | ENERGY | NOTE]

[SECTION 사전(고정)]
- Intro
- Hook A
- Verse 1
- Pre-Chorus
- Chorus
- Interlude
- Verse 2
- Dance Break
- Bridge
- Final Chorus
- Outro

[FUNCTION 사전(고정)]
- Shout
- Hook
- Rhythmic trot
- Build
- Call & Response
- Variation
- Adlibs
- Instrumental
- Big statement
- Last hit

[VOCAL MODE 사전(권장)]
- Chant
- Lead
- Lead+Doubling
- Lead+Group
- Group
- Shout
- No Vocal

[ENERGY 사전(권장)]
- Low
- Mid
- High
- Peak

[NOTE 예시(선택)]
- Hot one-shot only
- Korean only
- No long build
- 2-syllable hook
- Plosive consonants
- End-rhyme pair
- 8-bar turn fill
- Double-hook ending

****************************************
[1] FORM 라이브러리 (곡 구조 템플릿: “길이/진입 속도/후렴 반복”을 고정)
****************************************

공통 불변 규칙(모든 FORM에 적용)
1) Intro는 최대 4 bars  
2) Hook(훅/후렴 핵심 멜로디)은 첫 2 bars 안에 “리프/구호 형태”로 반드시 등장  
3) Chorus(후렴)는 곡 시작 후 0:12 전후(체감)까지 반드시 도착  
4) Dance Break는 4~8 bars, 보컬은 ‘구호/지시어’만, 긴 영어 가사 금지  
5) Outro는 길게 끌지 말고 “딱” 또는 “원샷”으로 종료(Last hit)

FORM_01 “Hook-first Festival Standard”
- 목적: 행사형/단체 떼창 최우선, 가장 안정적인 기본형
- 길이: 2:50 ~ 3:20 체감
- 구조(권장 bars):
  1) Intro 2~4
  2) Hook A 4
  3) Verse 1 8
  4) Pre-Chorus 4
  5) Chorus 8
  6) Interlude 4
  7) Verse 2 8
  8) Chorus 8
  9) Dance Break 4
  10) Bridge 8
  11) Final Chorus 12(더블훅)
  12) Outro 1~2(Last hit)

FORM_02 “Ultra-Short Intro → Chorus Rush”
- 목적: 인트로 늘어지는 모델 행동 교정, 초반 몰입 강제
- 구조(권장 bars):
  1) Intro 1~2
  2) Chorus 8(바로 메인 훅)
  3) Verse 1 8
  4) Pre-Chorus 4
  5) Chorus 8
  6) Verse 2 8
  7) Dance Break 4
  8) Final Chorus 12
  9) Outro 1

FORM_03 “Call&Response 강화형”
- 목적: 훅이 ‘콜-리스폰스’로 강하게 박히게, 관객 참여 최대화
- 구조(권장 bars):
  1) Intro 2(Shout)
  2) Hook A 4(Call)
  3) Hook A 4(Response)
  4) Verse 1 8
  5) Pre-Chorus 4
  6) Chorus 8(콜-리스폰스 문장 2쌍 반복)
  7) Interlude 4(브라스 변주)
  8) Verse 2 8
  9) Chorus 8
  10) Dance Break 4(지시어)
  11) Final Chorus 12(콜-리스폰스 + 더블훅)
  12) Outro 1

FORM_04 “Bridge 축소, 훅 반복 증폭형”
- 목적: 벌스/브릿지에서 길게 설명하다 캐치함 떨어지는 실패 방지
- 구조(권장 bars):
  1) Intro 2~4
  2) Hook A 4
  3) Verse 1 8
  4) Pre-Chorus 4
  5) Chorus 8
  6) Verse 2 8
  7) Chorus 8
  8) Dance Break 4
  9) Bridge 4(문장 최소화)
  10) Final Chorus 16(훅 반복 확대)
  11) Outro 1

FORM_05 “Major-key Feelgood Variation”
- 목적: 앨범 내 변주(장조/밝은 감정)로 귀 피로도 낮추기
- 구조는 FORM_01과 동일하되, Bridge에서 ‘선언’을 더 밝게, Verse의 이미지도 ‘밤/불/열’만 쓰지 않고 ‘빛/웃음/바람/반짝’ 쪽으로 이동

FORM_06 “Electro Chic Variation”
- 목적: EDM으로 쏠리지 않으면서 도시적 질감 추가
- 핵심은 사운드가 아니라 “가사의 트로트 리듬/꺾기/콜-리스폰스” 유지
- 구조는 FORM_02 또는 FORM_03을 추천(빠른 진입으로 EDM 빌드업 방지)

****************************************
[2] SECTION별 마이크로 템플릿 (섹션 기능에 맞는 ‘문장 형태’ 고정)
****************************************

공통 문장 규칙(모든 섹션)
- 한 줄은 “짧고 타격감 있게” 쪼갠다.  
- 장문 설명은 금지. 긴 설명이 필요하면 2줄로 쪼개서 리듬을 만든다.  
- 반복 훅 구간은 “의미”보다 “발음/타격/리듬” 우선이다.  
- 영어는 “원샷 애드립”만 허용한다. 문장형 영어 가사 금지.

----------------------------------------
[2-1] Intro 템플릿 (최대 4 bars)
----------------------------------------

목표
- “시작하자마자 온도 올리기”
- 훅 리프/핵심 단어를 암시
- 긴 빌드업 금지

권장 구성
- 1) 1음절~2음절 구호 2~4회 반복
- 2) 곧바로 메인 훅 키워드 1회 던지기
- 3) “지금부터” 같은 시동 문장 1줄(선택)

템플릿
[Intro | Shout | Chant | High | Korean only]
[[SHOUT_1]]! [[SHOUT_1]]! [[SHOUT_1]]! [[SHOUT_1]]!
[[SHOUT_2]]! [[SHOUT_2]]! [[TRIGGER_WORD]]!

권장 SHOUT 후보(짧게만)
- 야 / 어이 / 헤이 / 자 / 가자 / 간다 / 붙어 / 불붙어 / 더 / 크게

----------------------------------------
[2-2] Hook A 템플릿 (4 bars, 곡의 로고)
----------------------------------------

목표
- 2~3음절 반복 훅을 ‘로고’처럼 고정
- (Hot!) 같은 편곡 트리거로 빈칸을 설계
- 콜-리스폰스 구조를 “가사 구조”로 강제

훅 문장 규칙
- 1행: [[INTERJECTION]] + [[HOOK_2SYLL]] 반복 + (Hot!)
- 2행: “너만 보면/네가 오면/니 앞이면” + [[BODY_REACTION_VERB_PAIR]] + (Hot!)
- 3행: 1행 반복(조금 변형 가능)
- 4행: 2행 반복(동사쌍만 바꿔도 됨)

템플릿
[Hook A | Hook | Lead+Group | Peak | Hot one-shot only]
[[INTERJECTION]] [[HOOK_2SYLL]] [[HOOK_2SYLL]] (Hot!) [[INTERJECTION]] [[HOOK_2SYLL]] [[HOOK_2SYLL]] (Hot!)
[[YOU_TRIGGER]] [[HEART_NOUN]] [[VERBPAIR_A]] (Hot!)
[[INTERJECTION]] [[HOOK_2SYLL]] [[HOOK_2SYLL]] (Hot!) [[INTERJECTION]] [[HOOK_2SYLL]] [[HOOK_2SYLL]] (Hot!)
[[YOU_TRIGGER]] [[HEART_NOUN]] [[VERBPAIR_B]] (Hot!)

----------------------------------------
[2-3] Verse 템플릿 (8 bars, 찰짐의 본체)
----------------------------------------

목표
- 번역체 금지, “한국어 라임의 착착 감김”이 핵심
- ㅂ/ㄷ/ㄱ/ㅈ 같은 타격 자음을 의도적으로 배치
- 끝소리 라임(근접 라임 포함)을 2~3줄 단위로 묶는다
- 단어 반복은 하되, 훅처럼 과하지 않게 “리듬 재료”로 쓴다

Verse 설계 규칙(최소 요구)
1) 8줄 기준으로 2줄씩 “라임 페어”를 만든다(총 4페어)  
2) 각 라임 페어는 동일 종성 또는 유사 모음군으로 묶는다  
3) 각 라임 페어마다 “플로시브(ㅂ/ㄷ/ㄱ)” 단어를 최소 2개 배치한다  
4) 문장은 “짧게 끊기”를 기본으로 하고, 연결어 남발 금지  

Verse 템플릿 A(서술 + 내부운)
[Verse 1 | Rhythmic trot | Lead | Mid | Plosive consonants]
[[YOU_FEATURE]] 한 번이면 [[REACTION_1]], [[REACTION_2]]로 [[FALL_VERB]]
[[SMALL_ACTION]] 스치기만 해도 [[MIND_NOUN]]이 [[CRACK_VERB]]
[[WORLD_SUPERLATIVE]] [[SWEET_NOUN]], [[YOUR_WORD_NOUN]]이 [[SLIDE_VERB]]
[[RUN_VERB]] 해도 안 돼, [[HEART_NOUN]]으로 [[INTO_VERB]]
[[COLOR_IMAGE]] [[SKY_OBJECT]]도 오늘은 [[YOUR_SIDE]]
[[FACE_IMAGE]] [[BURN_VERB]]는 거, [[DONTSMILE]] 말고 [[LOOK_VERB]]

Verse 템플릿 B(열거 + 라임 페어)
[Verse 2 | Rhythmic trot | Lead+Doubling | High | End-rhyme pair]
[[LIKE_1]] [[YOU_TYPE_1]]가 좋아, [[LIKE_2]] [[YOU_TYPE_2]]
[[LIKE_3]] [[YOU_TYPE_3]]가 좋아, [[HIT_VERB]] [[HIT_VERB]]
[[HONEST_WORD]] 해서 더 좋아, [[HEART_GRAB_VERB]]
[[TRIGGER_WORD]] 하게 더 좋아, [[SHAKE_VERB]] [[SHAKE_VERB]]
[[ONE_MORE]] 웃어줘, [[AGAIN_REACTION]]
[[ONE_MORE]] 불러줘, [[AGAIN_ACTION]]

----------------------------------------
[2-4] Pre-Chorus 템플릿 (4 bars, 빌드업은 짧게)
----------------------------------------

목표
- 스네어 롤 업을 “가사”로도 지지
- 문장은 짧고 반복적(“잠깐만/근데/한 걸음” 계열)
- 설명 금지, 긴장감만 올린다

템플릿
[Pre-Chorus | Build | Lead | High | No long build]
[[HOLD_WORD]], [[HOLD_WORD]] [[BREATH_WORD]]
근데 [[YOU_APPROACH]]하면 [[FASTER_VERB]]
[[STEP_WORD]], [[STEP_WORD]] [[DISTANCE_WORD]]
나 진짜로 [[STOP_HARD_VERB]]!

----------------------------------------
[2-5] Chorus 템플릿 (8 bars, Hook A와 동일하거나 더 압축)
----------------------------------------

목표
- Hook A를 그대로 박아 넣는다
- 멜로디는 이미 Hook A에서 고정되어 있다고 가정
- 후렴은 ‘의미’보다 ‘반복’이 우선

템플릿
[Chorus | Call & Response | Lead+Group | Peak | 2-syllable hook]
(= Hook A 4줄을 그대로 2회 반복하거나, 4줄 + 2줄 요약 반복)

----------------------------------------
[2-6] Interlude 템플릿 (4 bars, 악기 변주)
----------------------------------------

목표
- 보컬은 최소(가능하면 No Vocal)
- 브라스 리프 변주, 기타 ‘궁짝’ 유지
- 다음 Verse로 자연스럽게 밀어 넣기

템플릿
[Interlude | Variation | No Vocal | High | Brass riff variation]
(가사 출력이 필요하면 “Hey!/야!” 같은 1음절 구호만 2회 이하)

----------------------------------------
[2-7] Dance Break 템플릿 (4~8 bars, 퍼포먼스 지시)
----------------------------------------

목표
- 보컬 문장은 금지
- 지시어/구호만 사용
- 오른쪽/왼쪽/한 바퀴/더 크게 같은 단체 동작 유도

템플릿
[Dance Break | Instrumental | Shout | Peak | Hot one-shot only]
(Hot!) (Hot!)
[[HOOK_2SYLL]]! [[HOOK_2SYLL]]!
[[RIGHT]]! [[LEFT]]! [[TURN]]!
[[LOUDER]]! [[STRONGER]]!

----------------------------------------
[2-8] Bridge 템플릿 (4~8 bars, 문장 최소화)
----------------------------------------

목표
- “선언형” 두 줄을 반복해서 꽂는다
- 말 수를 줄여서 ‘훅 대비(밀도 대비)’를 만든다
- 대체로 2~3음절 단어 + 짧은 문장 위주

템플릿 A(양보-선언)
[Bridge | Big statement | Lead | High | Minimal words]
[[CONCESSION_A]]도 좋아, [[CONCESSION_B]]도 좋아
[[CONDITION_LINE]] (Hot!)
[[IDENTITY_LINE_A]] (Hot!) [[IDENTITY_LINE_B]] (Hot!)
[[REASON_LINE_A]] (Hot!)
[[REASON_LINE_B]] (Hot!)

템플릿 B(짧은 반전-확신)
[Bridge | Big statement | Lead | High | Minimal words]
[[HOLD_WORD]]만 해, 더는 못 참아
[[YOU_NAME]]이면 난 [[DECIDE_VERB]]
[[CONCESSION_A]]도 좋아 (Hot!)
[[FINAL_REASON]] (Hot!)

----------------------------------------
[2-9] Final Chorus 템플릿 (12~16 bars, 더블훅)
----------------------------------------

목표
- “더블훅”을 반드시 구현한다
- 훅 문장을 1단 더 줄여서 반복 밀도를 올린다
- 마지막 2 bars는 “그냥 훅”만 남긴다

템플릿
[Final Chorus | Hook | Lead+Group | Peak | Double-hook ending]
Hook A 4줄
Hook A 4줄
[[INTERJECTION]] [[HOOK_2SYLL]] [[HOOK_2SYLL]] (Hot!) x2
Hot! Hot! Hot! Hot! (또는 [[SHOUT_1]] 반복)

----------------------------------------
[2-10] Outro 템플릿 (1~2 bars, Last hit)
----------------------------------------

목표
- 페이드아웃 금지(권장)
- 마지막 한 방 “딱” 찍고 끝

템플릿
[Outro | Last hit | Shout | Peak | Hard stop]
[[INTERJECTION]] [[HOOK_2SYLL]]— 딱

****************************************
[3] 훅(Chorus) “찰짐” 설계 템플릿 (가사 엔진의 핵심 조립식 블록)
****************************************

[3-1] 훅 코어 부품(필수 변수)
- [[INTERJECTION]]: “앗 / 아 / 어 / 야” 중 택1(곡마다 1개 고정)
- [[HOOK_2SYLL]]: 2음절(또는 2음절로 들리는 3글자) 1개를 곡의 로고로 고정
- [[YOU_TRIGGER]]: “너만 보면 / 네가 오면 / 니 앞이면 / 네 생각만” 중 택1
- [[HEART_NOUN]]: “가슴 / 심장 / 머리 / 속” 중 택1
- [[VERBPAIR_A]], [[VERBPAIR_B]]: 동사쌍(반복-변형 구조)

[3-2] 동사쌍(Verb Pair) 규칙
- 반드시 “동사 반복 구조”로 만든다
- 형태: [[동사]]+“는다” [[동사]]+“져/쳐/나/가/와”처럼 2연타
- 예: “번진다 번져”, “녹는다 녹아”, “미친다 미쳐”, “터진다 터져”
- 각 곡은 최소 2쌍, 최대 4쌍만 사용(과다 변형 금지)

[3-3] (Hot!) 트리거 규칙
- 영어 단어는 “Hot”만 허용(권장)
- 표기는 항상 괄호로 고정: (Hot!)
- 위치는 훅의 빈칸을 채우는 “리듬 트리거”로만 사용
- 문장형 영어 금지, 번역체 영어 금지

[3-4] 훅 변주 규칙(앨범 베리에이션)
- 훅 멜로디가 바뀌는 것처럼 느껴지면 실패다
- 변주 허용 범위는 아래만
  1) [[VERBPAIR_A/B]] 교체
  2) [[YOU_TRIGGER]] 교체
  3) 훅 2행의 조사 1개 변경(“때문에/앞에/만”) 정도
  4) 마지막 훅에서만 “[[HOOK_2SYLL]]” 앞뒤 1음절 구호 추가

****************************************
[4] Verse “찰짐” 템플릿 (라임/발음/타격의 조립 규칙)
****************************************

[4-1] Verse 라임 페어(End-rhyme Pair) 규칙
- Verse 8줄이면 2줄씩 4묶음
- 각 묶음은 “끝소리”가 가까워야 한다
- 완전 동일 라임이 아니어도 “모음군”이 같으면 인정
- 곡마다 라임 페어 최소 2종, 최대 4종만 사용

[4-2] 자음 타격(Plosive) 규칙
- Verse는 ‘발음 타격’으로 춤을 춘다
- ㅂ/ㄷ/ㄱ/ㅈ/ㅊ 중 최소 2종을 해당 Verse의 주력 자음으로 선택
- 선택한 주력 자음이 들어간 단어를 8줄 중 최소 6줄에 1개 이상 포함

[4-3] Verse 문장 구조 규칙(번역체 방지)
- “어우 뜨끈 뜨끈, 내 마음 과열!” 같은 서술은 금지
- 대신 “상황 → 반응 → 과장 → 확신”의 짧은 구어 구조로 쓴다
- 조사/어미는 최대한 한국어 구어체로 고정
- 한 줄에 의미가 2개 넘으면 쪼갠다

[4-4] Verse 리듬 편의 장치(필수)
- 2~3음절 반복을 Verse에도 ‘조미료’로 넣는다
- 단, Chorus 수준으로 반복하면 안 된다
- 예: “딱-”, “확-”, “퍽-”, “훅-” 같은 1음절 타격도 허용(남발 금지)

****************************************
[5] Dance Break / Bridge 베리에이션 설계 (앨범 단위 반복 피로도 방지)
****************************************

[5-1] Dance Break 베리에이션(지시어 세트 교체)
- SET_A: 오른쪽/왼쪽/한 바퀴/더 크게
- SET_B: 앞으로/뒤로/두 번/더 세게
- SET_C: 손 위로/손 아래/어깨/박수
- SET_D: 뛰어/붙어/돌아/소리 질러
- 곡마다 SET 1개만 선택해서 끝까지 유지

[5-2] Bridge 베리에이션(선언 방식 교체)
- TYPE_1: “A도 좋아 B도 좋아” 양보형
- TYPE_2: “이게 좋아 그래서 좋아” 확신형
- TYPE_3: “한 번 사는 인생” 결심형
- TYPE_4: “너만이면 된다” 조건형
- TYPE_5: “남자/사람” 정체성 선언형
- 앨범에서는 TYPE이 연속으로 반복되지 않게 순환

****************************************
[6] 섹션 밀도 대비 규칙 (Verse/Hook 대비를 시스템으로 고정)
****************************************

밀도 정의
- Hook 밀도: 반복률이 높고, 문장 길이가 짧고, 트리거가 많다
- Verse 밀도: 정보량이 높지만, 라임/타격으로 “잘게 쪼개진 정보”여야 한다
- Bridge 밀도: 정보량을 줄여서 ‘쉬는 구간’을 만들고, Final Chorus를 크게 느끼게 한다

강제 규칙
1) Hook는 2~3음절 반복을 최소 6회 이상 포함  
2) Verse는 동일 훅 단어([[HOOK_2SYLL]])를 2회 이하로만 사용  
3) Bridge는 고유 단어 수를 의도적으로 줄여서 반복률을 올린다(문장 길이는 짧게)  
4) Final Chorus는 “Hook 반복 + Group”으로 밀도를 최대로 올린다  

****************************************
[7] QC 체크리스트 (출력 직전, 실패 유형 자동 차단)
****************************************

구조 체크
- Intro가 4 bars를 넘지 않는가
- Hook 리프/구호가 첫 2 bars 안에 존재하는가
- Chorus가 체감 0:12 전후까지 도착하는가
- Dance Break가 4~8 bars이며 문장형 보컬이 없는가
- Outro가 페이드아웃이 아닌 Last hit로 끝나는가

가사 체크
- 영어 문장이 있는가(있으면 실패)
- 영어는 (Hot!) 같은 원샷 트리거 외에 존재하는가(있으면 실패)
- 훅이 2~3음절 반복 구조를 만족하는가
- 훅의 동사쌍 반복이 최소 2회 이상 들리는가
- Verse에 라임 페어가 최소 2묶음 이상 있는가
- Verse에 ㅂ/ㄷ/ㄱ 계열 타격 단어가 충분한가

스타일 체크(EDM으로 기울어짐 방지)
- 긴 빌드업/드롭 설명이 있는가(있으면 실패)
- “클럽/EDM/레이브” 같은 단어가 가사에 들어갔는가(권장하지 않음)
- ‘트로트 구어체’ 대신 번역체 감탄문이 늘었는가(있으면 실패)

****************************************
[8] 빠른 조립 가이드 (템플릿 선택 순서)
****************************************

STEP 1) FORM 선택  
- 기본은 FORM_01, 인트로가 늘어지면 FORM_02로 강제

STEP 2) 훅 부품 선택  
- [[INTERJECTION]] 1개 고정  
- [[HOOK_2SYLL]] 1개 고정  
- [[VERBPAIR_A/B]] 2쌍 선택

STEP 3) Verse 라임 페어 선택  
- 모음군 2개만 선택해서 Verse 전체를 묶는다

STEP 4) Dance Break SET 선택  
- SET_A~D 중 1개만

STEP 5) Bridge TYPE 선택  
- TYPE_1~5 중 1개만

STEP 6) QC 체크 후 출력  
- 실패 조건 1개라도 걸리면 즉시 수정 후 출력

