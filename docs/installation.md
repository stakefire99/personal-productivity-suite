# Installation Guide

## 📌 Overview

This guide explains how to install and run the Complete Personal Productivity Suite on your local system.

---

## 🖥 System Requirements

- Operating System: Windows / macOS / Linux
- Python Version: 3.10 or higher
- Git (optional, for cloning repository)
- VS Code (recommended)

---

## 🐍 Step 1: Install Python

1. Download Python from:
   https://www.python.org/downloads/

2. During installation:
   - Check the box **"Add Python to PATH"**
   - Click Install

3. Verify installation:

   Open terminal and run:
   python --version
   
You should see Python 3.10+ installed.

---

## 📥 Step 2: Clone the Repository

If using Git:
git clone <repository-link>


Then navigate to the project directory:
cd personal-productivity-suite


If downloading manually:
- Download ZIP file
- Extract it
- Open folder in VS Code

---

## 📦 Step 3: Install Dependencies

This project uses only Python standard libraries.

No external packages are required.

If needed:
pip install -r requirements.txt

---

## ▶️ Step 4: Run the Application

Inside the project directory, run:
python main.py

The main menu will appear in the terminal.

---

## 📂 Important Project Structure

Ensure the following folders exist:
data/
data/backups/
modules/
docs/
screenshots/
tests/

If `data/backups/` does not exist, create it manually.

---

## 🚀 Application Launch

After running:
python main.py


You will see:
PERSONAL PRODUCTIVITY SUITE
1.Calculator
2.Notes Manager
3.Timer & Stopwatch
4.File Organizer
5.Unit Converter
6.Backup & Restore
7.Exit

You can now navigate through the tools using numeric input.

---

## ✅ Installation Complete

If the application runs without errors, installation is successful.
