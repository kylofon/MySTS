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

        # Step 2: Display hand and choose card
        while True:
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
                    card = hand[card_index]  # Get the selected card from the hand

                    # Check if player has enough energy to play the card
                    if player.energy > 0:
                        hand.pop(card_index)  # Remove the selected card from the hand
                        print(f"\nYou played {card} on {target.name}!")

                        # Apply card effect (assuming Strike deals 6 damage)
                        if card == "Strike":
                            play_card("Strike", player, target, lambda t: apply_damage(t, 6))

                        # Deduct energy for playing the card
                        player.energy -= 1
                        print(f"\nEnergy remaining: {player.energy}")

                        # Show updated trackers for player and target
                        trackerset_debug(player)
                        trackerset_debug(target)

                        # Check if the target is dead
                        if target.health_current <= 0:
                            print(f"\n{target.name} is dead!")
                            enemies.remove(target)
                            break  # Go back to target selection if the target is dead

                        # If there are still cards left, go back to target selection
                        break
                    else:
                        print("\nNot enough energy to play the card!")
                else:
                    print("Invalid choice. Please select a valid card number.")
            except ValueError:
                print("Invalid input. Please enter a valid card number.")

# Play card with an effect
def play_card(card_name, player, target, action):
    print(f"\n{card_name} played by {player.character_class}: Deals 6 damage to {target.name}")
    action(target)

# End turn function
def end_turn(player):
    print("\nEnding turn...")
    player.energy = player.max_energy  # Restore player's energy to the default value
    # Execute any end-of-turn actions here
    print("Energy restored to max.")