#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: Game_Start

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from control import Game_Control
from system_components.frame import frame_height, frame_width

__author__ = "Viv Sedov"


def game_restart():
    ...


def colour_button_handler(snake, colour):
    snake.color.SNAKE_COLOR = colour


class GameStart:
    # Can be omitted, Python will give a default implementation
    def __new__(cls, **kwargs):

        # This would allow for this to be expanded
        snake = Game_Control(kwargs.get("length", 5))

        snake.color.SNAKE_COLOR = kwargs.get("colours", "purple")

        def red_button_handler():
            snake.color.SNAKE_COLOR = "Red"

        def orange_button_handler():
            snake.color.SNAKE_COLOR = "Orange"

        def yellow_button_handler():
            snake.color.SNAKE_COLOR = "Yellow"

        def green_button_handler():
            snake.color.SNAKE_COLOR = "Green"

        def blue_button_handler():
            snake.color.SNAKE_COLOR = "Blue"

        def purple_button_handler():
            snake.color.SNAKE_COLOR = "Purple"

        def pink_button_handler():
            snake.color.SNAKE_COLOR = "Pink"

        frame = simplegui.create_frame("Snake", frame_width, frame_height)
        frame.set_keydown_handler(snake.key_down)
        frame.set_draw_handler(snake.draw_self)
        frame.add_label("Colour Options")
        frame.add_button("Red", red_button_handler)
        frame.add_label("")
        frame.add_button("Orange", orange_button_handler)
        frame.add_label("")
        frame.add_button("Yellow", yellow_button_handler)
        frame.add_label("")
        frame.add_button("Green", green_button_handler)
        frame.add_label("")
        frame.add_button("Blue", blue_button_handler)
        frame.add_label("")
        frame.add_button("Purple", purple_button_handler)
        frame.add_label("")
        frame.add_button("Pink", pink_button_handler)
        # We do not change the background colour
        frame.set_canvas_background(snake.color.BACKGROUND_COLOR)

        timer = simplegui.create_timer(snake.speed, snake.timer_handler)

        snake.timer = timer

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

GameStart()
