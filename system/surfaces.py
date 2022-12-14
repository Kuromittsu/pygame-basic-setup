import pygame as pg

from system.settings import *

class Surfaces():

    def __init__(self):
        self.base = pg.display.set_mode(FULLSCREEN)
        self.game = pg.Surface(FULLSCREEN)
        self.game_rect = self.game.get_rect(topleft = (0, 0))

    def _before_flip(self):
        self.base.blit(self.game, (0, 0))

    def _change_title(self, title):
        pg.display.set_caption(title)

    def clear_base(self):
        self.base.fill('#2C3A47')

    def clear_game(self):
        self.game.fill('#55E6C1')

    def flip(self):
        # better use update() function
        pg.display.flip()

    def update(self):
        # according to the documentation,
        # the update() function is an optimization
        # of the flip() function
        pg.display.update()
