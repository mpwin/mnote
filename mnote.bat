@echo off

set "mpath=%1"

if "%mpath%"=="" set "mpath=%USERPROFILE%\Mnotes"

for /f "delims=" %%a in ('py %~dp0mnote_picker.py %mpath%') do set "mnote=%%a"

py %~dp0mnote_reader.py "%mnote%"
