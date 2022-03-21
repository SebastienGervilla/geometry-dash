import json
from objects.block import Block

import pygame
SETTINGS = json.load(open('settings.json'))

class Player(pygame.sprite.Sprite):

    def __init__(self, size: tuple, velocity: tuple, start_pos: tuple, image: pygame.Surface):
        self.image = image
        self.rect = self.image.get_rect(topleft=start_pos)
        self.player_sprite = pygame.sprite.Group()
        super().__init__(self.player_sprite)

        self.size = size
        self.velocity = list(velocity)
        self.pos = list(start_pos)
        self.on_ground = False
        self.is_jumping = False
        self.jump_height = 20

        self.is_dead = False
        self.has_won = False

    def jump(self):
        self.is_jumping = True

    def move(self):
        self.velocity[1] -= self.jump_height

    def update(self, game_size: tuple, platforms: pygame.sprite.Group):
        if self.is_jumping:
            if self.on_ground:
                self.move()
                self.on_ground = False

        if not self.on_ground:
            self.velocity[1] += SETTINGS['Gravity']

        if self.velocity[1] > 50:
            self.velocity[1] = 50

        self.collide(0, platforms)

        self.rect.y += self.velocity[1]

        self.on_ground = False

        self.collide(self.velocity[1], platforms)

        # temporary collide only with ground

        if self.rect.y >= game_size[1] - self.size[1]:
            self.on_ground = True
            self.is_jumping = False
            self.rect.y = game_size[1] - self.size[1]

    def setOnGround(self, on_ground):
        self.on_ground = on_ground

    def collide(self, vel: int, platforms: pygame.sprite.Group):

        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                
                if isinstance(p, Block):
                    if vel > 0:
                        self.velocity[1] = 0
                        self.on_ground = True
                        self.is_jumping = False
                    elif vel < 0:
                        self.rect.top = p.rect.bottom
                    else:
                        self.velocity[0] = 0
                        self.rect.right = p.rect.left
                        self.is_dead = True

    def getPos(self):
        return self.pos

    def getSize(self):
        return self.size
    
    def getRect(self):
        return self.rect

    def getVel(self):
        return self.velocity

    def getPlayerSprite(self):
        return self.player_sprite

    def getOutcome(self):
        return (self.has_won, self.is_dead)