import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from src.Game_Start import GameStart
from system_components.frame import frame_height, frame_width


class Welcome:
    def draw_handler(self, canvas):
        canvas.draw_text("Snake Game", [frame_width / 2, frame_height / 2], 48, "Red")


welcome = Welcome()


class Interation:
    def __init__(self):
        # Screeens
        self.game = GameStart()
        self.welcome = Welcome()

        # Initial Screen
        self.screen = "Welcome"
        self.frame = simplegui.create_frame("Game", frame_width, frame_height)
        self.frame.set_draw_handler(self.welcome.draw_handler)

        # Button
        self.button = self.frame.add_button("Start Game", self.game_button_handler)

        # Start frame
        self.frame.start()

    def game_button_handler(self):
        if self.screen == "Welcome":
            self.screen = "Game"
            self.frame.set_draw_handler(self.game.draw_handler)
            self.button.set_text("Exit Game")
        else:
            self.screen = "Welcome"
            self.frame.set_draw_handler(self.welcome.draw_handler)
            self.button.set_text("Restart Game")


Interation()
