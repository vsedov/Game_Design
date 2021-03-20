try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import sys
##import codeskulptor
from time import sleep

IMG = simplegui.load_image('https://opengameart.org/sites/default/files/attack1_1.png')
l1 = [-12,-8,-4,0,4,8,12]
IMG2 = simplegui.load_image('http://personal.rhul.ac.uk/zjac/281/snake.png')
l2 = [-11,-7,-3,1,5,9,13]
IMG3 = simplegui.load_image('https://opengameart.org/sites/default/files/styles/medium/public/apple_1_0.png')
l3 = [-10,-6,-2,2,6,10,14]
IMG4 = simplegui.load_image('https://opengameart.org/sites/default/files/styles/medium/public/SneckoCreature.PNG')
l4 = [-9,-5,-1,3,7,11,15]
#IMG_CENTRE = (200, 200)
#IMG_DIMS = (400, 400)
IMG_CENTRE = (78, 66)
IMG_DIMS = (156, 132)
theme = 1
sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/week7-brrring.m4a")
    
class Menu:
#    def __init__(self):
        

    def click(pos):
        global theme
        if (pos[1] >=30 and pos [1] <= 48):
            if (pos[0] >=460  and pos[0] <=475):
                theme -= 1
            elif (pos[0] >=478 and pos[0] <=506):
                theme += 1
                
                
        if (pos[0] >= 128 and pos[0] <= 384):
            if (pos[1] >= 64 and pos[1] <= 128):
                print("Start Player 1")
                sound.play()
                
                
            elif (pos[1] >= 192 and pos[1] <= 256):
                print("Options")
                sound.play()

                opt_obj = options()
                opt_obj.draw()
                
                
            elif (pos[1] >= 320 and pos[1] <= 384):
                sound.play()
                print("Exit")
                sleep(1.00)
                sys.exit("user option was to leave " )
                

    def user(username):
        username = str(username)
    
    def draw(canvas):
        global theme
        
        if theme in l1:
            canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, (300, (2*512 /4)), (512,512))
        elif theme in l2:
            canvas.draw_image(IMG2, IMG_CENTRE, IMG_DIMS, (256, (2*512 /4)), (512,512))
        elif theme in l3:
            canvas.draw_image(IMG3, IMG_CENTRE, IMG_DIMS, (256, (2*512 /4)), (512,512))
        elif theme in l4:
            canvas.draw_image(IMG4, IMG_CENTRE, IMG_DIMS, (256, (2*512 /4)), (512,512))
        
        canvas.draw_polygon([(460, 48), (506, 48), (506, 0), (460, 0)], 5, '#660099')
        canvas.draw_text('Theme', (463, 27), 15, 'White', 'monospace')
        canvas.draw_text('<--', (465, 40), 15, 'White', 'monospace')
        canvas.draw_text('-->', (478, 40), 15, 'White', 'monospace')

        canvas.draw_polygon([(128, 64), (384, 64), (384, 0), (128, 0)], 5, '#660099')
        canvas.draw_text('Easy', (204.8, 45), 23, 'White', 'monospace')
        
        canvas.draw_polygon([(128, 192), (384, 192), (384, 128), (128, 128)], 5, '#660099')
        canvas.draw_text('Medium', (204.8, 170), 23, 'White', 'monospace')
        
        canvas.draw_polygon([(128, 320), (384, 320), (384, 256), (128, 256)], 5, '#660099')
        canvas.draw_text('Hard', (217.6, 295), 23, 'White','monospace')
        
        canvas.draw_polygon([(128, 448), (384, 448), (384, 384), (128, 384)], 5, '#660099')
        canvas.draw_text('Exit', (230.4, 420), 23, 'White','monospace')
        
        canvas.draw_text('High score: ', (339.2, 486.4), 23, 'White','monospace')
        canvas.draw_text(('Name: '), (10, 486.4), 23, 'White','monospace')
        

        
        
    frame = simplegui.create_frame("Home", 512, 512)
    frame.add_input("Enter your name", user, 100)
    frame.set_canvas_background('#2C6A6A')
    frame.set_mouseclick_handler(click)

    frame.set_draw_handler(draw)

    frame.start()
