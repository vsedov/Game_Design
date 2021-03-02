#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: control
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore

from main import Snake_Main
from system_components.frame import frame_height, frame_width


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
