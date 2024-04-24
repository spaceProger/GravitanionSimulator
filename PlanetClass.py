import pygame as pg
import numpy as np

from config import G, min_r


class Planet:
    def __init__(self, position: list[float], mass: float, speed: list[float], color: tuple[int], radius: int, movable: bool):
        self.position = np.array(position)
        self.mass = mass
        self.speed = np.array(speed)
        self._forse = np.array([.0, .0])
        self.color = color
        self.radius = radius
        if radius < min_r:
            self.radius = min_r
        self.movable = movable
    
    def render(self, screen, camera, screen_size: tuple[int]) -> None:
        radius = self.radius / camera.approach
        if radius < min_r:
            radius = min_r
        position = np.array(screen_size) / 2 + (self.position + camera.position) / camera.approach
        if position[0] and position[1] and position[0] < screen_size[0] and position[1] < screen_size[1]:
            pg.draw.circle(surface=screen, color=self.color, center=position, radius=radius)
    
    def move(self, objects: list, index: int, fps: int) -> None:
        objects = objects[:]
        objects.pop(index)
        self._set_forse(objects=objects)

        self._set_new_pos(fps=fps)
    
    def _set_new_pos(self, fps: int) -> None:
        self.speed += self.forse * self.mass
        self.position += self.speed / fps
    
    def _set_forse(self, objects: list) -> None:
        self.forse = 0
        if objects:
            for object in objects:
                vec = object.position - self.position
                sq = np.square(vec)
                r_square = np.sum(sq)
                forse = G * self.mass * object.mass / r_square
                forse_vector = (object.position - self.position) / (r_square ** .5)
                self.forse += forse_vector * forse
