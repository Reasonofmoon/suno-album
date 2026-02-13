# QUALITY_GATE - SUNO Album Workflow

## Quick Gate
- [ ] 트랙 수가 정확히 15곡인가?
- [ ] 앨범 컨셉 필드(Title/Tagline/Theme/Keywords/Palette/Curve)가 모두 있는가?
- [ ] 각 트랙에 `Title/Intent/Energy/Variation Axis/Suno Style Prompt/Suno Style Prompt Char Count/Lyrics`가 모두 있는가?
- [ ] `lyrics_input` 없음(`INSTRUMENTAL`)에서 모든 트랙 `Lyrics`가 `Instrumental`로 표기되었는가?
- [ ] `lyrics_input` 있음(`VOCAL`)에서 15트랙 모두 완성 가사이며 무단 `Instrumental` 트랙이 0개인가?
- [ ] 금지 항목(직접 카피/직접 모사) 위반이 없는가?

## Diversity Gate
- [ ] 에너지 분포가 곡 전체에서 변화하는가?
- [ ] 최소 5곡 이상이 명확히 다른 Variation Axis를 가지는가?
- [ ] 악기/리듬/질감 키워드가 과도하게 단일 패턴으로 반복되지 않는가?

## Style Prompt Gate (HARD)
- [ ] 자동 검증 스크립트 실행: `../scripts/validate_album_file.ps1 -AlbumFilePath <album_file.md> -BasePrompt "<style_prompt>" -ExpectedMode <VOCAL|INSTRUMENTAL> -LyricsTemplateFilePath <lyrics_template.txt>`
- [ ] 각 트랙 `Suno Style Prompt`가 입력 원문 `style_prompt`를 verbatim으로 포함하는가?
- [ ] 각 트랙 `Suno Style Prompt`가 한 줄인가? (줄바꿈/엔터 없음)
- [ ] 각 트랙 `Suno Style Prompt` 길이가 공백 포함 1000자 미만인가?
- [ ] 각 트랙 `Suno Style Prompt Char Count` 값이 실제 길이와 일치하는가?
- [ ] 각 트랙 `Suno Style Prompt` 길이가 너무 짧지 않은가? (권장 450자 이상)
- [ ] `Identity:`, `Mood:`, `Instruments:`, `Performance:`, `Production:` 라벨이 없는가?
- [ ] 악기 묘사에 `plays`/`provides`/`supports` 동사가 포함되는가?
- [ ] 보컬 수행 정보(텍스처/전달/레인지/프레이징)가 포함되는가?
- [ ] 프로덕션 정보(공간/리버브/믹스/새츄레이션/클린-로파이)가 포함되는가?

## Lyrics Gate (VOCAL only)
- [ ] 입력 가사에서 추출한 섹션 시그니처(순서/개수)와 15트랙 가사 시그니처가 모두 일치하는가?
- [ ] 섹션별 라인 수가 입력 가사 템플릿과 일치하는가?
- [ ] 트랙별 총 분량(문자 수)이 입력 가사 대비 허용 배수 범위(기본 0.85~1.25)인가?
- [ ] 입력 가사 verbatim 복붙이 검출되지 않았는가? (라인 재사용 비율 기본 0.25 이하)
- [ ] 가사가 완전 신규 텍스트인가?
- [ ] 상투어 반복이 과도하지 않은가?
- [ ] 곡당 최소 2개 이상의 구체 이미지(장면/감각)가 있는가?

## Fail -> Fix
- 통일감 부족: 공통 키워드 3~5개 재고정 후 전체 트랙 프롬프트 재정렬
- 다양성 부족: Variation Axis를 강제로 재배분(tempo/instrument/rhythm/POV)
- 가사 품질 부족: 훅 문장 1개 + 구체 이미지 2개를 각 트랙에 추가
- 모드 위반: `lyrics_input` 존재 여부 기준으로 모드를 재결정하고 15트랙 전체를 일괄 수정
- 가사 구조 불량: 입력 가사 섹션 시그니처를 재추출해 Track 01~15 섹션 순서/라인 수를 동일화
- 가사 분량 불량: 섹션별 문장 길이를 조정해 입력 템플릿 분량 배수 범위로 복구
- 가사 복붙 검출: 템플릿 중복 라인을 제거하고 동일 의미를 신규 문장으로 치환
- 프롬프트 길이 부족: 원문 보존 뒤 Performance/Production 절을 확장해 450자 이상으로 재작성
- 프롬프트 구조 불량: 라벨 제거 후 5요소를 한 줄로 다시 압축
- 프롬프트 형식 불량: 줄바꿈 제거, 1000자 미만으로 재압축
