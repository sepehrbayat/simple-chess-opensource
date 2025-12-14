# Script to upload project to GitHub
# Usage: .\upload_to_github.ps1 -Username "YOUR_GITHUB_USERNAME"

param(
    [Parameter(Mandatory=$true)]
    [string]$Username
)

Write-Host "🚀 Preparing to upload Simple Chess to GitHub..." -ForegroundColor Cyan
Write-Host ""

# Check if git is initialized
if (-not (Test-Path .git)) {
    Write-Host "❌ Git repository not initialized!" -ForegroundColor Red
    exit 1
}

# Check if remote already exists
$remoteExists = git remote get-url origin 2>$null
if ($remoteExists) {
    Write-Host "⚠️  Remote 'origin' already exists: $remoteExists" -ForegroundColor Yellow
    $response = Read-Host "Do you want to update it? (y/n)"
    if ($response -eq "y" -or $response -eq "Y") {
        git remote set-url origin "https://github.com/$Username/simple-chess-opensource.git"
        Write-Host "✅ Remote updated!" -ForegroundColor Green
    } else {
        Write-Host "ℹ️  Using existing remote" -ForegroundColor Blue
    }
} else {
    git remote add origin "https://github.com/$Username/simple-chess-opensource.git"
    Write-Host "✅ Remote 'origin' added!" -ForegroundColor Green
}

Write-Host ""
Write-Host "📋 Repository URL: https://github.com/$Username/simple-chess-opensource.git" -ForegroundColor Cyan
Write-Host ""

# Check current branch
$currentBranch = git branch --show-current
Write-Host "📍 Current branch: $currentBranch" -ForegroundColor Blue

# Check if there are uncommitted changes
$status = git status --porcelain
if ($status) {
    Write-Host "⚠️  You have uncommitted changes!" -ForegroundColor Yellow
    Write-Host "Uncommitted files:" -ForegroundColor Yellow
    git status --short
    Write-Host ""
    $response = Read-Host "Do you want to commit them now? (y/n)"
    if ($response -eq "y" -or $response -eq "Y") {
        $commitMessage = Read-Host "Enter commit message (or press Enter for default)"
        if ([string]::IsNullOrWhiteSpace($commitMessage)) {
            $commitMessage = "Update project files"
        }
        git add .
        git commit -m $commitMessage
        Write-Host "✅ Changes committed!" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "🔄 Pushing to GitHub..." -ForegroundColor Cyan
Write-Host ""

# Push to GitHub
try {
    git push -u origin main
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ Successfully uploaded to GitHub!" -ForegroundColor Green
        Write-Host ""
        Write-Host "🌐 Repository URL: https://github.com/$Username/simple-chess-opensource" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "📝 Next steps:" -ForegroundColor Yellow
        Write-Host "   1. Go to your repository on GitHub" -ForegroundColor White
        Write-Host "   2. Add repository description (see .github/REPOSITORY_INFO.md)" -ForegroundColor White
        Write-Host "   3. Add topics/tags (see GITHUB_SETUP.md)" -ForegroundColor White
        Write-Host "   4. Update README.md with your actual username" -ForegroundColor White
        Write-Host ""
    } else {
        Write-Host "❌ Push failed! Please check the error above." -ForegroundColor Red
        Write-Host ""
        Write-Host "💡 Common issues:" -ForegroundColor Yellow
        Write-Host "   - Repository doesn't exist on GitHub (create it first)" -ForegroundColor White
        Write-Host "   - Authentication failed (check your GitHub credentials)" -ForegroundColor White
        Write-Host "   - Network issues" -ForegroundColor White
    }
} catch {
    Write-Host "❌ Error: $_" -ForegroundColor Red
}

Write-Host ""
