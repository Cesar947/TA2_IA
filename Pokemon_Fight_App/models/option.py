import pygame
from models.component import Component

opt1 = pygame.image.load('./Pokemon_Fight_App/assets/option_1.png')
opt2 = pygame.image.load('./Pokemon_Fight_App/assets/option_2.png')

class Option(Component):
    def __init__(self, i, x, y, width = opt1.get_rect().width, height = opt2.get_rect().height):
        Component.__init__(self, x, y, width, height)
        if i == 1:
            self.asset = opt1
        else:
            self.asset = opt2

    def draw_option(self, window):
        window.blit(self.asset, (self.x, self.y))