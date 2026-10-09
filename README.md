# ppt-craft

An agent skill for designing and building PowerPoint presentations. It gives any AI agent a repeatable pipeline: **intake → type dispatch → ghost-outline plan → template-first python-pptx build → evidence-gated verification with LibreOffice render QA**.

Scope is locked to seven deck-type modules (case study, academic/class, marketing & sales, investor pitch, consulting, thesis defense, hackathon incl. SIH submodule) plus **GitHub-URL → presentation as a first-class capability**: no existing skill does GitHub URL + emphasis notes → faithful general-purpose PPTX (verified in the research). India-specific formats (SIH template, UGC viva norms, B-school case comps, WhatsApp-channel sales notes) are applied when relevant, never by default.

## Why this skill exists

Existing PPT skills either teach mechanics without content (anthropics/skills `pptx`: proprietary, 3-route mechanics), build great pipelines but ignore repo intake (siril9/presentation-skill: MIT, best architecture), do HTML instead of PPTX (guizang: AGPL, wrong medium), or cover repo→deck only for one output format (adewale/slide-maker: Slidev/Markdown only; pitchkit: local-repo-only; asrayg: Marp/hackathon-scoped). The research verified the gap: **GitHub URL + emphasis notes → faithful general-purpose PPTX exists nowhere.** ppt-craft fills it, with a standing rule the research forced: **code wins over README/docs** (the SmartLease pipeline produced 17 false claims out of 40 audited when it trusted prose over code).

## Install

```bash
npx skills add Kronos-10101/ppt-craft
```

## Module map

| File | Purpose | Status |
|---|---|---|
| `SKILL.md` | Router: intake, type dispatch, plan, build, QA | Built |
| `references/design-core.md` | Typography ladder, color, layout, density rules, anti-slop list | Built |
| `references/python-pptx-engineering.md` | Template-first workflow, corruption footguns, engine limits | Built |
| `references/evidence-discipline.md` | VERIFIED/ESTIMATE/ASSUMPTION/MISSING labels, claim ledger | Built |
| `references/case-study.md` | CBS toolkit 5-part arc, Indian case comps (LIME, Interrobang, Brandstorm) | Built |
| `references/academic-class.md` | Assertion-evidence model, seminar structures, VTU seminar norms | Built |
| `references/marketing-sales.md` | Zuora-style arc, WhatsApp-channel note, slideument avoidance | Built |
| `references/investor-pitch.md` | Sequoia/Y-C/10-20-30 reconciliation, Indian metric bar | Built |
| `references/consulting.md` | Minto pyramid, action titles, ghost-deck workflow, appendix discipline | Built |
| `references/thesis-defense.md` | IMRaD-to-talk, UGC 2022 viva norms, backup-slide discipline | Built |
| `references/hackathon.md` | Demo-day, SIH 6-slide submodule, sponsor-track tailoring | Built |
| `references/github-to-deck.md` | Repo intake, emphasis-weighted budgeting, coverage completeness | Built |
| `scripts/check-skill.py` | SKILL.md validator: frontmatter name/description checks | Built |
| `scripts/analyze-deck.py` | Deck analyzer: titles, words/slide, charts/images/tables, notes coverage | Built |
| `research/RESEARCH.md` | Full research dossier (13-worker sweep, 2026-10-09) | Complete |

## Quick start

1. **Intake**: identify deck type, audience, time limit/slide cap, repo URL + emphasis notes (if github-to-deck), and whether an India-specific format (SIH/UGC) applies.
2. **Plan**: read the dispatched `references/*.md` files, write a titles-only ghost outline, start the evidence ledger, get the outline approved.
3. **Build**: template-first: masters/layouts defined once, placeholders filled with python-pptx. Code wins over README for every repo claim. Fix source and rebuild, never patch the generated PPTX.
4. **QA**: evidence gate (every claim VERIFIED/ESTIMATE/ASSUMPTION/MISSING), coverage-completeness check, then `soffice --headless --convert-to pdf` and review every page.

## Design principles

- **Evidence first.** Every factual claim carries a provenance chain and a status label; MISSING claims get dropped or flagged, never invented.
- **Template-first builds.** Designers (or a locked .potx) define masters and layouts once; the agent fills placeholders. This is the pattern python-pptx was designed for.
- **Render QA is mandatory.** python-pptx has no rendering engine and cannot preview; every deck is converted with LibreOffice headless and reviewed page by page.
- **Genre honesty.** Assertion headlines for consulting, topic labels for class decks, self-explanatory density for read-only PDFs: the skill respects each genre's conventions instead of one generic template.
- **Unverified stays unverified.** Anecdotes (e.g. "Sanjeevani decks") and maintenance-status claims are labelled, never presented as measured fact.

## Engine requirements

- Python 3 with `pip install python-pptx`
- LibreOffice (for headless render QA: `soffice --headless --convert-to pdf deck.pptx`)
- No PowerPoint installation needed for building; python-pptx reads and writes `.pptx` natively

## Original content and license hygiene

All skill content is original. Ideas drawn from MIT-licensed sources (siril9/presentation-skill, adewale/slide-maker, liush2yuxjtu/pitchkit, asrayg hackathon skills) are credited, never copied. Nothing is lifted from the proprietary anthropics/skills `pptx` skill or the AGPL-3.0 guizang-ppt-skill: those informed design choices only. Research details live in `research/RESEARCH.md`.

## Key sources (from the research)

- SIH 2025 idea-presentation template (baseline): https://www.sih.gov.in/letters/SIH2025-IDEA-Presentation-Format.pptx
- Sequoia "Writing a Business Plan": sequoiacap.com/article/writing-a-business-plan
- Guy Kawasaki "The Art of the Pitch": guykawasaki.com
- MLH standard hackathon rules: github.com/MLH/mlh-policies
- UGC 2022 Regulations (Gazette of India): old.rvu.edu.in
- MIT-licensed architecture ideas: github.com/siril9/presentation-skill, github.com/adewale/slide-maker, github.com/liush2yuxjtu/pitchkit, github.com/asrayg/hackathon-agent-skills
- Whitepage pitch-deck guide (evidence discipline): whitepage.studio/blog/how-to-use-chatgpt-in-pitch-deck-design
