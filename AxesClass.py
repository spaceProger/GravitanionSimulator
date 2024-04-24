import pygame as pg
import numpy as np

from classes.CameraClass import Camera


class Axes:
    def __init__(self):
        self.color = (69, 68, 64)

    def render(self, screen, screen_size, camera: Camera) -> None:
        position = np.array(screen_size) / 2 + camera.position / camera.approach
        pg.draw.line(surface=screen, color=self.color, start_pos=(position[0], 0), end_pos=(position[0], screen_size[1]))
        pg.draw.line(surface=screen, color=self.color, start_pos=(0, position[1]), end_pos=(screen_size[0], position[1]))
