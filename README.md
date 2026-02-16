# Complete Personal Productivity Suite

## 📌 Project Overview

The Complete Personal Productivity Suite is a modular, command-line-based Python application that integrates multiple productivity tools into a single unified system.

It demonstrates object-oriented programming, modular architecture, file handling using multiple formats, error handling, and persistent data management.

---

## 🎯 Project Objectives

- Build a modular Python application
- Implement multiple integrated productivity tools
- Use file handling with JSON, CSV, and TXT formats
- Ensure data persistence across sessions
- Implement comprehensive error handling
- Provide backup and restore functionality
- Maintain clean and reusable code architecture

---

## 🛠 Features Implemented

### Core Tools
- Notes Manager (Add, View, Search, Edit, Delete, Export)
- Calculator (Basic arithmetic operations)
- Timer & Stopwatch
- File Organizer (Organize files by extension with CSV logging)
- Unit Converter (Length, Weight, Temperature)

### System Features
- JSON data persistence
- CSV logging system
- TXT export functionality
- Timestamp tracking
- Backup & Restore system
- Interactive CLI menu interface
- Input validation and error handling

---

## 🗂 Project Structure
personal-productivity-suite/
│
├── main.py
├── requirements.txt
├── README.md
│
├── modules/
│ ├── calculator.py
│ ├── notes_manager.py
│ ├── timer.py
│ ├── file_organizer.py
│ ├── unit_converter.py
│ └── backup_manager.py
│
├── data/
│ ├── notes.json
│ ├── file_log.csv
│ ├── notes_export.txt
│ └── backups/
│
├── docs/
│ ├── installation.md
│ ├── user_guide.md
│ └── troubleshooting.md
│
├── screenshots/
└── tests/


---

## 🧠 Technical Requirements Fulfilled

- Modular architecture with separate modules for each tool
- File operations implemented using JSON, CSV, and TXT
- Comprehensive input validation and error handling
- Interactive command-line interface with menu system
- Persistent data storage across sessions
- Backup and restore system
- Reusable, organized module structure
- Utility-based calculations and conversions

---

## ▶️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- VS Code (recommended)

### Steps to Run

1. Clone the repository:
   git clone

2. Navigate to project directory:
   cd personal-productivity-suite

3. Run the application:
   python main.py


---

## 💾 Data Storage Format

| File | Purpose |
|------|---------|
| notes.json | Stores persistent notes data |
| file_log.csv | Logs file organization activity |
| notes_export.txt | Exported notes file |
| backups/ | Contains timestamped backup files |

---

## 🧪 Error Handling Implemented

- Invalid menu input handling
- Non-numeric input validation
- Division/modulus by zero protection
- Invalid file path handling
- Empty note validation
- Backup existence validation
- Safe restore mechanism

---

## 📷 Screenshot Evidence

Screenshots demonstrating working functionality are available in the `screenshots/` folder.

---

## 📦 Submission Deliverables

- Fully working Python CLI application
- Modular structured codebase
- Complete documentation
- Screenshot evidence
- Error handling implementation
- Proper GitHub repository structure

---

## 📚 Technologies Used

- Python 3
- JSON (data persistence)
- CSV (logging)
- TXT (export functionality)
- os module
- shutil module
- datetime module
- Object-Oriented Programming (OOP)

---

## 📌 Conclusion

The Complete Personal Productivity Suite successfully demonstrates modular software design, structured file handling, error management, and persistent data architecture. The project fulfills all technical and documentation requirements outlined in the internship task.
