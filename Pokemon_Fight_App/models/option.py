import pygame
from pygame.display import set_palette
from models.component import Component

pygame.init()

opt1 = pygame.image.load('./Pokemon_Fight_App/assets/option_1.png')
opt2 = pygame.image.load('./Pokemon_Fight_App/assets/option_2.png')
opt1_sel = pygame.image.load('./Pokemon_Fight_App/assets/option1_selected.png')
opt2_sel = pygame.image.load('./Pokemon_Fight_App/assets/option2_selected.png')

font = pygame.font.Font(None, 30)

class Option(Component):
    def __init__(self, i, x, y, width = opt1.get_rect().width, height = opt2.get_rect().height):
        Component.__init__(self, x, y, width, height)
        self.i = i
        if i == 1:
            self.asset = opt1
        elif i == 2:
            self.asset = opt2
        self.selected = False
        self.blocked = False
        self.color = (0,0,0)
        

    def draw_option(self, window, text):           
        window.blit(self.asset, (self.x, self.y))
        value = font.render(text, 1, self.color)
        window.blit(value, (self.x + 30, self.y + 11))

    def is_over(self, pos):
        if self.selected == False and self.blocked == False:
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] <self.y + self.height:
                    if self.i == 1:
                        self.asset = opt1_sel
                        self.color = (255,255,255)
                    else:
                        self.asset = opt2_sel
                        self.color = (255,255,255)
                    return True
            if self.i == 1:
                self.asset = opt1
                self.color = (0,0,0)
            else:
                self.asset = opt2
                self.color = (0,0,0)
        return False

    def select(self, pos):
        if self.blocked == False:
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] <self.y + self.height:    
                    if self.i == 1:
                        self.asset = opt1_sel
                        self.color = (255,255,255)
                    else:
                        self.asset = opt2_sel
                        self.color = (255,255,255)
                    self.selected = True
    
    def to_block(self):
        if self.i == 1:
            self.asset = opt1
        else:
            self.asset = opt2
        self.blocked = True

    def get_selected(self):
        return self.selected

    def ia_options(self):
        if self.i == 1:
            self.asset = opt1_sel
            self.color = (255,255,255)
        elif self.i == 2:
            self.asset = opt2_sel
            self.color = (255,255,255)
