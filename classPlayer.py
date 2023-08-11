class Player:
    def __init__(self, name):
        self.name = name
        self.role = None
        self.alive = True
        self.vote = 0
        self.vote_k = 0
        self.win = 0
        self.gossip = 0

    def show(self):
        self.show_role =True

    def hide(self):
        self.show_role = False
    def __str__(self):
        return self.name