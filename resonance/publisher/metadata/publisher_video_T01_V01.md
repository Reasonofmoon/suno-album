# publisher_video_T01_V01

## Inputs

- Album ID:
- Theme:
- Source audio folder:
- Background asset:
- Chapter file:

## Render Spec

- Resolution: `1920x1080`
- FPS: `30`
- Codec: `H.264 (libx264)`
- Audio: `AAC 320k`
- Loudness target: `-14 LUFS`

## FFmpeg Runbook

1. Merge tracks (crossfade if needed).
2. Normalize loudness.
3. Combine with static or loop background.
4. Inject chapter metadata.
5. QC pass (first 2 min, mid point, last 2 min).

## QA Checklist

- [ ] No clipping.
- [ ] No sudden level jumps.
- [ ] No corrupted frames.
- [ ] Duration matches expected runtime.
- [ ] Chapters align with track boundaries.

## Outputs

- Final video:
- Fallback render:
- Publish-ready hash/checksum:

