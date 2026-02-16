import json
import os
from datetime import datetime


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

    def generate_id(self):
        if not self.notes:
            return 1
        return max(note["id"] for note in self.notes) + 1

    def show_menu(self):
        while True:
            print("\n--- NOTES MANAGER ---")
            print("1. View All Notes")
            print("2. Add New Note")
            print("3. Search Notes")
            print("4. Back to Main Menu")


            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                self.search_notes()
            elif choice == "4":
                break
            else:
                print("Invalid input. Please try again.")


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
