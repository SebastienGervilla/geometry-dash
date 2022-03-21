import pygame
from level import Level

class Game():

    def __init__(self, level: Level, screen_size: tuple, game_size: tuple) -> None:
        self.screen_size = screen_size
        self.game_size = game_size
        self.speed = 5
        self.clock = pygame.time.Clock()
        self.level = level

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.is_running = True
        while (self.is_running):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.is_running = False
            self.handleInputs()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def handleInputs(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE]):
            self.level.player.jump()

    def update(self):
        self.level.update()

    def draw(self):
        self.screen.fill((255, 255, 255))

        self.level.getObjects().draw(self.screen)
        self.level.player.getPlayerSprite().draw(self.screen)