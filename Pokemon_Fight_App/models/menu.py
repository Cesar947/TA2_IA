  
from models.pokemon_stats import PokemonStats


class Menu():
    def __init__(self, window):
        self.window = window
        self.pokemon_A = PokemonStats(250 , 330)
        self.pokemon_B = PokemonStats(650 , 330)

    def draw_menu(self):
        self.pokemon_A.draw_pokemon_stats(self.window)
        self.pokemon_B.draw_pokemon_stats(self.window)