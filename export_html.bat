@echo off
REM Wrapper for scripts\export_html.py; all arguments are passed through.
python "%~dp0scripts\export_html.py" %*
exit /b %errorlevel%
