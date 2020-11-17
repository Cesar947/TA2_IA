  
import pygame
from models.component import Component

pygame.init()

hp = pygame.image.load('./Pokemon_Fight_App/assets/hp.png')
atq = pygame.image.load('./Pokemon_Fight_App/assets/atq.png')
defs = pygame.image.load('./Pokemon_Fight_App/assets/def.png')
vel = pygame.image.load('./Pokemon_Fight_App/assets/vel.png')

font = pygame.font.Font(None, 30)

class Stat(Component):
    def __init__(self, i, x, y, width = hp.get_rect().width, height = hp.get_rect().height):
        Component.__init__(self, x, y, width, height)
        if i == 1:
            self.asset = hp
        elif i == 2:
            self.asset = atq
        elif i == 3:
            self.asset = defs   
        else :
            self.asset = vel

    def draw_stat(self, window, text):
        window.blit(self.asset, (self.x, self.y))
        value = font.render(text + " pts.", 1, (255,255,255))
        window.blit(value, (self.x + 30, self.y + 5))
