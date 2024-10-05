# coremechanics.py

from actions import action_immediate
from effects import apply_damage
from trackers import trackerset_debug

# Initialize the player's hand with starting cards
def initialize_hand():
    return ["Strike", "Strike", "Strike", "Strike"]  # You can expand this list later

# Function to choose a target from available enemies
def choose_target(enemies):
    while True:
        print("\n--- Choose target ---")
        for i, enemy in enumerate(enemies):
            print(f"{i + 1}. {enemy.name} ({enemy.health_current} HP)")
        try:
            choice = int(input("Select a target: ")) - 1
            if 0 <= choice < len(enemies):
                return enemies[choice]
            else:
                print("Invalid choice. Please select a valid target.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to display current hand and ask for card selection
def player_phase(player, enemies, hand):
    while True:
        if not enemies:
            print("\nAll enemies are dead. Combat ends.")
            return "end_turn"

        # Step 1: Choose a target
        target = choose_target(enemies)

        print("\n--- Your current hand ---")
        for i, card in enumerate(hand):
            print(f"{i + 1}. {card}")
        print("E. End turn")

        # Input from the player
        choice = input("Choose a card to play or press 'E' to end turn: ")

        # End turn if 'E' is pressed
        if choice.lower() == 'e':
            print("\nEnd of turn!")
            return "end_turn"

        try:
            # Convert choice to a number and play the corresponding card
            card_index = int(choice) - 1
            if 0 <= card_index < len(hand):
                card = hand.pop(card_index)  # Remove the selected card from the hand
                print(f"\nYou played {card} on {target.name}!")

                # Apply card effect (assuming Strike deals 6 damage)
                if card == "Strike":
                    play_card("Strike", player, target, lambda t: apply_damage(t, 6))

                # Show updated trackers for player and target
                trackerset_debug(player)
                trackerset_debug(target)

                # Check if the target is dead
                if target.health_current <= 0:
                    print(f"\n{target.name} is dead!")
                    enemies.remove(target)

                # Check if all cards have been played
                if not hand:
                    print("\nNo more cards to play.")
                    return "end_turn"
            else:
                print("Invalid choice. Please select a valid card number.")
        except ValueError:
            print("Invalid input. Please enter a valid card number.")

# Play card with an effect
def play_card(card_name, player, target, action):
    print(f"\n{card_name} played by {player.character_class}: Deals 6 damage to {target.name}")
    action(target)
