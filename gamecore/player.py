import pygame as pg
from pygame.math import Vector2


class Player():

    def __init__(self, core, position: tuple, dimension: tuple):
        self.core = core
        self.image = pg.Surface(dimension)
        self.rect = self.image.get_rect(center=position)
        self.position = Vector2(self.rect.center)
        self.move = Vector2(0, 0)
        self.default_speed = {
            'walk': 200,
            'run': 400,
        }
        self.speed = self.default_speed['walk']
        self.facing = Vector2()

        self.setup()
    
    def _event(self):
        for evt in self.core.event:

            if evt.type == pg.KEYDOWN: 
                if evt.key == pg.K_LSHIFT:
                    self._run()

            if evt.type == pg.KEYUP:
                if evt.key == pg.K_LSHIFT:
                    self._walk()

    def _walk(self):
        self.speed = self.default_speed['walk']

    def _run(self):
        self.speed = self.default_speed['run']
    
    def _facing(self):
        self.facing = self.move

    def _input(self):
        keys = pg.key.get_pressed()
        self.move.x = int(keys[pg.K_d]) - int(keys[pg.K_a])
        self.move.y = int(keys[pg.K_s]) - int(keys[pg.K_w])
        self._facing()
        if self.move.magnitude() > 0:
            self.move = self.move.normalize()

    def _move(self):
        self.position += self.move * self.speed * self.core.delta_time
        self.rect.center = [round(self.position.x), round(self.position.y)]

    def setup(self):
        self.image.fill('#474787')

    def update(self):
        self._input()
        self._event()
        self._move()

    def draw(self):
        self.core.surfaces.render_to_game(self.image, self.rect)
