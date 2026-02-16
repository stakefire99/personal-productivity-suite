class NotesManager:
    def __init__(self):
        self.notes = []

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
        print("Note added successfully!")

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
            return

        for index, note in enumerate(self.notes, start=1):
            print(f"\nNote {index}")
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
