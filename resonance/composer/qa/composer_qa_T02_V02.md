# composer_qa_T02_V02

## QA Gate

- Minimum composite score: `4.0`
- Rubric weights:
  - Background-ability: `0.30`
  - Audio quality: `0.20`
  - Theme fit: `0.20`
  - Consistency: `0.15`
  - Listenability: `0.15`

## Prompt Compliance Gate

- [x] Prompt is one line.
- [x] Prompt length in target range (`450-999` for album tracks).
- [x] Prompt includes 5 elements (Identity/Mood/Instruments/Performance/Production).
- [x] Instrument action verbs `plays/provides/supports` are present.
- [x] No artist-name style mimicry.

## Track QA Table

| Track | Prompt Compliance | Background | Audio | Theme Fit | Consistency | Listenability | Composite | Decision | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 01 | ✅ |  |  |  |  |  |  |  |  |
| 02 | ✅ |  |  |  |  |  |  |  |  |
| 03 | ✅ |  |  |  |  |  |  |  |  |
| 04 | ✅ |  |  |  |  |  |  |  |  |
| 05 | ✅ |  |  |  |  |  |  |  |  |
| 06 | ✅ |  |  |  |  |  |  |  |  |
| 07 | ✅ |  |  |  |  |  |  |  |  |
| 08 | ✅ |  |  |  |  |  |  |  |  |
| 09 | ✅ |  |  |  |  |  |  |  |  |
| 10 | ✅ |  |  |  |  |  |  |  |  |
| 11 | ✅ |  |  |  |  |  |  |  |  |
| 12 | ✅ |  |  |  |  |  |  |  |  |
| 13 | ✅ |  |  |  |  |  |  |  |  |
| 14 | ✅ |  |  |  |  |  |  |  |  |
| 15 | ✅ |  |  |  |  |  |  |  |  |

## Album-Level Checks

- [ ] No silence gaps > 3 seconds.
- [ ] No abrupt volume spikes.
- [ ] Smooth handoff across track boundaries.
- [ ] Target loudness profile is consistent.
- [ ] Content ID pre-check completed.

## Handoff Summary

- Album ID: `T02_V02`
- Approved tracks:
- Rejected tracks:
- Final average score:
- Handoff status: `awaiting_generation`
