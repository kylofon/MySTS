# combat.py

class Combat:
    def __init__(self, participants):
        self.participants = participants  # List of player(s) and enemy(s)
        self.turn_number = 1  # Start at turn 1
        self.action_queue = []  # Queue for end-of-turn actions

    # Add action to the end-of-turn queue
    def add_action_to_queue(self, action):
        self.action_queue.append(action)

    # Increment the turn number
    def next_turn(self):
        self.turn_number += 1
        print(f"\n--- Turn {self.turn_number} ---")

# Initialize combat
combat_instance = Combat(participants=[])