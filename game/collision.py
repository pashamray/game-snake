class CollisionDetector:
    @staticmethod
    def check_wall_collision(position: tuple, width: int, height: int):
        x, y = position
        return x < 0 or x >= width or y < 0 or y >= height

    @staticmethod
    def check_self_collision(snake_body: list):
        head = snake_body[0]
        return head in snake_body[1:]

    @staticmethod
    def check_fruit_collision(snake_head: tuple, fruits: list):
        return snake_head in [fruit.position() for fruit in fruits]
