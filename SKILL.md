---
name: ppt-craft
description: Designs and builds PowerPoint decks from briefs or GitHub URLs: 7 deck-type modules (case study, academic, marketing/sales, investor pitch, consulting, thesis defense, hackathon incl. SIH), India-specific formats, template-first python-pptx builds, evidence-gated claims, and LibreOffice headless render QA.
---

# ppt-craft

## Purpose

Design and build PowerPoint presentations for any purpose: a client brief, a classroom talk, a sales meeting, a funding pitch, an executive decision, a thesis viva, a hackathon, or a GitHub repository turned into a project-showcase deck. Route each task to the right deck-type module, plan the narrative before building, fill templates with python-pptx, gate every claim on evidence, and verify by rendering.

## When to use

Use when asked to make a deck, build slides, design a presentation, turn a document or repository into slides, prepare for a pitch, a case competition, a viva, or a demo day. Trigger phrases: "make me a deck", "build me slides", "design a presentation", "pitch deck", "case comp slides", "thesis defense deck", "hackathon presentation", "turn this repo into a presentation", "SIH presentation", "viva slides".

## How to use this skill (reading order)

Never improvise the process. Follow this exact order:

1. **Read this file fully**: it defines the workflow.
2. **Intake (P-1):** classify the intent with the checklist below.
3. **Dispatch:** read every routed `references/*.md` file listed in the table, **before** drafting any slide.
4. **Plan (P-2):** write a ghost outline (titles only), start the evidence ledger, get approval.
5. **Build (P-3):** template-first python-pptx; fix source and rebuild, never patch the generated PPTX.
6. **Verify (P-4):** evidence gate, coverage check, LibreOffice headless render QA.
7. **Report (P-5):** deliver the deck, the ledger, and the open items.

Skipping steps 3-4 is how decks full of false claims get shipped. The order is load-bearing: intake → dispatch → plan → build → verify → report.

## Workflow

### P-0. Triage: what kind of job is this

- [ ] New deck from a brief → full pipeline P-1 through P-5.
- [ ] GitHub URL → deck → bounded repo analysis first (README → entry points → git log → key modules), then P-1 through P-5 with emphasis-weighted slide budgeting.
- [ ] Rework of an existing deck → read the .pptx with python-pptx first (round-trip preserves all elements), classify the changes, rebuild from the fill script; every touched slide re-runs P-4.

- [ ] Deck type identified: case study / academic-class / marketing-sales / investor-pitch / consulting / thesis-defense / hackathon / github-to-deck.
- [ ] Audience named (who decides: jury, examiner, buyer, investor, judge) and delivery mode (live talk vs read-only PDF vs open viva). Decks read without the presenter must be self-explanatory.
- [ ] Time limit and slide cap captured. Canonical budgets (2026-10-09): case study 10-15 slides, 10-20 min + 5-10 min Q&A (ITC: 10-slide cap); academic ~1 min/slide; pitch 10-12 core slides + appendix, hard ceiling ~20; thesis ~1 slide/min cap, 20-30 slides; SIH idea stage: hard 6-slide cap, PDF upload only.
- [ ] github-to-deck: repo URL + emphasis notes captured. Emphasis notes drive slide budgeting (more slides for emphasized modules).
- [ ] India-specific format asked explicitly: SIH / UGC viva / B-school case comp? Applied when relevant, never by default.
- [ ] Claim-criticality flagged: the 2-3 claims the deck's argument depends on (these get the strictest provenance in P-4).
- [ ] Brand assets captured: existing .potx/template, fonts, color palette. If none, a neutral deck system is built once up front; styles are never improvised slide by slide.

### Type dispatch table

| Intent | Read first |
|---|---|
| GitHub URL → repo showcase deck | `references/github-to-deck.md` |
| Case competition / business case deck | `references/case-study.md` |
| Class seminar / lecture / project talk | `references/academic-class.md` |
| Product marketing / sales enablement | `references/marketing-sales.md` |
| Fundraising / startup pitch | `references/investor-pitch.md` |
| Strategy / executive decision deck | `references/consulting.md` |
| Thesis / PhD viva defense | `references/thesis-defense.md` |
| Hackathon demo-day / SIH / sponsor track | `references/hackathon.md` |
| Deep research before drafting (claim-heavy decks) | `references/research-system.md` |
| Deck engineering mechanics (every build) | `references/python-pptx-engineering.md` |
| Claim truthfulness / provenance (every build) | `references/evidence-discipline.md` |
| Layout, typography, density, anti-slop (every build) | `references/design-core.md` |

### Canonical budgets by type (2026-10-09)

| Type | Slide budget | Time |
|---|---|---|
| Case study | 10-15 (winner decks: 38-106 with appendix) | 10-20 min + 5-10 min Q&A |
| Academic / class | ~1 min per slide; 5-6 slides/10 min | 10-15 min typical |
| Investor pitch | 10-12 core + appendix, ceiling ~20 | 20 min talk, 3:44 avg read |
| Consulting | 15 tight appendix slides beat 60-slide dumps | Read-alone document |
| Thesis defense | ~1 slide/min cap, 20-30 slides | 20-45 min + Q&A |
| Hackathon demo-day | 5-9 (3-min: max 6) | 3-5 min, demo is the largest block |
| SIH idea stage | Hard 6-slide cap, PDF only | Evaluated by reading, no live pitch |

### P-2. Plan: ghost outline first

- [ ] Research first on claim-heavy decks: run `references/research-system.md`
      (R-0 frame → R-7 synthesize) and produce the one-page answer-first brief
      BEFORE the ghost outline. No new research during outlining except
      R-5 gap-filling.
- [ ] Ghost outline built: titles-only deck approved before any building starts.
- [ ] Assertion titles where the genre demands them (complete-sentence takeaways; consulting: a title-only read-through must reconstruct the argument).
- [ ] Evidence ledger started: Claim | Evidence | Slide | Status. Every factual claim tagged VERIFIED / ESTIMATE / ASSUMPTION / MISSING before it earns a slide.
- [ ] github-to-deck: module inventory built from the repo (README → entry points → git log → key modules); slide budget weighted by emphasis notes; coverage target set (inventory vs slides covered).
- [ ] SIH check at plan time: idea stage (fixed 6-slide template, evaluated by reading) vs finale stage (observed 10-11 slide decks) distinguished before the outline is locked.
- [ ] Template selected or built: designer defines masters/layouts once, agent fills placeholders (the template-first pattern).

### P-3. Build: template-first, source-first

- [ ] python-pptx footguns observed: never `text_frame.text = ...` (collapses formatting to one unstyled run; assign `run.text` instead); `add_picture` raises on SVG/EMF; no slide duplication or cross-presentation copy (only `add_slide(layout)`); no SmartArt creation; no animation API; equations via LaTeX injection or pre-rendered images, never ASCII.
- [ ] Fix source and rebuild, never patch the generated PPTX.
- [ ] github-to-deck: code wins over README/docs for every claim; each claim carries a provenance chain (source file or commit it rests on).
- [ ] Density gates: one slide = one message; ≤6 lines/slide, ≤7 words/line; assertion headlines ≤2 lines; academic decks: body ≥24pt, titles 38-48pt. Case-comps and consulting decks run denser by convention; respect the genre, not the default.
- [ ] Visual discipline: images positioned and sized deliberately; charts native editable where possible (column/bar/line/pie, XY-scatter/bubble); color = insight emphasis only; contrast and alt-text checked.
- [ ] Equations: LaTeX→OMML injection or pre-rendered images only, never ASCII. `add_picture` raises on SVG/EMF, so rasterize equations to PNG first.
- [ ] Chart honesty: native editable charts where python-pptx supports them (column/bar/line/pie, XY-scatter/bubble); no multi-plot/combo creation (existing ones read fine); pasted-image charts keep aspect ratios and carry source lines.
- [ ] Anti-slop list (every deck): no text walls; no bare "Thank you" closing slide (end on a summary slide + Q&A instead); no logo soup; no decorative 3D or purple gradients; no meaningless icon rows; no teleprompter paragraphs read verbatim.
- [ ] Original content only: ideas from MIT-licensed sources are fine; no text or scripts lifted from the proprietary anthropics/skills or AGPL-licensed guizang.

### P-4. Verify: the deck does not ship red

- [ ] Evidence gate: every claim on every slide is VERIFIED (provenance chain present), ESTIMATE (labelled as such), ASSUMPTION (owner named), or MISSING (slide dropped or flagged). No mock data presented as implemented.
- [ ] github-to-deck coverage check: every module in the inventory is covered or explicitly de-scoped with a one-line reason.
- [ ] Render QA: `soffice --headless --convert-to pdf deck.pptx`; review every PDF page: text overflow, overlap, font substitution, broken charts. python-pptx has no rendering engine, so this step is not optional.
- [ ] Number and exhibit audit: units on every exhibit; source line on every chart/table; no smoothed hockey sticks in pitch traction; dates on traction claims.
- [ ] Speaker notes reviewed where they carry content (defense notes can carry near-transcripts; 31-75% of slides in observed real defenses).
- [ ] Type-specific rituals: consulting "so what?" per slide + number audit; pitch: stranger-must-understand-at-a-glance, no deal terms in the deck, team slide present; thesis: backup slides in a sectioned appendix; SIH: 6-slide cap, no paragraphs, PDF upload only.
- [ ] Authorship honesty: never claim fake firm provenance (no "McKinsey deck"); source Minto and practitioner consensus, not invented credentials.
- [ ] File hygiene: images embedded (not linked), fonts present on the delivery machine, PDF re-renders without substitution on a second machine.

### P-5. Report

- [ ] Deliverables handed over: the .pptx, the rendered PDF QA copy, the evidence ledger (Claim | Evidence | Slide | Status), and a one-paragraph build log (what was assumed, what is MISSING).
- [ ] Open items stated plainly: MISSING claims, de-scoped modules, India-switch choices made, unverified facts repeated with the unverified label attached.
- [ ] License confirmation: no lifted text or scripts from proprietary or AGPL sources; MIT-idea sources credited by name.

## India-reality switch

Applied when the intake says so, never by default:

- **SIH:** official 6-slide template (baseline: SIH2025 format, sih.gov.in/letters/SIH2025-IDEA-Presentation-Format.pptx); distinguish idea stage (fixed template, evaluated by reading) from finale stage (observed finale decks run 10-11 slides); SIH 2026 Phase 2 adds a narrated demo video (explicitly not AI-generated) plus a GitHub repo.
- **Thesis/viva:** UGC 2022 Regulations Clause 11(2): mandatory pre-submission presentation before the Research Advisory Committee, open to all faculty/scholars. Clause 11(5): supervisor + ≥2 external examiners (one preferably from outside India); open viva; viva proceeds only if both externals recommend acceptance; publication mandate removed (universities vary).
- **Marketing/sales:** WhatsApp is a first-class Indian sales channel; WhatsApp/email pitch assets must be short, scannable, with one clear next step.
- **Pitch/India:** ISFM 2026 format (Problem→Solution→Market→Model→GTM→Traction→Competition→Team→Financials→Ask + 3-min video); IIT Bombay Eureka!: rigorous unit economics, "use of funds" slide often decisive; no valuation in the outbound deck (Rule 11UA working when asked); vanity metrics (downloads, GMV, MoUs) carry little weight.
- **Case comps:** LIME one-pager with hard word limits (30/75/100); Interrobang: 10-slide cap, originality/creativity highest-weighted; Brandstorm: 10 slides max, 16:9, PDF.
- **Academic/class:** VTU-pattern graded seminar deliverables (4 mandatory seminars, hard+soft copy submitted) when applicable; motivation slide before agenda is expected in Indian classroom practice.
- **Honesty note:** "Sanjeevani decks", 78-slide meetings, and teleprompter culture are editorial anecdotes, directionally convergent, with no quantitative study. Never present them as measured fact. At VC level the "not common in India" observation does not hold: Indian VCs teach the identical global pitch format.

## Flags

All claims dated 2026-10-09:

- SIH 2025 template is the baseline. Re-verify the SIH 2026 template and rulebook live before hardcoding anything into a reference module.
- python-pptx maintenance status is unverified: third-party claims of no releases since Aug 2024 and the existence of a python-pptx-ng fork must be checked against PyPI before the skill repeats either claim.
- Honest provenance wall: no authentic MBB deck is freely downloadable; online "McKinsey decks" are unverifiable; "McKinsey Presentation Handbook" PDFs on SEO-spam domains are not evidence. Never fake firm authority.
- No famous pitch decks (.pptx) obtainable; Airbnb/Uber and similar are PDF-only. Real early-stage .pptx samples run 7-10 slides, shorter than canon.
- Tata/Deloitte case competitions unverified (Tata Crucible is a quiz, not a case comp, unverified either way). Current 2026-season rulebooks for some comps unverified. No quantitative India-vs-global text-density norms found.
- Alternative technical paths are options, not core: Marp (`marp deck.md --pptx`, git-friendly Markdown), Slidev (dev talks; PPTX export community-supported, fidelity unverified), Pandoc `--reference-doc=brand.pptx` (designer template + Markdown content), HTML→PDF→PPTX (max fidelity, lossy editability), pptxgenjs (Node-first, granular shapes, its own footguns).

## Non-goals

- HTML web decks (Slidev/Marp as alternatives, not core output)
- Animation/transition-heavy decks (python-pptx has no animation API)
- Legacy .ppt (unsupported by python-pptx)
- Real-time co-editing
