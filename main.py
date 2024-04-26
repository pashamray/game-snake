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
dt = 0
dx = 0
dy = -1
x = screen.get_width() / 2
y = screen.get_height() / 2

snake = []
snake_len = 3

for i in range(snake_len):
    snake.append((x, y + (i * SIZE)))

apple = (randrange(0, WIDTH, SIZE), randrange(0, HEIGHT, SIZE))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        dx = 0
        dy = -1
    if keys[pygame.K_s]:
        dx = 0
        dy = 1
    if keys[pygame.K_a]:
        dx = -1
        dy = 0
    if keys[pygame.K_d]:
        dx = 1
        dy = 0

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

pygame.quit()