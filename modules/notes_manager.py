import json
import os
from datetime import datetime


class NotesManager:
    def __init__(self):
        self.file_path = "data/notes.json"
        self.notes = []
        self.load_notes()

    # ----------------------------
    # File Handling
    # ----------------------------

    def load_notes(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as file:
                    self.notes = json.load(file)
            except json.JSONDecodeError:
                self.notes = []
        else:
            self.notes = []

    def save_notes(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.notes, file, indent=4)

    def generate_id(self):
        if not self.notes:
            return 1
        return max(note["id"] for note in self.notes) + 1

    # ----------------------------
    # Menu System
    # ----------------------------

    def show_menu(self):
        while True:
            print("\n--- NOTES MANAGER ---")
            print("1. View All Notes")
            print("2. Add New Note")
            print("3. Search Notes")
            print("4. Edit Note")
            print("5. Delete Note")
            print("6. Export Notes")
            print("7. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                self.search_notes()
            elif choice == "4":
                self.edit_note()
            elif choice == "5":
                self.delete_note()
            elif choice == "6":
                self.export_notes()
            elif choice == "7":
                break
            else:
                print("Invalid input. Please enter a number between 1 and 7.")

    # ----------------------------
    # CRUD Operations
    # ----------------------------

    def add_note(self):
        title = input("Enter note title: ").strip()
        content = input("Enter note content: ").strip()

        if not title or not content:
            print("Title and content cannot be empty.")
            return

        note = {
            "id": self.generate_id(),
            "title": title,
            "content": content,
            "created": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "modified": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        self.notes.append(note)
        self.save_notes()

        print("\nNote added successfully!")
        print(f"Note ID: {note['id']}")
        print(f"Created: {note['created']}")

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
            return

        for note in self.notes:
            print("\n---------------------------------")
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            print(f"Created: {note['created']}")
            print(f"Modified: {note['modified']}")

    def search_notes(self):
        keyword = input("Enter keyword to search: ").strip().lower()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        found = False

        for note in self.notes:
            if keyword in note["title"].lower() or keyword in note["content"].lower():
                print("\n---------------------------------")
                print(f"ID: {note['id']}")
                print(f"Title: {note['title']}")
                print(f"Content: {note['content']}")
                print(f"Created: {note['created']}")
                print(f"Modified: {note['modified']}")
                found = True

        if not found:
            print("No matching notes found.")

    def edit_note(self):
        if not self.notes:
            print("No notes available to edit.")
            return

        try:
            note_id = int(input("Enter Note ID to edit: "))
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
            return

        for note in self.notes:
            if note["id"] == note_id:
                print(f"Current Title: {note['title']}")
                print(f"Current Content: {note['content']}")

                new_title = input("Enter new title (leave blank to keep current): ").strip()
                new_content = input("Enter new content (leave blank to keep current): ").strip()

                if new_title:
                    note["title"] = new_title
                if new_content:
                    note["content"] = new_content

                note["modified"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                self.save_notes()
                print("Note updated successfully.")
                return

        print("Note ID not found.")

    def delete_note(self):
        if not self.notes:
            print("No notes available to delete.")
            return

        try:
            note_id = int(input("Enter Note ID to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
            return

        for note in self.notes:
            if note["id"] == note_id:
                self.notes.remove(note)
                self.save_notes()
                print("Note deleted successfully.")
                return

        print("Note ID not found.")

    # ----------------------------
    # Export Feature (TXT)
    # ----------------------------

    def export_notes(self):
        if not self.notes:
            print("No notes available to export.")
            return

        export_path = "data/notes_export.txt"

        try:
            with open(export_path, "w", encoding="utf-8") as file:
                file.write("NOTES EXPORT\n")
                file.write("=" * 40 + "\n\n")

                for note in self.notes:
                    file.write(f"ID: {note['id']}\n")
                    file.write(f"Title: {note['title']}\n")
                    file.write(f"Content: {note['content']}\n")
                    file.write(f"Created: {note['created']}\n")
                    file.write(f"Modified: {note['modified']}\n")
                    file.write("-" * 40 + "\n")

            print(f"Notes exported successfully to {export_path}")

        except Exception as e:
            print("Error exporting notes:", e)
