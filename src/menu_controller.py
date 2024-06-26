#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: menu_controller


from Game_Start import GameStart
from menu import ControlData, ToStart


def itself() -> None:

    game_starter = ToStart()
    game_starter.to_start()

    "This is for debugging purposes"
    # ic(ControlData.length)
    # ic(ControlData.speed)
    GameStart(length=ControlData.length, speed=ControlData.speed)
    # We just call this back
    itself()
