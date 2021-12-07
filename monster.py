from pico2d import *


class Monster1():
    def __init__(self, x, y):
        self.image1 = load_image('monster1-right.png')
        self.image2 = load_image('monster1-left.png')
        self.image3 = load_image('monster1-stop.png')
        self.x = x
        self.y = y
        self.frame = 0
        self.frame_control = 0
        self.turn = 1
        self.turn_count = 0
        self.speed = 0.3

    def draw(self):
        if self.turn == 1:
            self.image1.clip_draw(self.frame*20, 0, 20, 20, self.x, self.y, 40, 40)
        elif self.turn == -1:
            self.image2.clip_draw(self.frame * 20, 0, 20, 20, self.x, self.y, 40, 40)
        elif self.turn == 2:
            self.image3.clip_draw(0, 0, 20, 10, self.x, self.y, 40, 20)

    def update_moster1(self, x):
        self.x += x

    def update_frame_moster1(self):
        self.frame_control += 1
        self.x += self.speed
        if self.frame_control == 15 and self.turn != 2:
            self.frame = (self.frame+1) % 9
            self.frame_control = 0
            self.turn_count += 1

        elif self.frame_control == 15 and self.turn == 2:
            self.turn = 3
            self.frame_control = 0
            self.turn_count = 0

        if self.turn_count == 30 and self.turn != 2:
            self.turn *= -1
            self.turn_count = 0
            self.speed *= -1

    def change_monster1(self):
        if self.turn != 2:
            self.turn = 2
            self.speed = 0
            self.y = 80

class Monster2():
    def __init__(self, x, y):
        self.image1 = load_image('monster2-right-test.png')
        self.image2 = load_image('monster2-left-test.png')
        self.image3 = load_image('monster2-stop.png')
        self.x = x
        self.y = y
        self.frame = 0
        self.frame_control = 0
        self.turn = 1
        self.turn_count = 0
        self.speed = 0.3
        self.frame_y = 62
        self.timer = 1000

    def draw(self):
        if self.turn == 1:
            self.image1.clip_draw(self.frame * 18, 0, 18, 31, self.x, self.y, 40, 60)
        elif self.turn == -1:
            self.image2.clip_draw(self.frame * 18, 0, 18, 31, self.x, self.y, 40, 60)
        elif self.turn == 2:
            self.image3.clip_draw(0, 0, 18, 18, self.x, self.y, 40, 40)

    def update_moster2(self, x):
        self.x += x

    def update_frame_moster2(self):
        self.frame_control += 1
        self.x += self.speed
        if self.frame_control == 15 and self.turn != 2:
            self.frame = (self.frame+1) % 6
            self.frame_y -= 31
            self.frame_control = 0
            self.turn_count += 1

        if self.turn_count == 30 and self.turn != 2:
            self.turn *= -1
            self.turn_count = 0
            self.speed *= -1

        if self.turn == 2:
            if self.timer > 0:
                self.timer -= 1
            elif self.timer == 0:
                self.turn = 1
                self.speed = 0.3
                self.y += 10
                self.frame = 0
                self.frame_control = 0
                self.turn = 1
                self.turn_count = 0
                self.frame_y = 62
                self.timer = 1000

    def change_monster2(self):
        if self.turn != 2:
            self.turn = 2
            self.speed = 0
            self.y = 80
