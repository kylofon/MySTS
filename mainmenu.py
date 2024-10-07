import player
import scenario
import characters
import card
import combat
import coremechanics
import effects
import enemies
import trackers
import map as game_map

# Main Menu Functionality
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. New Game")
        choice = input("Choose an option: ")

        if choice == '1':
            new_game()
        else:
            print("Invalid choice, please try again.")

# New Game Functionality
def new_game():
    # Generate a new map
    current_map = game_map.generate_map()

    # Start class selection and scenario
    class_select()

# Class Selection Functionality
def class_select():
    while True:
        print("\n--- Class Selection ---")
        print("1. Test Class")
        choice = input("Choose your class: ")

        if choice == '1':
            print("\nYou have chosen the Test Class!")
            scenario.run_scenario()  # Directly run the scenario after class selection
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()