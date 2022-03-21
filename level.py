import pygame
from player import Player
from objects.block import Block

class Level():

    def __init__(self, screen_size: tuple, game_size: tuple, image_set: dict, player: Player):
        self.screen_size = screen_size
        self.game_size = game_size
        self.image_set = image_set
        self.objects = pygame.sprite.Group()
        self.setLevel()
        self.player = player
        
    def setLevel(self):
        Block(self.image_set["block"], (self.game_size[0], self.game_size[1] - self.image_set["block"].get_height()) , self.objects)

    def update(self):
        self.player.update(self.game_size, self.objects)
        if self.player.getOutcome()[0]:
            pass
        if self.player.getOutcome()[1]:
            print("-------------------\nYou lost\n-------------------")
            quit()
        self.move_map()

    def move_map(self):
        for object in self.objects:
            object.rect.x -= self.player.getVel()[0]

    def getObjects(self):
        return self.objects