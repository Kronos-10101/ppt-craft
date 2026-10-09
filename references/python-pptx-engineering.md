# python-pptx Engineering — the build engine for ppt-craft

Primary engine: python-pptx, template-first workflow, LibreOffice headless render QA.
All claims grounded in the research dossier (~/workspace/ppt-craft/research/RESEARCH.md),
capability/limit sheet verified against official python-pptx docs + field reports, dated 2026-10-09.

## 1. Template-first workflow (the designed pattern)

- [ ] A designer builds masters, layouts, and placeholders once in PowerPoint; the agent fills placeholders only. This is the pattern the library is designed around.
- [ ] Generate decks by code against a template — never by hand-editing output.
- [ ] Fix the source and rebuild; never patch the generated PPTX (siril9 architecture, via dossier). Rebuilds stay auditable; patches rot.
- [ ] Open question (dossier Q6, awaiting user verification): whether the skill ships starter .potx templates per deck type, or template-guidance only. Do not assume either.

## 2. What python-pptx can do

- [ ] Create, read, and update .pptx with no PowerPoint installed.
- [ ] Round-trip any OOXML — all elements are preserved through read/write.
- [ ] Add slides from layouts via `add_slide(layout)`; read theme/layout/master access.
- [ ] Text with run-level formatting (font, size, bold, color per run).
- [ ] Images at arbitrary position and size.
- [ ] Tables.
- [ ] Autoshapes + connectors + freeform builder + group shapes.
- [ ] Native editable charts: column, bar, line, pie + XY-scatter and bubble — "most chart types other than 3D" — with embedded workbooks.
- [ ] Notes slides, hyperlinks, and core properties.

## 3. FOOTGUN checklist (hard limits — design around them, never against them)

- [ ] `text_frame.text = ...` collapses all formatting to one unstyled run — assign `run.text` instead. (Most-hit footgun in field reports.)
- [ ] `add_picture` raises on SVG/EMF — convert to PNG/JPEG first.
- [ ] NO slide duplication and NO cross-presentation copy — only `add_slide(layout)`. Workaround: restructure the build so duplication is never needed (rebuild-from-source, section 1).
- [ ] NO SmartArt creation — SmartArt round-trips only. Pre-author any SmartArt in the template.
- [ ] NO multi-plot/combo chart creation — existing combo charts can be read, not created. Pre-build combo charts in the template.
- [ ] NO animation or transition API — the engine cannot set any of it. Keep built decks static-first (see design-core.md section 7).
- [ ] NO equation/OMML API — workarounds: LaTeX→OMML injection, or pre-rendered equation images (thesis decks: never ASCII equations).
- [ ] NO rendering engine — the library cannot preview anything. All visual QA goes through LibreOffice/PowerPoint (section 4).
- [ ] NO PPTX→PDF/image conversion inside the library — use LibreOffice.
- [ ] Gradients are linear-only.
- [ ] Legacy .ppt is unsupported — require .pptx input and output only.

## 4. LibreOffice render-QA loop (mandatory gate before delivery)

- [ ] Convert headless: `soffice --headless --convert-to pdf deck.pptx`.
- [ ] Visually review EVERY PDF page — not a sample — for text overflow, clipping, misalignment, and font substitution.
- [ ] Overflow/clipping found → fix the source and rebuild, re-convert, re-review. Never patch the PPTX.
- [ ] Delivery gate: no deck ships without a reviewed PDF. (Dossier: mandatory file+visual QA gate; render QA = LibreOffice headless → PDF → image review.)

## 5. Alternative engines — documented as OPTIONS, not core

- [ ] pptxgenjs — Node-first option; granular shapes; carries its own footguns.
- [ ] Marp — `marp deck.md --pptx`; git-friendly Markdown source. Good for text-heavy, version-controlled decks.
- [ ] Slidev — dev-talk option; PPTX export is community-supported. Export fidelity: UNVERIFIED (dossier honesty ledger, 2026-10-09).
- [ ] Pandoc — `--reference-doc=brand.pptx` gives designer-template + Markdown-content. Underused; worth knowing.
- [ ] HTML→PDF→PPTX — maximum visual fidelity, lossy editability. Last resort, not a pipeline.
- [ ] Core stays python-pptx until the user re-verifies the engine question (dossier Q3, awaiting verification).

## 6. Maintenance flag — UNVERIFIED, do not repeat as fact

- [ ] Third-party claim: no python-pptx releases since Aug 2024 — UNVERIFIED.
- [ ] Third-party claim: python-pptx-ng fork exists (group shapes, freeform, video, pattern fills) — UNVERIFIED.
- [ ] Verify both on PyPI before the skill repeats either claim (dossier instruction, 2026-10-09).

## 7. Build patterns (template-first)

- [ ] Title slide: title + subtitle placeholders only; subtitle carries the one-line thesis.
- [ ] Assertion slide: title placeholder = complete-sentence takeaway; content placeholder = ≤6 lines or one exhibit.
- [ ] Exhibit slide: title placeholder = the takeaway the exhibit proves; chart/table placeholder below; source line in the footer placeholder.
- [ ] Section divider: full-bleed title layout; one phrase per section.
- [ ] Speaker notes: notes-slide placeholders carry the script — observed as timed notes in strong hackathon decks and near-transcript notes in real defenses. Never leave notes empty on talk-aid decks.
- [ ] Footer chrome for document decks: source / units / date / page + "Preliminary / For Discussion" sticker where required (consulting dossier).

## 8. Chart data hygiene

- [ ] Chart numbers are claims too — every plotted number gets a ledger row (see evidence-discipline.md).
- [ ] Embedded workbooks ship inside the .pptx — keep them clean: no scratch sheets, no mock series labeled as real.
- [ ] Never smooth a hockey stick: show dated, specific data points (pitch dossier).

## Sources

- python-pptx official docs: https://python-pptx.readthedocs.io/ (capability/limit sheet verified against these, per dossier)
- https://github.com/siril9/presentation-skill (MIT) — source-first pipeline architecture (ideas only)
- https://github.com/anthropics/skills (Proprietary) — footgun/QA-gate ideas only; NO text or scripts reused
- Dossier honesty ledger (2026-10-09): SIH 2026 template changes, famous pitch decks as .pptx (PDF-only), Slidev export fidelity — all unverified
