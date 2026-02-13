# EXAMPLE_OUTPUT (Format-Compliance Sample)

> 이 파일은 포맷 검증 예시다. 실제 운영 출력은 15트랙 전체를 동일 규격으로 채워야 한다.

# Album Concept
- Album Title: `Solar Loner 2026`
- Tagline: `도시의 불빛 사이, 불안과 결심이 같은 박자로 뛴다`
- Theme Sentence: `새해의 희망과 불안을 동시에 안고 대도시의 고독을 정면으로 통과하는 1인 서사`
- Theme Keywords: `new year, resolve, anxiety, neon, solitude, survival, breakthrough`
- Sound Palette: `bongo pulse, upright bass vamp, brushy hard swing kit, muted trumpet stabs, tight sax unison`
- Energy Curve (1~15): `2,2,3,3,4,4,5,5,4,4,3,3,4,5,2`

# Tracklist (15)
## Track 01
- Title: `Midnight Collision`
- Intent: `도입부에서 고독과 결심의 핵심 모티프를 제시`
- Energy: `2`
- Variation Axis: `stop-time density`
- Suno Style Prompt: `Female solo vocal / Space-noir Latin Jazz × Hard Bop × Jazz-Funk, 138 BPM, 4/4 hard swing, C minor w/ Dorian color. Minimalist arrangement: bongo + upright bass vamp, brushy drums, sparse muted-trumpet hits, tight sax unison riffs. Whisper-to-punch dynamics, stop-time breaks, wide stage but intimate mics, warm vintage tone with modern clarity, anxious-but-hopeful new-year loner mood in a midnight Seoul avenue, bongo plays clipped heartbeats between stop-time gaps, upright bass provides a tense circular vamp, brushy drums support hard-swing lift without crowding the vocal, muted trumpet provides short gold flashes, sax unison supports narrow alley urgency, vocal texture starts breathy then turns firm in chest register, delivery stays controlled and determined, phrasing drags behind beat then locks on impact words, intimate front-center vocal mix, medium plate reverb, light tape saturation, warm body with modern transient clarity.`
- Suno Style Prompt Char Count: `942`
- Lyrics: `VOCAL full lyric sections`

## Track 02
- Title: `Rooftop Oath`
- Intent: `결심을 전면화하고 리듬 추진력을 확대`
- Energy: `3`
- Variation Axis: `trumpet response timing`
- Suno Style Prompt: `Female solo vocal / Space-noir Latin Jazz × Hard Bop × Jazz-Funk, 138 BPM, 4/4 hard swing, C minor w/ Dorian color. Minimalist arrangement: bongo + upright bass vamp, brushy drums, sparse muted-trumpet hits, tight sax unison riffs. Whisper-to-punch dynamics, stop-time breaks, wide stage but intimate mics, warm vintage tone with modern clarity, determined urban-renewal mood with a rising edge of uncertainty, bongo plays tighter off-beat taps, upright bass provides a slightly more forward vamp push, brushy drums support denser backbeat accents, muted trumpet provides delayed answer cuts, sax unison supports sharper pre-chorus pivots, vocal texture keeps smoky grain with brighter upper-mid reach, delivery shifts from restrained confidence to punchy declarations, phrasing uses short clipped tails before each stop-time hit, room space remains wide but vocal stays close-mic, controlled short reverb, subtle tape warmth, clean mix separation for rhythm section clarity.`
- Suno Style Prompt Char Count: `975`
- Lyrics: `VOCAL full lyric sections`

## Track 03~15
- 동일 필드 구조를 유지한다.
- 각 트랙 `Suno Style Prompt`는 `STYLE_PROMPT_SPEC.md` 하드 규격을 그대로 통과해야 한다.
- `lyrics_input`이 제공된 경우 Track 01~15 `Lyrics`는 동일한 섹션 시그니처와 섹션별 라인 수를 유지해야 하며 `Instrumental`이 섞이면 실패다.
- `lyrics_input`이 비어 있는 경우 Track 01~15 `Lyrics`는 모두 `Instrumental`이어야 한다.
