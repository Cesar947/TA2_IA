import pygame	
import sys
import time 	
import random
from models.menu import Menu 	

#initiate pygame
pygame.init()	

#display pygame
window = pygame.display.set_mode((1100, 900))		#set width & height of display
pygame.display.set_caption("Pokemon Quiz")		#set window name
background_color = (247, 36, 89)
bg = pygame.image.load('./Pokemon_Fight_App/assets/pokemon_pattern.png')

menu = Menu(window)


#game starts
while True:
    window.fill(background_color)
    window.blit(bg, (0, 0))
    menu.draw_menu()
    pygame.display.update()	

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            menu.click_option(pos)    
            
        if event.type == pygame.MOUSEMOTION:
            menu.select_option(pos)



