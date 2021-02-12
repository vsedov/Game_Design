#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from frosch import hook

from system_components.control import Control
from system_components.frame import frame_height, frame_width
from system_components.Vector import Vector


class SnakeMain(Control):
    def _init__(self, var=Vector(0, 0)):
        pass


def main() -> None:
    frame = simplegui.create_frame("Snake Game", frame_width, frame_height)
    frame.set_draw_handler(...)

    frame.start()


if __name__ == "__main__":
    hook()
    main()
