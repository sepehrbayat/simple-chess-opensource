@echo off
REM Batch script to set up Python environment for Chess project
echo === Chess Project Setup ===
echo.

REM Check if Python is installed
echo Checking for Python installation...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Python is installed
    python --version
) else (
    echo [ERROR] Python is not installed
    echo.
    echo Please install Python 3.7 or higher:
    echo 1. Visit: https://www.python.org/downloads/
    echo 2. Download Python 3.7+ for Windows
    echo 3. During installation, CHECK 'Add Python to PATH'
    echo 4. After installation, restart Command Prompt and run this script again
    echo.
    pause
    exit /b 1
)

echo.
echo Setting up virtual environment...
if exist venv (
    echo [OK] Virtual environment already exists
) else (
    python -m venv venv
    if %errorlevel% equ 0 (
        echo [OK] Virtual environment created successfully
    ) else (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing project dependencies...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo === Setup Complete! ===
    echo.
    echo To run the game:
    echo    python main.py
    echo.
    echo Note: Make sure to activate the virtual environment first:
    echo    venv\Scripts\activate.bat
) else (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

pause
