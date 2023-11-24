import pyxel
from game_object import GameObject
from direction import Direction

class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.body = [(x, y)]
        self.length = 1
        self.direction = Direction.RIGHT

    def update(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        self.body.insert(0, new_head)
        if len(self.body) > self.length:
            self.body.pop()

    def draw(self):
        for x, y in self.body:
            pyxel.rect(x * 10, y * 10, 10, 10, 14)

    def check_collision_with_bounds(self, screen_width, screen_height):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_y < 0 or head_x >= screen_width or head_y >= screen_height:
            return True
        return False
