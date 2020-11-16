import pygame
from models.component import Component
from models.option import Option
from models.stat import Stat

p_name = pygame.image.load('./Pokemon_Fight_App/assets/pokemon_name.png')
img_back = pygame.image.load('./Pokemon_Fight_App/assets/img_back.png')

class PokemonStats(Component):
    def __init__(self, x, y, width = 500, height = 500):
        Component.__init__(self, x, y, width, height)
        self.hp = Stat(1,x+70,y+360)
        self.atq = Stat(2,x+70,y+400)
        self.defs = Stat(3,x+70,y+440)
        self.vel = Stat(4,x+70,y+480)
        self.name = p_name
        self.back = img_back
        


    def draw_pokemon_stats(self, window):
        window.blit(self.back, (self.x, self.y))
        window.blit(self.name, (self.x, self.y+280))
        self.hp.draw_stat(window)
        self.atq.draw_stat(window)
        self.defs.draw_stat(window)
        self.vel.draw_stat(window)

        #window.blit(self.asset, (self.x, self.y))