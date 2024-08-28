@echo off

if "%~1"=="" (
    set "mpath=%HOME%\Mnotes"
) else (
    set "mpath=%~1"
)

:: Remove trailing backslash if present
if "%mpath:~-1%"=="\" set "mpath=%mpath:~0,-1%"

py "%HOME%\Scripts\mnote" "%mpath%"
