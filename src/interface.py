#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: interface


import argparse

from Game_Start import GameStart


def push_to_class(**kwargs):
    GameStart(length=kwargs.get("length"))


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--x",
        metavar="length",
        type=int,
        default=1.0,
        help="Enter number for snake length?",
    )
    args = parser.parse_args()
    push_to_class(length=args.x)


if __name__ == "__main__":
    main()
