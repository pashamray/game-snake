from enum import Enum


class SnakeDirection(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class Snake:
    def __init__(self, init_position: tuple, init_length: int):
        self.body = [init_position]
        self.direction = SnakeDirection.UP
        self.grow(init_length - 1)

    def grow(self, segments: int = 1):
        for _ in range(segments):
            self.body.append(self.body[-1])

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == SnakeDirection.UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == SnakeDirection.DOWN:
            new_head = (head_x, head_y + 1)
        elif self.direction == SnakeDirection.RIGHT:
            new_head = (head_x + 1, head_y)
        elif self.direction == SnakeDirection.LEFT:
            new_head = (head_x - 1, head_y)
        else:
            new_head = self.body[0]

        self.body = [new_head] + self.body[:-1]

    def change_direction(self, new_direction: SnakeDirection):
        if (self.direction == SnakeDirection.UP and new_direction != SnakeDirection.DOWN) or \
                (self.direction == SnakeDirection.DOWN and new_direction != SnakeDirection.UP) or \
                (self.direction == SnakeDirection.RIGHT and new_direction != SnakeDirection.LEFT) or \
                (self.direction == SnakeDirection.LEFT and new_direction != SnakeDirection.RIGHT):
            self.direction = new_direction
