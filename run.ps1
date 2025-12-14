# PowerShell script to run the Chess game
# This script activates the virtual environment and runs the game

Write-Host "Starting Chess Game..." -ForegroundColor Cyan

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "Error: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run setup.ps1 first to set up the project." -ForegroundColor Yellow
    exit 1
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Check if activation was successful
if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Virtual environment activation may have failed." -ForegroundColor Yellow
    Write-Host "Trying to run anyway..." -ForegroundColor Yellow
}

# Run the game
Write-Host "Launching game..." -ForegroundColor Green
python main.py
