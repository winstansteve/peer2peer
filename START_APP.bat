@echo off
echo ============================================
echo Secure File Transfer App - Quick Start
echo ============================================
echo.
echo Starting the application...
echo Your browser will open automatically.
echo.
echo IMPORTANT: Keep this window open while using the app!
echo.
echo To stop the app, close this window or press Ctrl+C
echo.
echo ============================================
echo.

cd /d "%~dp0"
streamlit run app.py

pause
