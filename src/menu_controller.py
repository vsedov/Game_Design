#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021-03-19 01:18 Viv Sedov
#
# File Name: menu_controller


from icecream import ic

from Game_Start import GameStart
from menu import ControlData, ToStart


def main() -> None:

    game_starter = ToStart()
    game_starter.to_start()

    ic(ControlData.length)
    ic(ControlData.speed)

    GameStart(length=ControlData.length, speed=ControlData.speed)


if __name__ == "__main__":
    main()
