class Calculator:
    def __init__(self):
        pass

    def show_menu(self):
        while True:
            print("\n--- CALCULATOR ---")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Modulus")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice in ["1", "2", "3", "4", "5"]:
                self.perform_calculation(choice)
            elif choice == "6":
                break
            else:
                print("Invalid input. Please enter a number between 1 and 6.")

    def perform_calculation(self, choice):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        if choice == "1":
            result = num1 + num2
            operation = "Addition"
        elif choice == "2":
            result = num1 - num2
            operation = "Subtraction"
        elif choice == "3":
            result = num1 * num2
            operation = "Multiplication"
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "Division"
        elif choice == "5":
            if num2 == 0:
                print("Error: Modulus by zero is not allowed.")
                return
            result = num1 % num2
            operation = "Modulus"

        print(f"{operation} Result: {result}")
