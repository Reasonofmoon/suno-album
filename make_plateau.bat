@echo off
chcp 65001
echo ========================================================
echo       🌙 REASON MOON: PLATEAU GENERATOR SYSTEM
echo ========================================================
echo.

:: 1. Generate Music
echo [Step 1/3] Generating New Track...
python src/generate_track.py
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Generation Failed. Exiting.
    pause
    exit /b
)

:: 2. Read Task ID
set /p TASK_ID=<latest_task_id.txt
echo ✅ Generated Task ID: %TASK_ID%

:: 3. Publish to Player
echo.
echo [Step 2/3] Downloading Assets & Updating Player...
python src/publish.py %TASK_ID%
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Publishing Failed.
    pause
    exit /b
)

:: 4. Deploy to GitHub
echo.
echo [Step 3/3] Deploying to GitHub...
git add .
git commit -m "New Plateau Added: %TASK_ID%"
git push origin main

echo.
echo 🎉 SYSTEM COMPLETED. The new track is live on GitHub.
pause
