# 바이럴 싱글 트랙 워크플로우 템플릿

## 사용법
아래 변수만 채우고 SKILL.md의 싱글 트랙 워크플로우를 실행한다.

```yaml
TOPIC: "{{여기에 주제}}"
GENRE: "{{기본 장르}}"
VIBE: "{{분위기 한 줄}}"
LANGUAGE: "ko"    # ko / en / mixed
PLATFORM: "TikTok"  # TikTok / YouTube Shorts / Spotify / 없음
PERSONA: "auto"   # auto / VIRAL_BOMB / NIGHT_DRIFTER / STREET_POET / ...
```

## 9-Tool 릴레이 실행 순서

### 1️⃣ Simile → HOOK_SIMILE
TOPIC에 대한 짧고 강렬한 비유 5개 생성 → 가장 바이럴한 1개 선택

### 2️⃣ Explode → HOOK_SYLLABLES
HOOK에서 핵심 단어 1개 → 파편화 → 입에 붙는 2-3음절 조각 2-3개

### 3️⃣ Alliteration → TITLE + CATCH_PHRASE
두운법으로 제목 후보 2개 + 후렴 캐치프레이즈 1개

### 4️⃣ Acronym → MINI_STORY_LINES
TITLE 글자별 해체 → 3-4줄 마이크로 스토리

### 5️⃣ Chain → VERSE_KEYWORDS
감정 변화 체인 6-8개 → V1(초반) / V2(후반) 배분

### 6️⃣ Fuse → WORLD_CONCEPT
바이럴 공간 × 개인 공간 융합 → 곡 세계관 한 문장

### 7️⃣ Scene → V1_SCENE_LINES
WORLD_CONCEPT → 시네마틱 디테일 → Verse 1 첫 4줄

### 8️⃣ Unexpect → TWIST_LINE
예상 못한 전개 → Verse 2 핵심 이벤트

### 9️⃣ Unfold → DROP_LINES
워드플레이 숨은 단어 → Bridge/Drop용 1-2줄

## 최종 조립

```
[Suno Style]
Style of music: (GENRE 기반 + WORLD_CONCEPT 반영 하이브리드 장르)
Mood & vibe: (VIBE + HOOK_SIMILE 분위기)

[Suno Lyrics]
[Intro]
(선택 - 2줄 이내)

[Verse 1]
(V1_SCENE_LINES + VERSE_KEYWORDS 초반, 6-8줄)

[Pre-Chorus]
(CATCH_PHRASE 암시, 2-4줄)

[Chorus]
(HOOK_SIMILE or CATCH_PHRASE 중심 + HOOK_SYLLABLES 반복, ≤4줄)

[Verse 2]
(VERSE_KEYWORDS 후반 + TWIST_LINE, 6-8줄)

[Bridge]
(DROP_LINES + MINI_STORY_LINES, 2-4줄)

[Chorus]
(반복)
```

## 바이럴 체크리스트
- [ ] 각 줄 5-9음절?
- [ ] 훅 2회 이상 반복?
- [ ] 립싱크하기 쉬운 발음?
- [ ] 캡션으로 쓸 만한 문장 1개 이상?
- [ ] 15초 안에 훅 도달?
