# player.py

from characters import Character

# Create a new player character based on the template in characters.py
player_character = Character("Test")

# Variable to track the cards available to play this turn
player_character.current_hand = []  # This will hold the cards available for the current turn

# You can add extra functionality here to update the player's status as the game progresses