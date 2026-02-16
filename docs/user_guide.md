# User Guide

## 📌 Introduction

The Complete Personal Productivity Suite is a command-line based application that integrates multiple productivity tools into a single system.

This guide explains how to use each feature of the application.

---

# 🏠 Main Menu

After running:
python main.py

You will see the main menu:
1.Calculator
2.Notes Manager
3.Timer & Stopwatch
4.File Organizer
5.Unit Converter
6.Backup & Restore
7.Exit

Enter the number corresponding to the tool you want to use.

---

# 📝 Notes Manager

### Features:
- View All Notes
- Add New Note
- Search Notes
- Edit Note
- Delete Note
- Export Notes

### Add a Note
1. Select Notes Manager
2. Choose "Add New Note"
3. Enter title and content
4. Note is saved automatically

### Search Notes
- Enter a keyword
- System searches in title and content

### Edit Note
- Enter Note ID
- Update title or content
- Modified timestamp updates automatically

### Delete Note
- Enter Note ID
- Note is permanently removed

### Export Notes
- Creates `notes_export.txt` in the `data/` folder

Notes are stored persistently in:
data/notes.json

---

# 🧮 Calculator

### Supported Operations:
- Addition
- Subtraction
- Multiplication
- Division
- Modulus

### How to Use:
1. Select Calculator
2. Choose operation
3. Enter numeric values
4. Result is displayed

Division by zero is handled safely.

---

# ⏱ Timer & Stopwatch

### Countdown Timer
- Enter time in seconds
- Timer counts down
- Displays completion message

### Stopwatch
- Press Enter to start
- Press Enter again to stop
- Displays elapsed time

---

# 📂 File Organizer

### Purpose:
Organizes files in a selected directory by file extension.

### How to Use:
1. Select File Organizer
2. Enter full directory path
3. Files are moved into folders based on extension

Example:
TXT/
JPG/
PDF/

Operations are logged in:
data/file_log.csv

---

# 🔁 Unit Converter

### Supported Conversions:
- Meters ↔ Kilometers
- Grams ↔ Kilograms
- Celsius ↔ Fahrenheit

### How to Use:
1. Select Unit Converter
2. Choose conversion type
3. Enter numeric value
4. Result is displayed

---

# 💾 Backup & Restore

### Create Backup
- Creates timestamped backup of notes.json
- Stored in:
data/backups/

### Restore Latest Backup
- Restores most recent backup
- Overwrites current notes.json

---

# ⚠ Important Notes

- All numeric inputs must be valid numbers.
- File paths must be valid directories.
- Backup restore overwrites existing notes.
- Data persists across application sessions.

---

# ✅ Exit Application

Select option 7 from main menu to safely exit.
