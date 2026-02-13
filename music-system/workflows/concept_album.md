# 컨셉 앨범 워크플로우 템플릿

## 사용법
아래 JSON 형식으로 입력값을 채우고 SKILL.md의 앨범 모드 워크플로우를 실행한다.

```json
{
  "style_prompt": "{{Suno 장르/스타일 프롬프트 원문}}",
  "lyrics_input": "",
  "concept_mode": "auto",
  "concept_request": "{{테마/키워드/금지 요소}}",
  "language": "ko",
  "track_count": 10,
  "persona": "auto"
}
```

## lyrics_input 모드 판별
- `lyrics_input` **비어있음** → `INSTRUMENTAL` 강제
- `lyrics_input` **있음** → `VOCAL` 강제

## Step-by-Step

### Step A1: 입력 정규화
- 누락값에 기본값 적용
- lyrics_input이 있으면 섹션 시그니처 추출 → `lyrics_structure_blueprint`

### Step A2: 앨범 컨셉 빌드
```markdown
# Album Concept
- Album Title: 
- Tagline: (한 줄 태그라인)
- Theme Sentence: (컨셉 한 문장)
- Theme Keywords: (3-5개)
- Sound Palette: (사운드 재료)
- Energy Curve: (1→N 에너지 설계)
```

**에너지 커브 설계 원칙:**
- 시작과 끝은 낮게 (1-2)
- 중반 클라이맥스 (4-5)
- 곡들 사이 에너지 변화는 ±2 이내
- 예: `[2, 3, 3, 4, 5, 5, 4, 3, 2, 1]`

### Step A3: 트랙 블루프린트
```markdown
## Track 01
- Title: 
- Intent: (이 곡의 역할/장면)
- Energy: (1-5)
- Variation Axis: (변주 축)
```

### Step A4: 트랙 생성
각 트랙에:
1. **Suno Style Prompt** (5-Element, 450-999자, 한 줄)
2. **Suno Style Prompt Char Count** (정수)
3. **Lyrics** (VOCAL: 완성 가사 / INSTRUMENTAL: `Instrumental`)

### Step A5: 품질 검증

#### Quick Gate
- [ ] 트랙 수 = 지정 곡 수
- [ ] 모드 일관성 (全VOCAL 또는 全INSTRUMENTAL)
- [ ] 제목 중복 없음

#### Style Prompt Gate
- [ ] 한 줄 (줄바꿈 없음)
- [ ] 450-999자
- [ ] 5요소 포함
- [ ] 라벨 문자열 없음
- [ ] `plays`/`provides`/`supports` 동사 ≥3회

#### Lyrics Gate (VOCAL only)
- [ ] 섹션 구조 일관성
- [ ] lyrics_input verbatim 복붙 없음
- [ ] reuse 비율 ≤ 0.25
- [ ] 총 분량 0.85~1.25배

#### Diversity Gate
- [ ] 에너지 커브 ≥3 단계 사용
- [ ] Variation Axis 중복 ≤30%

### Step A6: 최종 출력
마지막에 전체 앨범을 Markdown으로 정리하여 출력.

## 출력 포맷
```markdown
# Album Concept
- Album Title: ...
- Tagline: ...
- Theme Sentence: ...
- Theme Keywords: ...
- Sound Palette: ...
- Energy Curve: ...

# Tracklist
## Track 01
- Title: ...
- Intent: ...
- Energy: ...
- Variation Axis: ...
- Suno Style Prompt: (한 줄)
- Suno Style Prompt Char Count: N
- Lyrics: ...

## Track 02
...
```
