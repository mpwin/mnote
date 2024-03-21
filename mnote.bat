@echo off

if "%~1"=="" (
    set "mpath=%USERPROFILE%\Mnotes"
) else (
    set "mpath=%~1"
)

:: Remove trailing backslash if present
if "%mpath:~-1%"=="\" set "mpath=%mpath:~0,-1%"

for /f "delims=" %%a in ('
    py %~dp0picker.py "%mpath%" ^
') do (
    set "mnote=%%a"
)

setlocal
set "PYTHONPATH=%~dp0;%PYTHONPATH%"
py -m reader "%mnote%"
endlocal
