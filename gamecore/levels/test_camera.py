from gamecore.player import Player
from gamecore.objects.box import Box


class Test_camera():

    def __init__(self, core):
        self.core = core

        self.setup()

    def setup(self):
        self.player = Player(self.core, (100, 100), (60, 80))

        self.boxs = [
            Box(self.core.surfaces.game, (300, 200), '#1e3799', (50, 50)),
            Box(self.core.surfaces.game, (200, 200), '#1e3799', (50, 50)),
            Box(self.core.surfaces.game, (400, 300), '#1e3799', (50, 50)),
        ]

    def update(self):
        self.player.update()

        for box in self.boxs:
            box.update()

    def draw(self):
        self.player.draw()
        
        for box in self.boxs:
            box.draw()
