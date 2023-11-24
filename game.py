import pyxel
import random
from snake import Snake
from food import Food
from direction import Direction

class Game:
    def __init__(self):
        self.snake = Snake(5, 5)
        self.food = Food(random.randint(0, 39), random.randint(0, 39))
        self.screen_width = 40
        self.screen_height = 40
        self.update_interval = 3  # Tornar o jogo mais rápido
        self.frame_count = 0
        self.game_state = "START"  # Começar com a tela de boas-vindas
        pyxel.init(400, 400,)
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_state == "PLAYING":
            self.frame_count += 1
            if self.frame_count % self.update_interval == 0:
                self.snake.update()

                # Verifica colisão com as bordas
                if self.snake.check_collision_with_bounds(self.screen_width, self.screen_height):
                    self.game_state = "GAME_OVER"

                # Verifica se a cobra comeu a comida
                if self.snake.body[0] == (self.food.x, self.food.y):
                    self.snake.length += 1
                    self.food = Food(random.randint(0, 39), random.randint(0, 39))

            # Controles
            if pyxel.btn(pyxel.KEY_W):
                self.snake.direction = Direction.UP
            elif pyxel.btn(pyxel.KEY_S):
                self.snake.direction = Direction.DOWN
            elif pyxel.btn(pyxel.KEY_A):
                self.snake.direction = Direction.LEFT
            elif pyxel.btn(pyxel.KEY_D):
                self.snake.direction = Direction.RIGHT

        elif self.game_state == "START":
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.game_state = "PLAYING"

        elif self.game_state == "GAME_OVER":
            if pyxel.btnp(pyxel.KEY_R):
                self.restart_game()

    def draw(self):
        pyxel.cls(0)
        if self.game_state == "PLAYING":
            self.snake.draw()
            self.food.draw()
        elif self.game_state == "START":
            self.draw_start_screen()
        elif self.game_state == "GAME_OVER":
            self.draw_game_over_screen()

    def draw_start_screen(self):
        pyxel.text(150, 200, "Snake Game", pyxel.frame_count % 16)
        pyxel.text(130, 220, "Press Enter to Start", 7)

    def draw_game_over_screen(self):
        pyxel.text(160, 200, "GAME OVER", 8)
        pyxel.text(120, 220, "Press R to Restart", 7)

    def restart_game(self):
        self.snake = Snake(5, 5)
        self.food = Food(random.randint(0, 39), random.randint(0, 39))
        self.game_state = "PLAYING"

if __name__ == "__main__":
    Game()
