import pygame as pg


class Player():

    def __init__(self, pos, dimension):
        self.image = pg.Surface(dimension)
        self.rect = self.image.get_rect(center=pos)
