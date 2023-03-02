@echo off
color 04

echo Executing this script will reset all of the data included in your MrTomatoS, MsLemonS save files, proceed?
set /p input=
if /i %input%==yes goto delSave
if /i %input%==no goto AppExit
if not /i %input%==yes,no exit

:delSave
cls
del %userprofile%\AppData\Roaming\MMFApplications /s /q
cls
echo Reset save file success, press any key to exit
pause
exit
:AppExit
cls
echo Prompt returned no, press any key to exit
pause
exit