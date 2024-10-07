# scenario2.py

from card import strike_card, test_block_card
from effects import apply_damage, add_block
from player import player_character
from enemies import enemy_list
from coremechanics import play_card, end_turn
from trackers import trackerset_debug

# Scenario 2: Slime plays block twice, then player plays Strike
def run_scenario2():
    enemy_character = enemy_list[0]  # Pick the first enemy (Slime [S])

    # Turn 1: Slime plays Test Block Card twice
    print(f"\n--- Turn 1: Slime [S] Plays Test Block Card Twice ---")
    play_card(test_block_card, enemy_character, None, lambda target: add_block(enemy_character, 5))
    play_card(test_block_card, enemy_character, None, lambda target: add_block(enemy_character, 5))

    # Show trackers after Slime's actions
    trackerset_debug(enemy_character)
    trackerset_debug(player_character)

    # End of turn 1
    end_turn()

    # Turn 2: Player plays Strike on Slime
    print(f"\n--- Turn 2: Player Plays Strike ---")
    play_card(strike_card, player_character, enemy_character, lambda target: apply_damage(target, 6))

    # Show trackers after Player's action
    trackerset_debug(enemy_character)
    trackerset_debug(player_character)

    # End of turn 2 and scenario
    print("\n--- Final Status ---")
    print(f"Player: {player_character.health_current} HP, {player_character.block} block, {player_character.energy} energy.")
    print(f"Enemy {enemy_character.name}: {enemy_character.health_current} HP, {enemy_character.block} block.")