# enemies.py

from characters import Character

class Enemy(Character):
    def __init__(self, name, health_max):
        super().__init__(character_class="Enemy")  # Slime is an enemy class
        self.name = name  # Set enemy name
        self.health_max = health_max
        self.health_current = health_max

# List of possible enemies
enemy_list = [
    Enemy("Slime [S]", 12)  # Slime [S] with 12 health
]