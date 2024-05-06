from random import randrange


class Snake:
    __width = 0
    __height = 0

    __x = 0
    __y = 0

    __score = 0

    __snake_len = 0
    __snake = []

    __apples_count = 0
    __apples = []

    __moves = {"up": False, "down": False, "right": False, "left": False}

    __tick_count = 0

    def __init__(self, area: tuple):
        [self.__width, self.__height] = area

        self.__x = int(self.__width / 2)
        self.__y = int(self.__height / 2)

        self.__snake_len = 3
        for i in range(0, self.__snake_len):
            self.__snake.append((self.__x, self.__y + i))

        self.__apples_count = 2
        for i in range(0, self.__apples_count):
            self.__apples.append((randrange(0, self.__width), randrange(0, self.__height)))

        self.__moves = {"up": True, "down": False, "right": False, "left": False}

    def get_snake(self) -> list:
        return self.__snake

    def get_apples(self) -> list:
        return self.__apples

    def get_score(self) -> int:
        return self.__score

    def move_up(self) -> None:
        if not self.__moves["down"]:
            self.__moves = {"up": True, "down": False, "right": False, "left": False}

    def move_down(self) -> None:
        if not self.__moves["up"]:
            self.__moves = {"up": False, "down": True, "right": False, "left": False}

    def move_right(self) -> None:
        if not self.__moves["left"]:
            self.__moves = {"up": False, "down": False, "right": True, "left": False}

    def move_left(self) -> None:
        if not self.__moves["right"]:
            self.__moves = {"up": False, "down": False, "right": False, "left": True}

    def tick(self) -> None:
        self.__tick_count += 1

        if self.__tick_count > 200:
            self.__tick_count = 0

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

            self.__snake.insert(0, (self.__x, self.__y))
            last = self.__snake.pop()
            try:
                hint = self.__apples.index(self.__snake[0])
                self.__apples.remove(self.__snake[0])

                self.__score += 1
                self.__apples.append((randrange(0, self.__width), randrange(0, self.__height)))

                self.__snake.append(last)
            except ValueError:
                pass
