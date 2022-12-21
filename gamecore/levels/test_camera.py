from gamecore.player import Player


class Test_camera():

    def __init__(self, core):
        self.core = core

        self.setup()

    def setup(self):
        self.player = Player(self.core, (100, 100), (60, 80))

    def update(self):
        self.player.update()

    def draw(self):
        self.player.draw()
