import classPlayer

class Fool(classPlayer.Player):
    def __int__(self,name):
        super.__init__(name)
        self.role = "Fool"
        self.alive = True

    def __str__(self):
        return f"{self.name} (Fool)"