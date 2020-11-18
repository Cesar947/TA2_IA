import pygame
from models.component import Component
from models.option import Option
from models.stat import Stat
from models.option import Option

pygame.init()

n_player = pygame.image.load('./Pokemon_Fight_App/assets/name_player.png')
n_ia = pygame.image.load('./Pokemon_Fight_App/assets/name_ia.png')

font = pygame.font.Font(None, 50)

puntos_player = 0
puntos_ia = 0

class Player(Component):
    def __init__(self, i, x, y, nombre1, nombre2, width = 500, height = 500):
        Component.__init__(self, x, y, width, height)
        if i == 1:
            self.asset = n_player
        else:
            self.asset = n_ia
        self.i = i
        #options
        self.opt1 = Option(1, x+80,y+100)
        self.opt2 = Option(2, x+80, y+160)
        self.opcion1 = nombre1
        self.opcion2 = nombre2
        self.opciones_seleccionadas = 0


    def draw_player(self, window):
        window.blit(self.asset, (self.x, self.y))
        if self.opt1.get_selected():
            self.opt2.to_block()
        if self.opt2.get_selected():
            self.opt1.to_block()
        #options
        self.opt1.draw_option(window, self.opcion1)  
        self.opt2.draw_option(window, self.opcion2)
        #points
        if self.i == 1:
            global puntos_player
            points = font.render(str(puntos_player), 1, (255,255,255))
        if self.i == 2:
            global puntos_ia
            points = font.render(str(puntos_ia), 1, (255,255,255))
        window.blit(points, (self.x + 60, self.y + 20))
        
    def select_option(self, pos):
        self.opt1.is_over(pos)
        self.opt2.is_over(pos)

    def click_option(self, pos):
        self.opt1.select(pos)  
        self.opt2.select(pos)

    def answer(self, opcion):
        if opcion == 0:
            self.opt1.ia_options()
        elif opcion == 1:   
            self.opt2.ia_options()

    def validar_opciones(self):
        if self.opt1.get_selected() == True or self.opt2.get_selected() == True:
            self.opciones_seleccionadas += 1
        return self.opciones_seleccionadas

    def opcion_elegida(self):
        if self.opt1.get_selected() == True:
            return 0
        elif self.opt2.get_selected() == True:
            return 1

    def sumar_puntos(self):
        if self.i == 1:
            global puntos_player
            puntos_player += 1
        if self.i == 2:
            global puntos_ia
            puntos_ia += 1

    def reset(self):
        self.opt1.deselect()
        self.opt2.deselect()