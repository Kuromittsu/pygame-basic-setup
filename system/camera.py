from pygame.math import Vector2


class Camera():

    def __init__(self, core):
        self.core = core
        self.offset = Vector2()
