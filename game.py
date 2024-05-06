import pygame

from snake import Snake


class Game:

    def __init__(self) -> None:
        width = 800
        height = 600
        game_width = 600
        game_height = 600

        self.__size = 20
        # pygame setup
        pygame.init()
        self.__screen = pygame.display.set_mode((width, height))
        self.__game_screen = self.__screen.subsurface(
            pygame.Rect(((width - game_width) / 2, (height - game_height) / 2, game_width, game_height))
        )
        self.__font = pygame.font.SysFont("notosansmono", 20)

        self.__clock = pygame.time.Clock()

        self.__game = Snake((self.__game_screen.get_width() / self.__size, self.__game_screen.get_height() / self.__size))
        self.__running = True

    def run(self) -> None:
        while self.__running:
            # fill the screen with a color to wipe away anything from last frame
            self.__screen.fill((2, 48, 32))
            self.__game_screen.fill("dark green")

            # draw snake
            for i, (snakeX, snakeY) in enumerate(self.__game.get_snake()):
                color = "green"
                width = 2
                if i == 0:
                    width = 0
                pygame.draw.rect(self.__game_screen, color, (snakeX * self.__size, snakeY * self.__size, self.__size, self.__size), width, border_radius=4)

            # draw apples
            for i, (appleX, appleY) in enumerate(self.__game.get_apples()):
                pygame.draw.rect(self.__game_screen, "red", (appleX * self.__size, appleY * self.__size, self.__size, self.__size),
                                 border_radius=int(self.__size / 2))

            # draw scores
            score_txt = self.__font.render("SCORE:", True, (255, 255, 255))
            score_num = self.__font.render(str(self.__game.get_score()), True, (255, 255, 255))
            self.__screen.blit(score_txt, (20, 20))
            self.__screen.blit(score_num, (20, 40))

            moves = pygame.key.get_pressed()
            if moves[pygame.K_w]:
                self.__game.move_up()

            if moves[pygame.K_s]:
                self.__game.move_down()

            if moves[pygame.K_d]:
                self.__game.move_right()

            if moves[pygame.K_a]:
                self.__game.move_left()

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.__game.tick()
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.__clock.tick(1000)

            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False

        pygame.quit()
