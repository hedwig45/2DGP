__author__ = 'hedwig45'
import random
import json
import os

Crash = False

from pico2d import *
running = False

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.x = 400
        self.y = 30
        self.x2 = 1200
        self.y2 = 30

    def update(self):
        self.x -= 10
        self.x2 -= 10
        if(self.x == -400):
             self.x = 400
        if(self.x2 == 400):
            self.x2 = 1200
    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x2, self.y2)

class ObstacleWood:
    def __init__(self):
        self.image = load_image('ObstacleWood.png')
        self.x = 700
        self.y = 60

    if(Crash == False):
        def update(self):
            self.x -= 10
            if(self.x == -400):
                self.x = 1000

    def draw(self):
        self.image.draw(self.x, self.y)

class Boy:
    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = 0
        self.image = load_image('Cookie_sheet.png')
        self.dir = 1
        self.distance = 20
        self.jumpingCount = 0

        self.RUN = True
        self.JUMP = False

        self.JumpingUp = True
        self.JumpingDown = False

        self.state = 0
        pass

    def handle_events(self):
        global running

        events = get_events()
        for event in events:

            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_SPACE:
                    self.RUN = False
                    self.JUMP = True

    def update(self):
        global obWood
        global ObstacleWood
        global Crash

        if(self.RUN == True):
            self.state = 0
            self.frame = (self.frame + 1) % 3

        if(ObstacleWood().x < 500):
            Crash = True

        if(self.JUMP == True):
            self.state = 2
            self.frame = (self.frame + 1) % 7
            if(self.jumpingCount == 0):
                #self.oriYposition = self.y
                self.jumpingCount += 1

            if(self.JumpingUp == True):
                self.y += self.distance
                if(self.y >= + 400):
                    self.JumpingUp = False
                    self.JumpingDown = True

            if(self.JumpingDown == True):
                self.y -= self.distance
                if(self.y <= 90):
                    self.RUN = True
                    self.JUMP = False
                    self.JumpingUp = True
                    self.JumpingDown = False


    def draw(self):
        self.image.clip_draw(self.frame * 100,self.state*100, 100, 100, self.x, self.y)
    pass

def main():
    global running
    open_canvas()

    boy = Boy()
    grass = Grass()
    obWood = ObstacleWood()

    running = True

    while running:
        #handle_events()

        boy.handle_events()

        boy.update()
        grass.update()
        obWood.update()

        clear_canvas()
        grass.draw()
        obWood.draw()
        boy.draw()
        update_canvas()

        delay(0.04)

    close_canvas()
    pass

if __name__ == '__main__':
    main()