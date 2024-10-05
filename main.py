# main.py

from card import Card
from effects import apply_damage, add_block

# Define the Character class (including active effects)
class Character:
    def __init__(self, character_class):
        self.character_class = character_class
        self.starting_deck = []
        self.current_deck = self.starting_deck.copy()
        self.health_max = 100
        self.health_current = self.health_max
        self.block = 0  # Attribute to track the character's block
        self.money = 99
        self.potion_slots = [None, None, None]
        self.relics = []
        self.active_effects = []  # New field for storing active buffs/debuffs

# Define an Enemy class (inherits from Character)
class Enemy(Character):
    def __init__(self, name, health_max):
        super().__init__(character_class="Enemy")  # Slime is an enemy class
        self.name = name  # Set enemy name
        self.health_max = health_max
        self.health_current = health_max

# Define a list of possible enemies (for future use)
enemy_list = [
    Enemy("Slime [S]", 12)  # Slime [S] with 12 health
]

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