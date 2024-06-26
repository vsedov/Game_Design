#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: control

import random

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore

from json_controller import JsonData
from main import Snake_Main
from menu import ControlData
from system_components.frame import frame_height, frame_width
from system_components.Vector import Vector


class Game_Control(Snake_Main):
    def __init__(self, amount=10, speed=100, timer=None, frame=None):
        super().__init__(
            x_pos=1, y_pos=0, width=frame_width, height=frame_height, length=amount
        )
        self.width = frame_width
        self.height = frame_height

        "Good apple incrase length"
        self.app_pos, self.app_seg = self._app()
        "Bad apple reduces length"
        self.bad_app_pos, self.bad_app_seg = self._app()

        self.speed = speed
        self.max_speed = 10
        self.main_points = 0
        self.label = None
        self.lives = None
        self.timer = timer
        self.frame = frame
        "Due to Username not being defined properly , username will be Bob"
        self.user_name = ControlData.username

    def update_self(self, canvas):
        """update_self

        ABC class method : has to be static , has to be called update self
        refer to control class docs for further infomation .

        segment , creates a block of a 4 x 4 , allows us to map and define values

        Args:
            canvas: canvas for updating and drawing extra items [ not required ]
        """

        self.segment_list = []
        for pos in self.position:
            x = pos.x
            y = pos.y
            segment = [
                Vector(x * self.grid - self.grid, y * self.grid),
                Vector(x * self.grid, y * self.grid),
                Vector(x * self.grid, pos.y * self.grid - self.grid),
                Vector(x * self.grid - self.grid, y * self.grid - self.grid),
            ]
            self.segment_list.append(segment)

    def draw_self(self, canvas):
        """draw_self

        ABC method similar to update_self, static , main draw must be done in here
        this is a wraper , and allows multiple instances to run at teh same time

        snake is a block of squares that is constantly update , then you have app seg
        whihc is teh apple which is updated with the methods that have been shown below

        Args:
            canvas: canvas alows stuff to be draw onto the canvas , parser
        """
        for block in self.segment_list:
            x = [i.get_p() for i in block]
            canvas.draw_polygon(x, 1, "purple", self.color.SNAKE_COLOR)

        self.update_self(canvas)

        # Good apple
        canvas.draw_polygon(self.app_seg, 1, "green", "#5EE06F")

        # Bad apple
        canvas.draw_polygon(self.bad_app_seg, 1, "red", "#EA4D43")

        # Game Over state is very quick and just ends the program
        if self.GAME_STATE is False:
            canvas.draw_text(
                "GAME OVER", (self.width // 2, self.height // 2), 50, "Blue"
            )

            "You have to stop the timer : before writing otherwise you get multiple write instances"
            self._save()

    def speed_increase(self):
        """
        Increase speed with max speed of 10 - which is the fastest

        Checker to define when the game is running live
        """
        if self.speed < self.max_speed:

            self.speed = self.max_speed

        else:
            self.speed -= 1

        # Isue this doesnt update the timer , so the speed does not increase like i wanted to

    def __life_decrease(self):
        """
        Life decreaser

        decrease life
        """

        if self.life < 1:
            self.GAME_STATE = False
        else:
            self.life -= 1

    def __point_increase(self):
        """
        Live point score

        Increases points when called
        """
        self.main_points += 1

    def __point_decrease(self):
        """
        point decreaser

        if hit red apple  points will decrease
        """
        self.main_points -= 1

    def _app_eaten(self):
        """apple eaten

        if the apple is eaten , from the position list, self.eat_control is active and
        redifines it self:

        Args:
            self.app_pos: this is the location of the current apple gets redifined when
            eaten
        """

        for i in self.position:

            if i.get_p() == self.app_pos:
                self.eat_control = True
                # Redifine the given apple
                self.app_pos, self.app_seg = self._app()
                self.speed_increase()
                self.__point_increase()

    def _bad_app_eaten(self):
        for i in self.position:
            if i.get_p() == self.bad_app_pos:
                "remove"
                self.position.pop()
                self.__point_decrease()
                self.__life_decrease()
                self.bad_app_pos, self.bad_app_seg = self._app()

    def _grower_eaten(self):
        """grower_eaten

        Given Function states if the eat_control from main is true , such that value is
        poped

        Funciton ever grows , we pop at certain moments given teh defined legnth . this
        allows it to grow
        """
        if not self.eat_control:
            self.position.pop(0)

    def timer_handler(self):
        """time_handler

        all main functinos like control , wraping , apple beeing eaten ,
        collisions must all be parsed via the timer , hence why its wise to do so this
        way wrapper has been included to adjust for errors {@ .... }
        """
        # ic(self.user_name)
        self._control()
        self._self_collision()
        self._app_eaten()
        self._bad_app_eaten()
        self._grower_eaten()
        self.label.set_text("Points = " + str(self.main_points))
        self.lives.set_text("lives = " + str(self.life))
        self.eat_control = False

    def _app(self):
        """app

        Apple segments , to create blocks , this CAN be Changed , though you need to
        define a value within the snake class first for teh HEAD of the snake to do so .
        """
        app = self.random_app()

        # This can be changed to what ever - so long as the cords are the same .
        # You can change those values.
        x = app[0]
        y = app[1]

        segements = [
            (x * self.grid - self.grid, y * self.grid),
            (x * self.grid, y * self.grid),
            (x * self.grid, y * self.grid - self.grid),
            (x * self.grid - self.grid, y * self.grid - self.grid),
        ]

        return app, segements

    def random_app(self) -> tuple:
        """random_app

        returns an random apple location

        Returns:
            tuple: Tuple to be modified
        """
        return (
            random.randrange(1, self.width // self.grid),
            random.randrange(1, self.height // self.grid),
        )

    def _save(self):
        """
        Save

        Save and end game - with user infomation
        """

        self.timer.stop()
        JsonData(self.main_points, self.user_name)
        self._save_exit()

    def _save_exit(self):
        """
        Exit if the save command has been executed

        exits frame to go back to menu
        """
        self.frame.stop()

    def _exit(self):
        """
        exit

        exit without user infomation
        """
        self.timer.stop()
        self.frame.stop()
        # sys.exit(0)
