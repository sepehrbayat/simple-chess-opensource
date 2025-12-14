@echo off
REM Batch script to run the Chess game
echo Starting Chess Game...

REM Check if virtual environment exists
if not exist venv (
    echo [ERROR] Virtual environment not found!
    echo Please run setup.bat first to set up the project.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Run the game
echo Launching game...
python main.py

pause
