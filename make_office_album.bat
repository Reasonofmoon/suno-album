@echo off
chcp 65001
echo ========================================================
echo       🌙 REASON MOON: OFFICE SERENDIPITY PRODUCER
echo ========================================================
echo.
echo This script will:
echo 1. Read 10 pre-defined tracks from src/album2_data.json
echo 2. Call Suno AI API to generate them (Cost: ~100 credits)
echo 3. Automatically download and add them to your player.
echo.
echo ⚠️  MAKE SURE 'SUNO_COOKIE' IS SET IN YOUR .ENV FILE!
echo.
pause

python src/produce_office_serendipity.py

echo.
echo Done.
pause
