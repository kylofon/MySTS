from player import player_character
from enemies import SlimeSmall
import copy

# Map Generation Functionality
def generate_map():
    # Create a new map with a single room
    print("\n--- Generating New Map ---")

    # Create instances of enemies using the SlimeSmall archetype
    enemy1 = copy.deepcopy(SlimeSmall)
    enemy2 = copy.deepcopy(SlimeSmall)

    # Assign unique attributes if needed
    enemy1.name = "Slime Small A"
    enemy2.name = "Slime Small B"

    room = {
        "player": player_character,
        "enemies": [enemy1, enemy2]  # Add two slime monsters to the room
    }

    # Display room information
    print("\n--- New Room Created ---")
    print(f"Player: {room['player'].character_class}")
    for i, enemy in enumerate(room['enemies']):
        print(f"Enemy {i + 1}: {enemy.name} (HP: {enemy.health_current})")

    return room

if __name__ == "__main__":
    generate_map()