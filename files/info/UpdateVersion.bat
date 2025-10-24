@echo off
title MAP - UpdateVersion
set path=%cd:map_tool\files\info=Python system 3.12.2\python.exe%
cls
"%path%" "UpdateVersion.py"
pause