#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021-03-22 19:53 Viv Sedov
#
# File Name: another_testoftest
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from frosch import hook


class WhoAmI:
    def __new__(cls):
        print("Some  infomation about me :")
        return super(WhoAmI, cls).__new__(cls)

    def __init__(self):
        self.name = "Viv Sedov"
        self.email = "viv.sv@hotmail.com"
        self.role = "Sudent"
        self.hobbies = [
            "Programming (allot)",
            "Watching Anime",
            "Reading Manga",
            "Learning Japanese",
            "Being up all Night figuring out how to FIX that ONE BUG...",
        ]


def main() -> None:
    bob = WhoAmI()


if __name__ == "__main__":
    hook()
    main()
