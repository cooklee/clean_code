class Player(object):

    def __init__(self):
        self.hit_points = 300
        self.stamina = 100

        self.speed = 10
        self.strength = 10
        self.agility = 10
        self.wisdom = 10
        self.knowledge = 10

    def run_forest_run(self):
        if self.stamina > 0:
            self.speed *= 3
        else:
            self.speed /= 3

    def didKickedTheBucked(self):
        if self.hit_points <= 0:
            return -1
        else:
            return 1



