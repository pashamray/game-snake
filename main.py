from random import randrange
import pygame

from game import Snake

WIDTH = 800
HEIGHT = 600
GAME_WIDTH = 600
GAME_HEIGHT = 600

SIZE = 20

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_screen = screen.subsurface(pygame.Rect(((WIDTH - GAME_WIDTH) / 2, (HEIGHT - GAME_HEIGHT) / 2, GAME_WIDTH, GAME_HEIGHT)))
font = pygame.font.SysFont("notosansmono", 20)

print(pygame.font.get_fonts())

clock = pygame.time.Clock()
running = True

game = Snake((game_screen.get_width() / SIZE, game_screen.get_height() / SIZE))

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    game_screen.fill("dark green")

    # draw snake
    for i, (snakeX, snakeY) in enumerate(game.get_snake()):
        color = "green"
        width = 2
        if i == 0:
            width = 0
        pygame.draw.rect(game_screen, color, (snakeX * SIZE, snakeY * SIZE, SIZE, SIZE), width, border_radius=4)

    # draw apples
    for i, (appleX, appleY) in enumerate(game.get_apples()):
        pygame.draw.rect(game_screen, "red", (appleX * SIZE, appleY * SIZE, SIZE, SIZE), border_radius=int(SIZE / 2))

    # draw scores
    score_txt = font.render("SCORE:", True, (255, 255, 255))
    score_num = font.render(str(game.get_score()), True, (255, 255, 255))
    screen.blit(score_txt, (20, 20))
    screen.blit(score_num, (20, 40))

    moves = pygame.key.get_pressed()
    if moves[pygame.K_w]:
        game.move_up()

    if moves[pygame.K_s]:
        game.move_down()

    if moves[pygame.K_d]:
        game.move_right()

    if moves[pygame.K_a]:
        game.move_left()

    # flip() the display to put your work on screen
    pygame.display.flip()

    game.tick()
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(1000)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
