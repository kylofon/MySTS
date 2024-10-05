# effects.py

def apply_damage(target, damage_amount):
    print(f"Dealing {damage_amount} damage to {target.character_class}.")
    target.health_current -= damage_amount
    if target.health_current <= 0:
        target.is_alive = False# coremechanics.py

from combat import combat_instance
from player import player_character

# Play a card if the player has enough energy, or skip energy calculation if flag is set to "no"
def play_card(card, player, target, action):
    if player.player == "no" or player.energy >= card.energy_cost:
        print(f"\n{card.name} played by {player.character_class}: {card.description} (Cost: {card.energy_cost} energy)")
        if player.player == "yes":
            player.energy -= card.energy_cost  # Deduct the energy cost only if it's a player character
        action(target)
        print(f"{player.character_class} now has {player.energy} energy left.\n")
    else:
        print(f"Not enough energy to play {card.name}! {player.character_class} has {player.energy} energy.")

# Restore player's energy and execute end-of-turn actions
def end_turn():
    print("\nEnd of Turn:")
    player_character.energy = 3  # Restore player's energy to default
    print(f"Player's energy restored to {player_character.energy}.")

    # Execute actions in the queue
    if combat_instance.action_queue:
        print("Executing end-of-turn actions...")
        for action in combat_instance.action_queue:
            action()
        combat_instance.action_queue.clear()

# Define action types
def action_immediate(action):
    action()

def action_end_of_turn(action):
    combat_instance.add_action_to_queue(action)
    print("Action added to end-of-turn queue.")