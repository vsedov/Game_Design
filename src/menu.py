try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import sys
##import codeskulptor
from time import sleep

from Game_Start import GameStart

IMG = simplegui.load_image("http://personal.rhul.ac.uk/zjac/281/snake.png")
# IMG_CENTRE = (200, 200)
# IMG_DIMS = (400, 400)
IMG_CENTRE = (78, 66)
IMG_DIMS = (156, 132)
sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/week7-brrring.m4a"
)


class Menu:
    #    def __init__(self):

    def click(pos):
        if pos[0] >= 128 and pos[0] <= 384:
            if pos[1] >= 0 and pos[1] <= 64:
                print("EASY")
                sound.play()
                GameStart(120)

            elif pos[1] >= 128 and pos[1] <= 192:
                print("Medium")
                sound.play()
                GameStart(140)

            elif pos[1] >= 256 and pos[1] <= 320:
                print("Hard")
                sound.play()
                GameStart(160)

            elif pos[1] >= 384 and pos[1] <= 448:
                sound.play()
                print("Exit")
                sleep(1.00)
                sys.exit("user option was to leave ")

    def draw(canvas):
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, (256, (2 * 512 / 3)), (512, 512))

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
    frame.set_canvas_background("#2C6A6A")
    frame.set_mouseclick_handler(click)

    frame.set_draw_handler(draw)

    frame.start()
