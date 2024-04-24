import pygame as pg
import numpy as np


class Button:
    def __init__(self, text: str, size: tuple[int], color: tuple[int], font_color: tuple[int], position: tuple[int], action: object):
        self.text = text
        self.size = np.array(size)
        self.font_color = font_color
        self.color = color
        self.position = np.array(position)
        self.action = action
    
    def render(self, screen, font) -> None:
        pg.draw.rect(surface=screen, color=self.color, rect=(*self.position, *(self.position + self.size)))
        image = font.render(self.text, True, self.font_color)
        text_size = np.array(image.get_size())
        position = self.position + (self.size - text_size) / 2
        screen.blit(image, position)
    
    def on_button(self, mouse_pos: tuple[int]) -> bool:
        end_pos = self.position + self.size
        if self.position[0] <= mouse_pos[0] and end_pos[0] >= mouse_pos[0] and \
            self.position[1] <= mouse_pos[1] and end_pos[1] >= mouse_pos[1]:
            self.action()
            return True
        return False
