# 01_LEXICON_CHAJJIM.md
Version: v0.1 (Stable)
Role: “찰짐 맵 작곡 사전 / Lexicon Field”
Purpose: 고반복 훅형 네오트로트(Dance-Trot / Neo-Trot) 곡을 만들 때, 훅·라임·자음 타격·트리거·메타포를 “선택 가능한 부품”으로 제공하는 표준 사전

---

## [A] SYSTEM CORE (Lexicon Edition)

### A-1. Grand Premise
이 문서는 “가사/훅 찰짐”의 재현성을 올리기 위한 단어·구문·발음 설계 사전이다.  
이 문서의 항목들은 “의미”보다 “입모양·타격감·반복 내구성·콜앤리스폰스 슬롯”을 우선으로 설계한다.

### A-2. Laws (Absolute)
0. [LAW 0: ORIGINALITY LOCK] 실존 곡의 특정 문장, 훅 라인, 시그니처 구문을 그대로 재사용하지 않는다. 짧은 일반 단어는 허용되나, 연쇄 구조가 식별 가능하면 즉시 변형한다.

1. [LAW 1: HOOK PRIORITY] 후렴의 후킹 토큰(HookToken)은 2~3음절 반복형을 최우선으로 사용한다.

2. [LAW 2: VERB-PAIR MANDATE] 후렴에는 최소 1개 이상의 동사쌍(VerbPair)을 반드시 포함한다.

3. [LAW 3: RHYME COUPLET MANDATE] 벌스에는 최소 1세트 이상의 “끝소리 라임 2줄 고정(couplet)”이 반드시 존재해야 한다.

4. [LAW 4: TRIGGER SLOT DESIGN] 후렴 4줄 중 최소 3줄은 트리거(TriggerTag)로 끝을 찍는다. 사용자가 “NO ENGLISH”를 요구하면 영어 트리거는 금지되고, 한국어 트리거만 사용한다.

5. [LAW 5: DENSITY CONTRAST] 벌스는 서술 밀도(문장 길이)가 높고 트리거가 적다. 후렴은 짧고 반복이 많고 트리거가 많다.

6. [LAW 6: ALBUM ANTI-REUSE] 앨범 모드에서는 트랙마다 메인 HookToken 1개와 메인 VerbPair 1개를 고유하게 유지한다(재사용 금지).

7. [LAW 7: MOUTHFEEL] 후렴의 핵심 훅은 개방 모음(ㅏ/ㅓ) 비중이 높을수록 우선 선택한다. 자음 타격(ㄲ/ㅋ/ㅌ/ㅃ/ㅂ/ㄷ/ㄱ/ㅈ/ㅊ)이 적으면 “맹탕” 위험으로 감점한다.

---

## [B] DATA MODEL (Schema)

### B-1. Scoring Scale
모든 점수는 1~5 정수 스케일이다.

- 1: 거의 비권장
- 3: 평균, 상황 따라 사용
- 5: 강력 추천, 기본값 후보

### B-2. HookToken Entry Schema
| Field | Type | Meaning |
|---|---:|---|
| token | string | 훅 반복 토큰(2~3음절 권장) |
| syllables | int | 음절 수 |
| attack | 1~5 | 자음 타격감(파열/파찰 중심) |
| open_vowel | 1~5 | 개방 모음 비중(ㅏ/ㅓ) |
| chant | 1~5 | 합창/콜 가능성(반복 내구성) |
| trot_fit | 1~5 | 트로트 발화 적합성(말맛/꺾기 호환) |
| fatigue_risk | 1~5 | 과반복 시 질림 위험(높을수록 위험) |
| tags | list | heat, spark, motion, sweet, tease, crowd, neon 등 |

### B-3. VerbPair Entry Schema
| Field | Type | Meaning |
|---|---:|---|
| pair | string | “서술형 + 축약형” 동사쌍 |
| pattern | string | -는다/-다 + -어/-아, -해 + -해, -고 + -고 등 |
| attack | 1~5 | 발음 타격 |
| chant | 1~5 | 후렴 반복 적합 |
| intensity | 1~5 | 의미 강도(흥분/폭발/집착) |
| domain | list | heat, fire, electricity, speed, dizzy, sweet, neon 등 |
| notes | string | 사용 포지션(후렴 2줄, 브릿지 선언 등) |

### B-4. Rhyme Family Schema
| Field | Type | Meaning |
|---|---:|---|
| family_id | string | 예: RF-EO, RF-YEO |
| endings | list | 대표 종결(어/아/져/여/을/라 등) |
| strength | 1~5 | 라임 고정 시 찰짐 안정성 |
| pool | list | 추천 어휘 종결 후보 |
| cautions | string | 과사용 위험, 의미 제한 |

### B-5. TriggerTag Schema
| Field | Type | Meaning |
|---|---:|---|
| tag | string | (Hot!), (딱!), (와!) |
| language | KR/EN | 언어 |
| function | hit/fill/crowd/cut | 편곡 슬롯 용도 |
| energy | 1~5 | 에너지 상승 기여 |
| placement | string | 후렴 말미, 댄브 구호, 라스트 히트 등 |

---

## [C] HOOKTOKENS (2~3 syllable repeat hooks)

### C-1. Interjections (1음절, 훅/콜 선행 토큰)
앗, 야, 어, 와, 헉, 어우, 아이, 에이, 어이, 오, 으악, 좋아, 됐다

### C-2. Core HookTokens (2음절 중심)
| token | syl | atk | open | chant | trot | fatigue | tags |
|---|---:|---:|---:|---:|---:|---:|---|
| 화끈 | 2 | 4 | 5 | 5 | 5 | 2 | heat, tease, crowd |
| 후끈 | 2 | 4 | 4 | 5 | 5 | 2 | heat, romance |
| 뜨끈 | 2 | 3 | 4 | 4 | 4 | 2 | heat, comfy |
| 찌릿 | 2 | 4 | 2 | 4 | 4 | 3 | electricity, shock |
| 번쩍 | 2 | 4 | 3 | 4 | 4 | 3 | spark, neon |
| 활활 | 2 | 3 | 4 | 4 | 4 | 3 | fire, blaze |
| 두근 | 2 | 2 | 2 | 4 | 4 | 2 | heartbeat, romance |
| 콩닥 | 2 | 3 | 2 | 4 | 4 | 3 | heartbeat, cute |
| 쿵쾅 | 2 | 5 | 2 | 4 | 3 | 4 | impact, drums |
| 들썩 | 2 | 4 | 2 | 4 | 4 | 3 | dance, crowd |
| 펄쩍 | 2 | 4 | 3 | 4 | 3 | 4 | jump, surprise |
| 팡팡 | 2 | 5 | 2 | 4 | 3 | 4 | burst, impact |
| 빵빵 | 2 | 5 | 2 | 4 | 3 | 4 | horn, crowd |
| 탁탁 | 2 | 5 | 2 | 4 | 3 | 4 | cut, percussion |
| 딱딱 | 2 | 5 | 2 | 4 | 3 | 4 | cut, last_hit |
| 반짝 | 2 | 3 | 2 | 4 | 4 | 3 | sparkle, cute |
| 번뜩 | 2 | 3 | 2 | 3 | 3 | 3 | idea, flash |
| 달달 | 2 | 2 | 2 | 4 | 4 | 2 | sweet, flirt |
| 찐득 | 2 | 4 | 2 | 3 | 3 | 3 | sticky, groove |
| 끈끈 | 2 | 3 | 2 | 3 | 3 | 3 | sticky, cling |
| 찰칵 | 2 | 4 | 2 | 3 | 3 | 3 | camera, snap |
| 콕콕 | 2 | 4 | 2 | 4 | 4 | 3 | poke, tease |
| 뚝뚝 | 2 | 4 | 2 | 3 | 3 | 3 | drip, sweat |
| 쨍쨍 | 2 | 4 | 2 | 3 | 3 | 4 | bright, sun |
| 쌩쌩 | 2 | 4 | 2 | 4 | 3 | 4 | speed, engine |
| 붕붕 | 2 | 3 | 2 | 4 | 3 | 4 | engine, cute |
| 훅훅 | 2 | 3 | 2 | 3 | 3 | 4 | breathless |
| 휙휙 | 2 | 3 | 2 | 3 | 3 | 4 | fast, swing |
| 삐끗 | 2 | 3 | 2 | 3 | 3 | 3 | stumble, comedy |
| 아찔 | 2 | 2 | 2 | 3 | 3 | 3 | dizzy, romance |

### C-3. 3음절 HookTokens (고급 변주용, 과사용 금지)
| token | syl | atk | open | chant | trot | fatigue | tags |
|---|---:|---:|---:|---:|---:|---:|---|
| 화끈화끈 | 4 | 4 | 5 | 5 | 5 | 4 | heat, crowd |
| 후끈후끈 | 4 | 4 | 4 | 5 | 5 | 4 | heat |
| 번쩍번쩍 | 4 | 4 | 3 | 4 | 4 | 4 | neon |
| 반짝반짝 | 4 | 3 | 2 | 4 | 4 | 4 | sparkle |
| 두근두근 | 4 | 2 | 2 | 5 | 4 | 3 | heartbeat |
| 콩닥콩닥 | 4 | 3 | 2 | 4 | 4 | 4 | heartbeat |
| 쿵쾅쿵쾅 | 4 | 5 | 2 | 4 | 3 | 5 | impact |
| 빵빵빵빵 | 4 | 5 | 2 | 4 | 3 | 5 | horn, crowd |
| 달달달달 | 4 | 2 | 2 | 4 | 4 | 4 | sweet |

Rule: 4음절 반복형은 “후렴 1줄”에만 제한적으로 사용하고, 나머지 후렴은 2음절형으로 유지한다.

---

## [D] VERBPAIRS (동사쌍 라이브러리)

### D-1. Patterns (생성 규칙)
패턴 1: “-는다/-다 + -어/-아”  
예: 붙는다 붙어, 터진다 터져

패턴 2: “-한다 + -해”  
예: 흔든다 흔들어(변형), 당긴다 당겨

패턴 3: “-고 + -고” (구호/댄브)  
예: 돌고 돌고, 뛰고 뛰고

### D-2. High-Chant VerbPairs (후렴용 우선)
| pair | pattern | atk | chant | intensity | domain | notes |
|---|---|---:|---:|---:|---|---|
| 번진다 번져 | 1 | 3 | 5 | 4 | heat, fire | 후렴 2줄 끝 |
| 붙는다 붙어 | 1 | 4 | 5 | 4 | fire, cling | 후렴 2줄 끝 |
| 끓는다 끓어 | 1 | 3 | 4 | 4 | heat | 브릿지 선언 |
| 터진다 터져 | 1 | 4 | 4 | 5 | burst, impact | 후렴 클라이맥스 |
| 쏟아진다 쏟아 | 1 | 3 | 4 | 4 | spill, sweet | 벌스 말미 |
| 흔들린다 흔들려 | 1 | 3 | 4 | 4 | dance | 벌스 2, 댄브 |
| 달린다 달려 | 1 | 3 | 4 | 4 | speed, engine | 댄브 구호 |
| 박힌다 박혀 | 1 | 4 | 4 | 4 | tease, love | 훅 대비 라인 |
| 꽂힌다 꽂혀 | 1 | 4 | 4 | 4 | tease, love | 훅 대비 라인 |
| 감긴다 감겨 | 1 | 2 | 4 | 3 | spell, romance | 벌스 감정 |
| 넘친다 넘쳐 | 1 | 3 | 4 | 4 | crowd, emotion | 후렴 4줄 |
| 미친다 미쳐 | 1 | 4 | 4 | 5 | crazy, love | 후렴 4줄 |
| 돌아선다 돌아서 | 1 | 3 | 3 | 3 | comedy, drama | 벌스 전개 |
| 달아난다 달아 | 1 | 3 | 3 | 3 | chase, comedy | 벌스 전개 |
| 솟는다 솟아 | 1 | 3 | 3 | 3 | hype, energy | 프리 상승 |
| 뛰는다 뛰어 | 1 | 3 | 4 | 4 | heartbeat | 후렴 원인문 |
| 들킨다 들켜 | 1 | 4 | 3 | 3 | comedy, tease | 벌스 유머 |
| 잠긴다 잠겨 | 1 | 2 | 3 | 3 | romance | 벌스 촉감 |
| 박차인다 박차 | 1 | 4 | 3 | 4 | speed | 프리-후렴 진입 |
| 번쩍인다 번쩍여 | 1 | 3 | 3 | 3 | neon | 벌스 네온 |

### D-3. Heat/Fire Domain VerbPairs (앨범 변주 풀)
타오른다 타올라  
달아오른다 달아올라  
후끈해진다 후끈해져  
뜨거워진다 뜨거워져  
불붙는다 불붙어  
활활해진다 활활해져  
연기난다 연기나  
열오른다 열올라

### D-4. Electricity/Neon Domain VerbPairs
찌른다 찔러  
번쩍인다 번쩍여  
감전된다 감전돼  
스친다 스쳐  
튄다 튀어  
번개친다 번개쳐  
반짝인다 반짝여  
깜빡인다 깜빡여

### D-5. Engine/Speed Domain VerbPairs
부릉댄다 부릉대  
치고간다 치고가  
달린다 달려  
치솟는다 치솟아  
쏜다 쏴  
질주한다 질주해  
가속한다 가속해  
밀어붙인다 밀어붙여

### D-6. Sweet/Liquor Domain VerbPairs
달아진다 달아져  
녹아든다 녹아들어  
취한다 취해  
스민다 스며  
퍼진다 퍼져  
넘어간다 넘어가  
홀린다 홀려  
감미롭다 감미로워

Rule: 동일 트랙 안에서 VerbPair는 2개까지만 강제한다. 3개 이상은 “기교 과다” 위험으로 제한한다.

---

## [E] RHYME FAMILIES (끝소리 라임 패밀리)

### E-1. Primary Families (권장 8종)
| family_id | endings | strength | pool (종결 후보) | cautions |
|---|---|---:|---|---|
| RF-A | 아/봐/놔/와/가 | 4 | 가, 와, 봐, 놔, 나 | 단순 반복 과다 주의 |
| RF-EO | 어/어도/어서/어라 | 5 | 넘어, 들어, 붙어, 불러, 걸어 | 의미가 흐려지면 동사 교체 |
| RF-YEO | 져/려/여/였어 | 5 | 쓰러져, 무너져, 흔들려, 끌려 | 벌스 2줄 고정에 최적 |
| RF-UL | 을/를/술/불 | 4 | 술, 불, 꿀, 돌, 줄 | “-ul”은 의미 결속 필요 |
| RF-E | 게/네/왜/에 | 3 | 왜, 네, 게, 예 | 라임 강도 낮음 |
| RF-I | 지/지마/이지 | 3 | 있지, 쉽지, 그렇지 | 말맛은 좋으나 훅엔 과다 금지 |
| RF-ANG | 앙/짱/빵 | 3 | 빵, 짱, 꽝 | 코믹 트랙에서만 |
| RF-OK | 옥/톡/콕 | 4 | 톡, 콕, 툭 | 자음 타격 강함 |

### E-2. Verse Rhyme Couplet Templates (2줄 고정)
템플릿 1: (라인1 끝 = RF-YEO) / (라인2 끝 = RF-YEO)  
템플릿 2: (라인1 끝 = RF-EO) / (라인2 끝 = RF-EO)  
템플릿 3: (라인1 끝 = RF-A) / (라인2 끝 = RF-A)

Rule: 벌스 6줄 중 최소 2줄은 같은 family_id로 끝난다.

---

## [F] CONSONANT ATTACK MAP (자음 타격 지도)

### F-1. Attack Classes
- 최고 타격(후렴 최우선): ㄲ, ㅋ, ㅌ, ㅃ, ㅂ, ㄷ, ㄱ, ㅉ, ㅈ, ㅊ  
- 중간 타격(벌스 연결): ㅅ, ㅎ, ㅍ  
- 연결/완충(과다 시 맹탕): ㅁ, ㄴ, ㅇ, ㄹ

### F-2. Chorus Attack Heuristic
후렴 각 줄은 최소 1개 이상의 “타격 자음 군집”을 포함한다.

군집 예시(어휘 선택 기준):
- ㅂ/ㅃ 계열: 박히, 빡, 번, 불, 빵, 뻥
- ㄷ/ㅌ 계열: 딱, 탁, 터, 툭, 톡
- ㄱ/ㅋ/ㄲ 계열: 꽂, 콕, 쿵, 끓, 꺾
- ㅈ/ㅊ 계열: 찌, 쫙, 촥, 찰

### F-3. Verse Attack Control
벌스는 타격 자음을 “라인 끝”에 배치해 문장 흐름을 해치지 않게 한다.  
후렴처럼 전 구간 타격을 올리면 “말이 딱딱해져서” 노래성이 떨어진다.

---

## [G] VOWEL MOUTH-SHAPE MAP (모음 구강 지도)

### G-1. Open Vowels (후렴 벨팅 우선)
- ㅏ, ㅓ 계열: 화, 끈, 후, 끈, 터, 져, 박, 히, 딱
효과: 시원한 고음, 합창 용이, 무대 발화 안정

### G-2. Front Vowels (벌스 속도·말맛)
- ㅣ, ㅔ 계열: 미, 치, 기, 이, 네, 예
효과: 빠른 딕션, 랩처럼 촘촘한 느낌  
주의: 후렴 훅에 과다 사용하면 “얇고 번역체”처럼 들릴 위험이 있다.

### G-3. Mixed Vowel Strategy
- 벌스: 전설 모음(ㅣ/ㅔ)로 속도감을 만들고, 라인 끝은 개방 모음으로 착지한다.
- 후렴: 개방 모음 중심으로 설계하고, 트리거는 단타로 찍는다.

---

## [H] TRIGGER TAGS (편곡 트리거 라이브러리)

### H-1. English Triggers (Whitelist)
(Hot!), (Hey!), (Yeah!)

Rule: 사용자가 “NO ENGLISH”를 선언하면 EN 트리거는 전부 금지한다.

### H-2. Korean Triggers (기본값)
(와!), (야!), (하!), (어이!), (좋아!), (더!), (한 번!), (또!), (가자!)

### H-3. Hit/Cut Triggers (라스트 히트/컷)
(딱!), (탁!), (빵!), (팍!), (꽉!), (쾅!), (빠밤!)

### H-4. Placement Rules
- 후렴 4줄 중 최소 3줄: 라인 끝에 TriggerTag 1개
- 프리코러스: 마지막 1줄만 TriggerTag 허용
- 벌스: 최대 1개만 허용(과다 시 밀도 대비 붕괴)

---

## [I] METAPHOR POOLS (앨범 변주용 의미 풀)

### I-1. Domain: HEAT/FIRE (열/불)
- Nouns: 불, 열, 온도, 화염, 노을, 햇살, 열기
- Verbs: 달아오르다, 타오르다, 번지다, 붙다, 끓다
- Adjectives: 뜨거운, 화끈한, 후끈한, 빨간
- Scene Props: 여름밤, 무대 조명, 야외 행사, 박수

### I-2. Domain: ELECTRIC/NEON (전기/네온)
- Nouns: 전기, 스파크, 네온, 번개, 불빛, 신호
- Verbs: 찌릿하다, 번쩍이다, 튀다, 깜빡이다
- Adjectives: 반짝, 번쩍, 날카로운, 눈부신
- Scene Props: 도시 밤, 간판, 횡단보도, 클럽 입구

### I-3. Domain: ENGINE/SPEED (엔진/속도)
- Nouns: 엔진, 기어, 가속, 브레이크, 바퀴, 바람
- Verbs: 달리다, 질주하다, 쏘다, 밀어붙이다
- Adjectives: 빠른, 거친, 쌩쌩한, 붕붕한
- Scene Props: 드라이브, 도로, 신호등, 헬멧

### I-4. Domain: SWEET/LIQUOR (달콤/술)
- Nouns: 달콤함, 꿀, 설탕, 잔, 한 모금, 향
- Verbs: 넘어가다, 스미다, 녹아들다, 취하다
- Adjectives: 달달한, 부드러운, 진한, 향긋한
- Scene Props: 잔, 얼음, 밤공기, 한 잔 분위기

### I-5. Domain: CROWD/FESTIVAL (군중/축제)
- Nouns: 함성, 박수, 무대, 조명, 떼창, 손뼉
- Verbs: 뛰다, 흔들다, 외치다, 돌다
- Adjectives: 신나는, 크게, 더 세게, 다 같이
- Scene Props: 오른쪽/왼쪽 구호, 한 바퀴, 손 들어

Rule: 앨범 모드에서는 트랙마다 Domain을 최소 2트랙 연속으로 반복하지 않는다.

---

## [J] BANNED REUSE RULES (중복 방지 규칙)

### J-1. Track-Level (한 트랙 내부)
- HookToken은 1개를 “메인”으로 고정하고, 추가 HookToken은 최대 1개까지 보조로만 사용한다.
- VerbPair는 후렴에 2개 이하를 권장한다.
- TriggerTag는 후렴에서만 집중적으로 사용하고, 벌스에는 최대 1개만 허용한다.

### J-2. Album-Level (트랙 간)
- 메인 HookToken: 트랙 간 재사용 금지
- 메인 VerbPair: 트랙 간 재사용 금지
- Verse Rhyme Family: 인접 트랙 간 중복 금지
- 메타포 Domain: 인접 트랙 간 중복 금지
- “후렴 4줄 전체”는 트랙 간 재사용 금지(구조는 동일해도 어휘는 교체)

---

## [K] RECIPE CARDS (빠른 조합 카드)

### K-1. Recipe Template
Interjection + HookToken + VerbPairA + VerbPairB + RhymeFamilyVerse + TriggerSet + MetaphorDomain

### K-2. Example Recipes (10)
1) 야 + 화끈 + 번진다 번져 + 미친다 미쳐 + RF-YEO + (Hot!)/(딱!) + HEAT/FIRE  
2) 앗 + 찌릿 + 튄다 튀어 + 꽂힌다 꽂혀 + RF-EO + (와!)/(탁!) + ELECTRIC/NEON  
3) 와 + 붕붕 + 달린다 달려 + 밀어붙인다 밀어붙여 + RF-A + (가자!)/(빵!) + ENGINE/SPEED  
4) 어우 + 달달 + 넘어간다 넘어가 + 스민다 스며 + RF-EO + (좋아!)/(딱!) + SWEET/LIQUOR  
5) 야 + 들썩 + 흔들린다 흔들려 + 넘친다 넘쳐 + RF-YEO + (더!)/(한 번!) + CROWD/FESTIVAL  
6) 헉 + 번쩍 + 번쩍인다 번쩍여 + 감긴다 감겨 + RF-YEO + (와!)/(빠밤!) + ELECTRIC/NEON  
7) 오 + 팡팡 + 터진다 터져 + 쏟아진다 쏟아 + RF-EO + (Hey!)/(빵!) + HEAT/FIRE  
8) 어이 + 후끈 + 붙는다 붙어 + 뛰는다 뛰어 + RF-EO + (Hot!)/(딱!) + HEAT/FIRE  
9) 야 + 반짝 + 반짝인다 반짝여 + 들킨다 들켜 + RF-YEO + (와!)/(탁!) + NEON/CROWD  
10) 앗 + 쿵쾅 + 박힌다 박혀 + 흔들린다 흔들려 + RF-A + (하!)/(쾅!) + CROWD/FESTIVAL

Rule: Recipe는 “구조 예시”일 뿐이며, 실제 가사는 동일 문장으로 고정하지 않는다.

---

## [L] TRACKLOG TEMPLATE (사용자 반환용 기록)

TRACKLOG:
HookToken=
VerbPairA=
VerbPairB=
RhymeFamilyVerse=
MetaphorDomain=
TriggerSet=
Key=
BPM=
Notes=

---

## [M] ALBUM ALLOCATION SHEET (신규)

앨범 세션 시작 시 아래 표를 먼저 채운다. 이 표가 TRACKLOG_COLLECTION의 기준이 된다.

| TrackID | Role | HookToken | VerbPairA/B | RhymeFamilyVerse | MetaphorDomain | Key | BPM | Form | Status |
|---|---|---|---|---|---|---|---:|---|---|
| T01 | opener |  |  |  |  |  |  |  | planned |
| T02 | title-track |  |  |  |  |  |  |  | planned |
| T03 | variation-1 |  |  |  |  |  |  |  | planned |
| T04 | variation-2 |  |  |  |  |  |  |  | planned |
| T05 | crowd-peak |  |  |  |  |  |  |  | planned |
| T06 | finale |  |  |  |  |  |  |  | planned |

규칙:
- HookToken, 메인 VerbPair, RhymeFamilyVerse는 트랙 간 중복 금지.
- 인접 트랙끼리 MetaphorDomain 중복 금지.
- Key는 동일 키 2회 초과 금지.

## [N] TRACKLOG_COLLECTION TEMPLATE (신규)

```text
TRACKLOG_COLLECTION:
- T01: HookToken=, VerbPairA=, VerbPairB=, RhymeFamilyVerse=, MetaphorDomain=, TriggerSet=, LeadRiffBias=, Key=, BPM=, Status=planned
- T02: HookToken=, VerbPairA=, VerbPairB=, RhymeFamilyVerse=, MetaphorDomain=, TriggerSet=, LeadRiffBias=, Key=, BPM=, Status=planned
- T03: HookToken=, VerbPairA=, VerbPairB=, RhymeFamilyVerse=, MetaphorDomain=, TriggerSet=, LeadRiffBias=, Key=, BPM=, Status=planned
- T04: HookToken=, VerbPairA=, VerbPairB=, RhymeFamilyVerse=, MetaphorDomain=, TriggerSet=, LeadRiffBias=, Key=, BPM=, Status=planned
- T05: HookToken=, VerbPairA=, VerbPairB=, RhymeFamilyVerse=, MetaphorDomain=, TriggerSet=, LeadRiffBias=, Key=, BPM=, Status=planned
- T06: HookToken=, VerbPairA=, VerbPairB=, RhymeFamilyVerse=, MetaphorDomain=, TriggerSet=, LeadRiffBias=, Key=, BPM=, Status=planned
```

Status 값:
- planned / drafting / qa_fail / qa_pass / locked

END OF 01_LEXICON_CHAJJIM.md
