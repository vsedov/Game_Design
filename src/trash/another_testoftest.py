#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021-03-22 19:53 Viv Sedov
#
# File Name: another_testoftest
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from frosch import hook
from icecream import ic


class Welcome:
    def __init__(self, frame):
        self.inp = None
        self.frame = frame

        self.message = "Good job!"

    def click(self, pos):
        ic(pos)

    def input_handle(self):
        pass

    def draw(self, canvas):
        canvas.draw_text("Welcome", [175, 256], 48, "Purple")

    def input_handle(self, text):
        ic(text)


def main() -> None:

    # -------------------------------------------------
    frame = simplegui.create_frame("Home", 512, 512)
    # -------------------------------------------------

    bob = Welcome(frame)

    inp = frame.add_input("Name", bob.input_handle, 100)

    bob.inp = inp
    frame.set_draw_handler(bob.draw)
    frame.set_mouseclick_handler(bob.click)

    frame.start()


if __name__ == "__main__":
    hook()
    main()
