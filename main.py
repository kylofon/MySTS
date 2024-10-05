# main.py

from card import Card
from effects import apply_damage, add_block
from characters import Character  # Import player character
from enemies import enemy_list  # Import enemy list

# Create a player and an enemy character for testing
player_character = Character("Test")
enemy_character = enemy_list[0]  # Pick the first enemy (Slime [S])

# Create a 'Strike' card for the player
strike_card = Card("Strike", "Deals 6 damage", 1, "Test")

# Create a 'Test Block Card' for the enemy
test_block_card = Card("Test Block Card", "Gain 5 block", 1, "Enemy")

# Simulate combat sequence

# Step 1: Slime plays the Test Block Card (block is applied to Slime itself)
print(f"\n--- Turn 1: Slime [S] Plays Test Block Card ---")
add_block(enemy_character, 5)

# Step 2: Player plays Strike card on Slime (damage is dealt to the Slime)
print(f"\n--- Turn 2: Player Plays Strike ---")
apply_damage(enemy_character, 6)

# Step 3: Display the final status of both player and enemy
print(f"\n--- Final Status ---")
print(f"Player: {player_character.health_current} HP, {player_character.block} block.")
print(f"Enemy {enemy_character.name}: {enemy_character.health_current} HP, {enemy_character.block} block.")