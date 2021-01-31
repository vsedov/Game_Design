#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8
#
# Copyright © 2021-01-31 Viv Sedov
#
# File Name: control.py
__author__ = "Viv Sedov"
__email__ = "viv.sb@hotmail.com"

import abc


class Control(metaclass=abc.ABCMeta):
    def __init__(self, **kwargs):
        self.x = kwargs.get("x", 0.0)
        self.y = kwargs.get("y", 0.0)
        self.width = kwargs.get("width", 0)
        self.height = kwargs.get("height", 0)

    @abc.abstractmethod
    def update_control(self):
        pass

    @abc.abstractmethod
    def draw_self(self):
        pass
