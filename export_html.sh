#!/bin/bash
set -e

# Check if notebooks directory exists
if [ ! -d "notebooks" ]; then
    echo "Error: notebooks directory not found"
    exit 1
fi

# Check if html directory exists, create if needed
if [ ! -d "html" ]; then
    echo "Creating html directory..."
    mkdir -p html
fi

# Check if jupyter is available
if ! command -v jupyter &> /dev/null; then
    echo "Error: jupyter not found. Please install jupyter: pip install jupyter nbconvert"
    exit 1
fi

echo "Converting notebooks to HTML..."
count=0
failed=0

for filename in ./notebooks/*.ipynb; do
    # Check if glob matched any files
    [ -e "$filename" ] || { echo "No .ipynb files found in notebooks directory"; exit 1; }
    
    echo "Converting $(basename "$filename")..."
    if jupyter nbconvert --output-dir=./html --to html "$filename"; then
        echo "  [OK] $(basename "$filename")"
        ((count++))
    else
        echo "  [FAILED] $(basename "$filename")"
        ((failed++))
    fi
done

echo ""
echo "Conversion complete: $count succeeded, $failed failed"
[ $failed -eq 0 ] || exit 1

