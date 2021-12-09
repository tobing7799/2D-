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
        self.num1 = load_image('number-1.png')
        self.num2 = load_image('number-2.png')
        self.num3 = load_image('number-3.png')
        self.num4 = load_image('number-4.png')

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
        self.num1.clip_draw(0, 0, 800, 800, 220, 30, 300, 300)
        self.num2.clip_draw(0, 0, 800, 800, 335, 30, 300, 300)
        self.num3.clip_draw(0, 0, 800, 800, 465, 30, 300, 300)
        self.num4.clip_draw(0, 0, 800, 800, 580, 30, 300, 300)

class Over():
    def __init__(self):
        self.image = load_image('gameover.png')
    def draw(self):
        self.image.draw(400,300,800,600)

class Clear():
    def __init__(self):
        self.image = load_image('clear.png')
    def draw(self):
        self.image.draw(400,300,800,600)

class Life():
    def __init__(self):
        self.image = load_image('mario-face.png')
        self.coin_image = load_image('coin.png')
        self.image_life = load_image('life_image.png')
        self.image0 = load_image('number-0.png')
        self.image1 = load_image('number-1.png')
        self.image2 = load_image('number-2.png')
        self.image3 = load_image('number-3.png')
        self.image4 = load_image('number-4.png')
        self.image5 = load_image('number-5.png')
        self.image6 = load_image('number-6.png')
        self.image7 = load_image('number-7.png')
        self.image8 = load_image('number-8.png')
        self.image9 = load_image('number-9.png')
        self.life_count = 3
        self.coin_count = 0

    def draw(self):
        self.image.clip_draw(0,0,240,273,50,550,50,50)
        self.image_life.clip_draw(0,0,800,800,80,550,200,200)
        if self.life_count//10 == 0:
            self.image0.clip_draw(0,0,800,800,100,550,200,200)
        elif self.life_count//10 == 1:
            self.image1.clip_draw(0,0,800,800,100,550,200,200)
        elif self.life_count//10 == 2:
            self.image2.clip_draw(0,0,800,800,100,550,200,200)
        elif self.life_count//10 == 3:
            self.image3.clip_draw(0,0,800,800,100,550,200,200)
        elif self.life_count//10 == 4:
            self.image4.clip_draw(0,0,800,800,100,550,200,200)
        elif self.life_count//10 == 5:
            self.image5.clip_draw(0,0,800,800,100,550,200,200)
        elif self.life_count//10 == 6:
            self.image6.clip_draw(0,0,800,800,100,550,200,200)
        elif self.life_count//10 == 7:
            self.image7.clip_draw(0,0,800,800,100,550,200,200)
        elif self.life_count//10 == 8:
            self.image8.clip_draw(0,0,800,800,100,550,200,200)
        elif self.life_count//10 == 9:
            self.image9.clip_draw(0,0,800,800,100,550,200,200)

        if self.life_count%10 == 0:
            self.image0.clip_draw(0,0,800,800,120,550,200,200)
        elif self.life_count%10 == 1:
            self.image1.clip_draw(0,0,800,800,120,550,200,200)
        elif self.life_count%10 == 2:
            self.image2.clip_draw(0,0,800,800,120,550,200,200)
        elif self.life_count%10 == 3:
            self.image3.clip_draw(0,0,800,800,120,550,200,200)
        elif self.life_count%10 == 4:
            self.image4.clip_draw(0,0,800,800,120,550,200,200)
        elif self.life_count%10 == 5:
            self.image5.clip_draw(0,0,800,800,120,550,200,200)
        elif self.life_count%10 == 6:
            self.image6.clip_draw(0,0,800,800,120,550,200,200)
        elif self.life_count%10 == 7:
            self.image7.clip_draw(0,0,800,800,120,550,200,200)
        elif self.life_count%10 == 8:
            self.image8.clip_draw(0,0,800,800,120,550,200,200)
        elif self.life_count%10 == 9:
            self.image9.clip_draw(0,0,800,800,120,550,200,200)

        self.coin_image.clip_draw(0,0,24,20,50,500,50,50)
        self.image_life.clip_draw(0,0,800,800,80,500,200,200)
        if self.coin_count//10 == 0:
            self.image0.clip_draw(0,0,800,800,100,500,200,200)
        elif self.coin_count//10 == 1:
            self.image1.clip_draw(0,0,800,800,100,500,200,200)
        elif self.coin_count//10 == 2:
            self.image2.clip_draw(0,0,800,800,100,500,200,200)
        elif self.coin_count//10 == 3:
            self.image3.clip_draw(0,0,800,800,100,500,200,200)
        elif self.coin_count//10 == 4:
            self.image4.clip_draw(0,0,800,800,100,500,200,200)
        elif self.coin_count//10 == 5:
            self.image5.clip_draw(0,0,800,800,100,500,200,200)
        elif self.coin_count//10 == 6:
            self.image6.clip_draw(0,0,800,800,100,500,200,200)
        elif self.coin_count//10 == 7:
            self.image7.clip_draw(0,0,800,800,100,500,200,200)
        elif self.coin_count//10 == 8:
            self.image8.clip_draw(0,0,800,800,100,500,200,200)
        elif self.coin_count//10 == 9:
            self.image9.clip_draw(0,0,800,800,100,500,200,200)

        if self.coin_count%10 == 0:
            self.image0.clip_draw(0,0,800,800,120,500,200,200)
        elif self.coin_count%10 == 1:
            self.image1.clip_draw(0,0,800,800,120,500,200,200)
        elif self.coin_count%10 == 2:
            self.image2.clip_draw(0,0,800,800,120,500,200,200)
        elif self.coin_count%10 == 3:
            self.image3.clip_draw(0,0,800,800,120,500,200,200)
        elif self.coin_count%10 == 4:
            self.image4.clip_draw(0,0,800,800,120,500,200,200)
        elif self.coin_count%10 == 5:
            self.image5.clip_draw(0,0,800,800,120,500,200,200)
        elif self.coin_count%10 == 6:
            self.image6.clip_draw(0,0,800,800,120,500,200,200)
        elif self.coin_count%10 == 7:
            self.image7.clip_draw(0,0,800,800,120,500,200,200)
        elif self.coin_count%10 == 8:
            self.image8.clip_draw(0,0,800,800,120,500,200,200)
        elif self.coin_count%10 == 9:
            self.image9.clip_draw(0,0,800,800,120,500,200,200)

    def less_life(self):
        self.life_count -= 1
        if self.life_count == 0:
            return 1

    def more_life(self):
        self.life_count += 1

    def more_coin(self):
        self.coin_count += 1

    def coin_control(self,x):
        self.coin_count=x

    def coin_return(self):
        return self.coin_count

class Item():
    def __init__(self):
        self.ms = load_image('ms1.png')
        self.flower = load_image('flower1.png')
        self.star = load_image('star1.png')
        self.item_count=0

    def draw(self):
        if self.item_count == 1:
            self.ms.clip_draw(0, 0, 39, 39, 50, 450, 50, 50)
        if self.item_count == 3:
            self.flower.clip_draw(0, 0, 37, 37, 50, 450, 50, 50)
        if self.item_count == 4:
            self.star.clip_draw(0, 0, 37, 37, 50, 450, 50, 50)

    def update_item(self,num):
        self.item_count = num

    def item_return(self):
        return self.item_count
