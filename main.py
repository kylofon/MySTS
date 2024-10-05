# main.py

from coremechanics import initialize_hand, player_phase
from player import player_character
from enemies import Enemy

# Load two distinct enemies (small slimes)
enemy_character_1 = Enemy("Slime [S1]", 12)  # Create a unique instance of Slime 1
enemy_character_2 = Enemy("Slime [S2]", 12)  # Create a unique instance of Slime 2

# Create a list of enemies for combat
enemies = [enemy_character_1, enemy_character_2]

# Initialize player's hand
hand = initialize_hand()

# Start the player phase
result = player_phase(player_character, enemies, hand)

# End turn and terminate if 'E' is pressed or all enemies are dead
if result == "end_turn":
    print("\nCombat ends. Program terminated.")
