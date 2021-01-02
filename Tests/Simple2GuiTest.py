#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8
#
# Copyright © 2021-01-02 Viv Sedov
#
# File Name: Simple2GuiTest.py
__author__ = "Viv Sedov"
__email__ = "viv.sb@hotmail.com"

import numpy as np
from frosch import hook
from pprintpp import pprint as pp

#Would be nice if the inputs were better ... managed instead of this 
try:
    import simplegui  # pytype: disable=import-error
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access

WIDTH = 400
HEIGHT = 300


def click() -> None:
    print("click")


def draw(canvas) -> None:

    text = "foo"

    font_size = 40
    text_width = FRAME.get_canvas_textwidth(text, font_size)

    # This part is just pointless . 
    canvas.draw_text(
        text,
        ((WIDTH - text_width) // 2, HEIGHT // 2 + font_size // 4),
        font_size,
        "Green",
    )


def stop_all():  # type: () -> None
    """Handler function to the Quit button."""
    TIMER.stop()
    FRAME.stop()

# This part should be fine . 

FRAME = simplegui.create_frame("Stop example", WIDTH, HEIGHT)

FRAME.add_button("Quit", stop_all)

FRAME.set_draw_handler(draw)

TIMER = simplegui.create_timer(1000, click)
TIMER.start()

FRAME.start()

if __name__ == "__main__":
    hook()
