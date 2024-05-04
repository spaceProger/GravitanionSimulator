import pygame as pg

from config import min_r


class Cursor:
    def __init__(self):
        self.enable = False
        self.radius = min_r
        self.color = (213, 213, 194)
    
    def render(self, screen) -> None:
        if self.enable:
            pg.draw.circle(surface=screen, color=self.color, center=pg.mouse.get_pos(), radius=self.radius)
