from game.collision import CollisionDetector
from game.fruits import Apple
from game.snake import Snake, SnakeDirection


class Game:
    def __init__(self, area: tuple, block_size: int):
        self.__width = int(area[0] / block_size)
        self.__height = int(area[1] / block_size)

        init_position = (self.__width // 2, self.__height // 2)

        self.__snake = Snake(init_position, 3)
        self.__fruits = [Apple.spawn(self.__width, self.__height) for _ in range(2)]
        self.__score = 0
        self.__game_over = False

    def get_snake(self):
        return self.__snake.body

    def get_fruits(self):
        return [fruit for fruit in self.__fruits]

    def get_score(self):
        return self.__score

    def get_game_over(self):
        return self.__game_over

    def tick(self, direction: SnakeDirection):
        if self.__game_over:
            return

        self.__snake.change_direction(direction)
        self.__snake.move()

        if CollisionDetector.check_wall_collision(self.__snake.body[0], self.__width, self.__height) or \
                CollisionDetector.check_self_collision(self.__snake.body):
            self.__game_over = True
            return

        if CollisionDetector.check_fruit_collision(self.__snake.body[0], self.__fruits):
            self.__snake.grow()
            self.__score += 1
            self.__fruits = [fruit for fruit in self.__fruits if fruit.position() != self.__snake.body[0]]
            self.__fruits.append(Apple.spawn(self.__width, self.__height))