#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021-03-19 01:18 Viv Sedov
#
# File Name: menu_controller

from Game_Start import GameStart
from menu import to_start


class MenuStartGame:
    def __new__(cls, *kwargs):

        pass


def main() -> None:
    to_start()
    GameStart(length=10)


if __name__ == "__main__":
    main()
