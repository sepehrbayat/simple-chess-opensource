# راهنمای تنظیم GitHub Repository با استفاده از اسکریپت

## مرحله 1: ایجاد Personal Access Token

برای استفاده از اسکریپت، نیاز به یک GitHub Personal Access Token دارید:

1. به https://github.com/settings/tokens بروید
2. روی **"Generate new token"** > **"Generate new token (classic)"** کلیک کنید
3. یک نام برای token انتخاب کنید (مثلاً: "Simple Chess Setup")
4. مدت اعتبار را انتخاب کنید (مثلاً: 90 days)
5. دسترسی‌های زیر را فعال کنید:
   - ✅ `repo` (Full control of private repositories)
     - ✅ `repo:status`
     - ✅ `repo_deployment`
     - ✅ `public_repo`
     - ✅ `repo:invite`
     - ✅ `security_events`
6. روی **"Generate token"** کلیک کنید
7. **Token را کپی کنید** (فقط یک بار نمایش داده می‌شود!)

## مرحله 2: اجرای اسکریپت

بعد از دریافت token، اسکریپت را اجرا کنید:

```powershell
.\setup_github_repo.ps1 -Token "YOUR_TOKEN_HERE"
```

**مثال:**
```powershell
.\setup_github_repo.ps1 -Token "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## کارهایی که اسکریپت انجام می‌دهد

✅ تنظیم توضیحات Repository  
✅ اضافه کردن Topics/Tags  
✅ ایجاد Release v1.0.0  

## روش جایگزین: استفاده از GitHub CLI

اگر GitHub CLI نصب دارید:

```powershell
# نصب GitHub CLI (اگر نصب نیست)
winget install --id GitHub.cli

# Login
gh auth login

# تنظیم description
gh repo edit sepehrbayat/simple-chess-opensource --description "A complete open-source chess game with AI opponent, move evaluation, and beautiful UI. Built with Python and Pygame."

# اضافه کردن topics
gh repo edit sepehrbayat/simple-chess-opensource --add-topic chess,python,pygame,game-development,minimax,alpha-beta-pruning,ai,artificial-intelligence,open-source,educational,game-engine,board-game,chess-engine,python-game,pygame-tutorial

# ایجاد release
gh release create v1.0.0 --title "Simple Chess v1.0.0 - Initial Release" --notes "Initial release with complete chess implementation, AI opponent, and move evaluation system."
```

---

**نکته امنیتی:** هرگز token خود را در کد یا commit نکنید!
