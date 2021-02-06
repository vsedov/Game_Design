#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8

import abc

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore

from system_components import frame as f
from system_components.Vector import Vector


class Control(metaclass=abc.ABCMeta):
    def __init__(self, **kwargs):
        self.x = kwargs.get("x", Vector(0, 0))
        self.y = kwargs.get("y", Vector(0, 0))
        self.debug = kwargs.get("debug", False)
        self.width = kwargs.get("width", f.frame_width)
        self.height = kwargs.get("height", f.frame_width)

    @abc.abstractmethod
    def update_self(self):
        ...

    @abc.abstractmethod
    def draw_self(self):
        ...
