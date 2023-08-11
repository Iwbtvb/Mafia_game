import classPlayer

class Seer(classPlayer.Player):
    def __int__(self,name):
        super().__int__(name)
        self.role = "Seer"
        self.alive = True

    def __str__(self):
        return f"{self.name} (Seer)"