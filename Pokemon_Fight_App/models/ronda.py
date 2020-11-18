from models.pokemon_stats import PokemonStats
from neural_network.backpropagation import seleccionar_enfrentamiento
from neural_network.backpropagation import decision

class Ronda():
    def __init__(self):
        self.diccionario_pokemon, self.test_label = seleccionar_enfrentamiento()
        self.nombre_pokemon_1 = self.diccionario_pokemon['nombre_pokemon_1']
        self.nombre_pokemon_2 = self.diccionario_pokemon['nombre_pokemon_2']
        self.numero_pokemon_1 = self.diccionario_pokemon['numero_pokemon_1']
        self.numero_pokemon_2 = self.diccionario_pokemon['numero_pokemon_2']
        self.stats_pokemon_1 = self.diccionario_pokemon['stats_1']
        self.stats_pokemon_2 = self.diccionario_pokemon['stats_2']
        self.opcion_ia = decision(self.test_label)
        self.pokemon_A = PokemonStats(120 , 100, self.stats_pokemon_1, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/"+ str(self.numero_pokemon_1) +".png")
        self.pokemon_B = PokemonStats(625 , 100, self.stats_pokemon_2,"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/"+ str(self.numero_pokemon_2) +".png")
        self.respuesta_correcta = self.diccionario_pokemon['ganador_real']

    def draw_ronda(self, window):
        self.pokemon_A.draw_pokemon_stats(window, self.nombre_pokemon_1)
        self.pokemon_B.draw_pokemon_stats(window, self.nombre_pokemon_2)

    def get_respuesta_correcta(self):
        return self.respuesta_correcta
    
    def get_nombre_pokemon_1(self):
        return self.nombre_pokemon_1
    
    def get_nombre_pokemon_2(self):
        return self.nombre_pokemon_2
    
    def get_opcion_ia(self):
        return self.opcion_ia[0][0]
