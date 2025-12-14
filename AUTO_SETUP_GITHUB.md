# راهنمای کامل تنظیم خودکار GitHub Repository

## مرحله 1: Login به GitHub CLI

دستور زیر را در PowerShell اجرا کنید:

```powershell
gh auth login
```

سپس:
1. **GitHub.com** را انتخاب کنید (Enter)
2. **HTTPS** را انتخاب کنید (Enter)
3. **Yes** برای Git credential helper (Y)
4. **Login with a web browser** را انتخاب کنید (Enter)
5. کد نمایش داده شده را کپی کنید
6. در مرورگر که باز می‌شود، کد را وارد کنید
7. روی **Authorize** کلیک کنید

## مرحله 2: اجرای اسکریپت تنظیمات

بعد از login موفق، این دستور را اجرا کنید:

```powershell
.\configure_github_repo.ps1
```

این اسکریپت به صورت خودکار:
- ✅ توضیحات Repository را تنظیم می‌کند
- ✅ Topics/Tags را اضافه می‌کند
- ✅ Release v1.0.0 را ایجاد می‌کند

## روش جایگزین: دستورات دستی

اگر ترجیح می‌دهید دستورات را خودتان اجرا کنید:

```powershell
# تنظیم description
gh repo edit sepehrbayat/simple-chess-opensource --description "A complete open-source chess game with AI opponent, move evaluation, and beautiful UI. Built with Python and Pygame."

# اضافه کردن topics
gh repo edit sepehrbayat/simple-chess-opensource --add-topic chess,python,pygame,game-development,minimax,alpha-beta-pruning,ai,artificial-intelligence,open-source,educational,game-engine,board-game,chess-engine,python-game,pygame-tutorial

# ایجاد release
gh release create v1.0.0 --title "Simple Chess v1.0.0 - Initial Release" --notes "Initial release with complete chess implementation, AI opponent, and move evaluation system." --repo sepehrbayat/simple-chess-opensource
```

---

**نکته:** اگر مشکلی پیش آمد، می‌توانید تنظیمات را به صورت دستی از صفحه GitHub repository انجام دهید.
