import pygame
from objects.gameElements import GameElement

class Block(GameElement):

    def __init__(self, image: pygame.Surface, pos: tuple, *groups):
        super().__init__(image, pos, *groups)