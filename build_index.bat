@echo off
REM Wrapper for scripts\build_index.py; all arguments are passed through.
python "%~dp0scripts\build_index.py" %*
exit /b %errorlevel%
