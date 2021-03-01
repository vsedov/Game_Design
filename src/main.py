#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8

<<<<<<< HEAD
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from frosch import hook
=======
__author__ = ["Vivian", "Ahmed"]
__status__ = "development"

from dataclasses import dataclass

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore

from system_components.control import Control
from system_components.frame import frame_height, frame_width
from system_components.status import GameState
from system_components.Vector import Vector


@dataclass
class Colors:
    BACKGROUND_COLOR: str = "black"
    SNAKE_COLOR: str = "red"


class Snake_Main(Control, GameState):
    def __init__(
        self, *, x_pos=1, y_pos=0, width=frame_width, height=frame_height, length=5
    ):
        """Init : Local Var

        Main Control of games , assertion of any data will be advised here for debugging

        Args:
            x_pos,y_pos: used for debugging , activate debug = True

            colors: All colors of teh given map , images will be added to this class

            grid: the way the snake will move is via a grid method of 10

            position: start amount of blocks - this can be anything

            eat_control: If eaten speed and increase snake size by one.

            segment_list: control of how many segments there are and controls the class
            such that it does not keep on growing Look at Game_Control for further info

            snake_amount: start and pointer to increase how many snake blocks you want
        """
        super(Snake_Main, self).__init__(
            width=frame_width,
            height=frame_height,
            x=x_pos,
            y=y_pos,
            debug=False,
        )
        self.color = Colors()

        self.segment_list = []
        self.width = width
        self.height = height
        self.grid = 10
        self.GAME_STATE = True  # We will have to localise this for now i want it here .
        self.snake_amount = length

        self.position = [
            Vector(self.width // self.internal_grid, self.height // self.internal_grid)
            for _ in range(self.snake_amount)
        ]

        isinstance(x_pos, int)
        isinstance(y_pos, int)

        self.dir = Vector(x_pos, y_pos)
        self.eat_control = False
        self.segment_list = []

    def changer(self, x: int, y: int):
        self.x, self.y = self.dir.x, self.dir.y = x, y

    def change_dir(self, direction):
        if direction == "right":
            self.changer(1, 0)
        elif direction == "left":
            self.changer(-1, 0)
        elif direction == "up":
            self.changer(0, -1)
        elif direction == "down":
            self.changer(0, 1)

    def __position_compare_x(self):
        return self.position[-1].x + self.dir.x

    def __position_compare_y(self):
        return self.position[-1].y + self.dir.y

    def _control(self):
        """Control / Wrap

        This code allows wrapping of each edge , such that, the snake
        will wrap around teh borders of the grid
        """
        if self.__position_compare_x() > self.width // self.grid:
            self.position.append(Vector(1, self.__position_compare_y()))

        elif self.__position_compare_x() < 1:
            print("This was ?")
            self.position.append(Vector(1024 / 10, self.__position_compare_y()))

        elif self.__position_compare_y() > self.height // self.grid:
            self.position.append(Vector(self.__position_compare_x(), 1))

        elif self.__position_compare_y() < 1:
            self.position.append(Vector(self.__position_compare_x(), self.height / 10))

        else:

            self.position.append(
                Vector(self.__position_compare_x(), self.__position_compare_y())
            )

    def debuger(self):
        if self.debug is True:
            __import__("ipdb").set_trace()  # Can be changed to pdb if you want
            # breakpoint()
            # Use breakpoint() if you do not have ipdb

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
        self.segment_list = []
        for pos in self.position:
            segment = [
                Vector(pos.x * self.grid - self.grid, pos.y * self.grid),
                Vector(pos.x * self.grid, pos.y * self.grid),
                Vector(pos.x * self.grid, pos.y * self.grid - self.grid),
                Vector(pos.x * self.grid - self.grid, pos.y * self.grid - self.grid),
            ]
            self.segment_list.append(segment)

        self.debuger()

    def draw_self(self, canvas):
        for k in self.segment_list:
            x = [i.get_p() for i in k]
            canvas.draw_polygon(x, 1, self.color.SNAKE_COLOR, self.color.SNAKE_COLOR)
        self.update_self()


class Game_Control(Snake_Main):
    def __init__(self, amount=10):
        super().__init__(
            x_pos=1, y_pos=0, width=frame_width, height=frame_height, length=amount
        )

    def timer_handler(self):
        self._control()
        if not self.eat_control:
            self.position.pop(0)
            # Each move , removes it , such that it does not keep on going
        self.eat_control = False

        # For debugging
        # print(self.x, "with ", self.y)

    # Another button ?
    def pause(self):
        pass

    # Thsi can be button
    def leave(self):
        pass
>>>>>>> Conditional

from system_components.control import Control
from system_components.frame import frame_height, frame_width
from system_components.Vector import Vector


class SnakeMain(Control):
    def _init__(self, var=Vector(0, 0)):
        pass


def main() -> None:
<<<<<<< HEAD
    frame = simplegui.create_frame("Snake Game", frame_width, frame_height)
    frame.set_draw_handler(...)
=======
    snake = Game_Control()

    frame = simplegui.create_frame("Snake", frame_width, frame_height)
    frame.set_keydown_handler(snake.key_down)
    frame.set_draw_handler(snake.draw_self)
    frame.set_canvas_background(Colors.BACKGROUND_COLOR)

    timer = simplegui.create_timer(100, snake.timer_handler)
    timer.start()
>>>>>>> Conditional

    frame.start()


if __name__ == "__main__":
    main()
    print("Authors ", __author__)
    print("Status ", __status__)
