from random import randrange


class SnakeGame:

    def __init__(self, area: tuple):
        [self.__width, self.__height] = area

        self.__x = int(self.__width / 2)
        self.__y = int(self.__height / 2)

        self.__snake = []
        self.__snake_len = 3
        for i in range(0, self.__snake_len):
            self.__snake.append((self.__x, self.__y + i))

        self.__apples = []
        self.__apples_count = 2
        for i in range(0, self.__apples_count):
            self.__apples.append((randrange(0, self.__width), randrange(0, self.__height)))

        self.__moves = {"up": True, "down": False, "right": False, "left": False}
        self.__moves_allow = False
        self.__score = 0
        self.__game_over = False

    def get_snake(self) -> list:
        return self.__snake

    def get_apples(self) -> list:
        return self.__apples

    def get_score(self) -> int:
        return self.__score

    def get_game_over(self) -> bool:
        return self.__game_over

    def move_up(self) -> None:
        if not self.__moves["down"] and self.__moves_allow:
            self.__moves = {"up": True, "down": False, "right": False, "left": False}
            self.__moves_allow = False

    def move_down(self) -> None:
        if not self.__moves["up"] and self.__moves_allow:
            self.__moves = {"up": False, "down": True, "right": False, "left": False}
            self.__moves_allow = False

    def move_right(self) -> None:
        if not self.__moves["left"] and self.__moves_allow:
            self.__moves = {"up": False, "down": False, "right": True, "left": False}
            self.__moves_allow = False

    def move_left(self) -> None:
        if not self.__moves["right"] and self.__moves_allow:
            self.__moves = {"up": False, "down": False, "right": False, "left": True}
            self.__moves_allow = False

    def tick(self) -> None:
        if self.__game_over:
            return

        if self.__moves["up"]:
            self.__y += -1
            self.__x += 0

        if self.__moves["down"]:
            self.__y += 1
            self.__x += 0

        if self.__moves["right"]:
            self.__y += 0
            self.__x += 1

        if self.__moves["left"]:
            self.__y += 0
            self.__x += -1

        if self.__x >= self.__width or self.__x < 0:
            self.__game_over = True
            return

        if self.__y >= self.__height or self.__y < 0:
            self.__game_over = True
            return

        try:
            self.__snake.index((self.__x, self.__y))
            self.__game_over = True
            return
        except ValueError:
            pass

        self.__snake.insert(0, (self.__x, self.__y))
        snake_first = self.__snake[0]
        snake_last = self.__snake.pop()
        try:
            self.__apples.index(snake_first)
            self.__apples.remove(snake_first)

            self.__score += 1
            self.__apples.append((randrange(0, self.__width), randrange(0, self.__height)))

            self.__snake.append(snake_last)
        except ValueError:
            pass

        self.__moves_allow = True
