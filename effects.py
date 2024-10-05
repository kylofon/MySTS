# effects.py

def apply_damage(target, damage):
    if target.block > 0:
        if target.block >= damage:
            print(f"Damage ({damage}) is fully blocked by {target.block} block.")
            target.block -= damage
            damage = 0
        else:
            print(f"Damage ({damage}) is partially blocked. {target.block} block reduces damage to {damage - target.block}.")
            damage -= target.block
            target.block = 0

    target.health_current -= damage
    if target.health_current < 0:
        target.health_current = 0  # Ensure health doesn't go below 0
    print(f"After damage: Target has {target.health_current} HP and {target.block} block remaining.\n")


def add_block(player, block_amount):
    print(f"Before block: {player.character_class} has {player.health_current} HP and {player.block} block.")
    player.block += block_amount
    print(f"After block: {player.character_class} has {player.block} block (added {block_amount} block).\n")