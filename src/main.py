#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8

from dataclasses import dataclass

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore
from frosch import hook

from status import GameState
from system_components.control import Control
from system_components.frame import frame_height, frame_width
from system_components.Vector import Vector


@dataclass
class Colors:
    BACKGROUND_COLOR: str = "black"
    SNAKE_COLOR: str = "red"


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

        self.segmentation = []

        # Change name of this , and make
        self.snake = [
            Vector(self.width // self.GRID, self.height // self.GRID) for _ in range(2)
        ]

        self.velocity = Vector(1, 0)
        self.mover = Vector(0, 0)

        self.eat = False
        self.RUNNING = True

    # Velocity Change
    def _movement_change(self, x, y):
        """Movement_change
        Change Velocity Depending on Vector
        Args:
            x: X Direction
            y: Y Direction
        """
        self.velocity.x, self.velocity.y = x, y

        self.velocity.add(0, 0)

    # You would want to call this statement before teh update it self
    def eaten(self):
        if self.eat is True:
            self.velocity + 1

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

    def draw_self(self, canvas):

        canvas.draw_polygon([(10, 20), (20, 30), (30, 10)], 12, "Green")


def main() -> None:

    main_snake = SnakeMain()

    frame = simplegui.create_frame("Snake Game", frame_width, frame_height)
    frame.set_draw_handler(main_snake.draw_self)
    frame.set_canvas_background("red")

    frame.start()


if __name__ == "__main__":
    hook()
    main()
    print(__doc__)
