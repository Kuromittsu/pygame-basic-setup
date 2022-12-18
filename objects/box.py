import pygame as pg


class Box():

    def __init__(self, surface, pos, fill, dimension):
        self.surface = surface
        self.fill = fill
        self.image = pg.Surface(dimension)
        self.rect = self.image.get_rect(center=pos)

        self.setup()

    def setup(self):
        self.image.fill(self.fill)

    def update(self):
        pass

    def draw(self):
        self.surface.blit(self.image, self.rect)
