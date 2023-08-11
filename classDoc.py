import classPlayer

class Doc(classPlayer.Player):
    def __int__(self,name):
        super.__init__(name)
        self.role = "Doctor"
        self.alive = True

    def __str__(self):
        return f"{self.name} (Doctor)"