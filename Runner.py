#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021-03-24 18:17 Viv Sedov
#
# File Name: Runner
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from frosch import hook

from src.menu_controller import itself


def main() -> None:

    itself()


if __name__ == "__main__":
    hook()
    main()
