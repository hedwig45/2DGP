import random

from pico2d import *

class Crown:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(1000, 1790), random.randint(200, 390)
        self.ex = 1
        if Crown.image == None:
            Crown.image = load_image('GoldCrown.png')

    def update(self, frame_time):
        self.x -= 1
        if self.x < 0:
            self.x , self.y = random.randint(100, 1800), random.randint(200, 390)
            self.ex = 1
        pass

    def draw(self):
        if self.ex:
            self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10