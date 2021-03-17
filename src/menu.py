try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import sys
##import codeskulptor
from time import sleep

IMG = simplegui.load_image("http://personal.rhul.ac.uk/zjac/281/snake.png")
# IMG_CENTRE = (200, 200)
# IMG_DIMS = (400, 400)
IMG_CENTRE = (78, 66)
IMG_DIMS = (156, 132)
sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/week7-brrring.m4a"
)


class Menu:
    def click(pos):
        if pos[0] >= 100 and pos[0] <= 300:
            if pos[1] >= 50 and pos[1] <= 100:
                print("Start Player 1")
                sound.play()

            elif pos[1] >= 150 and pos[1] <= 200:
                print("Options")
                sound.play()

                opt_obj = options()
                opt_obj.draw()

            elif pos[1] >= 250 and pos[1] <= 300:
                sound.play()
                print("Exit")
                sleep(1.00)
                sys.exit("user option was to leave ")

    def draw(canvas):
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, (200, (2 * 300 / 3)), (400, 400))

        canvas.draw_polygon(
            [(100, 50), (300, 50), (300, 100), (100, 100)], 5, "#660099"
        )
        canvas.draw_text("1 player", (160, 80), 18, "White", "monospace")

        canvas.draw_polygon(
            [(100, 150), (300, 150), (300, 200), (100, 200)], 5, "#660099"
        )
        canvas.draw_text("Options", (170, 180), 18, "White", "monospace")

        canvas.draw_polygon(
            [(100, 250), (300, 250), (300, 300), (100, 300)], 5, "#660099"
        )
        canvas.draw_text("Exit", (180, 280), 18, "White", "monospace")

        canvas.draw_text("High score: ", (265, 380), 18, "White", "monospace")

    frame = simplegui.create_frame("Home", 400, 400)
    frame.set_canvas_background("#2C6A6A")
    frame.set_mouseclick_handler(click)

    frame.set_draw_handler(draw)

    frame.start()


class options:
    IMG = simplegui.load_image("http://personal.rhul.ac.uk/zjac/281/snake.png")
    # IMG_CENTRE = (200, 200)
    # IMG_DIMS = (400, 400)
    IMG_CENTRE = (78, 66)
    IMG_DIMS = (156, 132)

    def click(pos):
        if pos[0] >= 100 and pos[0] <= 300:
            if pos[1] >= 50 and pos[1] <= 100:
                print("Start")

            elif pos[1] >= 150 and pos[1] <= 200:
                print("Options")

            elif pos[1] >= 250 and pos[1] <= 300:
                print("Exit")
                sys.exit("user option was to leave ")

            elif pos[1] >= 20 and pos[1] <= 40:
                if pos[0] <= 120:
                    print("GREEN")
                elif pos[0] <= 160:
                    print("RED")
                elif pos[0] <= 200:
                    print("Blue")
                elif pos[0] <= 240:
                    print("White")
                elif pos[0] <= 280:
                    print("Fu")

    def draw(canvas):
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, (200, (2 * 300 / 3)), (400, 400))

        canvas.draw_polygon(
            [(100, 20), (120, 20), (120, 40), (100, 40)], 5, "Green", "Green"
        )
        canvas.draw_polygon(
            [(140, 20), (160, 20), (160, 40), (140, 40)], 5, "Red", "Red"
        )
        canvas.draw_polygon(
            [(180, 20), (200, 20), (200, 40), (180, 40)], 5, "Blue", "Blue"
        )
        canvas.draw_polygon(
            [(220, 20), (240, 20), (240, 40), (220, 40)], 5, "White", "White"
        )
        canvas.draw_polygon(
            [(260, 20), (280, 20), (280, 40), (260, 40)], 5, "Fuchsia", "Fuchsia"
        )
        canvas.draw_polygon([(100, 50), (300, 50), (300, 100), (100, 100)], 5, "Blue")

        canvas.draw_text("Change snake colour", (120, 80), 18, "White", "monospace")

        canvas.draw_polygon([(100, 150), (300, 150), (300, 200), (100, 200)], 5, "Blue")

        canvas.draw_text("Easy", (150, 175), 12, "Red")

        canvas.draw_polygon([(100, 250), (300, 250), (300, 300), (100, 300)], 5, "Blue")
        canvas.draw_text("Exit", (160, 275), 18, "White", "monospace")

        canvas.draw_text("High score: ", (265, 380), 18, "White", "monospace")
