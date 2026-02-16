# Troubleshooting Guide

This guide helps resolve common issues that may occur while using the Complete Personal Productivity Suite.

---

## 1️⃣ Application Does Not Start

### Issue:
Running:
python main.py

produces an error.

### Solution:
- Ensure Python 3.10+ is installed
- Verify Python is added to PATH
- Run:
python --version


- Make sure you are inside the project directory before running the command.

---

## 2️⃣ Module Import Error

### Issue:
Error like:
ModuleNotFoundError: No module named 'module_name'

### Solution:
- Confirm you are inside the root project folder:
personal-productivity-suite/

- Ensure the `modules/` folder exists.
- Do not rename module files.

---

## 3️⃣ Notes Not Saving

### Issue:
Notes disappear after restarting application.

### Solution:
- Ensure `data/notes.json` exists.
- If missing, create file and add:
[]

- Confirm the application has write permissions.

---

## 4️⃣ File Organizer Path Error

### Issue:
Error message:
Dictionary do not exist.


### Solution:
- Provide full directory path.
- Do not include quotation marks.
- Example (Correct):
C:\Users\Username\Desktop\test_folder

---

## 5️⃣ Backup Creation Error

### Issue:
Backup fails with path-related errors.

### Solution:
- Ensure `data/backups/` folder exists.
- Confirm `data/notes.json` exists.
- Do not delete the `data/` directory structure.

---

## 6️⃣ Restore Not Working

### Issue:
Restore does not update notes.

### Solution:
- Ensure at least one backup file exists inside:
data/backups/
- Restart application after restore to reload data.

---

## 7️⃣ Invalid Input Errors

### Issue:
Entering letters instead of numbers causes errors.

### Solution:
- Enter numeric values where required.
- Follow menu prompts carefully.
- Application includes input validation and error handling.

---

## 8️⃣ Permission Errors (Windows)

### Issue:
File access denied errors.

### Solution:
- Do not run project from system-protected folders.
- Ensure project folder is not read-only.
- Avoid running from restricted directories.

---

## 9️⃣ Git Push Errors

### Issue:
Push rejected due to remote changes.

### Solution:
Run:
git pull origin main --rebase
git push

Ensure working directory is clean before pushing.

---

# ✅ If Problems Persist

- Restart terminal
- Restart VS Code
- Verify folder structure matches documentation
- Ensure no files were accidentally renamed or deleted

