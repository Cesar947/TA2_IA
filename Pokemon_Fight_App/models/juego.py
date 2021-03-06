  
import pygame

from models.pokemon_stats import PokemonStats
from models.player import Player
from neural_network.backpropagation import seleccionar_enfrentamiento
from neural_network.backpropagation import decision

#print("Ganador de la LoliCup: " + str(opcion_ia[0][0]))

pygame.init()

font = pygame.font.Font(None, 50)
font_med = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 80)

winner_screen = pygame.image.load('./Pokemon_Fight_App/assets/winner_screen.jpg')

puntos_jugador = 0
puntos_ia = 0

class Juego():
    def __init__(self, window):
        self.diccionario_pokemon, self.test_label = seleccionar_enfrentamiento()
        self.window = window
        self.nombre_pokemon_1 = self.diccionario_pokemon['nombre_pokemon_1']
        self.nombre_pokemon_2 = self.diccionario_pokemon['nombre_pokemon_2']
        self.numero_pokemon_1 = self.diccionario_pokemon['numero_pokemon_1']
        self.numero_pokemon_2 = self.diccionario_pokemon['numero_pokemon_2']
        self.stats_pokemon_1 = self.diccionario_pokemon['stats_1']
        self.stats_pokemon_2 = self.diccionario_pokemon['stats_2']
        self.opcion_ia = decision(self.test_label)
        self.pokemon_A = PokemonStats(120 , 100, self.stats_pokemon_1, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/"+ str(self.numero_pokemon_1) +".png")
        self.pokemon_B = PokemonStats(625 , 100, self.stats_pokemon_2,"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/"+ str(self.numero_pokemon_2) +".png")
        self.player_1 = Player(1, -20, 650, self.nombre_pokemon_1, self.nombre_pokemon_2)
        self.player_2 = Player(2, 750, 650, self.nombre_pokemon_1, self.nombre_pokemon_2)
        self.respuesta_correcta = self.diccionario_pokemon['ganador_real']
        self.ahora_juega_tu = False
        self.ronda_puede_terminar = False

    def draw_menu(self):
        vs = font.render("VS", 1, (255,255,255))
        text_select = font_med.render("Elige al ganador", 1, (255,255,255))
        self.window.blit(vs, (510, 400))
        self.window.blit(text_select, (445, 670))
        self.pokemon_A.draw_pokemon_stats(self.window, self.nombre_pokemon_1)
        self.pokemon_B.draw_pokemon_stats(self.window, self.nombre_pokemon_2)
        self.player_1.draw_player(self.window)
        self.player_2.draw_player(self.window)
        
    def juega_ia(self):
        if self.ahora_juega_tu == True:
            self.player_2.answer(self.opcion_ia[0][0])
            self.ronda_puede_terminar = True
    
    def select_option(self, pos):
        self.player_1.select_option(pos)
        
    def click_option(self, pos):
        self.player_1.click_option(pos)
        self.ahora_juega_tu = True
        
    def ronda_terminada(self):
        if self.player_1.validar_opciones() > 0 and self.player_2.validar_opciones() > 0:
            return True
        return False

    def ganador(self):
        if self.player_1.opcion_elegida() == self.respuesta_correcta:
            self.player_1.sumar_puntos()
        if self.player_2.opcion_elegida() == self.respuesta_correcta:
            self.player_2.sumar_puntos()

    def print_winner_player(self):
        winner = font2.render("GANA PLAYER 1", 1, (255,255,255))
        self.window.blit(winner_screen, (0, 0))
        self.window.blit(winner, (450, 200))

    def print_winner_ia(self):
        winner = font2.render("GANA IA", 1, (255,255,255))
        self.window.blit(winner_screen, (0, 0))
        self.window.blit(winner, (450, 200))

    def print_draw(self):
        winner = font.render("EMPATE", 1, (255,255,255))
        self.window.blit(winner_screen, (0, 0))
        self.window.blit(winner, (450, 200))

    def terminar_juego(self):
        if self.player_1.get_puntos() == 10 and self.player_2.get_puntos() < 10:
            self.print_winner_player()
            self.terminado = True
        if self.player_2.get_puntos() == 10 and self.player_1.get_puntos() < 10:
            self.print_winner_ia()
        if self.player_2.get_puntos() == 10 and self.player_1.get_puntos() == 10:
            self.print_draw()
