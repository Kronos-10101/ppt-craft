# GitHub repo → presentation (2026-10-09)

FIRST-CLASS capability: a GitHub repo URL plus the user's emphasis notes becomes a
full-fledged presentation. No existing skill does GitHub-URL + emphasis-notes →
faithful general-purpose PPTX: adewale/slide-maker is Slidev/Markdown-only and refuses
PPTX; liush2yuxjtu/pitchkit is local-repo-only and launch-specific; asrayg
pitch-deck-pressure is Marp output and hackathon-scoped. That gap is the rationale.

## INTAKE SPEC

- [ ] Repo URL — required (GitHub).
- [ ] Emphasis notes — optional, free text ("emphasize the scheduler", "skip the frontend").
- [ ] Deck purpose/audience override — optional; default: project showcase.

## BOUNDED ANALYSIS PASSES (in order)

- [ ] Pass 1: README + docs.
- [ ] Pass 2: entry points (main, CLI, app bootstrap).
- [ ] Pass 3: git log — what changed recently, velocity.
- [ ] Pass 4: key modules — top-level dirs, dependency-graph sketch.
- [ ] Pass 5: configs/manifests (package.json, pyproject.toml, go.mod) — stack + scripts.
- [ ] Time-box: if the repo is huge, state what was skipped and why.

## PER-PASS OUTPUT CONTRACT

Each pass produces notes that feed the ledger, not slides:

- [ ] Pass 1 output: claimed features list (each tagged "per docs", unverified).
- [ ] Pass 2 output: real entry points + CLI surface (confirms what actually runs).
- [ ] Pass 3 output: recency + velocity note (active/stale; last meaningful change).
- [ ] Pass 4 output: module list with one-line roles (feeds the appendix inventory).
- [ ] Pass 5 output: stack + scripts table (tech-stack slide, how-to-run slide).
- [ ] Contradiction found in a later pass OVERWRITES an earlier claim and is logged in
      the ledger as VERIFIED-by-code; the README version stays visible as superseded.
      Dossier example: docs claimed NPU execution and on-device models; code
      contradicted both — 17 FALSE of 40 audited claims.

## PROVENANCE-CHAIN FORMAT

- [ ] On-slide source note uses slide-maker's `Sources:` pattern, e.g.
      `Sources: src/scheduler/fair.py:40-88 (VERIFIED)`.
- [ ] Ledger example row: Claim "scheduler enforces fair queueing" |
      Evidence "src/scheduler/fair.py:40-88" | Slide 5 | VERIFIED.

## TRUTHFULNESS RULES

- [ ] CODE WINS OVER README/docs for every claim. Dossier field report: in one
      SmartLease repo→deck pipeline, 17 FALSE of 40 audited claims where code
      contradicted docs (NPU execution, on-device models).
- [ ] Every claim gets a provenance chain: file path + line ref
      (adewale/slide-maker's `Sources:` pattern).
- [ ] Evidence ledger on Claim | Evidence | Slide | Status
      (asrayg build-hackathon-pitch-deck pattern).
- [ ] Never present mock data as implemented.
- [ ] Label each ledger row VERIFIED / ESTIMATE / ASSUMPTION / MISSING
      (Whitepage "ChatGPT Pitch Deck" guide discipline).

## CANONICAL PROJECT-SHOWCASE ARC

1. [ ] Title + one-line thesis.
2. [ ] Problem it solves.
3. [ ] Solution demo/overview.
4. [ ] Architecture — one diagram.
5. [ ] Key components/modules, mapped from repo structure.
6. [ ] Tech stack.
7. [ ] How to run/use.
8. [ ] Highlights/surprising details.
9. [ ] Roadmap/future.
10. [ ] Appendix: module inventory.

## EMPHASIS-WEIGHTED SLIDE BUDGETING

- [ ] User-emphasized areas get proportionally more slides: ≥40% of body slides.
- [ ] Explicitly deprioritized areas get ≤1 slide or move to the appendix.
- [ ] Fixed narrative arc is the default; emphasis notes drive the weighting.

## COVERAGE-COMPLETENESS CHECK

- [ ] Every top-level repo module is either covered on a slide or EXPLICITLY CUT with a
      one-line reason in the appendix inventory — no silent omissions.
- [ ] No existing skill does this; it is part of the gap rationale.

## ANTI-OVERCLAIM CULTURE

- [ ] "WORKING MVP, HONESTLY" — only demo what runs.
- [ ] Do not claim features, platforms, or scale the code does not show.

**Sources:** adewale/slide-maker (MIT) — SOURCES.md extraction doc, source-type table
(README/CHANGELOG/ARCHITECTURE/configs), provenance chain per fact, bounded passes;
liush2yuxjtu/pitchkit (MIT) — 12-step playbook, ProductContext JSON + validation,
live demo recording; asrayg pitch-deck-pressure (MIT) — repo mining priority
(README → entry point → git log → assets), "code wins over README";
asrayg build-hackathon-pitch-deck (MIT) — Claim|Evidence|Slide|Status ledger;
Whitepage "ChatGPT Pitch Deck" guide — VERIFIED/ESTIMATE/ASSUMPTION/MISSING;
siril9/presentation-skill (MIT) — evidence-first data rules, "fix source and rebuild".
