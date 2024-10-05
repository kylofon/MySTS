# card.py

class Card:
    def __init__(self, name, description, energy_cost, allowed_class):
        self.name = name
        self.description = description
        self.energy_cost = energy_cost
        self.allowed_class = allowed_class

# Define individual cards
strike_card = Card("Strike", "Deals 6 damage", 1, "Test")
test_block_card = Card("Test Block Card", "Gain 5 block", 0, "Enemy")  # Set energy cost to 0