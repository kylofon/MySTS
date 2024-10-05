# card.py

class Card:
    def __init__(self, name, description, energy_cost, allowed_class):
        self.name = name
        self.description = description
        self.energy_cost = energy_cost
        self.allowed_class = allowed_class

    # Method to describe the card when played
    def describe(self):
        return f"{self.name}: {self.description} (Cost: {self.energy_cost})"