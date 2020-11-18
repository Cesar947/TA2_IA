import pygame	
import sys
import time 	
import random
from models.juego import Juego 	

#initiate pygame
pygame.init()	

#display pygame
window = pygame.display.set_mode((1100, 900))		#set width & height of display
pygame.display.set_caption("Pokemon Quiz")		#set window name
background_color = (247, 36, 89)
bg = pygame.image.load('./Pokemon_Fight_App/assets/pokemon_pattern.png')

juego = Juego(window)

#game starts
while True:
    if juego.ronda_terminada():
        juego.ganador()
        juego = Juego(window)
    window.fill(background_color)
    window.blit(bg, (0, 0))
    juego.juega_ia()
    juego.draw_menu()
    juego.terminar_juego()
    pygame.display.update()	

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            juego.click_option(pos)    
            
        if event.type == pygame.MOUSEMOTION:
            juego.select_option(pos)



