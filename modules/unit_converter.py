class UnitConverter:
    def __init__(self):
        pass

    def show_menu(self):
        while True:
            print("\n--- UNIT CONVERTER ---")
            print("1. Length Conversion (Meters ↔ Kilometers)")
            print("2. Weight Conversion (Grams ↔ Kilograms)")
            print("3. Temperature Conversion (Celsius ↔ Fahrenheit)")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.length_conversion()
            elif choice == "2":
                self.weight_conversion()
            elif choice == "3":
                self.temperature_conversion()
            elif choice == "4":
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

    # ----------------------------
    # Length Conversion
    # ----------------------------

    def length_conversion(self):
        try:
            value = float(input("Enter value: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        print("1. Meters to Kilometers")
        print("2. Kilometers to Meters")
        option = input("Choose conversion type: ")

        if option == "1":
            result = value / 1000
            print(f"{value} meters = {result} kilometers")
        elif option == "2":
            result = value * 1000
            print(f"{value} kilometers = {result} meters")
        else:
            print("Invalid option.")

    # ----------------------------
    # Weight Conversion
    # ----------------------------

    def weight_conversion(self):
        try:
            value = float(input("Enter value: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        print("1. Grams to Kilograms")
        print("2. Kilograms to Grams")
        option = input("Choose conversion type: ")

        if option == "1":
            result = value / 1000
            print(f"{value} grams = {result} kilograms")
        elif option == "2":
            result = value * 1000
            print(f"{value} kilograms = {result} grams")
        else:
            print("Invalid option.")

    # ----------------------------
    # Temperature Conversion
    # ----------------------------

    def temperature_conversion(self):
        try:
            value = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        option = input("Choose conversion type: ")

        if option == "1":
            result = (value * 9/5) + 32
            print(f"{value}°C = {result}°F")
        elif option == "2":
            result = (value - 32) * 5/9
            print(f"{value}°F = {result}°C")
        else:
            print("Invalid option.")
