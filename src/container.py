from dataclasses import dataclass

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore

from system_components.control import Control
from system_components.frame import frame_height, frame_width
from system_components.status import GameState
from system_components.Vector import Vector


@dataclass
class Colors:
    BACKGROUND_COLOR: str = "blue"
    SNAKE_COLOR: str = "red"


class Snake_Main(Control, GameState):
    def __init__(self, *, x_pos=1, y_pos=0, width=frame_width, height=frame_height):
        super(Snake_Main, self).__init__(
            width=frame_width,
            height=frame_height,
            x=x_pos,
            y=y_pos,
            debug=False,
        )

        self.segment_list = []
        self.width = width
        self.height = height
        self.grid = 10
        self.GAME_STATE = True  # We will have to localise this for now i want it here .

        self.position = [
            Vector(self.width // self.internal_grid, self.height // self.internal_grid),
            Vector(self.width // self.internal_grid, self.height // self.internal_grid),
            Vector(self.width // self.internal_grid, self.height // self.internal_grid),
            Vector(self.width // self.internal_grid, self.height // self.internal_grid),
        ]

        isinstance(x_pos, int)
        isinstance(y_pos, int)

        self.dir = Vector(x_pos, y_pos)
        self.eat = False
        self.segment_list = []

    def changer(self, x, y):
        self.dir.x, self.dir.y = x, y

    def change_dir(self, direction):
        if direction == "right":
            self.changer(1, 0)
        elif direction == "left":
            self.changer(-1, 0)
        elif direction == "up":
            self.changer(0, -1)
        elif direction == "down":
            self.changer(0, 1)

    def _position_compare_x(self):
        return self.position[-1].x + self.dir.x

    def _position_compare_y(self):
        return self.position[-1].y + self.dir.y

    def _move(self):
        if self._position_compare_x() > self.width // self.grid:
            self.position.append(Vector(1, self._position_compare_y()))

        elif self._position_compare_x() < 1:
            self.position.append(Vector(60, self._position_compare_x()))

        elif self._position_compare_y() > self.height // self.grid:
            self.position.append(Vector(self._position_compare_x(), 1))

        elif self._position_compare_y() < 1:
            self.position.append(Vector(self._position_compare_x(), 60))

        else:
            self.position.append(
                Vector(self._position_compare_x(), self._position_compare_y())
            )

    def key_down(self, key):
        if key == simplegui.KEY_MAP["right"] and self.dir.x == 0:
            self.change_dir("right")
        elif key == simplegui.KEY_MAP["left"] and self.dir.x == 0:
            self.change_dir("left")
        elif key == simplegui.KEY_MAP["up"] and self.dir.y == 0:
            self.change_dir("up")
        elif key == simplegui.KEY_MAP["down"] and self.dir.y == 0:
            self.change_dir("down")

    def update_self(self):
        pass

    def draw_self(self, canvas):
        for k in self.segment_list:
            x = [i.get_p() for i in k]
            canvas.draw_polygon(x, 1, "DarkRed", "red")

        for pos in self.position:
            segment = [
                Vector(pos.x * self.grid - self.grid, pos.y * self.grid),
                Vector(pos.x * self.grid, pos.y * self.grid),
                Vector(pos.x * self.grid, pos.y * self.grid - self.grid),
                Vector(pos.x * self.grid - self.grid, pos.y * self.grid - self.grid),
            ]
            self.segment_list.append(segment)

    def timer_handler(self):
        self._move()  # This is teh update system

        if not self.eat:
            self.position.pop(0)
        self.eat = False


def main() -> None:
    snake = Snake_Main()
    # create frame and add a button and labels
    frame = simplegui.create_frame("Snake", frame_width, frame_height)

    timer = simplegui.create_timer(GameState.SPEED, snake.timer_handler)

    # register event handlers
    frame.set_keydown_handler(snake.key_down)
    frame.set_draw_handler(snake.draw_self)

    # get things rolling
    timer.start()
    frame.start()


if __name__ == "__main__":
    main()
