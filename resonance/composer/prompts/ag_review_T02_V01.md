# ag_review_T02_V01 — Prometheus GUARDIAN Review

> **Agent**: ANTIGRAVITY
> **Mode**: GUARDIAN (Quality Review + Risk Assessment)
> **Date**: 2026-02-17 11:32 KST
> **Target**: `composer_prompts_T02_V01.md`

---

## Executive Verdict: ❌ NON-COMPLIANT — Needs V02 Upgrade

The current T02 prompts **violate every 5-Element Spec rule** established in T01_V01.

---

## Compliance Audit (T01 5-Element Spec)

| Rule | T01 Standard | T02 V01 Status | Severity |
|---|---|---|---|
| Char Count | 450–999 chars | ❌ 120–180 chars (avg ~155) | **CRITICAL** |
| 5 Elements | Identity + Mood + Instruments + Performance + Production | ❌ Only 2–3 present | **CRITICAL** |
| Action Verbs | ≥3 instrument verbs (plays, walks, floats…) | ❌ 0–1 per prompt | **HIGH** |
| Key/Mode | Required (D major, G minor…) | ❌ Completely absent | **HIGH** |
| Negative Prompt | Universal negative appended | ❌ Only "instrumental only, no vocals" | **MEDIUM** |
| One-Line Format | No newlines in final prompt | ⚠️ Multi-line with commas | **MEDIUM** |
| Metadata Block | Char count, Verb count, BPM, Key, Duration | ❌ Completely absent | **LOW** |

---

## Track-Level Findings

### Recurring Issues (All 15 Tracks)

1. **Under-specified** — Suno needs dense, descriptive prompts. 150-char prompts produce generic filler music
2. **No Performance Element** — Missing delivery/phrasing/dynamics descriptions
3. **No Production Element** — Missing mic placement, stereo field, tape warmth, reverb type
4. **No Key Signature** — Suno responds better with key hints
5. **Weak Negative Prompt** — Only "no vocals" but missing: no EDM drops, no distortion, no harsh sounds, no sudden transitions

### Per-Track Risk Items

| Track | Char | Issues |
|---|---|---|
| 01 | ~147 | No key, no performance descriptors, "analog synth pad" too vague |
| 02 | ~153 | "brush drums" → no verb, "tape hiss" is ambiguous intent |
| 03 | ~148 | "rain ambience undertone" needs spatial context (far/close) |
| 04 | ~152 | "muted trumpet with deep reverb" → no articulation verbs |
| 05 | ~142 | Nearly identical to Track 03 in structure |
| 06 | ~145 | "evolving synth layers" is placeholder text, needs specifics |
| 07 | ~138 | "electronic pulse" undefined — what kind? |
| 08 | ~142 | "retro drum machine" — which era/pattern? |
| 09 | ~155 | "cosmic soundscape" is mood not instruction |
| 10 | ~140 | Most similar to Track 06 in structure |
| 11 | ~142 | "Moog synthesizer lead" good, but rest is thin |
| 12 | ~135 | "flute melody" has no articulation details |
| 13 | ~128 | Shortest prompt — most risk of generic output |
| 14 | ~125 | "Solo cello with wide reverb space" — barely a sentence |
| 15 | ~120 | Critical closer — too sparse for Suno to produce distinctive ending |

---

## Similarity Risk Matrix

| Track Pair | Risk | Reason |
|---|---|---|
| 03 ↔ 05 | 🔴 HIGH | Both lo-fi + piano + vinyl, 4 BPM apart |
| 06 ↔ 10 | 🔴 HIGH | Both cello + electronic, same BPM (85) |
| 01 ↔ 13 | 🟡 MED | Both solo piano + ambient, 6 BPM apart |
| 01 ↔ 15 | 🟡 MED | Both solo piano + minimalist, 3 BPM apart |
| 14 ↔ 15 | 🟡 MED | Same fade zone, solo instrument + reverb |

---

## Recommendations

### MUST FIX (Before Suno Generation)

1. **Expand all prompts to 450-999 chars** following 5-Element Spec
2. **Add key signatures** (use minor keys for melancholy, occasional major for bittersweet)
3. **Add ≥3 action verbs** per prompt (plays, floats, weaves, anchors, shimmers, cascades, drifts…)
4. **Add universal negative prompt** from T01 standard
5. **Add metadata blocks** (char count, verb count, BPM, key, duration)

### SHOULD FIX

6. **Differentiate similar tracks** — Track 03/05 need distinct instrument timbres; Track 06/10 need different rhythmic feels
7. **Add spatial/production details** — mic placement, stereo field, room type, saturation level
8. **Strengthen Track 13–15** — The closer tracks are the weakest but most important for listener retention

---

## Severity Summary

- **CRITICAL**: 2 items (char count, 5-element coverage)
- **HIGH**: 2 items (action verbs, key signature)
- **MEDIUM**: 2 items (negative prompt, one-line format)
- **LOW**: 1 item (metadata blocks)

> **Next Action**: ANTIGRAVITY will produce `composer_prompts_T02_V02.md` with full 5-Element compliance.
