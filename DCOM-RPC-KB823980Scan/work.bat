@echo off
:start
echo scanning range
KB823980Scan.exe /t:10000 /l:log /i:wss.txt
proc
del *.log
gen_report
sleeep
goto start