# Suno Album Production — Agent Instructions

## Available MCP Tools (noapi-google-search)

이 프로젝트에서는 다음 도구들을 우선 활용합니다:

### 🎵 앨범 기획
- **`google_trends`**: 음악 키워드/장르 트렌드 분석 → 시장 맞춤 테마 선정
- **`google_news`**: 음악 산업/AI 음악 관련 뉴스 수집
- **`google_images`**: 앨범 커버 레퍼런스 이미지 검색

### 📡 커뮤니티 모니터링
- **`subscribe("reddit", "SunoAI")`**: Suno AI 커뮤니티 트렌드 추적
- **`subscribe("reddit", "AIMusic")`**: AI 음악 전반 동향
- **`subscribe("youtube", "@SunoMusic")`**: Suno 공식 채널 업데이트
- **`check_feeds()`**: 구독 피드 일괄 수확
- **`search_feeds("lo-fi")`**: 특정 장르/키워드 검색

### 🚀 배포 & 마케팅
- **`shorten_url`**: 앨범 링크 단축 (SNS 공유용)
- **`generate_qr`**: 앨범 QR 코드 생성 (물리적 배포용)
- **`paste_text`**: 프로모션 텍스트 공유
- **`google_search(site:"suno.com")`**: Suno 플랫폼 내 트렌드곡 검색

### 📊 경쟁 분석
- **`google_search`**: 경쟁 AI 음악 프로젝트 조사
- **`visit_page`**: 경쟁사/트렌드 페이지 상세 분석
- **`google_scholar("AI music generation")`**: 학술적 배경 리서치

## Workflow: 앨범 기획 → 배포

```
1. google_trends("lo-fi study music 2026")    # 트렌드 확인
2. google_images("album cover minimalist")     # 커버 레퍼런스
3. subscribe("reddit", "SunoAI")              # 커뮤니티 등록
4. check_feeds()                               # 트렌드 수확
5. [Suno에서 트랙 생성]
6. shorten_url(album_url)                      # 배포 링크
7. generate_qr(shortened_url)                  # QR 생성
```

## Chrome AI (Optional)

`enable-chrome-ai`로 Chrome 내장 Gemini 활성화 시, 브라우저에서 직접 AI 기반 Suno 히스토리 검색 가능.
