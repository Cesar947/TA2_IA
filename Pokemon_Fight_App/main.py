import pygame	
import sys
import time 	
import random
from models.menu import Menu 	

#initiate pygame
pygame.init()	

#display pygame
window = pygame.display.set_mode((1100, 800))		#set width & height of display
pygame.display.set_caption("Pokemon Quiz")		#set window name


menu = Menu(window)


#game starts
while True:

    menu.draw_menu()
    pygame.display.update()	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


