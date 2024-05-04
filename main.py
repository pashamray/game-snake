from random import randrange
import pygame

WIDTH = 800
HEIGHT = 600

SIZE = 20

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
x = screen.get_width() / 2
y = screen.get_height() / 2

dt = 0
dx = 0
dy = -1

dir_up = pygame.K_w
dir_down = pygame.K_s
dir_left = pygame.K_a
dir_right = pygame.K_d

snake = []
snake_len = 3

for i in range(snake_len):
    snake.append((x, y + (i * SIZE)))

apple = (randrange(0, WIDTH, SIZE), randrange(0, HEIGHT, SIZE))

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark green")

    # draw snake
    for i, (snakeX, snakeY) in enumerate(snake):
        color = "green"
        width = 2
        if i == 0:
            width = 0
        pygame.draw.rect(screen, color, (snakeX, snakeY, SIZE, SIZE), width, border_radius=4)

    # draw apple
    (appleX, appleY) = apple
    pygame.draw.rect(screen, "red", (appleX, appleY, SIZE, SIZE), border_radius=int(SIZE / 2))

    moves = pygame.key.get_pressed()
    moves_x = (moves[dir_right] - moves[dir_left])
    moves_y = (moves[dir_down] - moves[dir_up])

    if dx == 0 and moves_x != 0:
        dx = moves_x
        dy = 0
    if dy == 0 and moves_y != 0:
        dx = 0
        dy = moves_y

    if dt > 200:
        dt = 0
        x += dx * SIZE
        y += dy * SIZE

        if x < 0:
            x = WIDTH - SIZE
        if x > WIDTH - SIZE:
            x = 0

        if y < 0:
            y = HEIGHT - SIZE
        if y > HEIGHT - SIZE:
            y = 0

        if snake[0] != apple:
            snake.pop()
        if snake[0] == apple:
            apple = (randrange(0, WIDTH, SIZE), randrange(0, HEIGHT, SIZE))
        snake.insert(0, (x, y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt += clock.tick(60)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()