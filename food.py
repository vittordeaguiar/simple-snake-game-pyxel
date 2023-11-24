import pyxel
from game_object import GameObject

class Food(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self):
        pyxel.rect(self.x * 10, self.y * 10, 10, 10, 10)
