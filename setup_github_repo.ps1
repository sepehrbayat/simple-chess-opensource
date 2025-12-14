# Script to configure GitHub repository settings
# Requires GitHub Personal Access Token with repo permissions

param(
    [Parameter(Mandatory=$true)]
    [string]$Token,
    
    [Parameter(Mandatory=$false)]
    [string]$Owner = "sepehrbayat",
    
    [Parameter(Mandatory=$false)]
    [string]$Repo = "simple-chess-opensource"
)

$ErrorActionPreference = "Stop"

Write-Host "🚀 Configuring GitHub repository settings..." -ForegroundColor Cyan
Write-Host ""

$baseUrl = "https://api.github.com/repos/$Owner/$Repo"
$headers = @{
    "Authorization" = "token $Token"
    "Accept" = "application/vnd.github.v3+json"
    "User-Agent" = "PowerShell"
}

# 1. Update repository description
Write-Host "📝 Setting repository description..." -ForegroundColor Yellow
$description = "A complete open-source chess game with AI opponent, move evaluation, and beautiful UI. Built with Python and Pygame."
$body = @{
    description = $description
    homepage = ""
    private = $false
    has_issues = $true
    has_projects = $true
    has_wiki = $false
    has_discussions = $true
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri $baseUrl -Method PATCH -Headers $headers -Body $body -ContentType "application/json"
    Write-Host "✅ Repository description updated!" -ForegroundColor Green
} catch {
    Write-Host "❌ Error updating description: $_" -ForegroundColor Red
    Write-Host "Response: $($_.Exception.Response)" -ForegroundColor Red
}

# 2. Add topics
Write-Host ""
Write-Host "🏷️  Adding topics..." -ForegroundColor Yellow
$topics = @(
    "chess",
    "python",
    "pygame",
    "game-development",
    "minimax",
    "alpha-beta-pruning",
    "ai",
    "artificial-intelligence",
    "open-source",
    "educational",
    "game-engine",
    "board-game",
    "chess-engine",
    "python-game",
    "pygame-tutorial"
)

$topicsBody = @{
    names = $topics
} | ConvertTo-Json

try {
    $topicsUrl = "$baseUrl/topics"
    $topicsHeaders = @{
        "Authorization" = "token $Token"
        "Accept" = "application/vnd.github.mercy-preview+json"
        "User-Agent" = "PowerShell"
    }
    $response = Invoke-RestMethod -Uri $topicsUrl -Method PUT -Headers $topicsHeaders -Body $topicsBody -ContentType "application/json"
    Write-Host "✅ Topics added successfully!" -ForegroundColor Green
    Write-Host "   Topics: $($topics -join ', ')" -ForegroundColor Gray
} catch {
    Write-Host "❌ Error adding topics: $_" -ForegroundColor Red
    if ($_.Exception.Response) {
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        $responseBody = $reader.ReadToEnd()
        Write-Host "Response: $responseBody" -ForegroundColor Red
    }
}

# 3. Create release
Write-Host ""
Write-Host "📦 Creating release v1.0.0..." -ForegroundColor Yellow

$releaseBody = @{
    tag_name = "v1.0.0"
    name = "Simple Chess v1.0.0 - Initial Release"
    body = @"
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
git clone https://github.com/$Owner/$Repo.git
cd $Repo
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
    draft = $false
    prerelease = $false
} | ConvertTo-Json

try {
    $releaseUrl = "$baseUrl/releases"
    $response = Invoke-RestMethod -Uri $releaseUrl -Method POST -Headers $headers -Body $releaseBody -ContentType "application/json"
    Write-Host "✅ Release v1.0.0 created successfully!" -ForegroundColor Green
    Write-Host "   Release URL: $($response.html_url)" -ForegroundColor Gray
} catch {
    if ($_.Exception.Response.StatusCode -eq 422) {
        Write-Host "⚠️  Release v1.0.0 might already exist. Skipping..." -ForegroundColor Yellow
    } else {
        Write-Host "❌ Error creating release: $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "✅ Repository configuration completed!" -ForegroundColor Green
Write-Host "🌐 Repository: https://github.com/$Owner/$Repo" -ForegroundColor Cyan
Write-Host ""
