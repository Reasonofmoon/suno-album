# Whisk Style Reference Set — T02 Comfortable Melancholy

> Purpose: generate consistent source images for `Flow -> Frames to Video` loops.
> Output target: dark, cinematic, neon-tinged melancholy visuals for long-form listening.

## Base Palette and Tone

- Primary: `#0D0D1A` (deep midnight)
- Secondary: `#4A148C` (cosmic purple)
- Highlight text tone: `#E8D5F5` (soft lavender)
- Mood curve: midnight stillness -> memory corridor -> neon peak -> acceptance -> first light

## Whisk Input Formula

Use 3-image input structure for each card:

- Subject image: object/space identity
- Scene image: lighting/weather context
- Style image: look and texture

Prompt suffix for all cards:

```text
cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up
```

## Reference Cards (12)

### W01 Midnight Rain Window

- Subject: dark window frame with rain streaks
- Scene: distant blurred neon lights on wet street
- Style: moody cinematic photography, deep blue-purple tones
- Whisk prompt:
  - `rain-streaked window at midnight, deep blue-purple tones, distant neon glow, soft interior darkness, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W02 Solo Piano Spotlight

- Subject: grand piano in dark room
- Scene: single moonbeam through window, dust motes
- Style: chiaroscuro concert photography
- Whisk prompt:
  - `grand piano in dark room with moonlight beam, floating dust particles, deep midnight tone, lonely elegant mood, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W03 Vinyl Warmth

- Subject: spinning vinyl record on turntable close-up
- Scene: amber needle light, dark surroundings
- Style: macro still life, warm analog film grain
- Whisk prompt:
  - `vinyl record spinning on turntable, warm amber needle light in dark room, purple ambient glow, nostalgic analog warmth, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W04 Neon City Rain

- Subject: wet urban street through glass
- Scene: blurred neon purple and blue, rain on window
- Style: cyberpunk-lite moody cinematography
- Whisk prompt:
  - `rain-soaked city street through wet window, blurred neon purple and blue signs, melancholy urban night, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W05 Cassette Desk

- Subject: cassette player and desk lamp
- Scene: warm pool of light in dark room
- Style: nostalgic lo-fi bedroom photo
- Whisk prompt:
  - `cassette tape player under warm desk lamp, dark room with purple shadows, nostalgic bedroom aesthetic, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W06 Cello in Concert Hall

- Subject: solo cello against dark stage
- Scene: single warm spotlight, deep blue ambient
- Style: editorial concert photography
- Whisk prompt:
  - `solo cello on dark stage with single spotlight, deep blue-purple ambient light, floating dust in beam, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W07 Synthwave Grid

- Subject: neon grid landscape horizon
- Scene: dark purple sky, star field
- Style: retro futurism digital art, 80s aesthetic
- Whisk prompt:
  - `retro synthwave neon grid landscape, dark purple horizon with stars, 80s retro futurism, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W08 Cosmic Milky Way

- Subject: night sky with milky way band
- Scene: mountain silhouette, deep cosmic colors
- Style: astrophotography, long exposure
- Whisk prompt:
  - `milky way night sky with dark mountain silhouette, deep cosmic purple and blue tones, vast scale, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W09 Foggy Bridge Dawn

- Subject: distant bridge in fog
- Scene: predawn blue-purple atmosphere, street halos
- Style: atmospheric landscape photography
- Whisk prompt:
  - `foggy bridge at predawn with warm street lamp halos, purple-blue atmosphere, melancholy and peaceful, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W10 Candle Solitude

- Subject: single candle on wooden surface
- Scene: dark room, warm amber light pool
- Style: dutch master still life, soft dramatic lighting
- Whisk prompt:
  - `single candle in dark room, warm amber light on wood, deep midnight blue shadows, solitary mood, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W11 Dawn Horizon

- Subject: first light line on eastern horizon
- Scene: deep purple sky transitioning to amber
- Style: minimal landscape, wide aspect film still
- Whisk prompt:
  - `first light of dawn on horizon, thin amber-pink line against deep purple sky, hopeful melancholy, cinematic wide composition, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

### W12 Morning Mist Resolution

- Subject: forest canopy in morning mist
- Scene: diffused warm light filtering through trees
- Style: serene nature photography, soft diffusion
- Whisk prompt:
  - `misty forest at dawn with gentle fog between trees, warm light filtering through canopy, peaceful resolution, cinematic, melancholy, low distraction, no text, no logo, no watermark, no human face close-up`

## Selection Checklist

- [ ] Human faces are absent or too far to be identifiable.
- [ ] Text/logo artifacts are not present.
- [ ] Palette aligns with T02 brand colors (`#0D0D1A` / `#4A148C` / `#E8D5F5`).
- [ ] Composition supports static camera looping.
- [ ] At least 6 images cover full energy curve from midnight to dawn.

## Handoff to Flow

For selected images:

1. Export as `16:9` high resolution PNG.
2. Feed to Flow as both first and last frame.
3. Use prompt IDs from `flow_video_prompts_T02.md`.
4. Save clips as `flow_t02_loop_XX.mp4`.
