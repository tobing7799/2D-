from pico2d import *

class Title():
    def __init__(self):
        self.image = load_image('title1.png')

    def draw(self):
        self.image.clip_draw(0, 0, 512, 512, 400, 320, 840, 640)

class Shop():
    def __init__(self):
        self.image = load_image('shop.jpg')
        self.image1 = load_image('ms1.png')
        self.image2 = load_image('ms2.png')
        self.image3 = load_image('flower1.png')
        self.image4 = load_image('star1.png')
        self.image5 = load_image('1.png')
        self.image6 = load_image('3.png')
        self.image7 = load_image('5.png')

    def draw(self):
        self.image.clip_draw(50, 0, 793, 500, 400, 320, 840, 640)
        self.image1.clip_draw(0, 0, 39, 39, 220, 160, 100, 100)
        self.image2.clip_draw(0, 0, 39, 37, 335, 160, 100, 100)
        self.image3.clip_draw(0, 0, 37, 37, 465, 160, 100, 100)
        self.image4.clip_draw(0, 0, 37, 37, 580, 160, 100, 100)
        self.image5.clip_draw(0, 0, 800, 800, 220, 80, 150, 150)
        self.image6.clip_draw(0, 0, 800, 800, 335, 80, 150, 150)
        self.image6.clip_draw(0, 0, 800, 800, 465, 80, 150, 150)
        self.image7.clip_draw(0, 0, 800, 800, 580, 80, 150, 150)