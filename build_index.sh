#!/bin/bash
# Wrapper for scripts/build_index.py; all arguments are passed through.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Use the first interpreter that actually runs Python 3 (skips the Windows Store stub).
for candidate in python3 python; do
    if "$candidate" -c 'import sys; sys.exit(sys.version_info[0] < 3)' >/dev/null 2>&1; then
        exec "$candidate" "$SCRIPT_DIR/scripts/build_index.py" "$@"
    fi
done
echo "Error: Python 3 not found" >&2
exit 1
