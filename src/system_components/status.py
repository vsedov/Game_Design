#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from dataclasses import dataclass


@dataclass
class GameState:
    GAME_STATE: bool = False
    POINTS: int = 0
    SPEED: int = 100
    internal_grid = 20
