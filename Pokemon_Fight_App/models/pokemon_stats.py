import pygame
from models.component import Component
from models.stat import Stat
import urllib.request
import io

pygame.init()


#img = Image.open(file)

p_name = pygame.image.load('./Pokemon_Fight_App/assets/pokemon_name.png')
img_back = pygame.image.load('./Pokemon_Fight_App/assets/img_back.png')

font = pygame.font.Font(None, 55)

HP, ATTACK, DEFENSE, SPEED = 1 , 2, 3, 4

class PokemonStats(Component):

    def __init__(self, x, y, stats_text, url, width = 500, height = 500):

        Component.__init__(self, x, y, width, height)
        self.hp = Stat(1,x+70,y+360)
        self.atq = Stat(2,x+70,y+400)
        self.defs = Stat(3,x+70,y+440)
        self.vel = Stat(4,x+70,y+480)
        self.name = p_name
        self.back = img_back

        self.file = io.BytesIO(urllib.request.urlopen(url).read())
        self.pokemon = pygame.transform.scale(pygame.image.load(self.file),(220,220))
        self.stats = stats_text



    def draw_pokemon_stats(self, window, text):
        window.blit(self.back, (self.x, self.y))
        window.blit(self.name, (self.x, self.y+280))
        window.blit(self.pokemon, (self.x+70, self.y + 20))
        #Pokemon name
        name_text = font.render(text, 1, (255,255,255))
        window.blit(name_text, (self.x + 100, self.y + 293))
        #Pokemon stats
        self.hp.draw_stat(window, str(self.stats[HP]))
        self.atq.draw_stat(window, str(self.stats[ATTACK]))
        self.defs.draw_stat(window, str(self.stats[DEFENSE]))
        self.vel.draw_stat(window, str(self.stats[SPEED]))


        #window.blit(self.asset, (self.x, self.y))