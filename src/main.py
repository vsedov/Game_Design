#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8

__author__ = ["Vivian"]
__status__ = "Development"

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
        self.grid = 10  # Add this to game state class
        self.GAME_STATE = True  # We will have to localise this for now i want it here .
        self.snake_amount = length
        self.snake_block = Vector(
            self.width // self.internal_grid, self.height // self.internal_grid
        )

        self.position = [self.snake_block for _ in range(self.snake_amount)]

        isinstance(x_pos, int)
        isinstance(y_pos, int)

        self.dir = Vector(x_pos, y_pos)
        self.eat_control = False
        self.segment_list = []

    def eaten(self):
        if self.eat_control is True:
            self.position.append(self.snake_block)
            self.eat_control = False

    def changer(self, x: int, y: int):
        Control.x, Control.y = self.dir.x, self.dir.y = x, y

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
            self.position.append(Vector(self.width / 10, self.__position_compare_y()))

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

            # This was for test purposes , i wanted to see if it would work , the legnth
            # growing
            # this infomation will get changed later
            self.eat_control = True

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

    def _self_collision(self):
        """Collision Checker with self values

        Uses slicing to check the previous position if collision , some given timer ends
        """
        for pointer in self.position[:-1]:
            if pointer.get_p() == self.position[-1].get_p():
                # This works, now i have to figure out a way that ends the given game

                # Points and live system , what exactly are we doing , and whos going
                # to be coding this up ?

                # exit , and say game over , or do you want some life meter ?
                pass

    def _apple_eaten(self):
        # Either have it the same as the segment list that i had before, or you could
        # just use a circle for now .

        pass

    def draw_self(self, canvas):

        for k in self.segment_list:
            x = [i.get_p() for i in k]

            canvas.draw_polygon(x, 1, self.color.SNAKE_COLOR, self.color.SNAKE_COLOR)

        self.update_self()

        # self.draw_apple(canvas)


if __name__ == "__main__":
    print("Authors ", __author__)
    print("Status ", __status__)
