#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: interface


import argparse

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore

from main import Colors, Game_Control
from system_components.frame import frame_height, frame_width


def push_to_class(**kwargs):
    legnth = kwargs.get("legnth")
    # Here you can add any other thing you want for now ,
    # if you want to use cli -< Very much expandable

    # Call gamestartup file - that has optinal parameters  .
    snake = Game_Control(legnth)

    frame = simplegui.create_frame("Snake", frame_width, frame_height)
    frame.set_keydown_handler(snake.key_down)
    frame.set_draw_handler(snake.draw_self)
    frame.set_canvas_background(Colors.BACKGROUND_COLOR)

    timer = simplegui.create_timer(100, snake.timer_handler)
    timer.start()
    frame.start()


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--x",
        metavar="legnth",
        type=int,
        default=1.0,
        help="Enter number for snake legnth?",
    )
    args = parser.parse_args()
    push_to_class(legnth=args.x)


if __name__ == "__main__":
    main()
