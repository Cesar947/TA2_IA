  
import pygame
from models.pokemon_stats import PokemonStats
from models.player import Player
from backpropagation import seleccionar_enfrentamiento

diccionario_pokemon = seleccionar_enfrentamiento()
stats_pokemon_1 = diccionario_pokemon['stats_1']
stats_pokemon_2
pygame.init()

font = pygame.font.Font(None, 50)
font_med = pygame.font.Font(None, 40)

class Menu():
    def __init__(self, window):
        self.window = window
        self.pokemon_A = PokemonStats(120 , 100, )
        self.pokemon_B = PokemonStats(625 , 100)
        self.player_1 = Player(1, -20, 650)
        self.player_2 = Player(2, 750, 650)

    def draw_menu(self):
        vs = font.render("VS", 1, (255,255,255))
        text_select = font_med.render("Elige al ganador", 1, (255,255,255))
        self.window.blit(vs, (510, 400))
        self.window.blit(text_select, (445, 670))
        self.pokemon_A.draw_pokemon_stats(self.window, "Bulbasaur")
        self.pokemon_B.draw_pokemon_stats(self.window, "Chikorita")
        self.player_1.draw_player(self.window)
        self.player_2.draw_player(self.window)
    
    def select_option(self, pos):
        self.player_1.select_option(pos)
        self.player_2.select_option(pos)
        
    def click_option(self, pos):
        self.player_1.click_option(pos)
        self.player_2.click_option(pos)

