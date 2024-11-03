# enemies.py

from characters import Character

class Enemy(Character):
    def __init__(self, name, health_max):
        super().__init__(character_class="Enemy")
        self.name = name
        self.health_max = health_max
        self.health_current = health_max
        self.player = "no"  # Flag to indicate this is not a player character

# List of possible enemies
enemy_list = [
    Enemy("Spike slime [S]", 12)  # Slime with 12 health
]