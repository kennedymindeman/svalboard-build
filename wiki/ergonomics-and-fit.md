---
type: Reference
title: Ergonomics and fit
description: Fit order and method, cluster geometry, key weight and fingertip sizing, palm rests, mounting and tenting, adaptation timelines, and fixes for specific pains.
tags: [svalboard, discord, ergonomics]
source: "discord #general 1124364902811844739, 2023-06-30..2026-08-15 (gap 2025-08-10..2025-10-17)"
---

# Ergonomics and fit

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; a few 6-digit suffixes collide in the 43k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## Fit method

- **Fit order (Cyrus)**: wrists straight and flat → middle-finger orientation and palm-rest distance →
  index → ring/little → thumb → pointing device last. Common failures: living at one end of the
  adjustment range, and squaring the board to the desk edge instead of twisting the baseplates (547230,
  407537, 848370). His 2024 phrasing started from the towers instead (230746), but the fitment guide and
  most users do palms first (808047). Budget hours for the first fit and a week or two of tweaking, then
  stop; the failure mode has a name, "config creep/bankruptcy with my sval" (801918, 651799, 416587).
- **Everything is relative to the palm rest, so start there**: it gives both monotonic (distance in Y)
  and relative (rotation about Z) adjustment, and "a mm or so can make ALL the difference" (274506,
  236532); Cyrus opens every fix by shoving the rest backwards to de-flex every finger at once (369913).
  **"Palm yaw is the most useful adjustment on the whole board"** — it "stops you having to do yaw on 5
  other elements" (691167, 716129) — and the rest *slides* as well as rotating, on two screws (816586).
- **"This is a fit issue, not a force issue."** If you feel like you're hovering, raise the hand or
  lower the clusters; claussen's test is adding a few mm on the palm rest and watching preload change.
  Bottoming out every key is expected at first; hunting for bottom means too much preload (803008,
  022660). Muscles firing to hold fingers off the keys is fit, not key weight, and cramping while
  learning is the same signal (253950, 076309). **You are meant to rest on the keys** — "S can take a
  huge amount of force… that's the purpose of the fitment mechanism" — and **the home row here is C or S,
  not a row** (475099, 032203); spurious repeats mean resting too hard, so lower the keys a hair (741351).
- **The core rule: "whatever you hit unintentionally, move away from your fingertip"** (231188, 104915,
  202526); too hard to hit → move the cluster toward you (491106). **Cyrus's diagnosis table**: false N/S
  → move the cluster fore/aft along that finger's ray; false E/W → adjust roll; mashing several keys at
  once → the fit is too tight, use thinner or back-set keys (977831, 970945). Fit by *typing*, not by
  measuring (659260); shaky fingers early on are a fit signal, answered by stretching the fit out and
  lowering the cluster (420136, 462952, 115482). **Adjustability is
  deliberate**, and a cascade of adjustments "will never completely destroy your fit" (953652, 907985,
  424617).
- **Aim for neutral resting pressure on every center key, and even spacing between N and S.** Resting
  against S "a *bit* is fine, touching N tends to be more error-prone as extension is less controlled"
  (010497). claussen's own industrial-design target for the whole fit is **the bottom of the pinky
  cluster within 1 mm of the desk surface** (896088). **Too much arch in the fingers throws N and center
  errors** — fingertips too vertical in the wells makes extension unstable and sympathetic; the fix is
  flattening the posture and moving the palms back a few mm rather than reaching forward (541964).

## Cluster geometry

- **Clusters should not be parallel** — fingers are rays converging at the wrist, each finger roughly
  perpendicular to its center key at rest (N = extension, S = flexion, E/W = splay). **North keys are a
  flick upward, not an outward extension.** **Don't tilt clusters toward the palm** (the Azeron ask):
  no muscle makes a finger longer, so at the extreme you can't press center at all (372621, 378344,
  340535). Cyrus decomposes the adjustment as *roll* (East rises and West drops, since wrist deviation
  moves the fingertip in an arc), *yaw* (line the cluster up with that finger's ray), and *height*
  (middle-finger-lowest gives equal tension, though mirroring your limp hand's MCP angles is often
  better) (455683, 198704, 059410).
- **Clusters deliberately don't pitch north-south** — bend the metal towers or print the
  pitch-adjustable ones, but don't add degrees of freedom before you're adapted (942065, 028865);
  "almost none *need* to" (668800). Flipping the towers to pitch clusters *up* (+6° vs the stock -10°)
  was built and rejected — "it makes N keys nicer and S keys horrible for me" — though Cyrus kept the
  flip because it frees vertical space for bigger trackballs (982646, 305008, 698016).
- **If every cluster is twisted the same direction in a photo, rotate the whole base instead.** Pinky
  fixes in order: raise the pinky cluster a hair so fingers "just touch"; shim under the outside of the
  cluster arm with paper; add pinky stagger; heat-bend the pinky S key; bend or reprint the tower
  (673577, 267235, 176670, 550306). Extreme stagger needs no custom parts: 25 mm ring-to-little is stock,
  and a flipped index tower adds 10 mm (997766).
- **Minimum splay by default, and flatter fits splay less**: "if you feel cramped, flatten out your fit"
  (751475, 519967). **"FLAT FIT DECREASES SPLAY!"** — the more curled the posture, the shorter the ray
  from the knuckle, so a flat fit spreads fingertips farther for the same finger splay, which is why
  small hands often want it flatter (716413, 132066, 894591, 519717). **Bias clusters inward more than
  feels natural, roll them outward to make inward keys easier**
  (697280); **if one cluster needs more height, lower all the others** (356736); preload center-south
  (924568). **Clusters touching is correct** (419206), and **working loose means you're hitting too
  hard**, not bad threads (065471). **A wandering automouse layer is usually fit, not firmware** — a
  shifted thumb cluster nudges the trackball on every click (298200); see
  [firmware-and-config](/firmware-and-config.md).

## Key weight

- **Key weight: ~20 gf default, set by the magnet offset baked into the key** — 0.7 mm ≈ 20 g, 1.0 mm ≈
  ~10 g, zero offset 60 g+, and a 0.1–0.2 mm change is huge. Changing weight means new **keys**, not
  clusters or magnets; go stiffer (1.0–1.2) for gaming (725607, 162743, 471865, 559). Fuller numbers:
  **larger offset = lower force**, 0.8 mm is the "touch lighter" step, **thumb knuckle ships at 0.4**
  because the knuckle is strong and false-actuates lighter, **zero offset with the lever ≈ 65-70 g**, and
  offset is vertical only, since lateral offset would twist the key in its well (866463, 029736, 744094,
  672924). The number printed on the key's back is the *offset*, not the width (974997); the 2025-04
  shipping default was **0.7 sides with a 0.9 centre** (581929, 393361).
  **Center-key stiffness is a second knob: the slider's backside magnet gap**, a dot pattern on the
  slider's bottom, typically 0.6; 0.4 mm ≈ 30 g and snappier (326836, 720337, 481243).
- **20 g here is not 20 g there.** The argument is work, not force: the profile falls ~1/x² so "the work
  is all right at the front", and the area under the curve is roughly an order of magnitude below a
  normal switch (062723, 599386, 787877). "Nobody gets it until they feel Sval/DH switches and then
  they're like 'OH THAT'S what 20g feels like when its fully front-loaded'" (814777, 518962, 630294).
  No reward for hammering: "there's nothing wrong with bottoming out with zero force" (855707).
- **Start at 20 g; don't order lighter sight-unseen.** phreaker's stiffer first board "felt fine for a
  month or two… then my hands started to regret it" (106644); rock climbers are the standing exception
  (306003). **Ultralight is worse than it sounds** — below ~10 g "everything goes very indistinct and
  almost non-tactile", because ultra-light keys "don't give enough of a stable resting place for the low
  level neuromuscular noise in the hand" (514408, 568129), though ~15 g is common and 5 g sets are usable
  (754333, 964680). **Tune weight per finger**: light E/W on ring and middle, a *stiffer* key under a
  mode key you keep hitting (040742, 412841).
- **A dead key: sand the flag ~0.1 mm, targeting 3.50 mm from the back of the key to the flag tip** — the
  sensor is on the N side, so a key torquing in its well goes dead (626132, 713863). **A sticky key:
  colour it with a #2 pencil**; center keys are press-fit, pop them from the bottom (800109, 453973).

## Fingertip sizing and key size

- **The measurement is your widest finger at 6 mm from the tip**: at the height of the tops of the side
  keys, finger resting in the well, take the **largest** across fingers (130216, 431307). Place, don't
  press; one eye closed; hand flat; no thumbs (200137). **Use `svalboard.com/sizer`, credit-card-scaled
  for on-screen sizing** — no printer needed (476342, 694848).
  **When borderline, go wider**: too tight is worse than too spacious for accuracy, and the Datahand
  default was ~20-21 mm, "huge by Sval standards" (612373, 217035, 012392, 022238). **16 mm is the
  smallest key size built** and 14/15 mm are the same physical key (752848, 655589, 609428). claussen's
  2023-08 framing was in **key-to-key interior keywell width**: "The DH fit seems to be a key-to-key
  interior keywell width of about 18mm. The lal/Svalboard default is about 16mm, and I actually prefer
  thicker keys that further reduce it to about 14mm" — narrower than DH on purpose, because DH forced
  smaller hands to actively splay (273232, 092453); his DH rigs measured 19.7 mm across at the key tops
  against a Svalboard's 20.7 mm (695137). **Thick-fingered users going the other way need ~18 mm or
  more**, reached with outward-offset or backset key tops; those limit how close the clusters can
  squeeze, because the keys tip outward when they actuate (273232, 092453, 735561, 687774). Put
  per-finger widths in the order form's **"Full Fingertip Measurements" box in `P R M I I M R P` order**
  (550421, 651815, 050172, 564136).
- **Taller side keys are a trap.** claussen printed +1 and +2 mm (8.5 mm inner, 7.5 mm outer vs 6.5 mm
  standard): "too tall is intrusive on the insides of the fingertips even though it does make fitment
  seem easier at first" (621147, 630290). The exception that shipped is the **thick + ultralight north
  key** (mainline 2024-05-21), which stopped fingers flying out of the socket on N combos (368122,
  638662). Raise E and W with tall keys rather than sinking the center, since "C can only go down by
  reducing travel" (444776).
- **Slim clusters for narrow hands** — mix with standard, print one first to test-fit, and pair opposite
  "missing corners" to squeeze tighter; slim clusters need slim PCBAs, no going back after purchase.
  **Laterals**: inward are light and quick to learn, outward awkward, worst on the ring (224460).
  They help most at a ≤16-17 mm fit by cutting splay; larger hands see less angular benefit and hit
  key-to-key interference instead, and the cost is reprinting every key (777213, 984800). The related
  "Ultralightly" variant, clusters with no outward keys, is for people who otherwise couldn't use the
  device (559848, 801302). See [printing](/printing.md) for reprint settings.

## Palm rests

- **Palm rests**: 5 mm shims by default, removable — "there's no right fit, there's just what fits you."
  **Rest the palm, don't hover.** **Don't build a cradle under the outer edge of the palm — that's
  Guyon's canal**; add traction instead. The Sval needs ~1 cm less splay than a DataHand (628081,
  405875, 451700, 150410).
- **They are palm rests, not wrist rests** — wrists in the air, base of palms down (093616, 358747,
  653079). claussen's underlying rule, stated for mice in 2023-08, is that the hand should rest
  comfortably **without touching the desk surface** at all: dragging "a square inch of flesh on the
  desktop" adds friction you'd never accept on a mouse, and "'You shouldn't rest your wrists' is only
  relevant in context of the alternatives" (875910, 953927). Support the fleshy pads at the base of the
  palm and behind the middle knuckle, not the centerline: "putting pressure on the middle is gonna give your median nerve a nice squeeze" (033293,
  344424). Load the **full width** — on a pressure map loaded only at the outer heel, "you'll eventually
  get arthritis under the pisiform" (935626). Palm-to-center-key drop is ~40 mm (534821).
- **Height is a shim job, not a screw job.** The pillar screws only locate the rest — "don't use those
  screws to bear load"; shim under the posts or the whole carrier, and note the stock range is biased low
  by demand for lower rests (373863, 280280). The shim mechanics have been the same since 2023-07: the
  four legs slip-fit into the pylons and are clamped by the side screws, so **an M2 4 mm screw dropped
  down a leg hole gives about 5 mm of lift**, up to ~8 mm total, and pulling the screws back out lowers
  it again; destructively shortening the rest works but is the last resort (593174, 142598). **Raise the
  palm rest before blaming the N key** — trouble hitting N is "universally… from having the palmrest too low",
  a higher palm giving a better entry angle against the fixed tower angle (560508, 222407, 621329).
  **Tighten the wrist-side screw harder than the fingertip-side one** to leave rotational play, using a
  washer rather than more torque if it must stay rotatable (809505, 732968).
- **The rests are the community's mod surface.** Custom-mold with plastic wrap over the printed rest and
  polymorph shaped mostly *off* the rest so you don't slump it, or lay memory foam on top to find your
  height (270236, 322124). Uneven contact has a fix: trim the **outer south leg by ~3-5 mm**, reinsert,
  then heat-gun *only that quadrant* on low and slump it to the carrier pylon (403287, 397506). Cover
  with pleather and CA glue or contact cement, though claussen prefers bare PLA (259762, 254437, 829002).
  At steep tent you want a hook under the side of the hand, but not close to the pinky (056596).
- **Gel rests and going palmless are both legitimate.** phreaker tolerates no hard rest — "do not cheap
  out. Get ones with cloth coverings" (792916). At least 5% of users go palmless (506304, 526144,
  903880) — a 2023-08 discovery, where mmarcello found it "super helpful" for his RSI and noted it
  "creates tons of space for a pointing device under the hand", with claussen agreeing after trying it on
  an original DataHand rig (934895, 216650), but users with joint-loading pathology find hovering "very
  painful" (668659, 888583). Learn
  *with* a rest either way (923424); the rests measurably *reduce* false N/S hits when going lateral
  (088414).
  **Datahand converts should expect more outward roll**: the truncated Sval rest gives "less support in
  the forward part of the hand… in order to make room for the trackballs" (431627), and **you don't hover
  over the trackball — your hand slides back on the rest** (871489).

## Mounting, tenting and desk height

- **Mounting is the biggest fit lever.** Two C-clamps plus two magic arms — **SmallRig 11" rosette arm
  (the rigid one; the light one wobbles under palm-rest load) and a CAMVATE C-clamp**, roughly half price
  on AliExpress. Sizing: no carrier plates → 11"; with plates → 7"; standing desk plus plates → maybe 5".
  The 1/4-20 threads are in the case bottom and carrier plates are laser-cut aluminum (292 g/pair),
  because a 1/4-20 in an off-center printed part fails under that torque; splay the halves wide and
  desk-mount on a sit-stand desk (252648, 479121, 383176, 661048, 396096); it has been the house answer
  since 2024 (735730, 451590). Details that recur: get the **rosette** arms and the **anti-rotation
  pins**, for which the case has holes next to the 1/4-20 thread (557541, 174323); **buy two clamps** so
  each arm sits on the side that tightens under load (182963, 394852); crank the end joints harder than
  feels right, since they have no teeth (395837). The clamp is `amazon.com/dp/B075WRLZ82`, with
  AliExpress "Minifocus" the EU substitute (591687, 953401). Avoid cheap flat-jaw clamps, ball-and-rubber
  -ring arms and quick-release mounts (931172, 714173, 736575, 343170). See
  [suppliers-and-parts](/suppliers-and-parts.md).
- **Cheapest adjustable tenting is M5 screws in assorted lengths** (the M5 inserts aren't obstructed at
  the top); cattongue tape stops a tented board sliding. **Every desk is too high** — remove chair
  armrests, raise the chair to meet the board, elbows ~70–90°, or use an under-desk tray or lap desk
  (048321, 855037, 033967, 642069, 114391). In numbers: the case is a ~5-6° wedge and the towers add
  ~8-9° for **~15° stock**, M5 screw legs get you to **25-30°**, and the 1/4-20 gives arbitrary freedom
  (259624, 606976, 483819); with ~98 mm from screw head to base, 60-80 mm screws land nearer 30-40°
  (693588). Start at "max tent angle… then modify to taste", though 35° printed tents got walked back to
  20° (591839, 815710, 406996, 367155). **Tilt is pitch, tenting is roll, negative tilt is nose-down**
  (345217).
- **"Table height is a lie — with no tenting it does more harm than good. Getting the pinky close to the
  table is all that matters."** That is claussen's standing answer to low-profile proposals, including
  Cyrus's thin A1-mini-sized base, which he built and rated "less comfortable, harder to adjust… and fits
  fewer hand sizes" (932565, 085511, 185920). **A keyboard tray with negative tilt is the cheap fix for
  high elbows** — "a 15 minute install that will fix all your shit" — and get a thin plate, since "thick
  keyboard trays just raise everything" (253500, 090182, 871527, 248640, 480243). **Low over the knees is
  the ideal**, a lap board sloping down over the thighs needing no tent (579773, 803648, 704653);
  phreaker's desk bottoms out at 25.2", "I've seen 28+ … which would be unacceptable" (548614).
- **Desk mount beats chair mount for most people**, and chair mounting conflicts with a standing desk:
  "when I stand my chair does not stand with me" (609920, 927115); **carrier plates are for desk
  mounting, the default mount point is friendlier for chair mounting** (553658). Chair mounts do exist —
  SmallRigs clamped to a chair, or wolfwood's cup-magnet inlay, a 14 × 60.5 × 5.5 mm hollow in the bottom
  case with 3.6 mm M3 holes 45 mm apart and 60+ lb magnets holding across a 1 mm gap (098688, 878248,
  460168) — but **don't stick a MagSafe puck directly on the case**, since the ring makes the board rock
  unmounted (849724). **Chair arms are the enemy if you have ulnar or elbow issues** (648747, 697050).

## Adaptation

- **Don't change your alpha layout at the same time as the board** — a multi-month commitment that
  raises the odds you quit; use what you already touch-type (claussen still types QWERTY after 25 years),
  and if you must optimize, Hands Down Neu or HD Promethium, flipping N/S because S keys beat N on a Sval
  (280360, 820933, 586853). The board transition is far easier than an alpha transition — "all but 2 keys
  stay on the same finger and 4 keys move at all" — with **prior multi-thumb-key experience the single
  biggest adaptation advantage** (553832, 768038, 541416, 621888); QWERTY-on-Sval still costs T, V, Y and
  B (427318). **The key-count scare is unfounded if you already use thumbs** — ~50 keys with 10 on thumbs,
  and five
  instantly accessible, not-confusable thumb keys is the design's actual argument (379692, 088754).
- **Expect a "quieting period" of one to two weeks** where your fingers fire extra keys, from two
  compounding causes — uncalm hands and an unadjusted board (058206, 547386, 355506). Early errors are
  neighbour-key bumps, not wrong keys (620766); landing stops being a thought in a week or two, helped by
  landing palms first onto the rests and then settling fingers and thumbs (288940, 148750). Practice on
  keybr, then Monkeytype with punctuation and symbols (502264, 576256, 734725); **Svalbr** is a keybr
  fork that renders your live keymap from the device (416726, 587482).
- **The long-form numbers, from claussen's own DataHand transition: functional at work in 4-6 weeks,
  fully adapted in 4-6 months.** Age matters, and coming from a thumby split puts you in good position
  (474226, 2023-07).
- **Speed is not the pitch**, and expect parity at best: "sval is focused on letting you go for longer,
  not faster", "comfort is endurance, endurance is productivity" (591063, 637888, 306488, 223691).
  **Posture beats keyboard, keyboard beats layout** (726878). **Do not ramp from 15 minutes a day to 8
  hours a week later** — that jump produced one user's "arthritic" weakness (372696, 564085). Take breaks
  and keep motions gentle, "these ain't 55g switches you have to slam" (363842), because the intrinsic
  hand muscles get a very different workout, especially independent ring-finger movement (781594, 810472).

## Laterals, norths and thumbs

- **Key difficulty runs "down > south > inward = north > outward"** (660969; the other two rankings put north last, "down, south, inward, outward, north" (456597), or above inward, "Middle > South > North > Inwards > Outwards" (159072)); porting a
  flat layout, put the inner diagonal reaches on inward middle/ring (177041). **HD-Promethium is the
  in-crowd pick**, with R on thumb but not E, since thumbs hate repeats (099753, 500369); **modifiers on
  thumbs with no home-row mods is a viable 20-year answer** (928060).
- **North keys and repeats are the universal complaint; thicker + lighter norths are the fix** (301843,
  004830), with heat-bending the keys in a bit and doing all north motions as flicks as alternatives
  (525194, 941269, 671642). Both date to 2023-08: cryptanon dipped his north keys in hot water and
  reshaped them to add a slope — "now they feel perfect" — but found an aggressive slope suited only his
  index fingers, cramping the rest and costing 20 wpm (872128, 034152, 239950); claussen made **thick N
  keys the default on all units going forward** that same week, while still not shipping them to
  big-fingered users who have trouble with them (273219). **Pinky north is the worst key; fix it in the
  layout** — myxfit's
  dvorak-for-DH swaps L↔Z, V↔R, C↔W plus a K→Q→P three-way, or bind a Repeat key (283944, 041266). Fit
  first, though: pinkies that "feel useless" on north usually need cluster rotation to match finger
  splay, since "if you have to push off-axis to hit a north key it's much harder" (447489, 442902).
  **Fingers flicking out of the north key usually means the hand sits too low** — move the clusters
  closer for a more curled fit (236261, 606174).
- **Lateral (E/W) keys are a learned skill, not a filter.** "Everyone has sympathetic movement in these
  directions, but the motions are so small and the forces so low and the hand posture flexible enough
  that it just works… Nobody has ever returned a board for this reason" — now the `!lateral` command,
  youtu.be/whvKJ12vwvU (716181, 812227); **"the number of returns due to pain from lateral motions is:
  one case with severe arthritis"** (104027, 472155). An estimated 1-2% can't get the motion, and you
  can't judge it by pantomiming in the air (521739, 438843). The drill is "spocks": move middle and ring
  *together* (843852). River's decomposition: inward is about as easy as down, so **only outward index
  and middle are genuinely new movements** (183424, 310331). **Ring-out is the exception everyone
  hates**; fix it with outward roll, a stiffer or more spacious key, or don't map it (619275, 013317,
  694694, 853835).
- **Thumbs: nail over knuckle, unanimously** (083694, 395392), with Pad the favourite (155753).
  **Knuckle is the worst thumb key and belongs to a modifier**, not a letter; the easiest thumb chords
  are Down + Pad, then Down + Pad + Knuckle, "but it's a bit of a contortion" (564050, 496731, 225903).
  **Thumb motion is inward, not lifting**, and the clusters sit *around* your thumbs, so they aren't reached for
  (387392, 701259). **Thumb-down's half-press is "the single hardest adjustment"**: the key can travel
  ~75% without actuating, and the fix is moving the cluster south with the thumb as deep in as is
  comfortable (729728, 761184). **Double-down is a separate mechanical tact switch the down key rests
  on** — stiff on purpose, impossible to press without first pressing down, rated 500k cycles and not for
  primary use (196816, 052409, 794521, 026035); "long boi" thumb keys at 0.8 mm offset are a workaround
  (170945,
  675539). **Bending the stainless thumb tower bracket is sanctioned** as a one-time change (664373), and
  **thumb clusters are marked L/R on the bottom** (982181). **Fingers get no sixth "up" key** (this is about
  finger clusters, not thumbs): "Fingers don't go up", "Up for fingers is really, really bad", "the anatomy
  just doesn't support it" (410610, 139005, 891237).

## Pain, injury and what the board can't fix

- **Where the pain originates decides whether a keyboard helps.** "Folks with carpal tunnel and ulnar
  nerve issues from pinky overuse/contortion are Sval's core market… once you're hurt, it comes back way
  easier", while cubital-tunnel (elbow) needs postural and mounting changes (245544, 885521). **The Sval
  fixes hands and fingers, not shoulders** — for higher problems "that's one hundred percent mounting"
  (835497, 927461) — and "anything misused will hurt you. Sval is no different" (903785, 759663, 801446).
- **Cubital tunnel and shoulder setup (Cyrus, who has cubital tunnel)**: shoulder fully relaxed, don't
  overextend forward, elbow under 90°, boards at your sides much lower than a normal desk — "if you can
  comfortably sit with your hands in your lap or on your thighs, you're basically copying that position"
  (226688). Bin the chair arms, get knee space so the halves take weight off your elbows, and stop
  pronating — the biggest single win is not lifting the hand out to mouse (032430, 212163). **If
  pronation feels forced, your halves are too close together** (241489). For shoulders, chase zero
  shoulder load rather than settings — elbows back, board low, "around the height of my lap" — and do PT
  (579220, 823325, 917715).
- **Don't rush into carpal-tunnel or trigger-finger release surgery.** Trigger finger resolves on its own
  with high frequency ("75%+ I believe") if you back off, though "you are looking at months" (152590),
  and Cyrus, from experience: "if you get surgery to release it, you will both lose strength in that
  digit forever, and also get random twinges in the surgery site, also forever" (479869, 823987, 945587).
  **Some things are medical signals, not fit problems**: probable sagittal band tears are visible in hand
  photos (968334), and fingers that don't flex in a straight line mean "you may have either a pulley
  injury or a torn sagittal band… see a rheumatologist" (420040, 814028). **Talon is worth learning but
  is not a keyboard replacement** (545960, 279048, 821768).
- **Trackball tendon pain comes from curling fingers** — use the middle phalanges, flatten the hand and
  slide south so contact is ~30° forward of apogee; raising the ball helps big hands (claussen ran an
  8 mm riser for a year). Skin flakes jamming the ball: moisturize (995248, 619124, 430484, 963296). See
  [pointing-devices](/pointing-devices.md).

## Noise, size, maintenance and travel

- **Foam-silenced center keys are a validated mod**: ~0.5 mm foam pads at the key's bottom plus a model
  with the IR window moved down by the foam thickness; dyamito said it "eliminated an entire symptom" of
  his RSI. Measured noise: Sval 51 dB vs Gateron browns 52. A mat and wrist strap is enough ESD gear, but
  treadmill desks are "literal Van de Graaff generators" (368980, 431794, 576642, 049458, 286578) —
  matching earlier reports of it being quieter than browns, "maybe a little bit louder than a recent
  (post-butterfly key) macbook keyboard" (350782). The 2023-08 originals of both: jeebus put it at "a
  little louder than browns, but so much smoother", and the noise "mostly comes from bottoming out"
  (967504, 561199). claussen's first foam test found the same trade the mod still has — quieter, but
  "the force profile is definitely less sharp"; kapton tape "did very little other than stopping the
  sharper 'tick' of the magnets", and gk's cheaper fix for that tick is a layer of glue over the magnets
  (894492, 492446). **Maintenance is light**: soapy water or a q-tip with
  rubbing alcohol, keys lifting straight out, center keycaps on press-fit sliders removable from the back
  once the cluster is loosened (348487); "you can easily go 6-9 months without cleaning it" (149168).
- **Size, weight and travel**: roughly 190-210 × 130 × 90-95 mm per half, ~85 mm without thumb-up keys,
  and **~270-300 g per side**, ~334 g with a trackball (156224, 530634, 692221, 168480, 493339).
  Transport in a hard case, currently the Nanuk 910, since "no matter how it's built, it's not gonna take
  a hammering. Think of it like an instrument" (339336, 425384, 034198); **don't leave it near a car
  heater**, which left one user with "very deformed clusters and melted towers" (570378).

## History

Older positions, kept because the reasoning still explains the current parts. Where these conflict with
the sections above, the sections above are current.

- **Fingertip sizer, 2023-11 to 2024-09.** The printable sizer landed 2023-11-17 with "print at 100% on
  letter paper" instructions and thresholds ≤16 mm → snug keys, 16-18 mm → wide keys, 18 mm+ → maybe
  backset (201652, 950676); it was pinned 2023-12-11, revised 2024-01-08 with per-key selection, and
  moved to `svalboard.com/sizer` 2024-03-22 (230201, 489226, 249546). Printing was then deprecated in
  favour of on-screen scaling after a scale line (2024-08-31) and a credit-card outline (2024-09-20) were
  added, because no printer driver can be trusted (533628, 683102, 075177).
- **Key force spec, 2023-11 to 2025-04.** ~20 g was chosen to match the Datahand spec as closely as
  possible (514408). Through mid-2024 the quoted numbers were 1.0 mm offset ≈ 12 gf (now stated as ~10 g)
  and old 0.6 mm-marked keys "a bit higher than 20g… more like 25-30g"; ultralights down to ~5 g were
  printed on request, and earlier builds with N52 magnets ran lighter still — "the 5g on his is like 0g
  on current standard" (182848, 982302, 351806, 908449).
- **Palm rest generations.** The OG Datahand rest "ran all the way up under the knuckles… but it does
  interfere with trackball usage" (002625). **Truncated palms** arrived 2023-11 supporting only heel and
  mid-palm, and need more tilt than the originals because the front of the full rest provided most of the
  palm tilt (573970, 897858, 845625). A super-mini test landed 2024-07-25 as **"Cyrus Mini" in the
  Onshape repo** (213208, 553128), with tripod/triangle rests following for small hands (608213).
