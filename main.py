import pygame

from ui.userinterface import UserInterface
from game.snake import SnakeDirection
from game.game import Game

# pygame setup
pygame.init()
clock = pygame.time.Clock()

user_interface = UserInterface()
game = Game((int(600 / 20), int(600 / 20)))

pause = False
direction = SnakeDirection.DOWN

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_w:
                direction = SnakeDirection.UP
            if event.key == pygame.K_s:
                direction = SnakeDirection.DOWN
            if event.key == pygame.K_d:
                direction = SnakeDirection.RIGHT
            if event.key == pygame.K_a:
                direction = SnakeDirection.LEFT
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if not pause:
        game.tick(direction)

    user_interface.set_snake(game.get_snake())
    user_interface.set_fruits(game.get_fruits())
    user_interface.set_score(game.get_score())
    user_interface.set_game_over(game.get_game_over())
    user_interface.set_pause(pause)
    user_interface.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)