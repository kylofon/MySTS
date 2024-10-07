import player
import scenario

# Main Menu Functionality
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. New Game")
        choice = input("Choose an option: ")

        if choice == '1':
            class_select()
        else:
            print("Invalid choice, please try again.")

# Class Selection Functionality
def class_select():
    while True:
        print("\n--- Class Selection ---")
        print("1. Test Class")
        choice = input("Choose your class: ")

        if choice == '1':
            print("\nYou have chosen the Test Class!")
            scenario.run_scenario()  # Run the test scenario after class selection
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()