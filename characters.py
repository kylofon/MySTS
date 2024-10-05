# characters.py

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