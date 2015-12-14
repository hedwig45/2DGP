from pico2d import *

import game_framework

from boy import Boy # import Boy class from boy.py
from ball import Ball
from grass import Grass
from crown import Crown
from eventBackground import EventBackground

name = "collision"

boy = None
balls = None
grass = None
crowns = None
eventback = None

normalMode = True
eventMode = False

def create_world():
    global boy, grass, balls, crowns, eventback
    boy = Boy()
    balls = [Ball() for i in range(10)]
    crowns = Crown()
    grass = Grass()
    eventback = EventBackground()

def destroy_world():
    global boy, grass, balls

    del(boy)
    del(balls)
    del(grass)
    #del(crowns)
    #del(eventback)

def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()

def exit():
    destroy_world()
    close_canvas()

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b :
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True

def update(frame_time):
    global normalMode, eventMode
    boy.update(frame_time)
    grass.update()
    eventback.update()
    for ball in balls:
        ball.update(frame_time)
    crowns.update(frame_time)

    for ball in balls:
        if collide(boy, ball):
            boy.score+=1
            ball.ex = 0
    if collide(boy, crowns):
        normalMode = False
        eventMode = True
        boy.normalMode = False
        boy.eventMode = True
        crowns.ex = 0
    pass

def draw(frame_time):
    clear_canvas()
    if(normalMode == True):
        grass.draw()
    if(eventMode == True):
        eventback.draw()
    boy.draw()
    for ball in balls:
        ball.draw()

    if normalMode == True:
        crowns.draw()

    update_canvas()






