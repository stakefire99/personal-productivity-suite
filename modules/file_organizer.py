import os
import shutil
import csv
from datetime import datetime


class FileOrganizer:
    def __init__(self):
        self.log_file = "data/file_log.csv"

    def show_menu(self):
        while True:
            print("\n--- FILE ORGANIZER ---")
            print("1. Organize Files by Extension")
            print("2. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.organize_files()
            elif choice == "2":
                break
            else:
                print("Invalid input. Please enter 1 or 2.")

    def organize_files(self):
        directory = input("Enter directory path to organize: ").strip()

        if not os.path.exists(directory):
            print("Directory does not exist.")
            return

        if not os.path.isdir(directory):
            print("Provided path is not a directory.")
            return

        try:
            files_moved = []

            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)

                if os.path.isfile(file_path):
                    extension = filename.split(".")[-1]

                    if "." not in filename:
                        continue

                    folder_path = os.path.join(directory, extension.upper())

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    new_path = os.path.join(folder_path, filename)
                    shutil.move(file_path, new_path)

                    files_moved.append((filename, extension.upper()))

            self.log_operations(files_moved)

            print("Files organized successfully.")

        except Exception as e:
            print("Error organizing files:", e)

    def log_operations(self, files_moved):
        if not files_moved:
            return

        file_exists = os.path.isfile(self.log_file)

        with open(self.log_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Filename", "Category", "Timestamp"])

            for filename, category in files_moved:
                writer.writerow([
                    filename,
                    category,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ])
