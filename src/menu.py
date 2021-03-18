import sys
from time import sleep  # import codeskulptor

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from icecream import ic


class Menu:
    def __init__(self):
        self.option: bool = False
        self.IMG = simplegui.load_image("http://personal.rhul.ac.uk/zjac/281/snake.png")
        self.IMG_CENTRE = (78, 66)
        self.IMG_DIMS = (156, 132)
        self.sound = simplegui.load_sound(
            "http://commondatastorage.googleapis.com/codeskulptor-assets/week7-brrring.m4a"
        )

    # This is active before eveyrthing else woudl starrt
    def __start_game(self, main_length: int, speed: int):
        if self.option is True:
            # pointer = GameStart(length=main_length)
            print(pointer)

    def click(self, pos):
        if pos[0] >= 128 and pos[0] <= 384:
            if pos[1] >= 0 and pos[1] <= 64:
                ic("Easy")
                self.sound.play()
                # GameStart(120)
                # self.__start_game(main_length=5, speed=100)

            elif pos[1] >= 128 and pos[1] <= 192:
                self.option = True
                ic("Medium")
                self.sound.play()
                # self.__start_game(main_length=15, speed=80)

            elif pos[1] >= 256 and pos[1] <= 320:
                ic("Hard")
                self.sound.play()
                # self.__start_game(main_length=25, speed=50)

            elif pos[1] >= 384 and pos[1] <= 448:
                self.sound.play()
                sleep(1.00)
                sys.exit()

    def draw(self, canvas):
        canvas.draw_image(
            self.IMG, self.IMG_CENTRE, self.IMG_DIMS, (256, (2 * 512 / 3)), (512, 512)
        )

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


def main() -> None:
    menu = Menu()
    frame = simplegui.create_frame("Home", 512, 512)

    frame.set_canvas_background("#2C6A6A")

    frame.set_mouseclick_handler(menu.click)

    frame.set_draw_handler(menu.draw)

    frame.start()


if __name__ == "__main__":
    main()
