#!/usr/bin/env python3
"""Analyze the structure of a .pptx deck and report its empirical profile.

This is the cleaned-up Track C tool from the ppt-craft research phase. It
reverse-engineers a deck's *structure* (not its design): slide count, titles
in order, words per slide, and how the deck leans on native charts, images,
tables, and speaker notes. That profile is what the type dossiers in the
research are built on — e.g. "median 66-71 words/slide, image-heavy, zero
native charts" is exactly the output of this tool run over real investor
pitch decks, and "notes on 13/13 slides" is its speaker-notes coverage.

Why structure matters for a PPT-design skill: different deck genres have
wildly different structural fingerprints (a 100-slide M&A document deck vs.
a 6-slide SIH idea deck vs. a 91-slide thesis defense). Measuring these
metrics on a reference deck tells the agent which genre's module to follow
and whether its own generated deck matches the genre's norms (density,
notes coverage, assertion vs. label titles) before it renders for QA.

Usage:
    python3 scripts/analyze-deck.py <deck.pptx> [--json]

Requires python-pptx (`pip install python-pptx`). Legacy .ppt files are
refused; corrupt or empty files produce a graceful error instead of a
traceback. With --json the same report is emitted as JSON.
"""

import json
import os
import statistics
import sys
from collections import Counter

try:
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE, PP_PLACEHOLDER
except ImportError:
    print(
        "error: python-pptx is not installed.\n"
        "Install it with: pip install python-pptx",
        file=sys.stderr,
    )
    sys.exit(1)


UNTITLED = "(untitled)"


def count_words(text: str) -> int:
    """Count whitespace-separated tokens; tables and placeholders included."""
    return len(text.split())


def slide_texts(slide) -> list:
    """All text-frame strings on the slide, in shape order."""
    texts = []
    for shape in slide.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text.strip()
            if text:
                texts.append(text)
    return texts


def extract_title(slide) -> str:
    """Title resolution used by the Track C study.

    1. The slide's title placeholder text (TITLE / CENTER_TITLE), if present.
    2. Otherwise the first non-empty text line on the slide.
    3. Otherwise "(untitled)".
    """
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        if shape.is_placeholder:
            phf = shape.placeholder_format
            if phf.type in (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE):
                text = shape.text_frame.text.strip()
                if text:
                    return text
    texts = slide_texts(slide)
    if texts:
        return texts[0].splitlines()[0].strip()
    return UNTITLED


def count_media(slide) -> tuple:
    """Return (charts, images, tables) counted on the slide.

    Only *native* PPTX objects count: embedded chart parts, PICTURE shapes,
    and table graphic frames. Pictures pasted from another app still arrive
    as PICTURE shapes, so "images" includes screenshots and pasted figures.
    """
    charts = images = tables = 0
    for shape in slide.shapes:
        if shape.has_chart:
            charts += 1
        elif shape.has_table:
            tables += 1
        elif shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            images += 1
    return charts, images, tables


def notes_text(slide) -> str:
    """Speaker-notes text for the slide, or an empty string if none."""
    try:
        notes_slide = slide.notes_slide
    except Exception:
        return ""
    text = notes_slide.notes_text_frame.text.strip()
    return text


def analyze(path: str) -> dict:
    """Build the structural report for the deck at `path`."""
    presentation = Presentation(path)
    slides = list(presentation.slides)
    if not slides:
        raise ValueError("deck contains no slides")

    per_slide = []
    words = []
    charts = images = tables = 0
    notes_count = 0
    layout_names = Counter()

    for index, slide in enumerate(slides, start=1):
        title = extract_title(slide)
        word_count = sum(count_words(t) for t in slide_texts(slide))
        slide_charts, slide_images, slide_tables = count_media(slide)
        has_notes = bool(notes_text(slide))

        words.append(word_count)
        charts += slide_charts
        images += slide_images
        tables += slide_tables
        notes_count += 1 if has_notes else 0

        layout = slide.slide_layout
        layout_names[layout.name] += 1

        per_slide.append(
            {
                "index": index,
                "title": title,
                "words": word_count,
                "charts": slide_charts,
                "images": slide_images,
                "tables": slide_tables,
                "has_notes": has_notes,
            }
        )

    return {
        "file": path,
        "slide_count": len(slides),
        "slides": per_slide,
        "words_per_slide": {
            "min": min(words),
            "median": statistics.median(words),
            "max": max(words),
            "total": sum(words),
        },
        "charts": charts,
        "images": images,
        "tables": tables,
        "notes_coverage": {
            "slides_with_notes": notes_count,
            "percent": round(100.0 * notes_count / len(slides), 1),
        },
        "layouts": [
            {"name": name, "count": count}
            for name, count in layout_names.most_common()
        ],
    }


def render_text(report: dict) -> str:
    """Human-readable rendering of the report."""
    lines = []
    lines.append(f"Deck: {report['file']}")
    lines.append(f"Slides: {report['slide_count']}")
    lines.append("")
    lines.append("Per slide:")
    for slide in report["slides"]:
        media = []
        if slide["charts"]:
            media.append(f"{slide['charts']} chart(s)")
        if slide["images"]:
            media.append(f"{slide['images']} image(s)")
        if slide["tables"]:
            media.append(f"{slide['tables']} table(s)")
        media_str = f" [{', '.join(media)}]" if media else ""
        notes_str = " [notes]" if slide["has_notes"] else ""
        lines.append(
            f"  {slide['index']:>3}. {slide['title']} "
            f"({slide['words']} words){media_str}{notes_str}"
        )
    lines.append("")
    wps = report["words_per_slide"]
    lines.append(
        f"Words/slide: min {wps['min']}, median {wps['median']}, "
        f"max {wps['max']} (total {wps['total']})"
    )
    lines.append(
        f"Media: {report['charts']} native chart(s), "
        f"{report['images']} image(s), {report['tables']} table(s)"
    )
    notes = report["notes_coverage"]
    lines.append(
        f"Speaker notes: {notes['slides_with_notes']}/{report['slide_count']} "
        f"slides ({notes['percent']}%)"
    )
    layouts = ", ".join(
        f"{entry['name']} x{entry['count']}" for entry in report["layouts"]
    )
    lines.append(f"Layouts (most common first): {layouts}")
    return "\n".join(lines)


def main(argv) -> int:
    args = [a for a in argv[1:] if a != "--json"]
    as_json = "--json" in argv[1:]
    if len(args) != 1:
        print(
            f"usage: {argv[0]} <deck.pptx> [--json]",
            file=sys.stderr,
        )
        return 2

    path = args[0]
    if path.lower().endswith(".ppt") and not path.lower().endswith(".pptx"):
        print(
            "error: legacy .ppt files are not supported "
            "(python-pptx reads .pptx only).",
            file=sys.stderr,
        )
        return 1

    try:
        if not os.path.isfile(path):
            print(f"error: file not found: {path}", file=sys.stderr)
            return 1
        report = analyze(path)
    except FileNotFoundError:
        print(f"error: file not found: {path}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"error: {path}: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # corrupt zip / bad OOXML -> graceful error
        print(f"error: could not read {path}: {exc}", file=sys.stderr)
        return 1

    if as_json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
