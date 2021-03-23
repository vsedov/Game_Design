#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: menu

import sys
from dataclasses import dataclass
from time import sleep  # import codeskulptor

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


@dataclass
class ControlData:
    length: int = 0
    speed: int = 0
    username: str = None


class Menu:
    def __init__(self, frame):
        """
        Init - start if menu

        Allow Side info to be parsed and to be modified
        Also starts menue from this file

        Parameters
        ----------
        frame : frame is teh frame in which i can force end or force frame.stop
            Allow ease of access from different sources
        """
        self.option: bool = False

        self.IMG: simplegui = simplegui.load_image(
            "http://personal.rhul.ac.uk/zjac/281/snake.png"
        )
        self.IMG_CENTRE: tuple = (78, 66)
        self.IMG_DIMS: tuple = (156, 132)
        self.theme_1: int = 0

        self.IMG2: simplegui = simplegui.load_image(
            "http://personal.rhul.ac.uk/zjac/281/Snake%20on%20an%20old%20stump_0.png"
        )
        self.IMG_CENTRE2: tuple = (125, 125)
        self.IMG_DIMS2: tuple = (250, 250)
        self.theme_2: int = 1

        self.IMG3: simplegui = simplegui.load_image(
            "http://personal.rhul.ac.uk/zjac/281/apple_1_0.png"
        )
        self.IMG_CENTRE3: tuple = (108, 125)
        self.IMG_DIMS3: tuple = (216, 250)
        self.theme_3: int = 2

        self.IMG4: simplegui = simplegui.load_image(
            "http://personal.rhul.ac.uk/zjac/281/SneckoCreature.PNG"
        )
        self.IMG_CENTRE4: tuple = (125, 69.5)
        self.IMG_DIMS4: tuple = (250, 139)
        self.theme_4: int = 3

        self.theme: int = 0

        self.sound = simplegui.load_sound(
            "http://commondatastorage.googleapis.com/codeskulptor-assets/week7-brrring.m4a"
        )

        self.input = self.frame.add_input("Name", menu.input_handler, 100)
        self.frame = frame

        self.input = None

    def start_game(self, main_length: int, speed: int):
        if self.option is True:

            self.speed = speed
            self.length = main_length
            ControlData.speed = self.speed
            ControlData.length = self.length
            self.none_checker()

            self.frame.stop()

    def input_handler():
        pass

    def none_checker(self):
        if self.input is None:
            pass

    def click(self, pos):
        """
        pos

        Define where the user mouse click is

        Parameters
        ----------
        pos : Position of mouse
            tuple argument , - x,y
        """
        if pos[0] >= 128 and pos[0] <= 384:
            if pos[1] >= 0 and pos[1] <= 64:
                # ic("Easy")
                self.sound.play()
                self.option = True
                self.start_game(main_length=5, speed=100)

            elif pos[1] >= 128 and pos[1] <= 192:
                self.option = True
                # ic("Medium")
                self.sound.play()
                self.start_game(main_length=50, speed=80)

            elif pos[1] >= 256 and pos[1] <= 320:
                self.option = True
                # ic("Hard")
                self.sound.play()
                self.start_game(main_length=100, speed=50)

            elif pos[1] >= 384 and pos[1] <= 448:
                self.sound.play()
                sleep(1.00)
                sys.exit()
            # print(self.frame.inp.get_text())

        if pos[1] >= 30 and pos[1] <= 48:
            if pos[0] >= 460 and pos[0] <= 475:
                if self.theme == 0:
                    self.theme = 3
                else:
                    self.theme -= 1
            elif pos[0] >= 478 and pos[0] <= 506:
                if self.theme == 3:
                    self.theme = 0
                else:
                    self.theme += 1
            print(self.theme)

    def input_handler(self, bob):
        print(bob)

    def draw(self, canvas):
        """
        Draw canvas

        Draw polygon size of blocks / rectangle this is the bassis of how hard teh game
        would have to be

        Parameters
        ----------
        canvas : Update to canvas
        """

        if self.theme == self.theme_1:
            canvas.draw_image(
                self.IMG,
                self.IMG_CENTRE,
                self.IMG_DIMS,
                (256, (2 * 512 / 4)),
                (512, 512),
            )
        elif self.theme == self.theme_2:
            canvas.draw_image(
                self.IMG2,
                self.IMG_CENTRE2,
                self.IMG_DIMS2,
                (256, (2 * 512 / 4)),
                (512, 512),
            )
        elif self.theme == self.theme_3:
            canvas.draw_image(
                self.IMG3,
                self.IMG_CENTRE3,
                self.IMG_DIMS3,
                (256, (2 * 512 / 4)),
                (400, 400),
            )
        elif self.theme == self.theme_4:
            canvas.draw_image(
                self.IMG4,
                self.IMG_CENTRE4,
                self.IMG_DIMS4,
                (256, (2 * 512 / 4)),
                (512, 512),
            )

        canvas.draw_polygon([(460, 48), (506, 48), (506, 0), (460, 0)], 5, "#660099")
        canvas.draw_text("Theme", (463, 27), 15, "White", "monospace")
        canvas.draw_text("<--", (465, 40), 15, "White", "monospace")
        canvas.draw_text("-->", (478, 40), 15, "White", "monospace")

        canvas.draw_polygon([(128, 64), (384, 64), (384, 0), (128, 0)], 5, "#660099")
        canvas.draw_text("Easy", (204.8, 45), 23, "White", "monospace")

        canvas.draw_polygon(
            [(128, 192), (384, 192), (384, 128), (128, 128)], 5, "#660099"
        )
        canvas.draw_text("Medium", (204.8, 170), 23, "White", "monospace")

        canvas.draw_polygon(
            [(128, 320), (384, 320), (384, 256), (128, 256)], 5, "#660099"
        )
        canvas.draw_text("Hard", (217.6, 295), 23, "White", "monospace")

        canvas.draw_polygon(
            [(128, 448), (384, 448), (384, 384), (128, 384)], 5, "#660099"
        )
        canvas.draw_text("Exit", (230.4, 420), 23, "White", "monospace")

        canvas.draw_text("High score: ", (150, 486.4), 23, "White", "monospace")


frame = simplegui.create_frame("Home", 512, 512)


class ToStart(ControlData):
    def __init__(self):
        super().__init__(frame)
        self.frame = frame

    #       self.inp = inp

    def to_start(self):

        menu = Menu(self.frame)

        self.frame.set_canvas_background("#2C6A6A")

        self.frame.set_mouseclick_handler(menu.click)

        self.frame.set_draw_handler(menu.draw)

        self.frame.add_input("Name", menu.input_handler, 100)

        self.frame.start()
