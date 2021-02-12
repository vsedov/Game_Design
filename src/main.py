#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8

from dataclasses import dataclass
from typing import List

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
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
        super(SnakeMain, self).__init__(
            width=frame_width,
            height=frame_height,
            x=position.x,
            y=position.y,
            debug=False,
        )
        # Start in the middle
        self.start_position = Vector(self.width / 2, self.height / 2)
        self.eat = False

        self.velocity = velocity
        self.position = position

    # Velocity Change
    def __movement_change(self, x, y):
        self.velocity.x, self.velocity.y = x, y

    def position_direction(self, direction):
        if direction == "right":
            self.movement_change(1, 0)
        elif direction == "left":
            self.movement_change(-1, 0)
        elif direction == "up":
            self.movement_change(0, -1)
        elif direction == "down":
            self.movement_change(0, 1)
        else:
            print("You have pressed the wrong key")

    def update_self(self):
        pass

    def draw_self(self, canvas):
        self.update_self()

        canvas.draw_line((0, 19), (19, 20), 1, "red")


# So you want draw handler that would change the grid
# You want another draw handler that yould hightlight those squares


def main() -> None:

    main_snake = SnakeMain()

    frame = simplegui.create_frame("Snake Game", frame_width, frame_height)
    frame.set_draw_handler(main_snake.draw_self)

    frame.start()


if __name__ == "__main__":
    hook()
    main()
