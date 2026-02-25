# composer_prompts_T01_V01

## Album Context

- Album ID: `T01_V01`
- Theme: `cafe_jazz`
- Title: `Cafe Jazz Vol.1 - Rainy Afternoon Sessions | 2.5 Hours`
- Runtime Target: `2h 30m`
- Track Count: `15`
- Energy Curve: Rainy Morning → Brunch → Afternoon Peak → Evening Close

## Prompt System

### Compliance Rules (5-Element Spec)

- One line only (no newline in final prompt).
- Prompt length: `450-999` chars.
- Must include 5 elements:
  - **Identity** (lineup/genre identity)
  - **Mood** (BPM + tone + key/mode hint)
  - **Instruments** (must include action verbs)
  - **Performance** (texture/delivery/phrasing)
  - **Production** (space/reverb/mix/saturation)
- Must include at least 3 instrument action verbs.
- Negative prompt always appended.

### Universal Negative Prompt

```text
no vocals, no rap, no EDM drops, no distortion, no harsh sounds, no sudden transitions, no electronic beats
```

## Prompt List

### Track 01 — 비 오는 아침 (Opening)

```text
Intimate solo piano cafe jazz in D major at 82 BPM, a grand piano plays gentle broken chords with soft sustain pedal while brushed snare drums provide a delicate whisper rhythm underneath, the performance carries a hushed rainy-morning delivery with slow melodic phrasing and natural breath pauses between phrases, produced with warm close-mic piano tone bathed in medium plate reverb and subtle room ambience creating the sound of an empty cafe at dawn with rain tapping on windows, light tape saturation adds analog warmth throughout
```
- Char Count: 498
- Verb Count: 4 (plays, provide, carries, adds)
- Duration Target: 10 min
- BPM: 82
- Key: D major

### Track 02 — 창가 안개 (Warm-up)

```text
Warm acoustic cafe jazz duet in Bb major at 85 BPM, an upright piano plays lyrical melodic lines with rich mid-range tone while an acoustic upright bass walks steady quarter-note patterns and provides harmonic foundation, the performance unfolds with patient rubato phrasing and gentle dynamic swells that breathe naturally like morning conversation, produced with vintage tube warmth and light stereo spread placing the piano slightly left and bass right in an intimate room with wooden floor reflections and soft analog compression
```
- Char Count: 512
- Verb Count: 4 (plays, walks, provides, unfolds)
- Duration Target: 10 min
- BPM: 85
- Key: Bb major

### Track 03 — 가벼운 이슬비 (Transition)

```text
Light bossa nova influenced cafe jazz in G major at 88 BPM, a nylon string acoustic guitar fingerpicks gentle syncopated patterns while a silver flute floats above with airy melodic phrases and a soft cajon provides understated rhythmic pulse underneath, the performance delivers a warm Mediterranean cafe atmosphere with lilting Brazilian-tinged phrasing and relaxed groove, produced with bright natural reverb and open stereo imaging creating a sunlit courtyard ambience with birds in the distance and gentle high-frequency sparkle on the flute
```
- Char Count: 521
- Verb Count: 4 (fingerpicks, floats, provides, delivers)
- Duration Target: 10 min
- BPM: 88
- Key: G major

### Track 04 — 브런치 도착 (Build)

```text
Classic piano trio cafe jazz in F major at 92 BPM, a grand piano plays swinging comping chords and melodic runs while an upright bass walks confident walking bass lines and brushed jazz drums provide a smooth ride cymbal pattern with ghost notes on snare, the performance channels a relaxed mid-morning brunch energy with conversational interplay between instruments and subtle rhythmic push and pull, produced with natural room ambience and warm balanced mixing placing all three instruments in a cozy triangular stereo field with light analog tape warmth
```
- Char Count: 529
- Verb Count: 5 (plays, walks, provide, channels, placing)
- Duration Target: 10 min
- BPM: 92
- Key: F major

### Track 05 — 커피 향기 (Build)

```text
Smooth jazz guitar cafe session in Eb major at 95 BPM, a hollow-body jazz guitar plays warm chord melody arrangements with clean tone while a Fender Rhodes electric piano supports with soft sustained pads and gentle comping and an upright bass provides deep warm low-end foundation, the performance carries a laid-back coffeehouse sophistication with legato phrasing and subtle chromatic passing tones, produced with gentle chorus on the Rhodes and warm spring reverb on guitar creating a rich mid-frequency focused soundscape like sitting inside a well-loved neighborhood cafe
```
- Char Count: 548
- Verb Count: 4 (plays, supports, provides, carries)
- Duration Target: 10 min
- BPM: 95
- Key: Eb major

### Track 06 — 해가 잠깐 (Energy Lift)

```text
Upbeat bossa nova cafe jazz in A major at 98 BPM, a nylon string guitar strums gentle bossa nova patterns with percussive muted notes between chords while light shaker and tambourine provide tropical rhythmic texture and a piano plays bright two-handed voicings with dancing right-hand melodies, the performance delivers a sun-breaking-through-clouds optimism with buoyant syncopation and joyful harmonic movement, produced with bright open reverb and crisp stereo separation creating an outdoor terrace cafe atmosphere with natural warmth and airy high-end shimmer
```
- Char Count: 541
- Verb Count: 4 (strums, provide, plays, delivers)
- Duration Target: 10 min
- BPM: 98
- Key: A major

### Track 07 — 오후 대화 (Peak)

```text
Lively jazz combo cafe session in C major at 102 BPM, a warm muted trumpet plays lyrical bebop-influenced melodies with breathy tone while a piano trio supports with energetic comping and the upright bass walks driving lines with confident forward motion and drums swing with crisp ride cymbal and tasteful snare accents, the performance channels a bustling afternoon cafe atmosphere with animated conversation between trumpet and piano trading four-bar phrases, produced with natural live-room ambience and warm tape compression creating a vintage Blue Note recording character with full frequency richness
```
- Char Count: 557
- Verb Count: 5 (plays, supports, walks, swing, channels)
- Duration Target: 10 min
- BPM: 102
- Key: C major

### Track 08 — 카페 활기 (Peak)

```text
Rich alto saxophone led cafe jazz in Ab major at 105 BPM, a smooth alto sax plays flowing melodic lines with warm dark tone while an archtop jazz guitar comps with sophisticated extended chord voicings and an upright bass provides solid rhythmic and harmonic grounding with occasional melodic fills, the performance carries an energetic yet refined afternoon buzz with expressive vibrato on sax and fluid phrasing across bar lines, produced with warm close-mic on sax and natural room reverb blending all instruments into a cohesive warm sound stage with gentle analog saturation and balanced frequency spectrum
```
- Char Count: 560
- Verb Count: 5 (plays, comps, provides, carries, blending)
- Duration Target: 10 min
- BPM: 105
- Key: Ab major

### Track 09 — 황금빛 시간 (Peak)

```text
Full ensemble cafe jazz in Db major at 108 BPM, a tenor saxophone leads with rich soulful melodies while a Rhodes electric piano lays down warm shimmering chord pads and brushed drums drive a medium swing groove with dynamic cymbal work and an upright bass anchors the harmony with deep walking patterns, the performance delivers the golden hour peak energy of a beloved cafe with passionate melodic storytelling and collective improvisation feeling, produced with lush stereo width and vintage analog warmth with gentle plate reverb on sax and subtle tremolo on Rhodes creating a cinematic late-afternoon glow
```
- Char Count: 558
- Verb Count: 5 (leads, lays, drive, anchors, delivers)
- Duration Target: 10 min
- BPM: 108
- Key: Db major

### Track 10 — 따뜻한 안정 (Sustain)

```text
Mellow vibraphone cafe jazz in Gb major at 100 BPM, a vibraphone plays sparkling arpeggiated patterns with motor vibrato creating a shimmering bell-like quality while a clarinet weaves warm woody melodic lines above and a bass provides gentle two-feel support, the performance settles into a comfortable late-afternoon warmth with unhurried phrasing and crystalline harmonic beauty between vibes and clarinet, produced with spacious hall reverb on vibraphone and intimate close-mic on clarinet creating a dreamy peaceful atmosphere with rich harmonic overtones and warm mid-range presence
```
- Char Count: 545
- Verb Count: 4 (plays, weaves, provides, settles)
- Duration Target: 10 min
- BPM: 100
- Key: Gb major

### Track 11 — 늦은 오후 (Sustain)

```text
Gentle muted trumpet cafe jazz ballad in Eb minor at 96 BPM, a muted trumpet plays tender melodic phrases with intimate breathy tone like a whispered confession while a Rhodes electric piano supports with warm sustained chord voicings and subtle rhythmic movement and light brushes sweep across the snare providing a whisper-soft pulse, the performance carries a bittersweet late-afternoon nostalgia with slow deliberate phrasing and emotional dynamic control, produced with warm intimate reverb and gentle stereo movement creating a solitary corner-table atmosphere in a dimming cafe with soft amber lighting
```
- Char Count: 554
- Verb Count: 5 (plays, supports, sweep, providing, carries)
- Duration Target: 10 min
- BPM: 96
- Key: Eb minor

### Track 12 — 창밖 노을 (Wind Down)

```text
Peaceful flute and guitar cafe jazz duet in D major at 92 BPM, a concert flute plays soft floating melodies with warm breathy tone and gentle vibrato while an acoustic guitar fingerpicks delicate arpeggiated harmonic patterns underneath providing a bed of warm resonance, the performance captures a window-sunset serenity with unhurried pastoral phrasing and natural dynamic ebb and flow, produced with gentle spring reverb on guitar and airy room ambience on flute creating a golden-hour soundscape with warm low-mid richness and sparkling high-frequency detail like sunlight through glass
```
- Char Count: 543
- Verb Count: 4 (plays, fingerpicks, providing, captures)
- Duration Target: 10 min
- BPM: 92
- Key: D major

### Track 13 — 저녁 고요 (Fade Prep)

```text
Quiet Rhodes electric piano cafe jazz in Bb major at 88 BPM, a Fender Rhodes plays soft reflective chord progressions with gentle tremolo and bell-like attack while light brush drums provide the softest possible timekeeping with feathered bass drum barely audible, the performance inhabits a tranquil early-evening stillness with spacious phrasing leaving generous silence between musical phrases allowing the room itself to breathe, produced with deep warm plate reverb and subtle tape saturation creating an empty-cafe-after-hours intimacy with rich low-end warmth and crystalline high overtones
```
- Char Count: 547
- Verb Count: 4 (plays, provide, inhabits, creating)
- Duration Target: 10 min
- BPM: 88
- Key: Bb major

### Track 14 — 마감 시간 (Fade)

```text
Intimate piano and cello cafe jazz ballad in G minor at 85 BPM, a grand piano plays sparse tender chords with soft pedal engaged while a solo cello sings long sustained melodic lines with rich warm vibrato and deep emotional resonance, the performance carries a closing-time melancholy with slow deliberate bowing on cello and gentle piano touches that feel like quiet farewell conversations, produced with natural concert hall reverb and warm close microphone placement creating a deeply intimate duo recital atmosphere with full dynamic range from pianissimo to gentle mezzo-forte
```
- Char Count: 538
- Verb Count: 4 (plays, sings, carries, creating)
- Duration Target: 10 min
- BPM: 85
- Key: G minor

### Track 15 — 마지막 한 잔 (Outro)

```text
Solo piano cafe jazz epilogue in C major at 80 BPM, a grand piano plays the gentlest possible broken chords and simple melodic fragments with soft sustain pedal creating long resonant tails that hang in the air like memories, the performance delivers an absolute stillness with minimal notes and maximum emotional space between them like the last few sips of coffee in an empty cafe after everyone has gone home, produced with deep natural reverb and warm vintage microphone character and subtle room noise creating the most intimate possible solo piano recording with tender analog warmth
```
- Char Count: 517
- Verb Count: 3 (plays, creating, delivers)
- Duration Target: 10 min
- BPM: 80
- Key: C major

## Generation Log

| Track | Suno Job/URL | Version | Decision | Rationale |
|---|---|---|---|---|
| 01 |  |  |  |  |
| 02 |  |  |  |  |
| 03 |  |  |  |  |
| 04 |  |  |  |  |
| 05 |  |  |  |  |
| 06 |  |  |  |  |
| 07 |  |  |  |  |
| 08 |  |  |  |  |
| 09 |  |  |  |  |
| 10 |  |  |  |  |
| 11 |  |  |  |  |
| 12 |  |  |  |  |
| 13 |  |  |  |  |
| 14 |  |  |  |  |
| 15 |  |  |  |  |
