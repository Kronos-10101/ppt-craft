#!/usr/bin/env python3
"""SKILL.md validator for the ppt-craft agent skill.

Checks that a SKILL.md file has a well-formed YAML frontmatter block and that
the skill identity (name) and description meet the ppt-craft contract.

Usage:
    python3 scripts/check-skill.py <path-to-SKILL.md>

Exit 0 and prints an OK line on success; prints a clear error to stderr and
exits non-zero on any failure. Standard library only.

Checks performed, in order:
  1. The file exists and is readable.
  2. The file starts with a YAML frontmatter block delimited by two `---` lines.
  3. The frontmatter contains both `name:` and `description:` keys.
  4. The `name` value is exactly `ppt-craft`.
  5. The `description` value is between 100 and 500 characters (inclusive).

Frontmatter parsing is a minimal key:value reader (top-level keys only, no
nested YAML), which is all SKILL.md frontmatter is expected to use.
"""

import sys


SKILL_NAME = "ppt-craft"
DESC_MIN = 100
DESC_MAX = 500


def error(message: str) -> int:
    """Print an error to stderr and return the non-zero exit code."""
    print(f"error: {message}", file=sys.stderr)
    return 1


def read_file(path: str):
    """Return the file's lines, or None after printing an error."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read().splitlines()
    except FileNotFoundError:
        error(f"file not found: {path}")
    except IsADirectoryError:
        error(f"not a file: {path}")
    except OSError as exc:
        error(f"cannot read {path}: {exc}")
    return None


def parse_frontmatter(lines):
    """Extract a dict of top-level key:value pairs from the frontmatter.

    The frontmatter is the block between the first two lines that are exactly
    `---`. Returns (dict, None) on success or (None, error-message) on
    failure. This is a minimal parser: only lines of the form `key: value`
    are considered; quoted values may use single or double quotes; a `|` or
    `>` block scalar value is read until a non-indented line.
    """
    if not lines or lines[0].strip() != "---":
        return None, "missing opening frontmatter delimiter '---' on line 1"

    closing = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing = index
            break
    if closing is None:
        return None, "frontmatter block is not closed (no second '---' line)"
    if closing == 1:
        return None, "frontmatter block is empty"

    fields = {}
    index = 1
    while index < closing:
        line = lines[index]
        if not line.strip() or line.strip().startswith("#"):
            index += 1
            continue
        if ":" not in line or line[0] in (" ", "\t"):
            return None, f"invalid frontmatter line {index + 1}: {line!r}"
        key, _, raw_value = line.partition(":")
        key = key.strip()
        value = raw_value.strip()
        if value in ("|", ">"):
            # Block scalar: consume following indented lines.
            index += 1
            block_lines = []
            while index < closing and (
                lines[index].startswith((" ", "\t")) or not lines[index].strip()
            ):
                block_lines.append(lines[index].strip())
                index += 1
            fields[key] = "\n".join(block_lines).strip()
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        fields[key] = value
        index += 1
    return fields, None


def main(argv) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} <path-to-SKILL.md>", file=sys.stderr)
        return 2

    path = argv[1]
    lines = read_file(path)
    if lines is None:
        return 1

    fields, failure = parse_frontmatter(lines)
    if failure is not None:
        return error(f"{path}: {failure}")

    if "name" not in fields:
        return error(f"{path}: frontmatter missing required 'name' key")
    if "description" not in fields:
        return error(f"{path}: frontmatter missing required 'description' key")

    name = fields["name"]
    if name != SKILL_NAME:
        return error(
            f"{path}: name is {name!r}, expected {SKILL_NAME!r}"
        )

    description = fields["description"]
    desc_len = len(description)
    if desc_len < DESC_MIN or desc_len > DESC_MAX:
        return error(
            f"{path}: description is {desc_len} chars, "
            f"must be {DESC_MIN}-{DESC_MAX} chars"
        )

    print(f"OK: 'ppt-craft' valid ({len(lines)} lines, description {desc_len} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
