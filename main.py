# Define the Card class
class Card:
    def __init__(self, name, description, energy_cost, allowed_class):
        self.name = name
        self.description = description
        self.energy_cost = energy_cost
        self.allowed_class = allowed_class

    # Method to play the card, affecting the target (deducting 8 HP for 'Strike')
    def play(self, target, player_class):
        if player_class == self.allowed_class:
            print(f"{self.name} played: {self.description}")
            target.health_current -= 8  # Deduct 8 HP from the target
            if target.health_current < 0:
                target.health_current = 0  # Ensure health doesn't go below 0
            print(f"Target now has {target.health_current} HP.")
        else:
            print(f"{self.name} cannot be played by this class.")

# Define the Character class
class Character:
    def __init__(self):
        self.character_class = "Test"
        self.starting_deck = []
        self.current_deck = self.starting_deck.copy()
        self.health_max = 100
        self.health_current = self.health_max
        self.money = 99
        self.potion_slots = [None, None, None]
        self.relics = []

# Create a player and a target character for testing
player_character = Character()
target_character = Character()

# Create a 'Strike' card that is playable only by the 'Test' class
strike_card = Card("Strike", "Deals 6 damage", 1, "Test")

# Play the card and see the result
strike_card.play(target_character, player_character.character_class)

# Print the target's current health after playing the card
print("Target's health after being attacked:", target_character.health_current)