import json
from objects.block import Block
from math import ceil

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
        self.jump_height = 13
        self.angle = 0

        self.is_dead = False
        self.has_won = False

    def jump(self):
        self.is_jumping = True

    def move(self):
        self.velocity[1] -= self.jump_height

    def update(self, platforms: pygame.sprite.Group):
        if self.is_jumping:
            if self.on_ground:
                self.move()
                self.on_ground = False

        if not self.on_ground:
            # if self.velocity[1] > 0:
            #     self.angle += .1
            pass
        self.velocity[1] += SETTINGS['Gravity']

        if self.velocity[1] > 50:
            self.velocity[1] = 50

        self.collide(0, platforms)

        self.rect.y += self.velocity[1]

        self.on_ground = False

        self.collide(self.velocity[1], platforms)

        self.calculateAngle()

    def collide(self, vel: int, platforms: pygame.sprite.Group):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, Block):
                    if vel > 0:
                        self.rect.bottom = p.rect.top
                        self.velocity[1] = 0
                        self.on_ground = True
                        self.is_jumping = False
                    elif vel < 0:
                        self.velocity[0] = 0
                        self.rect.top = p.rect.bottom
                        self.is_dead = True
                    else:
                        self.velocity[0] = 0
                        self.rect.right = p.rect.left
                        self.is_dead = True

    def calculateAngle(self):
        if not self.on_ground:
            if self.angle < -360: self.angle += 360
            self.angle = round(self.angle - 7.2, 1)
        else:
            multiplier = 1
            closest_angle = round(self.angle / 90) * 90
            if closest_angle - self.angle <= 0: multiplier = -1
            if (self.angle + 7.2 * multiplier) * multiplier > (closest_angle) * multiplier:
                self.angle += closest_angle - self.angle
            else:
                self.angle += 7.2 * multiplier



    def getPos(self):
        return self.pos

    def getSize(self):
        return self.size
    
    def getRect(self):
        return self.rect

    def getVel(self):
        return self.velocity

    def getAngle(self):
        return self.angle

    def getPlayerGroup(self):
        return self.player_sprite

    def getOutcome(self):
        return (self.has_won, self.is_dead)