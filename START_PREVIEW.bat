@echo off
title The University of Chicago - 1:1 Live Replica
echo ========================================================
echo   Launching The University of Chicago 1:1 Replica Server
echo ========================================================
echo Starting local preview server on http://localhost:3000...
start "" "http://localhost:3000"
py -m http.server 3000 --directory "%~dp0site_1to1"
pause
