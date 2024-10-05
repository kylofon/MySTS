# scenario.py

from card import strike_card
from effects import apply_damage
from player import player_character
from enemies import enemy_list
from coremechanics import play_card
from trackers import trackerset_debug

# Simple scenario: Player plays Strike on Slime
def run_scenario():
    enemy_character = enemy_list[0]  # Pick the first enemy (Slime [S])

    # Step 1: Show trackers before action
    print("\n--- Before Action: ---")
    trackerset_debug(player_character)  # Display tracker for player
    trackerset_debug(enemy_character)  # Display tracker for enemy

    # Step 2: Player plays Strike card on Slime (damage is dealt to the Slime)
    print(f"\n--- Player Plays Strike ---")
    play_card(strike_card, player_character, enemy_character, lambda target: apply_damage(target, 6))

    # Step 3: Show trackers after action
    print("\n--- After Action: ---")
    trackerset_debug(player_character)  # Display tracker for player
    trackerset_debug(enemy_character)  # Display tracker for enemy