#!/bin/sh

for filename in ./notebooks/*.ipynb; do
    jupyter nbconvert --output-dir=./html --to html "$filename"
    # echo "$filename"
done

