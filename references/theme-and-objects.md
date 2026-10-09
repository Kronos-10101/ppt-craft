# Theme & Objects — PPTX data model, color themes, object mechanics (2026-10-09)

The mechanics layer: how a .pptx stores data, how that data becomes visuals,
how to decide and apply a company color theme, and how to create and adjust
objects correctly with python-pptx. Design taste lives in
references/design-core.md; engine limits in references/python-pptx-engineering.md
— this file is the machinery underneath both.

## 1. How a PPTX stores data (the part model)

- [ ] A .pptx is a ZIP of XML parts. The agent-relevant parts: `ppt/slides/slideN.xml`
      (slide content), `ppt/slideLayouts/`, `ppt/slideMasters/`, `ppt/theme/theme1.xml`
      (the theme), `ppt/embeddings/` (chart workbooks), `ppt/media/` (images).
- [ ] Inheritance chain, always this order: slide → slideLayout → slideMaster →
      theme. A slide with no explicit fill gets it from its layout, then the
      master, then the theme. Nothing on a slide is ever truly "unstyled" —
      it is styled by inheritance.
- [ ] A shape whose fill type is `None` (the default for `add_shape`) inherits
      its fill from this chain — this is the re-theme-safe default. Setting
      `.fill.solid()` + `.fore_color.rgb` BREAKS the chain for that shape:
      it now ignores theme changes (python-pptx docs, dev analysis dml-fill).
- [ ] Tables are stored as `<a:tbl>` graphic frames, not as shapes with text —
      they do not inherit cell styling the way text placeholders do; style
      every cell explicitly.
- [ ] Chart data lives in an embedded workbook: `ppt/embeddings/Microsoft_Excel_WorksheetN.xlsx`.
      Editing chart data means rewriting that workbook — in python-pptx,
      `chart.replace_data(ChartData(...))` regenerates it. Never hand-edit the
      XML and expect the chart to follow.
- [ ] Images are stored as separate parts in `ppt/media/`, referenced by
      relationship id. Each `add_picture` call adds a part — reusing one
      source image across slides keeps file size down; ten crops of one photo
      should be one part, not ten.

## 2. How data becomes visuals (theme resolution)

- [ ] `ppt/theme/theme1.xml` holds exactly 12 theme colors in `<a:clrScheme>`
      (Microsoft Learn, "Creating Document Themes"): two dark/light text-background
      pairs (`dk1/lt1`, `dk2/lt2`), six accents (`accent1`–`accent6`), and two
      hyperlink colors (`hlink`, `folHlink`).
- [ ] PowerPoint's color picker rule, per Microsoft: the first four slots are
      text/background pairs (light text is always legible on dark, dark on
      light); the six accents are "always visible" over any background; the
      last two are links. (Microsoft Learn, "Use Office document themes".)
- [ ] Shapes never store "accent1" directly — they store a scheme reference
      plus luminance transforms: `lumMod` (multiply luminance), `lumOff`
      (shift luminance), per ISO/IEC 29500. "Accent 1, 25% darker" in the UI is
      literally `accent1 + lumMod`. Tints and shades are computed, not stored.
- [ ] Re-theming = swapping the 12 values in `theme1.xml`. Every object that
      references a theme slot re-renders; every object with a hardcoded
      `srgbClr` stays frozen. This is the entire reason the slot rule below
      exists (Finkelstein's theme-color demonstration, mechanism unchanged
      since PowerPoint 2007).
- [ ] Slide masters can remap the four text/background aliases via `<p:clrMap>`
      (default: `bg1→lt1`, `tx1→dk1`, `bg2→lt2`, `tx2→dk2`; verified in
      python-pptx issue #39 / FEP-017). Consequence: `tx1` on one master may
      resolve differently than `tx1` on another — when a deck has multiple
      masters, verify the color map per master, not once globally.

## 3. Deciding a company color theme

- [ ] Start from the brand's real palette (logo, website, brand guidelines) —
      never invent company colors. If no brand exists, pick one primary +
      one secondary + neutrals, then lock them before building.
- [ ] Map brand roles onto the 12 slots, in this order: primary brand color →
      `accent1`; secondary → `accent2`; supporting/tertiary → `accent3`–`accent6`
      (leave unused slots at neutral values, never at random hues); page
      background → `lt1`; body text → `dk1`; secondary surfaces/text →
      `lt2`/`dk2`.
- [ ] Text-safety rule per slot: body text lives ONLY on `dk1`/`lt1` (and
      `dk2`/`lt2` for secondary text). Accents are for fills, chart series,
      and emphasis — text set in an accent color must pass AA against its
      background; mid-luminance accents (yellows, light greens) fail on white.
- [ ] Derive tints/shades by luminance steps, never by eyeballing: from any
      accent, generate the working set at brightness −0.25 / +0.25 / +0.5
      (in python-pptx: `fore_color.brightness`). Three computed steps beat
      five hand-picked hexes — they stay in harmony and survive re-theming.
- [ ] Hyperlinks: set `hlink` to the primary accent (or a conventional blue)
      and `folHlink` one step darker. Unset hyperlink slots default to theme
      blue/purple and will clash with the brand.
- [ ] Record the mapping as a table (brand role → slot → hex → text-safe?),
      checked in with the build script. The next person re-theming the deck
      edits 12 values, not 200 shapes.

## 4. Using theme slots correctly (the slot rule)

- [ ] THE SLOT RULE: theme roles get theme slots, never raw hex. Every fill,
      line, and text color that represents a brand role is set via
      `MSO_THEME_COLOR`, not `RGBColor`. Raw hex is reserved for data-driven
      colors (chart series distinguishing categories) and photographic content.
- [ ] python-pptx CAN write theme colors (it just cannot read them): set
      `fill.fore_color.theme_color = MSO_THEME_COLOR.ACCENT_1`, then adjust
      with `fill.fore_color.brightness = -0.25` (official python-pptx docs,
      "Working with AutoShapes"). Same API works on `line.color` and
      `run.font.color`.
- [ ] Reading the theme back has NO public python-pptx API (confirmed in
      field reports): open the .pptx as a ZIP and parse
      `ppt/theme/theme1.xml` → `<a:clrScheme>` directly. Do this once at
      intake when matching an existing template — never eyeball colors from
      a screenshot.
- [ ] Brightness range is −1.0 to +1.0; stay within ±0.5 for working tints —
      beyond that, accents collapse toward black/white and lose brand identity.
- [ ] Placeholder text and fills already reference theme slots via the
      layout/master — filling a placeholder inherits the theme automatically.
      Only freeform shapes need explicit `theme_color` assignment.
- [ ] Re-theme test before delivery: swap one accent value in a COPY of the
      deck and confirm every brand element follows. Any element that does
      not follow has a hardcoded color — fix the source, not the copy.

## 5. Creating objects properly

- [ ] Prefer placeholders over freeform shapes: `slide.placeholders` inherit
      layout geometry, theme fills, and text styles. `shapes.add_shape(...)`
      creates orphans — correct geometry is then the agent's job, forever.
- [ ] When freeform is required: `shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
      left, top, width, height)`; set fill via theme slot (section 4); set
      `line.fill.background()` for no outline rather than a hairline in a
      random gray.
- [ ] Z-order = document order in `<p:spTree>`: shapes render back-to-front in
      the order they appear in the XML. python-pptx has NO public reorder API —
      plan insertion order up front (background first, foreground last), or
      reorder by moving the shape's element within `slide.shapes._spTree`.
- [ ] Connectors glue: `shapes.add_connector(MSO_CONNECTOR.STRAIGHT, ...)` then
      `connector.begin_connect(shape_a, site)` / `.end_connect(shape_b, site)`
      — glued connectors follow their shapes when the layout is adjusted.
      Unglued lines are decoration that breaks on the first nudge.
- [ ] Group related shapes (`shapes.add_group_shape()`) when they move as a
      unit (icon + label, chart + caption) — one bounding box, one alignment
      target, no drift.
- [ ] Images: `add_picture` needs explicit width/height or it drops the image
      at native resolution (often slide-breaking). Preserve aspect ratio:
      compute one dimension from the other. Compress sources before adding —
      a 5 MB photo on 20 slides is a 100 MB deck.
- [ ] Text autofit is opt-in, not automatic: `text_frame.auto_size =
      MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE` (shrink text) or
      `.SHAPE_TO_FIT_TEXT` (grow box). Default (`None`) clips overflow
      silently — the LibreOffice render QA in python-pptx-engine.md exists
      precisely because of this.

## 6. Adjusting and aligning (the computation patterns)

- [ ] python-pptx has NO alignment helpers — every alignment is arithmetic on
      EMU. Units: 914400 EMU = 1 inch; use `Cm()`, `Inches()`, `Pt()`,
      `Emu()` helpers, never raw integers.
- [ ] Center on slide: `shape.left = (prs.slide_width - shape.width) // 2`;
      vertical center likewise with `slide_height`. Default blank deck:
      10 × 7.5 in (4:3); 16:9 template: 13.33 × 7.5 in — read
      `prs.slide_width/height`, never assume.
- [ ] Distribute N shapes evenly across a span: `gap = (span - sum(widths)) //
      (n - 1)`; place sequentially with running offset. Equal gaps, not equal
      centers — equal centers on unequal widths looks wrong.
- [ ] Baseline grid: pick one vertical rhythm unit (e.g. 0.25 in) and snap
      every `top` to a multiple of it. Margins: one external margin value
      (e.g. 0.5 in) used on all four sides of every slide — the single
      cheapest alignment win.
- [ ] Nudge vs rebuild rule: moving ≤2 shapes by <0.25 in → adjust in the
      build script and re-run render QA. Anything structural (reflowing a
      slide, changing the grid, re-theming) → change the source constants
      and rebuild the deck. Never hand-edit coordinates into the .pptx.
- [ ] After ANY adjustment: re-run the LibreOffice render QA
      (`soffice --headless --convert-to pdf`). Alignment arithmetic is exact;
      font metrics and autofit are not — the PDF is the verdict.

## Sources

- Microsoft Learn, "Creating Document Themes with the Office Open XML Formats"
      — https://learn.microsoft.com/en-us/previous-versions/office/developer/office-2007/cc964302(v=office.12) (12-color clrScheme structure)
- Microsoft Learn, "Use Office document themes in your PowerPoint add-ins"
      — https://learn.microsoft.com/en-us/office/dev/add-ins/powerpoint/use-document-themes-in-your-powerpoint-add-ins (slot roles: 4 text/bg, 6 accents, 2 links)
- Microsoft Learn, StyleColor class docs — lum/lumOff/lumMod definitions per ISO/IEC 29500
- python-pptx official docs, "Working with AutoShapes" — https://python-pptx.readthedocs.io/en/stable/user/autoshapes.html (theme_color + brightness API)
- python-pptx dev analysis, dml-fill — https://python-pptx.readthedocs.io/en/latest/dev/analysis/dml-fill.html (fill type None = theme inheritance)
- python-pptx issue #39 / FEP-017 — clrMap defaults (bg1→lt1, tx1→dk1, bg2→lt2, tx2→dk2)
- Field report: claude-academic-skills native-pptx-workflows.md — no public python-pptx API for reading theme colors; parse theme1.xml as ZIP
- Ellen Finkelstein, "Create a theme in PowerPoint that changes colors" — theme-referenced shapes follow re-theming; hardcoded colors do not
