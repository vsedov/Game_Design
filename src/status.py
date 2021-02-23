#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from dataclasses import dataclass


@dataclass
class GameState:
    GAME_STATE: bool = False
    RUNNING: bool = False
    FINISHED: bool = False
    POINTS: int = 0
    SPEED: int = 100
    GRID: int = 10
