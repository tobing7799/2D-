from pico2d import *


class Map():
    def __init__(self):
        self.image = load_image('background-test.jpg')
        self.top,self.right=600,3000
        self.bottom,self.left=0,0

    def draw(self):
        self.image.clip_draw(self.left,self.bottom, 6000, self.top, self.right,300)

    def map_xy(self):
        return self.left,self.bottom,self.right,self.top

    def update_map(self,left,bottom,right,top):
        self.left=left
        self.right=right
        self.top=top
        self.bottom=bottom
