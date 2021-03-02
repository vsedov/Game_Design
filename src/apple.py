#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: apple
__author__ = ["Vivian"]

import random

from frosch import hook

from system_components.frame import frame_height, frame_width
from system_components.status import GameState


class Apple(GameState):
    def __init__(self, *, width=frame_width, height=frame_height):
        self.width = width
        self.height = height
        self.grid = 10  # Hard code this for now :: take from gamestate class

    def random_apple(self) -> frozenset:
        # x>= 2 and x<= 5 Avoid border issue
        # Allows this to be fixed for now, further modifications will be added
        return frozenset(
            (
                random.randrange(5, self.width // self.grid),
                random.randrange(5, self.height // self.grid),
            )
        )


hook()
