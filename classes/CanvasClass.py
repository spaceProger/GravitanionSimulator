import pygame as pg

from classes.CursorClass import Cursor


class Canvas:
    def __init__(self, font: int):
        self.objects = []
        self.cursor = Cursor()
        self.font = pg.font.SysFont(None, font)

    def render(self, screen) -> None:
        self.cursor.render(screen=screen)
        for object in self.objects:
            object.render(screen=screen, font=self.font)
