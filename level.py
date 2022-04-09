import csv
import pygame
from player import Player
from objects.block import Block

class Level():

    def __init__(self, screen_size: tuple, game_size: tuple, image_set: dict, player: Player):
        self.screen_size = screen_size
        self.game_size = game_size
        self.image_set = image_set
        self.objects = pygame.sprite.Group()
        self.player = player
        self.generateMap()
        self.setLevel()
        
    def setLevel(self):
        x = 0
        y = self.game_size[1]
        for row in reversed(self.lvl):
            for col in row:
                if col == "0":
                    Block(self.image_set["block"], (x , y) , self.objects)
                x += 32
            y -= 32
            x = 0


    def generateMap(self):
        self.lvl = []
        with open("levels/Level2.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in spamreader:
                self.lvl.append(row)
        return self.lvl

    def update(self):
        self.player.update(self.objects)
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