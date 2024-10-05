# effects.py

from actions import action_immediate

def apply_damage(target, damage):
    def action(damage):
        original_damage = damage
        if target.block > 0:
            if target.block >= original_damage:
                print(f"Damage ({original_damage}) is fully blocked by {target.block} block.")
                target.block -= original_damage
                damage = 0
            else:
                print(f"Damage ({original_damage}) is partially blocked. {target.block} block reduces damage to {original_damage - target.block}.")
                damage = original_damage - target.block
                target.block = 0
        target.health_current -= damage
        if target.health_current < 0:
            target.health_current = 0
        print(f"After damage: Target has {target.health_current} HP and {target.block} block remaining.\n")

    action_immediate(lambda: action(damage))

def add_block(player, block_amount):
    def action():
        print(f"Before block: {player.character_class} has {player.health_current} HP and {player.block} block.")
        player.block += block_amount
        print(f"After block: {player.character_class} has {player.block} block (added {block_amount} block).\n")

    action_immediate(action)