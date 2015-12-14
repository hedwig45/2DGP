import random

from pico2d import *

class EventBackground:
    image = None
    def __init__(self):
        self.image = load_image('eventBackground.png')
        self.x = 400
        self.y = 300
        self.x2 = 1200
        self.y2 = 300

    def update(self):
        self.x -= 1
        self.x2 -= 1
        if(self.x == -400):
             self.x = 400
        if(self.x2 == 400):
            self.x2 = 1200
    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, 300)
        #self.image.draw(self.x, self.y)
        #self.image.draw(self.x2, self.y2)



