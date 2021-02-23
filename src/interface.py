#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore

from main import DataContainer  # flake8: noqa
from main import SnakeMain


class Interface(SnakeMain):
    def __init__(self):
        super().__init__()

    def key_down(self, key_item):
        if key_item == simplegui.KEY_MAP[(x := ("right"))] and self.velocity.x == 0:
            self.position_direction(x)

        elif key_item == simplegui.KEY_MAP[(x := ("left"))] and self.velocity.x == 0:
            self.position_direction(x)

        elif key_item == simplegui.KEY_MAP[(x := ("up"))] and self.velocity.y == 0:
            self.position_direction("up")

        elif key_item == simplegui.KEY_MAP[(x := ("down"))] and self.velocity == 0:
            self.position_direction("down")


def main() -> None:
    pointer = Interface()
    pointer.checker()


if __name__ == "__main__":
    main()
