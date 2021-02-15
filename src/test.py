#! /usr/bin/env python3
# -- coding: utf-8 --
# vim:fenc=utf-8


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # pyflakes.ignore
from frosch import hook

from system_components.control import Control
from system_components.Vector import Vector


class Test(Control):
    def __init__(self, **kwargs):
        """
        Initialiser Class
        Width , Heeight , x , y and position
        Args:
            **kwargs:
                width : frame width
                height : frame height
                x : Vector for x
                y : Vector for y
        return :
            None

        """
        super().__init__(**kwargs)

        self.x = kwargs.get("x")
        self.y = kwargs.get("y")
        self.centre = (self.width / 2, self.height / 2)

        self.message = None

    @staticmethod
    def update_self():
        ...

    def draw_self(self, canvas):
        """
        Draw_self

        Takes abstract class defined in Control
        Allows any update method to be parsed only within
        The abstract class .

        Args:
            canvas: Simplegui command
        """
        ...
        canvas.draw_circle(self.centre, 20, 5, "Blue", "White")


def main() -> None:
    x_vector = Vector(1, 0)
    y_vector = Vector(0, 1)

    testing = Test(x=x_vector, y=y_vector)

    frame = simplegui.create_frame("Home", testing.width, testing.height)
    frame.set_draw_handler(testing.draw_self)

    frame.start()


if __name__ == "__main__":
    hook()
    # main()
    print(__doc__)

lister = ["Strimg" or "var"]
print(lister)
