# trackers.py

class Tracker:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def update(self, new_value):
        self.value = new_value

    def __str__(self):
        return f"{self.name}: {self.value}"

# Define individual trackers
class TrackerEnergy(Tracker):
    def __init__(self, target):
        super().__init__("Energy", value=target.energy)
        self.target = target

    def update(self):
        self.value = self.target.energy

class TrackerHealth(Tracker):
    def __init__(self, target):
        super().__init__("Health", value=target.health_current)
        self.target = target

    def update(self):
        self.value = self.target.health_current

class TrackerGold(Tracker):
    def __init__(self, target):
        super().__init__("Gold", value=target.money)
        self.target = target

    def update(self):
        self.value = self.target.money

class TrackerBlock(Tracker):
    def __init__(self, target):
        super().__init__("Block", value=target.block)
        self.target = target

    def update(self):
        self.value = self.target.block

class TrackerIncoming(Tracker):
    def __init__(self):
        super().__init__("Incoming Damage", value=0)

    def update(self, incoming_damage):
        self.value = incoming_damage

class TrackerTarget(Tracker):
    def __init__(self, target):
        super().__init__("Target", value=target.character_class)
        self.target = target

# Trackerset for displaying multiple trackers
class Trackerset:
    def __init__(self, target):
        self.energy = TrackerEnergy(target)
        self.health = TrackerHealth(target)
        self.gold = TrackerGold(target)
        self.block = TrackerBlock(target)
        self.incoming = TrackerIncoming()
        self.target = TrackerTarget(target)

    def update_all(self):
        self.energy.update()
        self.health.update()
        self.gold.update()
        self.block.update()

    def display(self):
        self.update_all()
        return f"{self.target}\n{self.energy}\n{self.health}\n{self.gold}\n{self.block}\n{self.incoming}"

# Define a debug set of trackers
def trackerset_debug(target):
    tracker_set = Trackerset(target)
    print(tracker_set.display())