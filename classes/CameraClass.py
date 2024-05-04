import numpy as np

from classes.PlanetClass import Planet


class Camera:
    def __init__(self, position: list[float] = [.0, .0]):
        self.position = np.array(position)
        self.appr_step = 10 ** (-1)
        self.approach_x = 40
        self.approach = self.get_approach()
    
    def get_approach(self) -> float:
        self.approach = np.e ** self.approach_x
        return self.approach
    
    def update_pos(self, golrud: list[int]) -> None:
        k_pos = np.array([.0, .0])
        if golrud[0]:
            k_pos[0] += 10
        if golrud[1]:
            k_pos[0] -= 10
        if golrud[2]:
            k_pos[1] += 10
        if golrud[3]:
            k_pos[1] -= 10
        
        self.position += k_pos * self.approach
    
    def render(self, objects: list[Planet], screen, screen_size: tuple[int]) -> None:
        for object in objects:
            object.render(screen=screen, screen_size=screen_size, camera=self)
