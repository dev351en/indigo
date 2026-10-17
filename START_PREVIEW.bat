@echo off
title The University of Chicago - Production Replica & Portal
echo =======================================================================
echo   The University of Chicago - Production Replica & Applicant Portal
echo =======================================================================
echo.
where node >nul 2>nul
if %ERRORLEVEL% equ 0 (
  echo [Engine] Node.js runtime detected. Starting full Express server with Payment API...
  echo [URL] Opening http://localhost:3000 in your browser...
  start "" "http://localhost:3000"
  node "%~dp0server.js"
) else (
  echo [Engine] Node.js not found. Falling back to Python HTTP server...
  echo [URL] Opening http://localhost:3000 in your browser...
  start "" "http://localhost:3000"
  py -m http.server 3000 --directory "%~dp0site_1to1"
)
pause
