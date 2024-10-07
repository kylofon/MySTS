import player
import scenario
import characters
import card
import combat
import coremechanics
import effects
import enemies
import trackers

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
            start_scenario_confirmation()
            break
        else:
            print("Invalid choice, please try again.")

# Start Scenario Confirmation
def start_scenario_confirmation():
    while True:
        confirm = input("\nAre you ready to start the scenario? (yes/no): ")
        if confirm.lower() == 'yes':
            scenario.run_scenario()  # Run the test scenario after confirmation
            break
        elif confirm.lower() == 'no':
            print("\nReturning to Main Menu...")
            main_menu()
            break
        else:
            print("Invalid choice, please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main_menu()