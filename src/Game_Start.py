#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: Game_Start

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from control import Game_Control
from main import Colors
from system_components.frame import frame_height, frame_width

__author__ = "Viv Sedov"


class GameStart:
    # Can be omitted, Python will give a default implementation
    def __new__(cls, **kwargs):

        # This would allow for this to be expanded
        snake = Game_Control(kwargs.get("length", 2))

        frame = simplegui.create_frame("Snake", frame_width, frame_height)
        frame.set_keydown_handler(snake.key_down)
        frame.set_draw_handler(snake.draw_self)
        frame.set_canvas_background(Colors.BACKGROUND_COLOR)

        timer = simplegui.create_timer(100, snake.timer_handler)
        timer.start()

        frame.start()

        return super().__new__(cls)


# get rid of this when you are done with this
# Use this when you are working
"""
Steps : 
 if you want to test a change have this file open and uncomment this , once you are 
 finished , uncomment this again . 
"""
# GameStart()
