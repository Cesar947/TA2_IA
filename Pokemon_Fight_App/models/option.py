import pygame
from pygame.display import set_palette
from models.component import Component

opt1 = pygame.image.load('./Pokemon_Fight_App/assets/option_1.png')
opt2 = pygame.image.load('./Pokemon_Fight_App/assets/option_2.png')
opt1_sel = pygame.image.load('./Pokemon_Fight_App/assets/option1_selected.png')
opt2_sel = pygame.image.load('./Pokemon_Fight_App/assets/option2_selected.png')

class Option(Component):
    def __init__(self, i, x, y, width = opt1.get_rect().width, height = opt2.get_rect().height):
        Component.__init__(self, x, y, width, height)
        self.i = i
        if i == 1:
            self.asset = opt1
        else:
            self.asset = opt2
        self.selected = False

    def draw_option(self, window):           
        window.blit(self.asset, (self.x, self.y))

    def is_over(self, pos):
        if self.selected == False:
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] <self.y + self.height:
                    if self.i == 1:
                        self.asset = opt1_sel
                    else:
                        self.asset = opt2_sel
                    return True
            if self.i == 1:
                self.asset = opt1
            else:
                self.asset = opt2
            return False
    
    def is_selected(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] <self.y + self.height:    
                if self.i == 1:
                    self.asset = opt1_sel
                else:
                    self.asset = opt2_sel
                self.selected = True

    def get_selected(self):
        return self.selected
    
    def set_selected(self, state):
        self.selected = state