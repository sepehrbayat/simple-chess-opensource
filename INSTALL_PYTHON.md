# راهنمای نصب Python برای پروژه Chess

## روش 1: نصب از سایت رسمی Python (توصیه می‌شود)

### مراحل نصب:

1. **دانلود Python:**
   - به آدرس زیر بروید: https://www.python.org/downloads/
   - آخرین نسخه Python 3.11 یا 3.12 را دانلود کنید

2. **نصب Python:**
   - فایل دانلود شده را اجرا کنید
   - **مهم:** حتماً گزینه **"Add Python to PATH"** را تیک بزنید ✓
   - روی "Install Now" کلیک کنید
   - منتظر بمانید تا نصب کامل شود

3. **بررسی نصب:**
   - PowerShell یا Command Prompt را باز کنید
   - دستور زیر را اجرا کنید:
     ```bash
     python --version
     ```
   - باید نسخه Python نمایش داده شود (مثلاً: Python 3.11.5)

4. **راه‌اندازی پروژه:**
   - در پوشه پروژه، یکی از دستورات زیر را اجرا کنید:
     - PowerShell: `.\setup.ps1`
     - Command Prompt: `setup.bat`

---

## روش 2: نصب از Microsoft Store

1. **باز کردن Microsoft Store:**
   - Windows Store را باز کنید
   - در جستجو "Python 3.11" یا "Python 3.12" را تایپ کنید

2. **نصب:**
   - روی "Get" یا "Install" کلیک کنید
   - منتظر بمانید تا نصب کامل شود

3. **بررسی نصب:**
   - PowerShell یا Command Prompt را باز کنید
   - دستور زیر را اجرا کنید:
     ```bash
     python --version
     ```

4. **راه‌اندازی پروژه:**
   - در پوشه پروژه، یکی از دستورات زیر را اجرا کنید:
     - PowerShell: `.\setup.ps1`
     - Command Prompt: `setup.bat`

---

## اگر Python نصب است اما در PATH نیست

اگر Python نصب است اما دستور `python` کار نمی‌کند:

1. **مسیر Python را پیدا کنید:**
   - معمولاً در `C:\Users\YourName\AppData\Local\Programs\Python\Python3XX\`
   - یا در `C:\Python3XX\`

2. **اضافه کردن به PATH:**
   - Windows + R را بزنید
   - `sysdm.cpl` را تایپ کنید و Enter بزنید
   - تب "Advanced" را باز کنید
   - روی "Environment Variables" کلیک کنید
   - در بخش "System variables"، متغیر "Path" را پیدا کنید
   - روی "Edit" کلیک کنید
   - "New" را بزنید و مسیر Python را اضافه کنید (مثلاً: `C:\Python311\`)
   - همچنین مسیر Scripts را اضافه کنید (مثلاً: `C:\Python311\Scripts\`)
   - OK را بزنید
   - PowerShell/Command Prompt را بسته و دوباره باز کنید

---

## استفاده از Virtual Environment (محیط مجازی)

پس از نصب Python، پروژه از یک محیط مجازی استفاده می‌کند که Python و کتابخانه‌ها را برای این پروژه جدا نگه می‌دارد.

### فعال‌سازی محیط مجازی:

**PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

### غیرفعال‌سازی:
```bash
deactivate
```

---

## اجرای بازی

پس از راه‌اندازی:

1. محیط مجازی را فعال کنید
2. دستور زیر را اجرا کنید:
   ```bash
   python main.py
   ```

---

## مشکلات رایج

### مشکل: "python is not recognized"
**راه حل:** Python به PATH اضافه نشده است. مراحل بالا را دنبال کنید.

### مشکل: "Execution Policy" در PowerShell
**راه حل:** دستور زیر را اجرا کنید:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### مشکل: "pip is not recognized"
**راه حل:** مطمئن شوید که Python به درستی نصب شده و Scripts به PATH اضافه شده است.

---

## نیازمندی‌های پروژه

- Python 3.7 یا بالاتر
- Pygame 2.5.0 یا بالاتر
- PyInstaller 6.0.0 یا بالاتر (برای ساخت فایل اجرایی)

همه این موارد به صورت خودکار با اجرای `setup.ps1` یا `setup.bat` نصب می‌شوند.
