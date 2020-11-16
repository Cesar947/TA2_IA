import pygame
from models.component import Component
from models.stat import Stat

class PokemonStats(Component):
    def __init__(self, x, y, width = 500, height = 500):
        Component.__init__(self, x, y, width, height)
        self.hp = Stat(1,x,y)
        self.atq = Stat(2,x,y+40)
        self.defs = Stat(3,x,y+80)
        self.vel = Stat(4,x,y+120)

    def draw_pokemon_stats(self, window):
        self.hp.draw_stat(window)
        self.atq.draw_stat(window)
        self.defs.draw_stat(window)
        self.vel.draw_stat(window)
        #window.blit(self.asset, (self.x, self.y))