import pygame	
import sys
import time 	
import random 	
#from gameLogic import game_loop

#initiate pygame
pygame.init()	

#display pygame
display = pygame.display.set_mode((600,600))		#set width & height of display
pygame.display.set_caption("Pokemon Quiz")		#set window name

#game starts
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()