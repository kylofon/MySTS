# Define the Card class
class Card:
    def __init__(self, name, description, energy_cost, allowed_class):
        self.name = name
        self.description = description
        self.energy_cost = energy_cost
        self.allowed_class = allowed_class

    # Method to play an attack card
    def play_attack(self, player, target):
        if player.character_class == self.allowed_class:
            print(f"\n{self.name} played by {player.character_class}: {self.description}")
            damage = 6  # Strike deals 6 damage

            # Apply block first
            print(f"Before damage: Target has {target.health_current} HP and {target.block} block.")
            if target.block > 0:
                if target.block >= damage:
                    print(f"Damage ({damage}) is fully blocked by {target.block} block.")
                    target.block -= damage
                    damage = 0
                else:
                    print(f"Damage ({damage}) is partially blocked. {target.block} block reduces damage to {damage - target.block}.")
                    damage -= target.block
                    target.block = 0

            target.health_current -= damage  # Deduct remaining damage from health
            if target.health_current < 0:
                target.health_current = 0  # Ensure health doesn't go below 0
            print(f"After damage: Target has {target.health_current} HP and {target.block} block remaining.\n")
        else:
            print(f"{self.name} cannot be played by this class.")

    # Method to play a defense card (applies block to self)
    def play_defense(self, player):
        if player.character_class == self.allowed_class:
            print(f"\n{self.name} played by {player.character_class}: {self.description}")
            print(f"Before block: {player.character_class} has {player.health_current} HP and {player.block} block.")
            player.block += 5  # Add 5 block points to the player casting the card
            print(f"After block: {player.character_class} has {player.block} block (added 5 block).\n")
        else:
            print(f"{self.name} cannot be played by this class.")

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
test_block_card.play_defense(enemy_character)

# Step 2: Player plays Strike card on Slime (damage is dealt to the Slime)
print(f"\n--- Turn 2: Player Plays Strike ---")
strike_card.play_attack(player_character, enemy_character)

# Step 3: Display the final status of both player and enemy
print(f"\n--- Final Status ---")
print(f"Player: {player_character.health_current} HP, {player_character.block} block.")
print(f"Enemy {enemy_character.name}: {enemy_character.health_current} HP, {enemy_character.block} block.")