# PowerShell script to set up Python environment for Chess project
# This script will help you install Python and set up the project

Write-Host "=== Chess Project Setup ===" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "Checking for Python installation..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Python is already installed: $pythonVersion" -ForegroundColor Green
    
    # Check Python version
    $version = python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>&1
    $majorVersion = [int]($version -split '\.')[0]
    $minorVersion = [int]($version -split '\.')[1]
    
    if ($majorVersion -lt 3 -or ($majorVersion -eq 3 -and $minorVersion -lt 7)) {
        Write-Host "⚠ Warning: Python 3.7+ is required. Current version: $version" -ForegroundColor Yellow
        Write-Host "Please install Python 3.7 or higher from https://www.python.org/downloads/" -ForegroundColor Yellow
        exit 1
    }
} else {
    Write-Host "✗ Python is not installed" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python 3.7 or higher:" -ForegroundColor Yellow
    Write-Host "1. Visit: https://www.python.org/downloads/" -ForegroundColor Cyan
    Write-Host "2. Download Python 3.7+ for Windows" -ForegroundColor Cyan
    Write-Host "3. During installation, CHECK 'Add Python to PATH'" -ForegroundColor Cyan
    Write-Host "4. After installation, restart PowerShell and run this script again" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Or install via Microsoft Store:" -ForegroundColor Yellow
    Write-Host "   Open Microsoft Store and search for 'Python 3.11' or 'Python 3.12'" -ForegroundColor Cyan
    Write-Host ""
    
    # Try to open Python download page
    $response = Read-Host "Would you like to open the Python download page? (Y/N)"
    if ($response -eq 'Y' -or $response -eq 'y') {
        Start-Process "https://www.python.org/downloads/"
    }
    
    exit 1
}

Write-Host ""
Write-Host "Setting up virtual environment..." -ForegroundColor Yellow

# Create virtual environment
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
} else {
    python -m venv venv
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Virtual environment created successfully" -ForegroundColor Green
    } else {
        Write-Host "✗ Failed to create virtual environment" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "⚠ Note: If activation failed, you may need to run:" -ForegroundColor Yellow
    Write-Host "   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

Write-Host ""
Write-Host "Installing project dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "=== Setup Complete! ===" -ForegroundColor Green
    Write-Host ""
    Write-Host "To run the game:" -ForegroundColor Cyan
    Write-Host "   python main.py" -ForegroundColor White
    Write-Host ""
    Write-Host "Note: Make sure to activate the virtual environment first:" -ForegroundColor Yellow
    Write-Host "   .\venv\Scripts\Activate.ps1" -ForegroundColor White
} else {
    Write-Host "✗ Failed to install dependencies" -ForegroundColor Red
    exit 1
}
