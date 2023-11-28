@echo off

setlocal EnableDelayedExpansion
set "mnotesDir=%USERPROFILE%\Mnotes"
set /a count=0

for /d %%D in ("%mnotesDir%\*.mnote") do (
    set /a count+=1
    set "dir[!count!]=%%D"
)

if %count% == 0 (
    echo No .mnotes found in %mnotesDir%.
    exit /b
)

set /a index=(%random% %% %count%) + 1
set "mnote=!dir[%index%]!"

py %~dp0mnote.py %mnote%
