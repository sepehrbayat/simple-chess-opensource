# Script to configure GitHub repository settings using GitHub CLI
# Make sure you're logged in: gh auth login

Write-Host "🚀 Configuring GitHub repository settings..." -ForegroundColor Cyan
Write-Host ""

$repo = "sepehrbayat/simple-chess-opensource"

# Refresh PATH to include GitHub CLI
$env:PATH = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Check if logged in
Write-Host "🔐 Checking authentication..." -ForegroundColor Yellow
$authStatus = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Not logged in to GitHub CLI!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please run: gh auth login" -ForegroundColor Yellow
    Write-Host "Then run this script again." -ForegroundColor Yellow
    exit 1
}
Write-Host "✅ Authenticated!" -ForegroundColor Green
Write-Host ""

# 1. Update repository description
Write-Host "📝 Setting repository description..." -ForegroundColor Yellow
$description = "A complete open-source chess game with AI opponent, move evaluation, and beautiful UI. Built with Python and Pygame."
try {
    gh repo edit $repo --description $description
    Write-Host "✅ Repository description updated!" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Could not update description: $_" -ForegroundColor Yellow
}
Write-Host ""

# 2. Add topics
Write-Host "🏷️  Adding topics..." -ForegroundColor Yellow
$topics = "chess,python,pygame,game-development,minimax,alpha-beta-pruning,ai,artificial-intelligence,open-source,educational,game-engine,board-game,chess-engine,python-game,pygame-tutorial"
try {
    gh repo edit $repo --add-topic $topics
    Write-Host "✅ Topics added successfully!" -ForegroundColor Green
    Write-Host "   Topics: $topics" -ForegroundColor Gray
} catch {
    Write-Host "⚠️  Could not add topics: $_" -ForegroundColor Yellow
}
Write-Host ""

# 3. Create release
Write-Host "📦 Creating release v1.0.0..." -ForegroundColor Yellow
$releaseNotes = @"
## 🎉 Initial Release

### Features
- Complete chess game implementation with all standard rules
- AI opponent using minimax algorithm with alpha-beta pruning
- Move quality evaluation system (0-100 scoring)
- Multiple game modes (User vs User, User vs AI, AI vs AI)
- Beautiful UI with high-quality piece rendering
- Comprehensive documentation and setup scripts

### Installation
\`\`\`bash
git clone https://github.com/sepehrbayat/simple-chess-opensource.git
cd simple-chess-opensource
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
\`\`\`

### Requirements
- Python 3.7+
- Pygame 2.5.0+

Enjoy playing! 🎮♟️
"@

try {
    # Check if release already exists
    $existingRelease = gh release view v1.0.0 --repo $repo 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "⚠️  Release v1.0.0 already exists. Skipping..." -ForegroundColor Yellow
    } else {
        gh release create v1.0.0 --title "Simple Chess v1.0.0 - Initial Release" --notes $releaseNotes --repo $repo
        Write-Host "✅ Release v1.0.0 created successfully!" -ForegroundColor Green
    }
} catch {
    Write-Host "⚠️  Could not create release: $_" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "✅ Repository configuration completed!" -ForegroundColor Green
Write-Host "🌐 Repository: https://github.com/$repo" -ForegroundColor Cyan
Write-Host ""
