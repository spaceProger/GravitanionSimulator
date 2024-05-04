import numpy as np

from classes.PlanetClass import Planet
from classes.CameraClass import Camera


class Scene:
    def __init__(self):
        self.objects: list[Planet] = []
    
    def action(self, fps: int) -> None:
        for i, object in enumerate(self.objects):
            if object.movable:
                object.move(objects=self.objects, index=i, fps=fps)
    
    def new_planet(self, position, screen_size: tuple[int], camera: Camera) -> None:
        self.objects.append(Planet(
            position=(np.array(position) - np.array(screen_size) / 2) * camera.approach - camera.position,
            mass=1.9885 * 10 ** 20,
            speed=[.0, .0],
            color=np.random.randint(255, size=3),
            radius=6.957 * 10 ** 8,
            movable=True
        ))

    def sun_system_planet_spawn(self) -> None:
        self.objects.append(
            Planet(
                mass=1.9885 * 10**30,
                position=np.array([.0, .0]),
                color=np.random.randint(255, size=3),
                speed=[.0, .0],
                movable=False,
                radius=6.957 * 10 ** 8
                )
        )
        self.objects.append(
            Planet(
                mass=5.9726 * 10 ** 24,
                position=[.0, 1.496 * 10 ** 11],
                color=np.random.randint(255, size=3),
                speed=[29.765 * 10 ** 3, .0],
                movable=True,
                radius=6.371 * 10 ** 6
                )
        )
