import time
import pygame


class UserInterface:

    def __init__(self, game_area: tuple, block_size: int) -> None:
        self.__game_width, self.__game_height = game_area

        self.__width = self.__game_width + 200
        self.__height = self.__game_height

        self.__block_size = block_size
        self.__clock = None
        self.__start_time = None
        self.__screen_main = pygame.display.set_mode((self.__width, self.__height))
        self.__screen_game = self.__screen_main.subsurface(
            pygame.Rect(((self.__width - self.__game_width) / 2, (self.__height - self.__game_height) / 2,
                         self.__game_width, self.__game_height))
        )
        self.__game_over = None
        self.__pause = None
        self.__score = 0
        self.__score_max = 0
        self.__fruits = None
        self.__snake = None

        self.reset()

    def reset(self):
        self.__game_over = False
        self.__pause = False
        self.__score = 0
        self.__fruits = []
        self.__snake = []

        self.__clock = pygame.time.Clock()

        self.__init_items()
        self.__start_time = time.perf_counter()

    def set_snake(self, snake: list) -> None:
        self.__snake = snake

    def set_fruits(self, fruits: list) -> None:
        self.__fruits = fruits

    def set_game_over(self, game_over: bool) -> None:
        self.__game_over = game_over

    def set_score(self, score: int) -> None:
        self.__score = score
        self.__score_max = max([self.__score, self.__score_max])

    def set_pause(self, pause: bool):
        self.__pause = pause

    def tick(self) -> None:
        if not self.__game_over and not self.__pause:
            # fill the screen with a color to wipe away anything from last frame
            self.__screen_main.fill((8, 56, 32))
            self.__screen_game.fill("dark green")

            self.__draw_snake()
            self.__draw_fruits()

            self.__draw_scores()
            self.__draw_time()

        self.__draw_screen_pause()
        self.__draw_screen_game_over()

        # flip() the display to put your work on screen
        pygame.display.flip()

    def __draw_snake(self):
        for i, (snakeX, snakeY) in enumerate(self.__snake):
            color = "green"
            width = 2
            if i == 0:
                width = 0
            pygame.draw.rect(
                self.__screen_game, color,
                (snakeX * self.__block_size, snakeY * self.__block_size, self.__block_size, self.__block_size), width,
                border_radius=4
            )

    def __draw_fruits(self):
        for fruit in self.__fruits:
            fruitX, fruitY = fruit.position()
            pygame.draw.rect(
                self.__screen_game, fruit.color(),
                (fruitX * self.__block_size, fruitY * self.__block_size, self.__block_size, self.__block_size),
                border_radius=int(self.__block_size / 2)
            )

    def __draw_scores(self):
        score_txt = self.__font.render("SCORE:", True, (255, 255, 255))
        score_num = self.__font.render(str(self.__score), True, (255, 255, 255))
        self.__screen_main.blit(score_txt, (10, 20))
        self.__screen_main.blit(score_num, (10, 40))

        score_max_txt = self.__font.render("SCORE MAX:", True, (255, 255, 255))
        score_max_num = self.__font.render(str(self.__score_max), True, (255, 255, 255))
        self.__screen_main.blit(score_max_txt, (self.__width - 100 + 10, 20))
        self.__screen_main.blit(score_max_num, (self.__width - 100 + 10, 40))

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
        if self.__pause and not self.__game_over:
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
        if self.__game_over:
            self.__game_over_screen.fill("red")
            game_over_txt = self.__font_big.render("GAME OVER", True, (255, 255, 255))
            self.__game_over_screen.blit(
                game_over_txt,
                (
                    (self.__game_over_screen.get_width() - game_over_txt.get_width()) / 2,
                    (self.__game_over_screen.get_height() - game_over_txt.get_height()) / 2,
                )
            )

    def __init_items(self):
        self.__font = pygame.font.Font("ui/fonts/homevideo/HomeVideo-Regular.otf", 16)
        self.__font_big = pygame.font.Font("ui/fonts/homevideo/HomeVideo-Regular.otf", 60)

        self.__init_screen_pause()
        self.__init_screen_game_over()
