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
    snake.append((x, y + (i * SIZE), SIZE, SIZE))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((92, 64, 51))

    # draw snake
    for i, rect in enumerate(snake):
        color = "dark green"
        if i == 0:
            color = "green"
        pygame.draw.rect(screen, color, rect, 2, border_radius=4)

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

    if dt > 500:
        dt = 0
        x += dx * SIZE
        y += dy * SIZE

        snake.insert(0, (x, y, SIZE, SIZE))
        snake.pop()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt += clock.tick(60)

pygame.quit()