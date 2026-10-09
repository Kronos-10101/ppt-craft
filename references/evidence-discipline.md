# Evidence Discipline — truthfulness system for ppt-craft

Every deck the skill builds is a truthfulness pipeline, not just a layout pipeline.
All claims grounded in the research dossier (~/workspace/ppt-craft/research/RESEARCH.md),
dated 2026-10-09. License posture: original content only; ideas from MIT sources OK;
NOTHING lifted from proprietary anthropics/skills or AGPL guizang.

## 1. Claim labels (Whitepage pitch-deck guide, via dossier)

- [ ] Every substantive claim on every slide carries exactly one label: VERIFIED / ESTIMATE / ASSUMPTION / MISSING.
- [ ] VERIFIED: backed by an inspected source or by code the agent actually read.
- [ ] ESTIMATE: a number derived with a stated method (method lives in notes or appendix).
- [ ] ASSUMPTION: taken as given; flagged for the user to confirm before the deck is used.
- [ ] MISSING: needed but not found — say so on the slide or in speaker notes; never silently drop it.
- [ ] Conclusion-led titles must still carry their label — a strong headline never upgrades a weak claim.

## 2. Claim→evidence→slide ledger (asrayg evidence-ledger pattern, via dossier)

- [ ] Maintain one ledger table per deck build:

  | Claim | Evidence | Slide | Status |
  |---|---|---|---|
  | (one row per substantive claim) | (source file, URL, or code path) | (slide #) | VERIFIED / ESTIMATE / ASSUMPTION / MISSING / FALSE |

- [ ] Ledger updates on every rebuild — fix source, rebuild, re-verify (siril9 pattern).
- [ ] Ledger ships with the build (hidden appendix or build notes), not thrown away at delivery.

## 3. Code-wins-over-README (repo-derived decks)

- [ ] For GitHub-URL → deck builds: where code contradicts docs, CODE WINS. Dossier, 2026-10-09: one repo→deck pipeline audit found 17 FALSE of 40 claims (e.g. NPU execution, on-device models contradicted by the code itself).
- [ ] Never present mock data as implemented (asrayg rule, via dossier).
- [ ] Provenance chain per fact: every claim traces to a specific file, commit, or doc (slide-maker SOURCES.md pattern, via dossier).
- [ ] Repo intake order (asrayg pitch-deck-pressure, via dossier): README → entry point → git log → assets. Bounded passes — timebox the mining, then build from what is verified.
- [ ] Repo-reading table (huytech, via dossier): check README / manifests / docs / src / issues in that sweep.

## 4. Red-team stress test (before delivery, every time)

- [ ] Ask: what would a skeptical judge or examiner attack? Answer it on a slide or in backup slides — never leave it unaddressed (Whitepage red-team; Tsekleves examiner pattern, via dossier).
- [ ] Pitch decks: fake-traction sweep — traction must be dated and specific; no undated hockey sticks, no MoUs-as-traction, no vanity top-down TAMs (pitch dossier).
- [ ] Pitch decks: never claim "we have no competitors" and never put deal terms/valuation in the outbound deck (pitch dossier: both are investor-blacklisted honesty failures).
- [ ] "So what?" per slide — if the claim cannot survive the question, cut it (consulting QA ritual).
- [ ] Thesis/defense decks: limitations stated proactively (contained / methodological / structural) — the examiner will find them anyway (thesis dossier).

## 5. Rebuild-from-source rule (keeps the evidence chain honest)

- [ ] Fix the source and rebuild; never patch the generated PPTX (siril9, via dossier). A hand-patched deck breaks the claim→evidence→slide chain silently.
- [ ] The build script + ledger + template together are the reproducible artifact. If a claim changes, the ledger row changes with it.

## 6. Per-deck delivery gate

- [ ] Every substantive claim labeled (section 1).
- [ ] Ledger complete: Claim | Evidence | Slide | Status filled for all claims.
- [ ] Red-team pass done; attacks addressed on slides or backups.
- [ ] LibreOffice render QA passed (see python-pptx-engineering.md section 4).
- [ ] No claim above its label: an ESTIMATE is never presented as VERIFIED, anywhere — headline, body, or speaker notes.

## 7. Surfacing labels in the deck

- [ ] Read-alone decks (case, consulting, SIH): labels live in source lines or the appendix; MISSING items appear in backup slides or are flagged to the user before delivery.
- [ ] Talk-aid decks (class, demo-day): labels live in speaker notes; the spoken claim never exceeds its label.
- [ ] An ASSUMPTION the user has not confirmed stays labeled ASSUMPTION through delivery — never silently upgraded.

## 8. Appendix and backup discipline

- [ ] 15 tight appendix slides beat a 60-slide dump (consulting dossier).
- [ ] Thesis defenses: formally sectioned backups ("Extra Slides", "Old Slides") — observed in real defenses (thesis dossier).
- [ ] Every backup slide is still labeled; backups are where ASSUMPTION and MISSING claims get their hearing.

## 9. Cross-references

- [ ] Render QA gate: python-pptx-engineering.md section 4.
- [ ] Repo-intake weighting and narrative arc: github-to-deck.md (same folder).
- [ ] Visual rules that keep claims honest (no fake metrics as decoration): design-core.md section 6.

## Sources

- Whitepage "ChatGPT Pitch Deck" guide: https://www.whitepage.studio/blog/how-to-use-chatgpt-in-pitch-deck-design (VERIFIED/ESTIMATE/ASSUMPTION/MISSING labels; red-team stress test)
- https://github.com/asrayg/hackathon-agent-skills (MIT) — evidence ledger (Claim|Evidence|Slide|Status); "never present mock data as implemented"; repo-mining priority order (ideas only)
- https://github.com/adewale/slide-maker (MIT) — SOURCES.md provenance chain per fact (ideas only)
- https://github.com/siril9/presentation-skill (MIT) — evidence-first data rules; "fix source and rebuild" (ideas only)
