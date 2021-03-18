try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import sys

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


def draw(canvas):
    canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, (200, (2 * 300 / 3)), (400, 400))

    canvas.draw_polygon([(100, 50), (200, 50), (200, 100), (100, 100)], 5, "Blue")
    canvas.draw_text("1 player", (130, 75), 12, "Red")

    canvas.draw_polygon([(200, 50), (300, 50), (300, 100), (200, 100)], 5, "Blue")
    canvas.draw_text("2 player", (230, 75), 12, "Red")

    canvas.draw_polygon([(100, 150), (300, 150), (300, 200), (100, 200)], 5, "Blue")
    canvas.draw_text("Options", (200, 175), 12, "Red")

    canvas.draw_polygon([(100, 250), (300, 250), (300, 300), (100, 300)], 5, "Blue")
    canvas.draw_text("Exit", (200, 275), 12, "Red")

    canvas.draw_text("High score: ", (35, 380), 12, "Red")


frame = simplegui.create_frame("Home", 512, 512)
frame.set_canvas_background("#2C6A6A")
frame.set_mouseclick_handler(click)

frame.set_draw_handler(draw)

frame.start()
