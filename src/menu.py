import sys
from dataclasses import dataclass
from time import sleep  # import codeskulptor

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


@dataclass
class ControlData:
    length: int = 0
    speed: int = 0


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
        self.IMG = simplegui.load_image("http://personal.rhul.ac.uk/zjac/281/snake.png")

        self.l1 = [-12, -8, -4, 0, 4, 8, 12]

        self.IMG2 = simplegui.load_image(
            "http://personal.rhul.ac.uk/zjac/281/snake.png"
        )
        self.l2 = [-11, -7, -3, 1, 5, 9, 13]
        self.IMG3 = simplegui.load_image(
            "https://opengameart.org/sites/default/files/styles/medium/public/apple_1_0.png"
        )
        self.l3 = [-10, -6, -2, 2, 6, 10, 14]
        self.IMG4 = simplegui.load_image(
            "https://opengameart.org/sites/default/files/styles/medium/public/SneckoCreature.PNG"
        )
        self.l4 = [-9, -5, -1, 3, 7, 11, 15]
        self.theme = 1
        self.IMG_CENTRE = (78, 66)
        self.IMG_DIMS = (156, 132)
        self.sound = simplegui.load_sound(
            "http://commondatastorage.googleapis.com/codeskulptor-assets/week7-brrring.m4a"
        )
        self.frame = frame

    def start_game(self, main_length: int, speed: int):
        if self.option is True:

            self.speed = speed
            self.length = main_length
            ControlData.speed = self.speed
            ControlData.length = self.length

            self.frame.stop()

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

        global theme
        if pos[1] >= 30 and pos[1] <= 48:
            if pos[0] >= 460 and pos[0] <= 475:
                theme -= 1
            elif pos[0] >= 478 and pos[0] <= 506:
                theme += 1

    def draw(self, canvas):
        """
        Draw canvas

        Draw polygon size of blocks / rectangle this is the bassis of how hard teh game
        would have to be

        Parameters
        ----------
        canvas : Update to canvas
        """

        if self.theme in self.l1:
            canvas.draw_image(
                self.IMG,
                self.IMG_CENTRE,
                self.IMG_DIMS,
                (300, (2 * 512 / 4)),
                (512, 512),
            )
        elif self.theme in self.l2:
            canvas.draw_image(
                self.IMG2,
                self.IMG_CENTRE,
                self.IMG_DIMS,
                (256, (2 * 512 / 4)),
                (512, 512),
            )
        elif self.theme in self.l3:
            canvas.draw_image(
                self.IMG3,
                self.IMG_CENTRE,
                self.IMG_DIMS,
                (256, (2 * 512 / 4)),
                (512, 512),
            )
        elif self.theme in self.l4:
            canvas.draw_image(
                self.IMG4,
                self.IMG_CENTRE,
                self.IMG_DIMS,
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

        canvas.draw_text("High score: ", (339.2, 486.4), 23, "White", "monospace")


frame = simplegui.create_frame("Home", 512, 512)


class ToStart(ControlData):
    def __init__(self):
        super().__init__(frame)
        self.frame = frame

    def to_start(self):

        menu = Menu(self.frame)

        self.frame.set_canvas_background("#2C6A6A")

        self.frame.set_mouseclick_handler(menu.click)

        self.frame.set_draw_handler(menu.draw)

        self.frame.start()
