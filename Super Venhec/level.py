import pygame
from tiles import Tile
from settings import tile_size
from player import Player

class Level:
    def __init__(self,level_data,surface):

        # Configuração do Level
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group() # Plataformas do jogo, o mapa
        self.player = pygame.sprite.GroupSingle()


        #Explorando onde o mapeamento está: em linhas e colunas,tipo coordenadas de batalha naval
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size #multiplica para ter tamanho do retangulo
                y = row_index * tile_size
                
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 200:
            self.world_shift = 8 
            player.speed = 0 

    def run(self):
        # Level tiles
        self.tiles.update(self.world_shift) #Por padrão é 0 e deixa estatico
        self.tiles.draw(self.display_surface)

        # Player
        self.player.update()
        self.player.draw(self.display_surface)