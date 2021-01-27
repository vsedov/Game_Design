#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8
#
# File Name: version.py

VERSION = (0, 0, 1)
__version__ = "".join(["-."[type(x) == int] + str(x) for x in VERSION])[1:]
