# Album Quality Checklist (v1.1)

이 체크리스트는 `.blueprint` / `.generate` / `.export` 단계에서 빠르게 품질을 점검하기 위한 용도다.

## A) Blueprint Gate (가사 생성 전)
- [ ] 앨범 logline이 1문장으로 명확하다.
- [ ] themes가 5~9개로 과밀하지 않고, 트랙별 sub_theme로 분해 가능하다.
- [ ] narrative_arc가 4~6단계로 설계되어 있고 트랙 순서에 반영된다.
- [ ] sonic_palette에 220–240 BPM 범위/드럼 질감/모티프/믹스 노트가 들어 있다.
- [ ] 15곡 모두 `primary_differentiator`가 있다(그리고 서로 겹치지 않는다).
- [ ] “같은 비트/같은 훅/같은 흐름”으로 15곡을 복붙하는 구조가 아니다.
- [ ] tracklist에 `hook_mode`(micro chant)와 `verse2_switch_tag`가 명시되어 있다.

**Fail → Fix 힌트**
- 차별점이 약하면: 각 트랙에 “드럼 그루브/훅 모드/플로우 팔레트/악기 모티프/수사 장치” 중 1개를 강제 배정.

## B) Track Gate (곡별)
- [ ] Genre Prompt가 800자 내외(1000자 미만)이며, rap-first 제약이 있다.
- [ ] Lyrics가 1,300~2,200자 가이드 안에 있으며, Global Style 태그 + 섹션 헤더/메타태그를 지킨다.
- [ ] Hook가 2–3줄 micro chant로 설계되어 있다(너무 산문형 X).
- [ ] Verse 2 시작 태그에 “Switch to …”가 포함되어 있고 chopper 구간 태그가 있다.
- [ ] Verse 1(격식/우아한 디스) → Verse 2(구어체/욕설 폭풍) 딕션 반전이 분명하다.
- [ ] Verse 2에 기술적 고조가 있더라도, 과도한 남발/똑같은 클라이맥스 복제는 피했다.
- [ ] Rap-only 규칙(No Singing/No Autotune)이 지켜졌다.
- [ ] 반복 모티프는 존재하지만, micro-variation으로 변주가 설명된다.

## C) Export Gate (단일 MD 파일)
- [ ] 앨범 제목/컨셉/트랙리스트/트랙별 프롬프트+가사/커버 프롬프트가 한 파일에 들어 있다.
- [ ] 파트 분할(`PART 1/N`)로 출력되었으면, 그대로 이어 붙이면 1개 파일이 된다.
- [ ] 표/헤더/코드블록이 깨지지 않는다.
