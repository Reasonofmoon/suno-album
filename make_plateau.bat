@echo off
chcp 65001
echo ========================================================
echo       🌙 REASON MOON: PLATEAU GENERATOR SYSTEM
echo ========================================================
echo.

:: 1. Multi-Agent Composition
echo [Step 1/4] Convening the Deleuzian Agents...
set /p TOPIC=Enter a Topic (or press Enter for 'Nomadology'): 
if "%TOPIC%"=="" set TOPIC=Nomadology
python src/compose.py "%TOPIC%"
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Composition Failed (Check API Keys).
    pause
    exit /b
)

:: 2. Generate Music
echo.
echo [Step 2/4] Generating New Track...
python src/generate_track.py
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Generation Failed. Exiting.
    pause
    exit /b
)

:: 3. Read Task ID
set /p TASK_ID=<latest_task_id.txt
echo ✅ Generated Task ID: %TASK_ID%

:: 4. Publish to Player
echo.
echo [Step 3/4] Downloading Assets & Updating Player...
python src/publish.py %TASK_ID%
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Publishing Failed.
    pause
    exit /b
)

:: 5. Deploy to GitHub
echo.
echo [Step 4/4] Deploying to GitHub...
git add .
git commit -m "New Plateau Added: %TASK_ID%"
git push origin main

echo.
echo 🎉 SYSTEM COMPLETED. The new track is live on GitHub.
pause
