from asyncio.windows_events import NULL
import os

import pygame

class ImageManager():

    def __init__(self):
        self.default_size = (32, 32)
        self.loadImages()

    def loadImages(self):
        self.image_set = {}
        self.image_set["player"] = pygame.image.load(os.path.join("assets", "avatar.png"))
        self.image_set["block"] = pygame.image.load(os.path.join("assets", "block.png"))

        if self.image_set == NULL:
            return

        for img_name, img in self.image_set.items():
            self.image_set[img_name] = self.resizeImage(img, self.default_size)


    def resizeImage(self, img, size):
        resized_img = pygame.transform.smoothscale(img, size)
        return resized_img

    def getImages(self):
        return self.image_set