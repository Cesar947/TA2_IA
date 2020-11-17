import pygame
from models.component import Component
from models.option import Option
from models.stat import Stat
from models.option import Option

n_player = pygame.image.load('./Pokemon_Fight_App/assets/name_player.png')
n_ia = pygame.image.load('./Pokemon_Fight_App/assets/name_ia.png')

class Player(Component):
    def __init__(self, i, x, y, width = 500, height = 500):
        Component.__init__(self, x, y, width, height)
        if i == 1:
            self.asset = n_player
        else:
            self.asset = n_ia
        #options
        self.opt1 = Option(1, x+80,y+100)
        self.opt2 = Option(2, x+80, y+160)


    def draw_player(self, window):
        window.blit(self.asset, (self.x, self.y))

        #options
        self.opt1.draw_option(window)  
        self.opt2.draw_option(window)
        

    def select_option(self, pos):
        self.opt1.is_over(pos)
        self.opt2.is_over(pos)
