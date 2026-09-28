"""Export notebooks to HTML fragments for radarsimx.com.

Usage:
    python scripts/export_html.py                  # export all notebooks
    python scripts/export_html.py imaging_* rcs_car  # export selected notebooks
    python scripts/export_html.py --changed        # only notebooks newer than their HTML
"""

import argparse
import sys
from pathlib import Path

from nbconvert import HTMLExporter

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"
HTML_DIR = ROOT / "html"
TEMPLATE_DIR = ROOT / "templates"


def select_notebooks(patterns):
    """Resolve notebook names or glob patterns (with or without .ipynb)."""
    if not patterns:
        return sorted(NOTEBOOK_DIR.glob("*.ipynb"))

    selected = []
    for pattern in patterns:
        name = Path(pattern).name
        if not name.endswith(".ipynb"):
            name += ".ipynb"
        matches = sorted(NOTEBOOK_DIR.glob(name))
        if not matches:
            raise SystemExit(f"Error: no notebook matches '{pattern}' in {NOTEBOOK_DIR}")
        selected.extend(m for m in matches if m not in selected)
    return selected


def is_stale(notebook):
    html = HTML_DIR / f"{notebook.stem}.html"
    return not html.exists() or notebook.stat().st_mtime > html.stat().st_mtime


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("notebooks", nargs="*", help="notebook names or glob patterns (default: all)")
    parser.add_argument("--changed", action="store_true", help="only export notebooks newer than their HTML")
    args = parser.parse_args()

    if not (TEMPLATE_DIR / "notebook_template").is_dir():
        raise SystemExit(f"Error: notebook_template not found in {TEMPLATE_DIR}")

    notebooks = select_notebooks(args.notebooks)
    if args.changed:
        notebooks = [nb for nb in notebooks if is_stale(nb)]
    if not notebooks:
        print("Nothing to export.")
        return 0

    HTML_DIR.mkdir(exist_ok=True)
    exporter = HTMLExporter(template_name="notebook_template", extra_template_basedirs=[str(TEMPLATE_DIR)])

    count = failed = 0
    for notebook in notebooks:
        print(f"Converting {notebook.name}...")
        try:
            body, _ = exporter.from_filename(str(notebook))
            (HTML_DIR / f"{notebook.stem}.html").write_text(body, encoding="utf-8")
        except Exception as exc:  # keep going so one bad notebook doesn't stop the batch
            print(f"  [FAILED] {notebook.name}: {exc}")
            failed += 1
        else:
            print(f"  [OK] {notebook.name}")
            count += 1

    print(f"\nConversion complete: {count} succeeded, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
