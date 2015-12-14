import random

from pico2d import *

normalMode = True
eventMode = False
charSize = 100
logo_time = 0

class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    feverimage = None

    RIGHT_RUN, LEFT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        global normalMode, eventMode, charSize
        self.x, self.y = 100, 50
        self.frame = 0
        self.life_time = 0.0
        self.font = load_font("ConsolaMalgun.TTF",40)
        #self.total_frames = 0.0
        self.dir = 0
        #self.distance = 20
        self.score = 0
        self.charSize = 100
        self.normalMode = True
        self.eventMode = False

        self.jumpingCount = 0
        self.JumpingUp = True
        self.JumpingDown = False

        self.RUN = True
        self.JUMP = False

        self.timer = 0

        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('Cookie_sheet.png')


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time

        if(self.RUN == True):
            self.state = 0
            self.frame = (self.frame + 1) % 3

        if(self.JUMP == True):
            self.state = 2
            self.frame = (self.frame + 1) % 7

            if(self.JumpingUp == True):
                self.y += (distance * 2)
                if(self.y >= 300):
                    self.JumpingUp = False
                    self.JumpingDown = True

            if(self.JumpingDown == True):
                self.y -= (distance * 2)
                if(self.y <= 50):
                    self.RUN = True
                    self.JUMP = False
                    self.JumpingUp = True
                    self.JumpingDown = False

        self.x = clamp(0, self.x, 800)


    def draw(self):
        global charSize, logo_time
        if self.normalMode == True:
            self.image.clip_draw(self.frame * 100, self.state * 100, charSize, charSize, self.x, self.y)
        if self.eventMode == True:
            if (logo_time < 0.2):
                Boy.image = load_image('cloud1.png')
                self.image.clip_draw(0, 0, 800, 600, 400, 300)
                logo_time += 0.01
            elif (logo_time < 0.4):
                Boy.image = load_image('cloud2.png')
                self.image.clip_draw(0, 0, 800, 600, 400, 300)
                logo_time += 0.01
            elif (logo_time < 0.6):
                Boy.image = load_image('cloud3.png')
                self.image.clip_draw(0, 0, 800, 600, 400, 300)
                logo_time += 0.01
            elif (logo_time < 0.8):
                Boy.image = load_image('cloud4.png')
                self.image.clip_draw(0, 0, 800, 600, 400, 300)
                logo_time += 0.01
            elif (logo_time < 1):
                Boy.image = load_image('fever_light.png')
                self.image.clip_draw(0, 0, 344, 344, self.x, self.y, 150, 150)
                logo_time += 0.01
            elif (logo_time < 1.5):
                Boy.image = load_image('fever_light2.png')
                self.image.clip_draw(0, 0, 344, 344, self.x, self.y, 300, 300)
                logo_time += 0.01
                 #delay(1.0)
                 #Boy.image = load_image('Cookie_sheet.png')
            else:
                Boy.image = load_image('Cookie_sheet.png')
                self.image.clip_draw(self.frame * 100, self.state * 100, charSize, charSize, self.x, self.y + 50, 300, 300)
        self.font.draw(10,580,'Score %d '% (self.score),(255,255,255))


    def get_bb(self):
        return self.x - 50, self.y -50, self.x + 50, self.y + 50
        pass

    def handle_event(self, event):
        events = get_events()
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.JUMP = True
            self.RUN = False





