FOR %%f IN (notebooks\*.*) DO jupyter nbconvert --output-dir=./html --to html %%f
