"""Generate the README notebook index from catalog.yml.

Usage:
    python scripts/build_index.py          # rewrite the README index section
    python scripts/build_index.py --check  # validate only; exit 1 if anything is out of sync
"""

import argparse
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.yml"
README = ROOT / "README.md"
NOTEBOOK_DIR = ROOT / "notebooks"
HTML_DIR = ROOT / "html"
START = "<!-- index:start -->"
END = "<!-- index:end -->"


def validate(catalog):
    """Return (errors, warnings) comparing catalog.yml with the files on disk."""
    errors, warnings = [], []
    categories = catalog["categories"]
    entries = catalog["notebooks"]

    names = [e["notebook"] for e in entries]
    for name, n in Counter(names).items():
        if n > 1:
            errors.append(f"{name} is listed {n} times in catalog.yml")

    on_disk = {p.stem for p in NOTEBOOK_DIR.glob("*.ipynb")}
    for name in sorted(on_disk - set(names)):
        errors.append(f"notebooks/{name}.ipynb is missing from catalog.yml")
    for name in sorted(set(names) - on_disk):
        errors.append(f"catalog.yml lists {name}, but notebooks/{name}.ipynb does not exist")

    for e in entries:
        if e["category"] not in categories:
            errors.append(f"{e['notebook']}: unknown category '{e['category']}'")
        elif not e["notebook"].startswith(e["category"] + "_"):
            errors.append(f"{e['notebook']}: filename should start with '{e['category']}_'")

    for html in sorted(HTML_DIR.glob("*.html")):
        if html.stem not in on_disk:
            warnings.append(f"html/{html.name} has no matching notebook")

    return errors, warnings


def render(catalog):
    lines = [START, "<!-- Generated from catalog.yml by scripts/build_index.py. Do not edit by hand. -->", ""]
    for key, cat in catalog["categories"].items():
        entries = [e for e in catalog["notebooks"] if e["category"] == key]
        if not entries:
            continue
        lines += [f"### {cat['name']}", "", cat["description"], "", "| Notebook | Title | Post |", "|---|---|---|"]
        for e in entries:
            post = f"[radarsimx.com]({e['post']})" if e.get("post") else "—"
            lines.append(f"| [{e['notebook']}](notebooks/{e['notebook']}.ipynb) | {e['title']} | {post} |")
        lines.append("")
    lines.append(END)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="validate without writing README.md")
    args = parser.parse_args()

    catalog = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    errors, warnings = validate(catalog)
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    if errors:
        return 1

    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        print(f"error: README.md must contain {START} and {END} markers")
        return 1
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    updated = head + render(catalog) + tail

    if args.check:
        if updated != readme:
            print("error: README.md index is out of date; run python scripts/build_index.py")
            return 1
        print("README.md index is up to date.")
        return 0

    README.write_text(updated, encoding="utf-8", newline="\n")
    print("README.md index updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
