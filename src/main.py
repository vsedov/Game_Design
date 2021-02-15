#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8

import random
from dataclasses import dataclass
from typing import List

from frosch import hook

from system_components.control import Control
from system_components.frame import frame_height, frame_width
from system_components.Vector import Vector


@dataclass
class GameState:
    GAME_STATE: bool = False
    RUNNING: bool = False
    FINISHED: bool = False
    POINTS: int = 0
    SPEED: int = 100
    GRID: int = 10


@dataclass
class Colors:
    BACKGROUND_COLOR: str = "black"
    SNAKE_COLOR: str = "red"


@dataclass
class DataContainer:
    segmentation = List[int]


class SnakeMain(Control, GameState):
    def __init__(
        self,
        frame_width=frame_width,
        frame_height=frame_height,
        position=Vector(1, 0),
        velocity=Vector(1, 0),
    ):
        """Initialiser
        Linked with Abc class Push Forward
        Vector and Positional Vecot

        Args:
            frame_width: Frame Width imported from local
            frame_height: Frame height imported from local
            position: positional Vector , start location Should be array
            velocity: Velocity of what changes should occour
        """

        super(SnakeMain, self).__init__(
            width=frame_width,
            height=frame_height,
            x=position.x,
            y=position.y,
            debug=False,
        )
        # If we Decide to do , you start with one blob, - we could make this an
        # option, within the menu ie - "How many start blocks would you like or something

        self.direction = [Vector(self.width // self.GRID, self.height // self.GRID)]
        self.velocity = Vector(1, 0)

        self.eat = False

    # Velocity Change
    def _movement_change(self, x, y):
        """Movement_change
        Change Velocity Depending on Vector
        Args:
            x: X Direction
            y: Y Direction
        """
        self.velocity.x, self.velocity.y = x, y

    def position_direction(self, direction):
        """Position_direction
        Adjusting vector cords for given
        position

        Args:
            direction: input mapper
        """
        if direction == "right":
            self._movement_change(1, 0)
        elif direction == "left":
            self._movement_change(-1, 0)
        elif direction == "up":
            self._movement_change(0, -1)
        elif direction == "down":
            self._movement_change(0, 1)

    def movement(self):
        # Im not sure what i should put here

        pass

    def game_logic(self):
        pass

    # This is required due to the abstract class
    def update_self(self):
        pass

    def draw_self(self):
        pass


class PositionalIncrease(SnakeMain):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.random_increaser = Vector(
            random.randrange(1, self.frame_width // self.GRID),
            random.randrange(1, self.frame_height // self.GRID),
        )

    def segmentation(self):

        pass

    # No Clue what to do , probs will figure it out later


def main() -> None:

    main_snake = SnakeMain()

    # Testing something out
    print(main_snake.direction[-1].x)

    frame = simplegui.create_frame("Snake Game", frame_width, frame_height)
    frame.set_draw_handler(main_snake.draw_self)

    frame.start()


if __name__ == "__main__":
    hook()
    main()
    print(__doc__)
