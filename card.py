# card.py

class Card:
    def __init__(self, name, description, energy_cost, allowed_class):
        self.name = name
        self.description = description
        self.energy_cost = energy_cost
        self.allowed_class = allowed_class if isinstance(allowed_class, list) else [allowed_class]

# Define individual cards
card_ironclad_strike = Card("Strike", "Deals 6 damage", 1, ["Ironclad", "Enemy"])
card_ironclad_defend = Card("Defend", "Gain 5 block", 1, ["Ironclad", "Enemy"])
card_enemy_tackle = Card("Defend", "Deals 5 damage", 1, ["Enemy"])