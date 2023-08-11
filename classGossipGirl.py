import classPlayer

class gossipGirl(classPlayer.Player):
    def __int__(self,name):
        super.__init__(name)
        self.role = "Gossip girl"
        self.alive = True

    def __str__(self):
        return f"{self.name} (Gossip girl)"