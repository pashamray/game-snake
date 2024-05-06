from random import randrange
import pygame

from game import Snake

WIDTH = 800
HEIGHT = 600

SIZE = 20

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

dt = 0
dx = 0
dy = -1

dir_up = pygame.K_w
dir_down = pygame.K_s
dir_left = pygame.K_a
dir_right = pygame.K_d

game = Snake((40, 30))

print(game.get_snake())

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark green")

    # draw snake
    for i, (snakeX, snakeY) in enumerate(game.get_snake()):
        color = "green"
        width = 2
        if i == 0:
            width = 0
        pygame.draw.rect(screen, color, (snakeX * SIZE, snakeY * SIZE, SIZE, SIZE), width, border_radius=4)

    # draw apple
    # (appleX, appleY) = apple
    # pygame.draw.rect(screen, "red", (appleX, appleY, SIZE, SIZE), border_radius=int(SIZE / 2))

    moves = pygame.key.get_pressed()
    if moves[dir_up]:
        game.move_up()

    if moves[dir_down]:
        game.move_down()

    if moves[dir_right]:
        game.move_right()

    if moves[dir_left]:
        game.move_left()


    # if dx == 0 and moves_x != 0:
    #     dx = moves_x
    #     dy = 0
    # if dy == 0 and moves_y != 0:
    #     dx = 0
    #     dy = moves_y
    #
    # if dt > 200:
    #     dt = 0
    #     x += dx * SIZE
    #     y += dy * SIZE
    #
    #     if x < 0:
    #         x = WIDTH - SIZE
    #     if x > WIDTH - SIZE:
    #         x = 0
    #
    #     if y < 0:
    #         y = HEIGHT - SIZE
    #     if y > HEIGHT - SIZE:
    #         y = 0
    #
    #     if snake[0] != apple:
    #         snake.pop()
    #     if snake[0] == apple:
    #         apple = (randrange(0, WIDTH, SIZE), randrange(0, HEIGHT, SIZE))
    #     snake.insert(0, (x, y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    game.tick()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt += clock.tick(1000)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()