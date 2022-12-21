import pygame as pg
from pygame.math import Vector2


class Player():

    def __init__(self, core, position: tuple, dimension: tuple):
        self.core = core
        self.image = pg.Surface(dimension)
        self.rect = self.image.get_rect(center=position)
        self.position = Vector2(self.rect.center)
        self.move = Vector2(0, 0)
        self.speed = 200

        self.setup()

    def _input(self):
        keys = pg.key.get_pressed()
        self.move.x = int(keys[pg.K_d]) - int(keys[pg.K_a])
        self.move.y = int(keys[pg.K_s]) - int(keys[pg.K_w])
        if self.move.magnitude() > 0:
            self.move = self.move.normalize()

    def _move(self):
        self.position += self.move * self.speed * self.core.delta_time
        self.rect.center = round(self.position.x), round(self.position.y)

    def setup(self):
        self.image.fill('#474787')

    def update(self):
        self._input()
        self._move()

    def draw(self):
        self.core.surfaces.render_to_game(self.image, self.rect)
