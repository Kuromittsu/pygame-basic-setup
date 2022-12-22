from pygame.math import Vector2

class Camera():

    def __init__(self, core):
        self.core = core
        self.base_size = self.core.surfaces.game_size()
        self.offset = Vector2()
