import classPlayer


class Killer(classPlayer.Player):
    def __int__(self,name):
        super().__init__(name)
        self.role = "killer"
        self.alive = True

    def __str__(self):
        return f"{self.name} (Killer)"
