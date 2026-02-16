import json
import os


class NotesManager:
    def __init__(self):
        self.file_path = "data/notes.json"
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    self.notes = json.load(file)
            except json.JSONDecodeError:
                self.notes = []
        else:
            self.notes = []

    def save_notes(self):
        with open(self.file_path, "w") as file:
            json.dump(self.notes, file, indent=4)

    def show_menu(self):
        while True:
            print("\n--- NOTES MANAGER ---")
            print("1. View Notes")
            print("2. Add Note")
            print("3. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                break
            else:
                print("Invalid input. Please try again.")

    def add_note(self):
        title = input("Enter note title: ")
        content = input("Enter note content: ")

        note = {
            "title": title,
            "content": content
        }

        self.notes.append(note)
        self.save_notes()
        print("Note added successfully!")

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
            return

        for index, note in enumerate(self.notes, start=1):
            print(f"\nNote {index}")
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
