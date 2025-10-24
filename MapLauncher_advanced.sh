#!/bin/bash
@echo off
mode con:cols=40 lines=10
set path=%cd:map_tool=Python system 3.12.2\python.exe%
set CMDOW="C:\Users\natha\AppData\Local\Temp\cmdow-master\bin\Release\cmdow.exe"
title MAP - Launcher (advanced)
%CMDOW% "MAP - Launcher (advanced)" /ena /res
cls
"%path%" "map_advanced.py"
%CMDOW% "MAP - Launcher (advanced)" /cls
