import os
import shutil
from datetime import datetime


class BackupManager:
    def __init__(self):
        base_dir = os.getcwd()

        self.source_file = os.path.join(base_dir, "data", "notes.json")
        self.backup_folder = os.path.join(base_dir, "data", "backups")

        os.makedirs(self.backup_folder, exist_ok=True)

    def show_menu(self):
        while True:
            print("\n--- BACKUP & RESTORE ---")
            print("1. Create Backup")
            print("2. Restore Latest Backup")
            print("3. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_backup()
            elif choice == "2":
                self.restore_backup()
            elif choice == "3":
                break
            else:
                print("Invalid input. Please enter a number between 1 and 3.")

    def create_backup(self):
        print("SOURCE:", self.source_file)
        print("BACKUP FOLDER:", self.backup_folder)

        if not os.path.exists(self.source_file):
            print("Source notes.json does NOT exist.")
            return

        os.makedirs(self.backup_folder, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f"notes_backup_{timestamp}.json"
        backup_path = os.path.join(self.backup_folder, backup_filename)

        print("BACKUP PATH:", backup_path)

        try:
            shutil.copy2(self.source_file, backup_path)
            print(f"Backup created successfully: {backup_filename}")
        except Exception as e:
            print("Error creating backup:", e)

    def restore_backup(self):
        backups = [
            f for f in os.listdir(self.backup_folder)
            if f.startswith("notes_backup_") and f.endswith(".json")
        ]

        if not backups:
            print("No backups available to restore.")
            return

        latest_backup = sorted(backups)[-1]
        backup_path = os.path.join(self.backup_folder, latest_backup)

        try:
            shutil.copy2(backup_path, self.source_file)
            print(f"Restored successfully from: {latest_backup}")
        except Exception as e:
            print("Error restoring backup:", e)
