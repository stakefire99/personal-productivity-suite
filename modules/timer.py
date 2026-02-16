import time


class Timer:
    def __init__(self):
        pass

    def show_menu(self):
        while True:
            print("\n--- TIMER & STOPWATCH ---")
            print("1. Countdown Timer")
            print("2. Stopwatch")
            print("3. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.countdown_timer()
            elif choice == "2":
                self.stopwatch()
            elif choice == "3":
                break
            else:
                print("Invalid input. Please enter a number between 1 and 3.")

    # ----------------------------
    # Countdown Timer
    # ----------------------------

    def countdown_timer(self):
        try:
            seconds = int(input("Enter time in seconds: "))
            if seconds <= 0:
                print("Please enter a positive number.")
                return
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        print("Countdown started...")
        while seconds > 0:
            print(f"Time remaining: {seconds} seconds", end="\r")
            time.sleep(1)
            seconds -= 1

        print("\nTime's up!")

    # ----------------------------
    # Stopwatch
    # ----------------------------

    def stopwatch(self):
        input("Press Enter to start the stopwatch...")
        start_time = time.time()

        input("Press Enter to stop the stopwatch...")
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Elapsed Time: {elapsed_time:.2f} seconds")
