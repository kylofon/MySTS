# characters.py

class Character:
    def __init__(self, character_class):
        self.character_class = character_class
        self.starting_deck = []
        self.current_deck = self.starting_deck.copy()
        self.health_max = 100
        self.health_current = self.health_max
        self.block = 0
        self.money = 99
        self.potion_slots = [None, None, None]
        self.relics = []
        self.active_effects = []
        self.energy = 3  # Default energy for the player
        self.player = "yes"  # Flag to indicate this is a player character