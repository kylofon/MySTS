class Character:
  def __init__(self):
      self.character_class = "Test"
      self.starting_deck = []
      self.current_deck = self.starting_deck.copy()
      self.health_max = 100
      self.health_current = self.health_max
      self.money = 99
      self.potion_slots = [None, None, None]
      self.relics = []  # New attribute to store relics, starts empty

# Create an instance of the Character class
player_character = Character()

# Print out the character's attributes to check everything is working
print("Character Class:", player_character.character_class)
print("Starting Deck:", player_character.starting_deck)
print("Current Deck:", player_character.current_deck)
print("Health (current/max):", player_character.health_current, "/", player_character.health_max)
print("Money:", player_character.money)
print("Potion Slots:", player_character.potion_slots)
print("Relics:", player_character.relics)  # Print relics, which is currently an empty list