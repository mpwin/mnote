@echo off

if "%~1"=="" (
    set "mpath=%USERPROFILE%\Mnotes"
) else (
    set "mpath=%~1"
)

:: Remove trailing backslash if present
if "%mpath:~-1%"=="\" set "mpath=%mpath:~0,-1%"

for /f "delims=" %%a in ('
    py %~dp0mnote_picker.py "%mpath%" ^
') do (
    set "mnote=%%a"
)

py %~dp0mnote_reader.py "%mnote%"
