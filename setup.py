#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8
#
# File Name: setup.py
from setuptools import find_packages, setup

setup(
    name="Game_Design",
    version="0.0.1",
    description="Python Snake Game in simplegui",
    url="https://github.com/vsedov/Game_Design",
    author=["Viv Sedov", "Ahmed Elsakaan", "Max Fisher", "Ollie"],
    license="GNU GENERAL PUBLIC LICENSE",
    classifiers=[
        "programming_language :: Python :: 3",
        "operating_system :: OS Independent",
    ],
    install_requires=["SimpleGUICS2Pygame", "frosch"],
    include_package_data=True,
    pacakges=find_packages(),
)
