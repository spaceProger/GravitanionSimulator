import pygame as pg
import numpy as np
import sys

from classes.CameraClass import Camera
from classes.SceneClass import Scene
from classes.CanvasClass import Canvas


class EventHandler:
    def __init__(self):
        self.key_list = [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]
        self.golrud = [0, 0, 0, 0]

    def handl(self, camera: Camera, scene: Scene, canvas: Canvas, simulation, screen_size: tuple[int]) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            self.mouse_event(event=event, camera=camera, scene=scene, canvas=canvas, screen_size=screen_size)
            self.keyboard_event(event=event, simulation=simulation)
        camera.update_pos(golrud=self.golrud)
    
    def mouse_event(self, event, camera: Camera, scene: Scene, canvas: Canvas, screen_size: tuple[int]) -> None:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                bool_list: list[bool] = []
                for object in canvas.objects:
                    bool_list.append(object.on_button(mouse_pos=event.pos))
                if True not in bool_list:
                    scene.new_planet(position=event.pos, screen_size=screen_size, camera=camera)
            elif event.button == 3:
                # scene.sun_system_planet_spawn()
                pass
            elif event.button in [4, 5]:
                past_appr = camera.approach
                if event.button == 5:
                    camera.approach_x += camera.appr_step
                elif event.button == 4:
                    camera.approach_x -= camera.appr_step
                delta_key = camera.get_approach() - past_appr
                camera.position += (np.array(event.pos) - np.array(screen_size) / 2) * delta_key

    def keyboard_event(self, event, simulation) -> None:
        d = -1
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                simulation.pause = not simulation.pause
            d = 1
        elif event.type == pg.KEYUP:
            d = 0

        if d > -1:
            for i, key in enumerate(self.key_list):
                if event.key == key:
                    self.golrud[i] = d
