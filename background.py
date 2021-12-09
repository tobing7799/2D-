from pico2d import *


class Map():
    def __init__(self):
        self.image1 = load_image('background-test.jpg')
        self.image2 = load_image('background-test0.jpg')
        self.image3 = load_image('background-test1.jpg')
        self.image4 = load_image('background-test2.jpg')
        self.top,self.right=600,3000
        self.bottom,self.left=0,0
        self.stage_count=0
        self.bgm = load_music('bgm.mp3')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()
        self.bgm_state=1

    def draw(self):
        if self.stage_count== 1:
            self.image1.clip_draw(self.left,self.bottom, 6000, self.top, self.right,300)
        if self.stage_count== 2:
            self.image2.clip_draw(self.left,self.bottom, 6000, self.top, self.right,300)
        if self.stage_count== 3:
            self.image3.clip_draw(self.left,self.bottom, 6000, self.top, self.right,300)
        if self.stage_count== 4:
            self.image4.clip_draw(self.left,self.bottom, 6000, self.top, self.right,300)
        

    def map_xy(self):
        return self.left,self.bottom,self.right,self.top

    def update_map(self,left,bottom,right,top):
        self.left=left
        self.right=right
        self.top=top
        self.bottom=bottom

    def update_stage_count(self,x):
        self.stage_count = x
