import pygame as pg
import sys

from system.settings import *
from system.surfaces import Surfaces
from system.camera import Camera

from game import Game


class Core():

    def __init__(self, title):
        self.title = title
        self.event = None
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.tick_last_frame = 0
        self.set_fps = GAME_CONFIG['fps']
        self.mouse_pos = (0, 0)
        self.show_fps = True

        self.is_run = True

        self._setup()
        self.setup()

    # default callback
    def _setup(self):
        self.camera = Camera(self)
        self.game = Game(self, self.title)
        self.surfaces = Surfaces()

    def _update(self):
        self.surfaces._change_title(
            f"{self.game.title} | ({int(self.game.fps)})" if self.show_fps else self.game.title)
        self.game.update()

    def _draw(self):
        self.surfaces.clear_base()
        self.surfaces.clear_game()
        self.game.draw()

    def _after_draw(self):
        self.game.after_draw()

    def _before_flip(self):
        self.surfaces._before_flip()
        self.game.before_flip()

    # core utility
    def _delta_time(self):
        tick = pg.time.get_ticks()
        self.delta_time = (tick - self.tick_last_frame) / 1000.0
        self.tick_last_frame = tick

    def _tick(self):
        self.clock.tick(self.set_fps)
        self.game.fps = self.clock.get_fps()

    def _input(self):
        self.mouse_pos = pg.mouse.get_pos()
        for event in self.event:
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_run = False

    def _main_loop(self):
        while (self.is_run):
            self.event = pg.event.get()
            self._delta_time()
            self._tick()
            self._input()

            self._update()
            self.update()

            self._draw()
            self.draw()

            self._after_draw()
            self.after_draw()

            self._before_flip()
            self.before_flip()

            self.surfaces.update()

    def run(self):
        pg.init()
        self._main_loop()
        pg.quit()
        sys.exit()

    # custom callback
    def setup(self):
        self.game.setup()

    def update(self):
        self.game.update()

    def draw(self):
        self.game.draw()

    def after_draw(self):
        self.game.after_draw()

    def before_flip(self):
        self.game.before_flip()
