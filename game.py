import time

import pygame

from snakegame import SnakeGame, SnakeDirection


class Game:

    def __init__(self) -> None:
        width = 800
        height = 600
        game_width = 600
        game_height = 600

        self.__size = 20

        # pygame setup
        pygame.init()
        self.__clock = pygame.time.Clock()
        self.__screen_main = pygame.display.set_mode((width, height))
        self.__screen_game = self.__screen_main.subsurface(
            pygame.Rect(((width - game_width) / 2, (height - game_height) / 2, game_width, game_height))
        )

        self.__init_items()

        self.__game = SnakeGame(
            (
                int(self.__screen_game.get_width() / self.__size),
                int(self.__screen_game.get_height() / self.__size)
            )
        )

        self.__pause = False
        self.__start_time = time.perf_counter()

    def run(self) -> None:
        direction = SnakeDirection.UP
        running = True
        dt = 0

        while running:
            if dt > 200:
                dt = 0
                if not self.__game.get_game_over() and not self.__pause:
                    self.__game.tick(direction)
            self.__draw_items()

            # flip() the display to put your work on screen
            pygame.display.flip()

            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt += self.__clock.tick(100)

            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.__pause = not self.__pause
                    if event.key == pygame.K_w:
                        direction = SnakeDirection.UP
                    if event.key == pygame.K_s:
                        direction = SnakeDirection.DOWN
                    if event.key == pygame.K_d:
                        direction = SnakeDirection.RIGHT
                    if event.key == pygame.K_a:
                        direction = SnakeDirection.LEFT
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

    def __draw_snake(self):
        for i, (snakeX, snakeY) in enumerate(self.__game.get_snake()):
            color = "green"
            width = 2
            if i == 0:
                width = 0
            pygame.draw.rect(
                self.__screen_game, color,
                (snakeX * self.__size, snakeY * self.__size, self.__size, self.__size), width,
                border_radius=4
            )

    def __draw_apples(self):
        for i, (appleX, appleY) in enumerate(self.__game.get_apples()):
            pygame.draw.rect(
                self.__screen_game, "red",
                (appleX * self.__size, appleY * self.__size, self.__size, self.__size),
                border_radius=int(self.__size / 2)
            )

    def __draw_scores(self):
        score_txt = self.__font.render("SCORE:", True, (255, 255, 255))
        score_num = self.__font.render(str(self.__game.get_score()), True, (255, 255, 255))
        self.__screen_main.blit(score_txt, (10, 20))
        self.__screen_main.blit(score_num, (10, 40))

    def __draw_time(self):
        time_txt = self.__font.render("TIME:", True, (255, 255, 255))
        time_num = self.__font.render(
            time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - self.__start_time)), True, (255, 255, 255))
        self.__screen_main.blit(time_txt, (10, 80))
        self.__screen_main.blit(time_num, (10, 100))

    def __init_screen_pause(self):
        self.__game_pause_screen = self.__screen_main.subsurface(
            pygame.Rect(
                (
                    self.__screen_main.get_width() // 4,
                    self.__screen_main.get_height() // 4,
                    self.__screen_main.get_width() // 2,
                    self.__screen_main.get_height() // 4
                )
            )
        )

    def __draw_screen_pause(self):
        if self.__pause and not self.__game.get_game_over():
            self.__game_pause_screen.fill("green")
            game_pause_txt = self.__font_big.render("PAUSE", True, (255, 255, 255))
            self.__game_pause_screen.blit(
                game_pause_txt,
                (
                    (self.__game_pause_screen.get_width() - game_pause_txt.get_width()) / 2,
                    (self.__game_pause_screen.get_height() - game_pause_txt.get_height()) / 2,
                )
            )

    def __init_screen_game_over(self):
        self.__game_over_screen = self.__screen_main.subsurface(
            pygame.Rect(
                (
                    self.__screen_main.get_width() // 4,
                    self.__screen_main.get_height() // 4,
                    self.__screen_main.get_width() // 2,
                    self.__screen_main.get_height() // 4
                )
            )
        )

    def __draw_screen_game_over(self):
        # draw game over screen
        if self.__game.get_game_over():
            self.__game_over_screen.fill("red")
            game_over_txt = self.__font_big.render("GAME OVER", True, (255, 255, 255))
            self.__game_over_screen.blit(
                game_over_txt,
                (
                    (self.__game_over_screen.get_width() - game_over_txt.get_width()) / 2,
                    (self.__game_over_screen.get_height() - game_over_txt.get_height()) / 2,
                )
            )

    def __draw_items(self):
        if not self.__game.get_game_over() and not self.__pause:
            # fill the screen with a color to wipe away anything from last frame
            self.__screen_main.fill((8, 56, 32))
            self.__screen_game.fill("dark green")

            self.__draw_snake()
            self.__draw_apples()

            self.__draw_scores()
            self.__draw_time()

        self.__draw_screen_pause()
        self.__draw_screen_game_over()

    def __init_items(self):
        self.__font = pygame.font.SysFont("notosansmono", 16)
        self.__font_big = pygame.font.SysFont("notosansmono", 60)

        self.__init_screen_pause()
        self.__init_screen_game_over()
