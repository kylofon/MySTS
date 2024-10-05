# actions.py

# Perform an immediate action
def action_immediate(action):
    action()

# Queue an action for the end of the turn
def action_end_of_turn(action, combat_instance):
    combat_instance.action_queue.append(action)
    print("Action added to end-of-turn queue.")
