from modules.notes_manager import NotesManager
from modules.calculator import Calculator
from modules.timer import Timer
from modules.file_organizer import FileOrganizer
from modules.unit_converter import UnitConverter

def main_menu():
    while True:
        print("\n" + "="*40)
        print("     PERSONAL PRODUCTIVITY SUITE")
        print("="*40)
        print("1. Calculator")
        print("2. Notes Manager")
        print("3. Timer")
        print("4. File Organizer")
        print("5. Unit Converter")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            calculator = Calculator()
            calculator.show_menu()
        elif choice == "2":
            notes_manager = NotesManager()
            notes_manager.show_menu()
        elif choice == "3":
            timer = Timer()
            timer.show_menu()
        elif choice == "4":
            organizer = FileOrganizer()
            organizer.show_menu()
        elif choice == "5":
            converter = UnitConverter()
            converter.show_menu()
        elif choice == "6":
            print("\nExiting application. Goodbye!")
            break
        else:
            print("\nInvalid input. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main_menu()
