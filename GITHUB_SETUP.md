# راهنمای آپلود پروژه روی GitHub

## مراحل آپلود

### 1. ایجاد Repository در GitHub

1. به [GitHub](https://github.com) بروید و وارد حساب کاربری خود شوید
2. روی دکمه **"+"** در گوشه بالا راست کلیک کنید
3. **"New repository"** را انتخاب کنید
4. نام repository را وارد کنید: **`simple-chess-opensource`**
5. توضیحات را وارد کنید (از فایل `.github/REPOSITORY_INFO.md` استفاده کنید)
6. Repository را **Public** انتخاب کنید
7. **توجه:** گزینه‌های "Initialize with README" را **خالی** بگذارید
8. روی **"Create repository"** کلیک کنید

### 2. اتصال Repository محلی به GitHub

بعد از ایجاد repository در GitHub، دستورات زیر را در PowerShell اجرا کنید:

```powershell
# اضافه کردن remote (نام کاربری خود را جایگزین کنید)
git remote add origin https://github.com/YOUR_USERNAME/simple-chess-opensource.git

# بررسی remote
git remote -v

# Push کردن به GitHub
git push -u origin main
```

### 3. تنظیمات Repository در GitHub

بعد از push، به صفحه repository بروید و تنظیمات زیر را انجام دهید:

#### توضیحات Repository

**Short Description (160 کاراکتر):**
```
A complete open-source chess game with AI opponent, move evaluation, and beautiful UI. Built with Python and Pygame.
```

**Full Description:**
```
A feature-rich, open-source chess game implementation built with Python and Pygame. This project demonstrates:

- Complete Chess Implementation: All standard chess rules including castling, en passant, and pawn promotion
- AI Opponent: Minimax algorithm with alpha-beta pruning for intelligent gameplay
- Move Evaluation: Real-time move quality scoring (0-100) based on material, position, and strategy
- Multiple Game Modes: Play against another player, against AI, or watch AI vs AI
- Beautiful UI: High-quality graphics with custom piece rendering and visual feedback
- Clean Architecture: Well-structured, object-oriented code perfect for learning and extending

Perfect for:
- Learning chess programming and game development
- Understanding AI algorithms (minimax, alpha-beta pruning)
- Studying Python and Pygame best practices
- Educational purposes and portfolio projects
```

#### Topics/Tags

در بخش "Topics" این کلمات کلیدی را اضافه کنید:

```
chess
python
pygame
game-development
minimax
alpha-beta-pruning
ai
artificial-intelligence
open-source
educational
game-engine
board-game
chess-engine
python-game
pygame-tutorial
```

#### تنظیمات Repository

1. به **Settings** > **General** بروید
2. در بخش **Features**:
   - ✅ Issues (فعال)
   - ✅ Discussions (اختیاری)
   - ✅ Projects (اختیاری)
   - ❌ Wiki (غیرفعال - از README استفاده می‌کنیم)

3. در بخش **Merge button**:
   - ✅ Allow merge commits
   - ✅ Allow squash merging
   - ✅ Allow rebase merging

#### Social Preview

برای نمایش بهتر در شبکه‌های اجتماعی:
1. یک screenshot از بازی بگیرید
2. آن را در پوشه repository آپلود کنید
3. در تنظیمات repository، آن را به عنوان social preview تنظیم کنید

### 4. به‌روزرسانی README

بعد از push، در فایل `README.md` جایگزین کنید:
- `YOUR_USERNAME` را با نام کاربری GitHub خود
- `@yourusername` را با نام کاربری GitHub خود

سپس دوباره commit و push کنید:

```powershell
git add README.md
git commit -m "Update README with GitHub username"
git push
```

### 5. ایجاد Release (اختیاری)

برای ایجاد اولین release:

1. به بخش **Releases** بروید
2. روی **"Create a new release"** کلیک کنید
3. Tag version: `v1.0.0`
4. Release title: `Simple Chess v1.0.0 - Initial Release`
5. Description را از `CHANGELOG.md` کپی کنید
6. روی **"Publish release"** کلیک کنید

## دستورات مفید

```powershell
# بررسی وضعیت
git status

# مشاهده commit ها
git log --oneline

# مشاهده remote ها
git remote -v

# Pull کردن تغییرات (اگر repository را در GitHub ویرایش کردید)
git pull origin main

# Force push (فقط در صورت نیاز و با احتیاط)
git push -f origin main
```

## نکات مهم

- ✅ همیشه قبل از push، `git status` را بررسی کنید
- ✅ از commit message های واضح و توصیفی استفاده کنید
- ✅ فایل‌های حساس (مثل API keys) را commit نکنید
- ✅ `.gitignore` را بررسی کنید تا فایل‌های غیرضروری commit نشوند

## مشکل دارید؟

اگر مشکلی پیش آمد:
1. بررسی کنید که repository در GitHub ایجاد شده باشد
2. URL remote را بررسی کنید: `git remote -v`
3. اطمینان حاصل کنید که به اینترنت متصل هستید
4. بررسی کنید که نام کاربری و رمز عبور GitHub صحیح باشد

---

**موفق باشید! 🚀**
