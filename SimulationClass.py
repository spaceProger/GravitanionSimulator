import pygame as pg
import numpy as np

from classes.CameraClass import Camera
from classes.SceneClass import Scene
from classes.CanvasClass import Canvas
from classes.EventHandlerClass import EventHandler
from classes.AxesClass import Axes
from classes.ButtonClass import Button


class Simulation:
    def __init__(self, screen_size: tuple[int], fps: int):
        pg.init()
        self.screen_size = np.array(screen_size)
        self.fps = fps
        self.camera = Camera()
        self.scene = Scene()
        self.event_handler = EventHandler()
        self.canvas = Canvas(font=24)
        self.axes = Axes()
        self.pause = True
        self.background_color = (21, 19, 26)

        self.canvas.objects.append(
            Button(
                text="Sun-system",
                size=(100, 30),
                color=(250, 222, 5),
                font_color=(24, 24, 24),
                position=(0, 0),
                action=self.scene.sun_system_planet_spawn
            )
        )
    
    def pause_rend(self):
        pos_start = self.screen_size - 10
        pg.draw.rect(self.screen, (255, 255, 255), (*pos_start, *self.screen_size))
    
    def get_screen_pos(self, position):
        return np.array(self.screen_size) / 2 + (position + self.camera.position) / self.camera.approach
    
    def run(self) -> None:
        self.screen = pg.display.set_mode(self.screen_size)
        self.clock = pg.time.Clock()
        while True:
            self.clock.tick(self.fps)

            self.event_handler.handl(camera=self.camera, scene=self.scene, canvas=self.canvas, simulation=self, screen_size=self.screen_size)
            self.axes.render(screen=self.screen, screen_size=self.screen_size, camera=self.camera)
            if not self.pause:
                self.scene.action(fps=self.fps)
            else:
                self.pause_rend()

            self.camera.render(objects=self.scene.objects, screen=self.screen, screen_size=self.screen_size)
            self.canvas.render(screen=self.screen)

            pg.display.update()
            self.screen.fill(self.background_color)
