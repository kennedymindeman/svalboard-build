---
type: Reference
title: Ergonomics and fit
description: Fit order, cluster geometry, key weight, palm rests, mounting, and fixes for specific pains.
tags: [svalboard, discord, ergonomics]
source: "discord #general 1124364902811844739, 2025-10-17..2026-08-15"
---

# Ergonomics and fit

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; agreement counts are floor estimates.

- **Don't change your alpha layout at the same time as the board** — a multi-month commitment that
  raises the odds you quit; use what you already touch-type (claussen still types QWERTY after 25 years),
  and if you must optimize, Hands Down Neu or HD Promethium, flipping N/S because S keys beat N on a Sval
  (280360, 820933, 586853).
- **"This is a fit issue, not a force issue."** If you feel like you're hovering, raise the hand or
  lower the clusters; claussen's test is adding a few mm on the palm rest and watching preload change.
  Bottoming out every key is expected at first; hunting for bottom means too much preload (803008, 022660).
- **Fit order (Cyrus)**: wrists straight and flat → middle-finger orientation and palm-rest distance →
  index → ring/little → thumb → pointing device last. Common failures: living at one end of the
  adjustment range, and squaring the board to the desk edge instead of twisting the baseplates (547230,
  407537, 848370).
- **Clusters should not be parallel** — fingers are rays converging at the wrist, each finger roughly
  perpendicular to its center key at rest (N = extension, S = flexion, E/W = splay). **North keys are a
  flick upward, not an outward extension.** **Don't tilt clusters toward the palm** (the Azeron ask):
  no muscle makes a finger longer, so at the extreme you can't press center at all (372621, 378344,
  340535).
- **Clusters deliberately don't pitch north-south** — bend the metal towers or print the
  pitch-adjustable ones, but don't add degrees of freedom before you're adapted (942065, 028865).
- **If every cluster is twisted the same direction in a photo, rotate the whole base instead.** Pinky
  fixes in order: raise the pinky cluster a hair so fingers "just touch"; shim under the outside of the
  cluster arm with paper; add pinky stagger; heat-bend the pinky S key; bend or reprint the tower
  (673577, 267235, 176670, 550306).
- **Key weight: ~20 gf default, set by the magnet offset baked into the key** — 0.7 mm ≈ 20 g, 1.0 mm ≈
  ~10 g, zero offset 60 g+, and a 0.1–0.2 mm change is huge. Changing weight means new **keys**, not
  clusters or magnets; go stiffer (1.0–1.2) for gaming (725607, 162743, 471865, 559).
- **Slim clusters for narrow hands** — mix with standard, print one first to test-fit, and pair opposite
  "missing corners" to squeeze tighter; slim clusters need slim PCBAs, no going back after purchase.
  **Laterals**: inward are light and quick to learn, outward awkward, worst on the ring (498001, 224460).
- **Palm rests**: 5 mm shims by default, removable — "there's no right fit, there's just what fits you."
  **Rest the palm, don't hover.** **Don't build a cradle under the outer edge of the palm — that's
  Guyon's canal**; add traction instead. The Sval needs ~1 cm less splay than a DataHand (628081, 405875,
  451700, 150410).
- **Mounting is the biggest fit lever.** Two C-clamps plus two magic arms — **SmallRig 11" rosette arm
  (the rigid one; the light one wobbles under palm-rest load) and a CAMVATE C-clamp**, roughly half price
  on AliExpress. Sizing: no carrier plates → 11"; with plates → 7"; standing desk plus plates → maybe 5".
  The 1/4-20 threads are in the case bottom and carrier plates are laser-cut aluminum (292 g/pair),
  because a 1/4-20 in an off-center printed part fails under that torque; splay the halves wide and
  desk-mount on a sit-stand desk (252648, 479121, 383176, 661048, 396096).
- **Cheapest adjustable tenting is M5 screws in assorted lengths** (the M5 inserts aren't obstructed at
  the top); cattongue tape stops a tented board sliding. **Every desk is too high** — remove chair
  armrests, raise the chair to meet the board, elbows ~70–90°, or use an under-desk tray or lap desk
  (048321, 855037, 033967, 642069, 114391).
- **Trackball tendon pain comes from curling fingers** — use the middle phalanges, flatten the hand and
  slide south so contact is ~30° forward of apogee; raising the ball helps big hands (claussen ran an
  8 mm riser for a year). Skin flakes jamming the ball: moisturize (995248, 619124, 430484, 963296).
- **Foam-silenced center keys are a validated mod**: ~0.5 mm foam pads at the key's bottom plus a model
  with the IR window moved down by the foam thickness; dyamito said it "eliminated an entire symptom" of
  his RSI. Measured noise: Sval 51 dB vs Gateron browns 52. A mat and wrist strap is enough ESD gear, but
  treadmill desks are "literal Van de Graaff generators" (368980, 431794, 576642, 049458, 286578).
