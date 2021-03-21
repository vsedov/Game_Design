#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8

__author__ = ["Vivian"]
__status__ = "Development"

from dataclasses import dataclass

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore
from icecream import ic

from system_components.control import Control
from system_components.frame import frame_height, frame_width
from system_components.status import GameState
from system_components.Vector import Vector


@dataclass
class Colors:
    BACKGROUND_COLOR: str = "black"
    SNAKE_COLOR: str = "purple"


class Snake_Main(Control, GameState):
    def __init__(
        self, *, x_pos=1, y_pos=0, width=frame_width, height=frame_height, length=2
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
        super().__init__(
            width=frame_width,
            height=frame_height,
            x=x_pos,
            y=y_pos,
            debug=False,
        )
        self.color = Colors()
        self.speed: int = 100
        self.life: int = 3
        self.width: int = width
        self.height: int = height
        self.grid: int = 17  # Add this to game state class
        self.GAME_STATE: bool = (
            True  # We will have to localise this for now i want it here .
        )
        self.points = self.POINTS
        self.snake_amount: int = length
        self.snake_block: Vector = Vector(
            self.width // self.internal_grid, self.height // self.internal_grid
        )

        self.position = [self.snake_block for _ in range(self.snake_amount)]

        isinstance(x_pos, int)
        isinstance(y_pos, int)

        self.dir: Vector = Vector(x_pos, y_pos)
        self.eat_control: bool = False
        self.segment_list = []

        self.life_counter: int = 0

        self.timer = None

    def changer(self, x: int, y: int, debug_direction: str):
        """Changer
            Control.x and Control.y there for debugging purposes
            but replaces teh direction of both values while updating the
            debugging value

        Args:
            x: updated direction of x
            y: updated direction of y
        """

        Control.x, Control.y = self.dir.x, self.dir.y = x, y

    def change_dir(self, direction):
        """
        Change Direction

        Update Direction / position of snake

        Parameters
        ----------
        direction : Call given by movement - SImplegui
        """
        if direction == "right":
            self.changer(1, 0, "right")
        elif direction == "left":
            self.changer(-1, 0, "left")
        elif direction == "up":
            self.changer(0, -1, "up")
        elif direction == "down":
            self.changer(0, 1, "down")

    def __position_compare_x(self):
        """position x wrapper

        wraps around x axis for snake
        """
        return self.position[-1].x + self.dir.x

    def __position_compare_y(self):
        """position compare y

        wraps around y axis for snake
        """
        return self.position[-1].y + self.dir.y

    def _control(self):
        """Control / Wrap

        This code allows wrapping of each edge , such that, the snake
        will wrap around teh borders of the grid
        """
        if self.__position_compare_x() > self.width // self.grid:
            self.position.append(Vector(1, self.__position_compare_y()))

        elif self.__position_compare_x() < 1:
            self.position.append(
                Vector(self.width / self.grid, self.__position_compare_y())
            )

        elif self.__position_compare_y() > self.height // self.grid:
            self.position.append(Vector(self.__position_compare_x(), 1))

        elif self.__position_compare_y() < 1:
            self.position.append(
                Vector(self.__position_compare_x(), self.height // self.grid)
            )

        else:

            self.position.append(
                Vector(self.__position_compare_x(), self.__position_compare_y())
            )

    def key_down(self, key):
        """key_down

        this can be for the first user , key down will take
        Fkey + [i in ["i","j","k","l"]] will update movement

        Args:
            key: SimpleGUICS2Pygame command
        """
        if key == simplegui.KEY_MAP["d"] and self.dir.x == 0:
            self.change_dir("right")
        elif key == simplegui.KEY_MAP["a"] and self.dir.x == 0:
            self.change_dir("left")
        elif key == simplegui.KEY_MAP["w"] and self.dir.y == 0:
            self.change_dir("up")
        elif key == simplegui.KEY_MAP["s"] and self.dir.y == 0:
            self.change_dir("down")

    def __life_change(self):
        """
        Life Change defined in the inherited class , if this is False
        Game should halt if the lifes have reached zero

        GAME STATE refer to control.py and main.py
        """
        ic("Your lives are ", self.life)
        if self.life == 0:
            self.GAME_STATE = False

        else:
            self.life_counter += 1
            self.life -= 1

    def __snake_reducer(self):
        """
        Snake reducer

        Decreases amount given to how ever much health there is
        """
        if len(self.position) > 2:
            self.position.pop()
        else:
            print("position is too small for me to remove anything")
            print("END OF GAME")

    def _self_collision(self):
        """Collision Checker with self values

        Uses slicing to check the previous position if collision , some given timer ends
        """
        for pointer in self.position[:-1]:
            if pointer.get_p() == self.position[-1].get_p():
                self.__life_change()
                self.__snake_reducer()


if __name__ == "__main__":
    print("Authors ", __author__)
    print("Status ", __status__)
