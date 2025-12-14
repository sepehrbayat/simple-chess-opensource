# دستورات نهایی برای آپلود روی GitHub

## ⚠️ مهم: قبل از اجرای دستورات

1. **ابتدا repository را در GitHub ایجاد کنید:**
   - به https://github.com/new بروید
   - نام repository: `simple-chess-opensource`
   - آن را **Public** انتخاب کنید
   - **توجه:** گزینه "Initialize with README" را **خالی** بگذارید
   - روی "Create repository" کلیک کنید

## روش 1: استفاده از اسکریپت PowerShell (پیشنهادی)

```powershell
.\upload_to_github.ps1 -Username "YOUR_GITHUB_USERNAME"
```

**مثال:**
```powershell
.\upload_to_github.ps1 -Username "sepehrbayat"
```

## روش 2: دستورات دستی

```powershell
# 1. اضافه کردن remote (نام کاربری خود را جایگزین کنید)
git remote add origin https://github.com/YOUR_USERNAME/simple-chess-opensource.git

# 2. بررسی remote
git remote -v

# 3. Push کردن به GitHub
git push -u origin main
```

**مثال:**
```powershell
git remote add origin https://github.com/sepehrbayat/simple-chess-opensource.git
git push -u origin main
```

## اگر remote قبلاً اضافه شده است

اگر خطای "remote origin already exists" دریافت کردید:

```powershell
# حذف remote قدیمی
git remote remove origin

# اضافه کردن remote جدید
git remote add origin https://github.com/YOUR_USERNAME/simple-chess-opensource.git

# Push
git push -u origin main
```

## بعد از Push موفق

1. به صفحه repository در GitHub بروید
2. توضیحات را از فایل `.github/REPOSITORY_INFO.md` کپی کنید
3. Topics/Tags را اضافه کنید (لیست در `GITHUB_SETUP.md`)
4. README.md را ویرایش کنید و `YOUR_USERNAME` را با نام کاربری خود جایگزین کنید
5. سپس دوباره commit و push کنید:

```powershell
git add README.md
git commit -m "Update README with GitHub username"
git push
```

---

**موفق باشید! 🚀**
