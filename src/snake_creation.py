#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8
#
# Copyright © 2021-01-31 Viv Sedov
#
# File Name: snake_creation.py
__author__ = "Viv Sedov"
__email__ = "viv.sb@hotmail.com"

import frame
from frosch import hook
from system.component import component

from Vector import Vector


class Snake(component):
    def __init__(self, *args, **kwargs):
        """Create Snake

        Create Sprite with Snake images .
        """
        super().__init__(*args, **kwargs)

        self.x = kwargs.get("vector_x")
        self.y = kwargs.get("vector_y")

        # This will have to change
        self._sprite = None

    def update_handler(self):
        """Update_handler

        Thid would do some calculations
        Somethign will be put here
        """

        pass

    def draw(self):
        pass
