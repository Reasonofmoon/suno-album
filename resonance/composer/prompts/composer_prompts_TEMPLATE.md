# composer_prompts_{album_id}

## Album Context

- Album ID:
- Theme:
- Title Candidate:
- Runtime Target:
- Track Count Target:

## Prompt System

### Base Prompt

```text
{genre and mood}, {instrumentation}, {bpm hint}, instrumental only,
background listening friendly, no sudden changes, no vocals, no harsh sounds
```

### Compliance Rules (Merged from Antigravity 5-Element Spec)

- One line only (no newline in final prompt).
- Album track prompt target length: `450-999` chars.
- Must include 5 elements in one sentence:
  - Identity (lineup/genre identity)
  - Mood (BPM + tone + key/mode hint)
  - Instruments (must include action verbs)
  - Performance (texture/delivery/phrasing)
  - Production (space/reverb/mix/saturation)
- Must include at least 3 instrument action verbs:
  - `plays`, `provides`, `supports`

### Variation Layers

- Layer 1 Base:
- Layer 2 Instrument rotation:
- Layer 3 BPM drift:
- Layer 4 Mood gradient:
- Layer 5 Texture evolution:

## Prompt List

| Track | Mode | Prompt (One-line) | Char Count | Verb Count | Negative Prompt | Target Duration (min) | Compliance | Notes |
|---|---|---|---:|---:|---|---:|---|---|
| 01 | INSTRUMENTAL |  |  |  |  |  |  |  |
| 02 | INSTRUMENTAL |  |  |  |  |  |  |  |
| 03 | INSTRUMENTAL |  |  |  |  |  |  |  |

## Generation Log

| Track | Suno Job/URL | Version | Decision | Rationale |
|---|---|---|---|---|
| 01 |  |  |  |  |
| 02 |  |  |  |  |
