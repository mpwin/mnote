@echo off

if "%~1"=="" (
    set "mpath=%HOME%\Mnotes"
) else (
    set "mpath=%~1"
)

py %HOME%\Scripts\mnote %mpath%
