# 5-Element 스타일 프롬프트 규격서

## 목적
각 트랙의 Suno Style Prompt를 태그 수준이 아닌 **실제 생성 제어가 가능한 밀도**로 작성한다.

## 하드 포맷
1. 반드시 **한 줄** (줄바꿈 금지)
2. 싱글 트랙: **200~999자** / 앨범 트랙: **450~999자**
3. 아래 5요소를 **라벨 없이** 모두 포함
4. 쉼표/세미콜론으로 정보 밀도를 높임

## 5 Elements (라벨 없이 포함)

| Element | 내용 | 예시 |
|---------|------|------|
| **Identity** | 보컬 성별/편성 + 장르 정체성 | `Female solo vocal / Space-noir Latin Jazz × Hard Bop` |
| **Mood** | 템포(BPM) + 정서 + 조성/모드 | `138 BPM, 4/4 hard swing, C minor w/ Dorian color` |
| **Instruments** | 악기 + **연주 동사** 필수 | `bongo plays clipped syncopation, bass provides vamp` |
| **Performance** | 보컬 텍스처, 딜리버리, 음역, 프레이징 | `breathy whisper to focused chest register` |
| **Production** | 공간감, 리버브, 믹스, 새츄레이션 | `intimate front-center mix, medium plate reverb` |

## 필수 키워드 (한 줄에 최소 1개씩)
- Instruments 동사: `plays` / `provides` / `supports`
- Performance 큐: `texture` / `delivery` / `register` / `range` / `phrasing`
- Production 큐: `space` / `reverb` / `mix` / `saturation` / `clarity`

## ❌ 비준수 예시
```
Female solo vocal, Jazz-Funk, high energy, wide stage.
```
→ 너무 짧음, 5요소 누락, 동사 미사용

## ✅ 준수 예시
```
Female solo vocal / Space-noir Latin Jazz × Hard Bop × Jazz-Funk, 138 BPM, 4/4 hard swing, C minor w/ Dorian color, bongo plays clipped heartbeat syncopation, upright bass provides a tense looping vamp, brush drums support hard-swing lift, muted trumpet provides short neon cuts, vocal texture moves from breathy whisper to focused chest register, delivery stays restrained then decisive, phrasing lands late then snaps on accents, intimate front-center mix with medium plate reverb, low tape saturation, clear transient edges
```
