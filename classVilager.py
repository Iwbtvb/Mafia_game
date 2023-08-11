import classPlayer
class Villager(classPlayer.Player):
    def __init__(self, name):
        super().__init__(name)
        self.role = "Villager"
        self.alive = True

    def __str__(self):
        return f"{self.name} (Villager)"