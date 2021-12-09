from pico2d import *


class Block():
    def __init__(self, x, y):
        self.image = load_image('block1.png')
        self.x = x
        self.y = y
        self.frame=0

    def draw(self):
        self.image.clip_draw(self.frame*18, 0, 18,19, self.x, self.y, 50, 50)

    def update_block(self,x):
        self.x += x

    def change_block(self):
        self.frame = 1

    def get_bb(self):
        return self.x-25,self.y-25,self.x+25,self.y+25


class Coin():
    def __init__(self, x, y):
        self.image = load_image('coin.png')
        self.x = x
        self.y = y
        self.frame=0
        self.frame_control = 0
        self.coin_count=0
        self.image_life = load_image('life_image.png')

    def draw(self):
        self.image.clip_draw(self.frame*23, 0, 24, 20, self.x, self.y, 40, 40)

    def update_frame_block(self):
        self.frame_control += 1
        if self.frame_control == 15:
            self.frame = (self.frame+1) % 4
            self.frame_control = 0

    def update_coin(self, x):
        self.x += x
        
    def get_bb(self):
        return self.x-20,self.y-20,self.x+20,self.y+20

class Mushroom1():
    def __init__(self, x, y):
        self.image = load_image('ms1.png')
        self.x = x
        self.y = y
        self.turn=0
        self.up = 1

    def draw(self):
        if self.turn == 1 and self.up<40:
            self.up += 1
        self.image.clip_draw(0, 0, 39, 39, self.x, self.y+self.up, 40, 40)

    def update_mushroom1(self, x):
        self.x += x

    def get_bb(self):
        return self.x-20,self.y-20,self.x+20,self.y+20+self.up

    def mushroom1_turn(self):
        self.turn = 1

class Mushroom2():
    def __init__(self, x, y):
        self.image = load_image('ms2.png')
        self.x = x
        self.y = y
        self.turn=0
        self.up = 1

    def draw(self):
        if self.turn == 1 and self.up<40:
            self.up += 1
        self.image.clip_draw(0, 0, 39, 37, self.x, self.y+self.up, 40, 40)

    def update_mushroom2(self, x):
        self.x += x

    def get_bb(self):
        return self.x-20,self.y-20,self.x+20,self.y+20+self.up
    
    def mushroom2_turn(self):
        self.turn = 1

class Flower():
    def __init__(self, x, y):
        self.image = load_image('flower1.png')
        self.x = x
        self.y = y
        self.turn=0
        self.up = 1

    def draw(self):
        if self.turn == 1 and self.up<40:
            self.up += 1
        self.image.clip_draw(0, 0, 37, 37, self.x, self.y+self.up, 40, 40)

    def update_flower(self, x):
        self.x += x

    def get_bb(self):
        return self.x-20,self.y-20,self.x+20,self.y+20+self.up

    def flower_turn(self):
        self.turn = 1
    
class Star():
    def __init__(self, x, y):
        self.image = load_image('star1.png')
        self.x = x
        self.y = y
        self.turn=0
        self.up = 1

    def draw(self):
        if self.turn == 1 and self.up<40:
             self.up += 1
        self.image.clip_draw(0, 0, 37, 37, self.x, self.y+self.up, 40, 40)

    def update_star(self, x):
        self.x += x

    def get_bb(self):
        return self.x-20,self.y-20,self.x+20,self.y+20+self.up
    
    def star_turn(self):
        self.turn = 1
    
class Flag():
    def __init__(self, x, y):
        self.image = load_image('mario-flag.png')
        self.x = x
        self.y = y

    def draw(self):
        self.image.clip_draw(0, 0, 236, 854, self.x, self.y, 100, 360)

    def update_flag(self, x):
        self.x += x

    def get_bb(self):
        return self.x-50,self.y-180,self.x+50,self.y+180
