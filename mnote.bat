@echo off

set "mnotes=%USERPROFILE%\Mnotes"
for /f "delims=" %%a in ('py mnote_picker.py %mnotes%') do set "mnote=%%a"

py %~dp0mnote_reader.py "%mnote%"
