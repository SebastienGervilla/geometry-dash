from imageManager import ImageManager
from game import Game
from level import Level
from player import Player
WIDTH, HEIGHT = 1000, 500
STARTING_POS = (100, 100)
PLAYER_SIZE = (32, 32)

def main():
    screen_size = (WIDTH, HEIGHT)
    game_size = (WIDTH, HEIGHT)
    image_manager = ImageManager()
    player = Player(PLAYER_SIZE, (6, 0), (game_size[0] / 2 - PLAYER_SIZE[0] / 2, game_size[1] - PLAYER_SIZE[1]), image_manager.getImages()["player"])
    level = Level(screen_size, game_size, image_manager.getImages(), player)
    game = Game(level, screen_size, game_size)
    game.run()

if __name__ == "__main__":
    main()