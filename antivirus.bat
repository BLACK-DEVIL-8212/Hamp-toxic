color cb
title Antivirus
cls
echo ===============
echo [ Batch-Scanner]
echo ===============
echo If There is no message ,You are protected.
set /p a=Enter a batch file to scan:
for /f %%x in (
‘findstr /i /m “virus r.i.p byebye ” %a%.bat’
) do (
if /i %%x equ %a%.bat (
for /f %%z in (
‘findstr /i /b /m “tskill del copy shutdown ipconfig ren reg” %a%.bat’
) do (
if /i %%z equ %a%.bat (
cls
echo Virus Detected!!
del %a%.bat
echo %a%.bat was deleted….
pause >nul
)
)
)
) 
pause >nul