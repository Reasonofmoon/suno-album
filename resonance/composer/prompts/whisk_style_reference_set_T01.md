# Whisk Style Reference Set — T01 Cafe Jazz Vol.1

> Purpose: generate consistent source images for `Flow -> Frames to Video` loops.
> Output target: warm, cinematic, low-distraction cafe visuals for long-form listening.

## Base Palette and Tone

- Primary: `#8B6914` (warm gold)
- Secondary: `#3E2723` (dark brown)
- Highlight text tone: `#FFF8E1` (cream)
- Mood curve: rainy morning -> brunch warmth -> golden peak -> quiet closing

## Whisk Input Formula

Use 3-image input structure for each card:

- Subject image: object/space identity
- Scene image: lighting/weather context
- Style image: look and texture

Prompt suffix for all cards:

```text
cinematic, cozy, low distraction, no text, no logo, no watermark, no human face close-up
```

## Reference Cards (12)

### W01 Rain Window Impressionist

- Subject: inside cafe window frame and wooden sill
- Scene: rain streaks on glass, blurred city lights
- Style: warm impressionist oil painting, soft brush texture
- Whisk prompt:
  - `cozy rainy cafe window, warm amber interior glow, gentle reflections, cinematic, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W02 Dawn Cup Macro

- Subject: ceramic coffee cup close-up
- Scene: dawn light from side window, rising steam
- Style: cinematic macro photography, shallow depth of field
- Whisk prompt:
  - `coffee cup macro with soft steam, dawn side light, polished wooden table, cinematic bokeh, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W03 Misty Glass Minimal

- Subject: fogged cafe glass and condensation drops
- Scene: light rain, quiet street outside
- Style: minimal fine art photo, muted warm-cool contrast
- Whisk prompt:
  - `misty cafe glass with condensation and rain traces, warm interior cool exterior contrast, minimal composition, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W04 Brunch Interior Amber

- Subject: wooden tables and chairs, small plants
- Scene: sunlight breaking through cloud gaps
- Style: film still, Kodak-like warm grain
- Whisk prompt:
  - `warm brunch cafe interior, sunbeams and dust particles, wooden textures, soft film grain, cinematic, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W05 Counter Steam Chiaroscuro

- Subject: espresso machine and counter top
- Scene: slow steam and practical lamp highlights
- Style: chiaroscuro lighting, moody cafe realism
- Whisk prompt:
  - `espresso counter with subtle steam and amber lamp reflections, dark brown cinematic contrast, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W06 Terrace Golden Leaves

- Subject: outdoor terrace table and string lights
- Scene: golden hour and light breeze
- Style: dreamy soft-focus photography
- Whisk prompt:
  - `golden hour cafe terrace, gentle leaf movement mood, string lights, warm dreamy optics, cinematic, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W07 Bottle Shelf Glow

- Subject: cafe shelf with bottles and cups
- Scene: late afternoon light rays and soft bokeh
- Style: vintage cinema still
- Whisk prompt:
  - `glass bottle shelf in warm afternoon rays, subtle reflections, vintage cafe cinema still look, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W08 Blue Hour Window

- Subject: rain window with table and candle
- Scene: blue hour outside, amber interior lamp
- Style: poetic night photography
- Whisk prompt:
  - `blue hour rainy cafe window with single candle, amber and navy harmony, poetic cinematic mood, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W09 Empty After Hours

- Subject: nearly empty cafe floor and chairs
- Scene: closing time, one lamp on
- Style: analog film realism, subtle grain
- Whisk prompt:
  - `empty cafe after hours, one warm lamp, quiet closing atmosphere, analog film texture, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W10 Last Cup Epilogue

- Subject: single cup on table near window
- Scene: faint rain and dim street lights
- Style: intimate still life, soft halation
- Whisk prompt:
  - `single final coffee cup near dark rainy window, intimate still life with soft halation, cinematic epilogue mood, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W11 Warm Monochrome Brown

- Subject: cafe interior mid shot
- Scene: steady low-intensity indoor light
- Style: monochrome warm-brown grade, print-like texture
- Whisk prompt:
  - `cozy cafe interior in warm monochrome brown palette, stable gentle light, print-like texture, cinematic, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

### W12 Painterly Jazz Poster Feel

- Subject: window table, cup, notebook, sax case silhouette
- Scene: rainy evening ambience
- Style: painterly editorial, modern jazz poster vibe
- Whisk prompt:
  - `rainy evening cafe table with notebook and coffee, subtle sax case silhouette, painterly editorial jazz mood, cinematic, cozy, low distraction, no text, no logo, no watermark, no human face close-up`

## Selection Checklist

- [ ] Human faces are absent or too far to be identifiable.
- [ ] Text/logo artifacts are not present.
- [ ] Palette aligns with T01 brand colors.
- [ ] Composition supports static camera looping.
- [ ] At least 6 images cover full energy curve from morning to closing.

## Handoff to Flow

For selected images:

1. Export as `16:9` high resolution PNG.
2. Feed to Flow as both first and last frame.
3. Use prompt IDs from `flow_video_prompts_T01.md`.
4. Save clips as `flow_t01_loop_XX.mp4`.
