from random import randrange


class Fruit:
    def __init__(self, position: tuple, color: str):
        self.__position = position
        self.__color = color

    def position(self) -> tuple:
        return self.__position

    def color(self) -> str:
        return self.__color


class Apple(Fruit):
    def __init__(self, position: tuple):
        super().__init__(position, 'red')

    @staticmethod
    def spawn(width: int, height: int):
        return Apple((randrange(width), randrange(height)))


class Banana(Fruit):
    def __init__(self, position: tuple):
        super().__init__(position, 'yellow')

    @staticmethod
    def spawn(width: int, height: int):
        return Banana((randrange(width), randrange(height)))
