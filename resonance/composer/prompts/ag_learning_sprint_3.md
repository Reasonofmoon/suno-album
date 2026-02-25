# Learning Sprint #3 — AI Video Generation for Music Album

> Date: 2026-02-15 | Agent: ANTIGRAVITY
> Topic: Google Flow (Veo), Whisk AI, Seamless Loop Video Production

## 🔍 탐색 소스

| Tier | 소스 | 핵심 수확 |
|------|------|-----------|
| Tier 4 | Google I/O 2025 발표 | Flow = Veo 3.1 기반 AI 영상 제작 도구 |
| Tier 4 | Google Labs (Whisk) | 이미지 기반 프롬프팅 → 스타일 리믹스 + 애니메이션 |
| Tier 4 | YouTube Creator 사례 | Looping 배경 영상 제작 워크플로우 |
| Tier 4 | Reddit r/VideoEditing | Flow "frames-to-video" 루프 트릭 검증 |

## 💡 핵심 인사이트

### 1. Google Flow (Veo 3 / 3.1)

**접속:** `labs.google/flow` (Google AI Pro/Ultra 구독 필요)

| 기능 | 설명 |
|------|------|
| Text-to-Video | 텍스트 프롬프트 → 시네마틱 영상 클립 |
| Frames-to-Video | 첫/끝 프레임 이미지 지정 → 영상 생성 |
| Expand | 영상 장면 확장 + 스타일 유지 |
| Synchronized Audio | Veo 3.1: 환경음/대화 자동 싱크 |
| 해상도 | 1080p (Veo 3), 4K (Veo 3.1) |

**🔑 루프 영상 핵심 기법: Frames-to-Video Same-Frame Trick**

```
1. 기준 이미지 1장 생성 (카페 창가, 비, 조명 등)
2. Flow에서 "Frames to Video" 선택
3. 첫 프레임 = 마지막 프레임 = 동일 이미지
4. 프롬프트: "gentle rain falling, steam rising from coffee, soft warm light"
5. 생성 → Veo가 시작과 끝이 같은 영상 제작
6. (선택) CapCut에서 앞뒤 2-3프레임 트리밍 → 완벽한 루프
```

### 2. Google Whisk AI

**접속:** `labs.google/whisk` (무료, Google 계정)

| 기능 | 설명 |
|------|------|
| Image-to-Image | 주제/장면/스타일 이미지 3개 입력 → 리믹스 |
| Image Animation | 정지 이미지 → 짧은 영상 변환 |
| Style Transfer | 한 이미지의 스타일을 다른 장면에 적용 |
| Imagen 3/4 | 고품질 이미지 생성 엔진 |

**활용법:**
```
1. Whisk에서 카페 장면 이미지 생성 (주제: 카페, 장면: 비오는 오후, 스타일: 유화)
2. 생성된 이미지를 Flow의 첫/끝 프레임으로 활용
3. 또는 Whisk 자체 Image Animation으로 짧은 클립 생성
```

### 3. 실전 워크플로우: T01 카페재즈 루프 영상 제작

```
Phase 1: 기준 이미지 생성 (Whisk + Imagen 4)
  ├── 장면 5-8개 (카페 4면: 창가/내부/테라스/바)
  ├── 시간대별 조명 변화 (아침→오후→저녁)
  └── 스타일 일관성: 동일 스타일 이미지 레퍼런스

Phase 2: 루프 영상 생성 (Flow / Veo 3.1)
  ├── 각 장면별 8-10초 루프 클립
  ├── Frames-to-Video (동일 프레임 트릭)
  ├── 프롬프트: 움직임 최소화 (비, 증기, 조명 깜빡임)
  └── 비용: Veo 3 Fast 모드 → 크레딧 절약

Phase 3: 후처리 + 조합 (FFmpeg / CapCut)
  ├── 앞뒤 프레임 트리밍 → 완벽 루프
  ├── 장면 간 크로스페이드 (4초)
  ├── 색보정: #8B6914 / #3E2723 / #FFF8E1 팔레트 매칭
  └── 최종 2.5시간 영상 = 3-4개 장면 순환

Phase 4: 음악 + 영상 합성 (FFmpeg)
  ├── 15트랙 연결 + 챕터 마커
  ├── 영상 루프 + 오디오 싱크
  └── YouTube 업로드용 최종 렌더링
```

## 🎬 트랙별 영상 장면 매핑

| 트랙 | 에너지 | 추천 장면 | Flow 프롬프트 |
|------|--------|-----------|---------------|
| 01-03 | 아침 | 비 내리는 창가 | Gentle rain on cafe window, warm yellow light inside, steam from coffee cup |
| 04-06 | 브런치 | 카페 내부 활기 | Cozy cafe interior, sunlight through rain clouds, people silhouettes |
| 07-09 | 피크 | 테라스 황금빛 | Golden hour terrace, warm amber light, gentle breeze on plants |
| 10-12 | 안정 | 바 카운터 | Warm bar counter, soft lamp light, coffee being poured slowly |
| 13-15 | 저녁 | 어두워지는 창가 | Dimming cafe window, street lights, last cup of coffee, candle |

## 💰 비용 분석

| 도구 | 비용 | 용도 |
|------|------|------|
| Whisk | 무료 | 기준 이미지 생성 |
| Flow (AI Pro) | $19.99/월 | 루프 영상 생성 |
| Flow (AI Ultra) | $49.99/월 | 4K + 더 많은 크레딧 |
| CapCut | 무료 | 후처리 트리밍 |
| FFmpeg | 무료 | 최종 조합 |

**추천:** AI Pro ($19.99/월) 1개월 → 전체 앨범 영상 제작 → 해지

## 🔗 스트림 연결

- **T01 카페재즈 프롬프트** → 영상 프롬프트와 무드 매칭 가능
- **Distribution Strategy** → YouTube 롱폼 영상에 루프 배경 필수
- **Shorts 파이프라인** → Flow 클립을 30-60초 세로 영상으로 재활용

## 💡 새 아이디어

1. **Whisk → Flow 파이프라인 자동화**: Whisk 이미지를 Flow API로 자동 전달
2. **시간대별 장면 전환**: 에너지 곡선에 맞춰 영상도 아침→저녁 전환
3. **Veo 3.1 환경음 활용**: 비 소리, 커피 머신 소리를 영상에서 생성 → 음악과 레이어링

## 📊 자기 평가

| 항목 | 점수 |
|------|------|
| 학습 깊이 | ★★★★☆ (4/5) — Flow/Whisk 핵심 기능 파악, API 레벨은 미탐색 |
| 적용 가능성 | ★★★★★ (5/5) — T01 앨범에 바로 적용 가능한 구체적 워크플로우 |
