Updated. Elapsed time: 0.972967 sec.
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#Done!
# File Name: control

import random

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore

from main import Snake_Main
from system_components.frame import frame_height, frame_width
from system_components.Vector import Vector


class Game_Control(Snake_Main):
    def __init__(self, amount=10):
        super().__init__(
            x_pos=1, y_pos=0, width=frame_width, height=frame_height, length=amount
        )
        self.width = frame_width
        self.height = frame_height
        self.app_pos, self.app_seg = self.app()
        self.image = simplegui.load_image("https://svgshare.com/i/Urn.svg")

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
            segment = [
                Vector(pos.x * self.grid - self.grid, pos.y * self.grid),
                Vector(pos.x * self.grid, pos.y * self.grid),
                Vector(pos.x * self.grid, pos.y * self.grid - self.grid),
                Vector(pos.x * self.grid - self.grid, pos.y * self.grid - self.grid),
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

        for k in self.segment_list:
            x = [i.get_p() for i in k]

            # canvas.draw_image(
            #     self.image,
            #     (self.width // 10, self.height // 10),
            #     (self.width, self.height),
            #     (5, 5),
            #     (10, 10),
            # )
            canvas.draw_polygon(x, 1, "Purple", "Black")

        self.update_self(canvas)

        canvas.draw_polygon(self.app_seg, 1, "Red", "blue")

    def _app_eaten(self):
        """apple eaten

        if the apple is eaten , from the position list, self.eat_control is active and
        redifines it self:

        Args:
            self.app_pos: this is the location of the current apple gets redifined when
            eaten
        """

        for i in self.position:

            # __import__('ipdb').set_trace()

            # This tends to fail
            if i.get_p() == self.app_pos:
                self.eat_control = True
                # Redifine the given apple
                self.app_pos, self.app_seg = self.app()

    def timer_handler(self):
        """time_handler

        all main functinos like control , wraping , apple beeing eaten ,
        collisions must all be parsed via the timer , hence why its wise to do so this
        way wrapper has been included to adjust for errors {@ .... }
        """
        self._control()
        self._self_collision()
        self._app_eaten()

        if not self.eat_control:
            # adds new item when there True
            self.position.pop(0)

        self.eat_control = False

    def app(self):
        """app

        Apple segments , to create blocks , this CAN be Changed , though you need to
        define a value within the snake class first for teh HEAD of the snake to do so .
        """
        app = self.random_app()

        # This can be changed to what ever - so long as the cords are the same .
        # You can change those values.

        segements = [
            (app[0] * self.grid - self.grid, app[1] * self.grid),
            (app[0] * self.grid, app[1] * self.grid),
            (app[0] * self.grid, app[1] * self.grid - self.grid),
            (app[0] * self.grid - self.grid, app[1] * self.grid - self.grid),
        ]

        return app, segements

    def random_app(self) -> tuple:
        """random_app

        returns an random apple location

        Returns:
            tuple: Tuple to be modified
        """
        return (
            random.randrange(2, self.width // self.grid),
            random.randrange(2, self.height // self.grid),
        )
