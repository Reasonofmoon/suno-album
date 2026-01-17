@echo off
cd /d "%~dp0"
echo ========================================================
echo  Reason Moon Album 3: Gumaetan Market Production Batch
echo ========================================================
echo.
echo  This script will:
echo  1. Read track data from src/album3_data.json
echo  2. Call Suno API to generate tracks
echo  3. Wait for generation
echo  4. Download and update discography.json
echo  5. Push to GitHub
echo.
pause

python src/produce_gumaetan_market.py

pause
