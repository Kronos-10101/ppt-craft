# Design Core — shared design system for ppt-craft

Applies to every deck type unless the type module explicitly overrides it.
All claims grounded in the research dossier (~/workspace/ppt-craft/research/RESEARCH.md),
dated 2026-10-09. Dossier-flagged-unverified items are marked as such.

## 1. Typography ladder

- [ ] Titles at 38–48pt (APSU guidance, academic dossier).
- [ ] Headers 28–32pt minimum; body text ≥24pt; never below 24pt for body.
- [ ] Figure labels 18–24pt (thesis dossier).
- [ ] Assertion headlines ≤2 lines, 28pt bold sans (Alley assertion-evidence model).
- [ ] One sans-serif family for titles + body where possible; max 1–2 fonts, one body size (consulting dossier).
- [ ] Kawasaki floor (≥30pt) treated as a psychological legibility filter, not a formatting law (pitch dossier).
- [ ] Equations via LaTeX/PPTX equation editor — never ASCII (thesis dossier).
- [ ] Author–year inline citations on thesis/academic slides.

## 2. Color

- [ ] 2–3 colors maximum across the whole deck (academic + sales dossiers).
- [ ] One icon style throughout (sales dossier).
- [ ] High contrast, dark on light preferred; color-blind-safe palettes (thesis dossier).
- [ ] Color marks the insight only — never decoration (consulting dossier: color = insight emphasis).
- [ ] Restrained, not decorative: white background + navy emphasis is the safe default (consulting dossier).

## 3. Layout

- [ ] One idea per slide (all seven dossiers agree).
- [ ] Whitespace is structural: ~½-inch gap under the headline before any content (Alley model).
- [ ] Every element snaps to a common grid/subgrid; external margin ≥ internal padding.
- [ ] Title-only read-through must reconstruct the full argument — reading headlines in sequence tells the story (consulting QA ritual).
- [ ] One chart/table per slide, each with a source line + units (case + consulting exhibit discipline).
- [ ] Slide anatomy: action title → framing subtitles → exhibit → footer (source/units/date/page) for read-alone document decks (consulting dossier).

## 4. Density rules

- [ ] ≤6 lines per slide, ~7 words per line (The Hindu 2014; academic dossier). Sales canon allows 6–8 for "billboard clarity" — never exceed 8.
- [ ] Assertion-evidence ceiling: ≤~20 words on content slides when the headline carries the takeaway; 2–4 item lists max (Alley model).
- [ ] 3-second test: a stranger gets the slide's point within 3 seconds (sales dossier).
- [ ] High-frequency interactions must respond in ≤150ms so animated/high-tempo decks feel live (build spec, 2026-10-09).
- [ ] Read-alone document decks (case, consulting) may run dense — observed 180–307 words/slide in real case decks — but talk-aid decks stay sparse (observed median 1–44 words/slide in class decks). Match density to delivery mode.

## 5. Headline discipline

- [ ] Default: assertion headlines — complete-sentence takeaways, never topic labels (consulting action titles; case action titles at 7±2 words).
- [ ] Topic labels only where the type demands: class decks (observed zero assertion headlines), SIH fixed template (pure topic labels), thesis chapter-title slides.
- [ ] "So what?" per slide before delivery — if the answer is nothing, cut or rewrite the slide (consulting QA).
- [ ] Scannable 3-second version and a detailed send-ahead version are different artifacts — design both, never one-deck-four-jobs (sales dual-mode; Indian "one-deck-four-jobs" antipattern, dossier 2026-10-09).

## 6. Anti-AI-slop checklist

- [ ] No generic purple/blue gradients.
- [ ] No icon tile above every heading.
- [ ] No emoji used as icons.
- [ ] No fake testimonials or fabricated metrics (dossier: fake traction is blacklisted in pitch decks; "never present mock data as implemented" — see evidence-discipline.md).
- [ ] No text walls — the #1 academic-deck mistake (academic dossier).
- [ ] No bare "Thank you" end slide (Hagen, via academic dossier: "completely useless") — end with a summary slide + Q&A.
- [ ] No logo soup (sales common mistake).
- [ ] No unreadable mini-diagrams pasted to look impressive (case presentation-day failure).

## 7. Motion restraint

- [ ] Animation is enhancement, never the message — the slide must work frozen.
- [ ] Every animated state change ships with a static cue carrying the same information.
- [ ] Respect prefers-reduced-motion: no animation when the user or system requests reduced motion.
- [ ] Progressive reveal is a delivery technique, not a deck property — keep the built file static-first (dossier: no animation API exists in the engine anyway).

## 8. Type-module overrides

- [ ] When a type module contradicts this core, the type module wins and this core stays the default. Known overrides: SIH (topic labels, no paragraphs, fixed 6-slide template); consulting document decks (denser pages, footer chrome); thesis (repeated outlines + per-chapter conclusions observed in real defenses).
- [ ] India-vs-global density norms: no quantitative study exists (dossier section C, 2026-10-09) — do NOT hardcode "Indian decks are denser" as a design rule. Encode India-specifics only where the dossier verifies them: SIH template, UGC viva norms, WhatsApp-channel brevity, sponsor formats (LIME/Interrobang/Brandstorm).

- [ ] Pasted images are legitimate exhibits (real case decks ran zero native charts — 552 pasted images in one deck) — but they must be high-resolution with original aspect ratios preserved (thesis dossier); native editable charts preferred wherever numbers must stay auditable (see evidence-discipline.md).

## 9. Accessibility minimums

- [ ] Contrast checked for projectors, not just laptop screens (academic dossier).
- [ ] Alt-text on every meaningful image; decorative images marked decorative.
- [ ] Reading order set correctly for screen readers (academic dossier).
- [ ] Never convey meaning by color alone — pair color with labels or direct annotation (color-blind-safe, thesis dossier).

## Sources

- Alley assertion-evidence model (via academic dossier; NSCC summary)
- Duarte slide:ology / resonate (via academic dossier)
- Minto Pyramid Principle summaries — mod482 (GitHub), befreed.ai (consulting dossier)
- CBS Case Competition Toolkit (scribd); Sequoia "Writing a Business Plan" (sequoiacap.com/article/writing-a-business-plan)
- The Hindu "Present it right" (2014); Raskin "Greatest Sales Deck" (medium.com); MLH standard hackathon rules (github.com/MLH/mlh-policies)
