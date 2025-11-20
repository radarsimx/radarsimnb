@echo off
setlocal enabledelayedexpansion

REM Check if notebooks directory exists
if not exist "notebooks\" (
    echo Error: notebooks directory not found
    exit /b 1
)

REM Check if html directory exists, create if needed
if not exist "html\" (
    echo Creating html directory...
    mkdir html
)

REM Check if jupyter is available
where jupyter >nul 2>&1
if errorlevel 1 (
    echo Error: jupyter not found. Please install jupyter: pip install jupyter nbconvert
    exit /b 1
)

echo Converting notebooks to HTML...
set count=0
set failed=0

FOR %%f IN (notebooks\*.ipynb) DO (
    echo Converting %%~nxf...
    jupyter nbconvert --output-dir=./html --to html "%%f"
    if errorlevel 1 (
        echo   [FAILED] %%~nxf
        set /a failed+=1
    ) else (
        echo   [OK] %%~nxf
        set /a count+=1
    )
)

echo.
echo Conversion complete: !count! succeeded, !failed! failed
if !failed! gtr 0 exit /b 1
