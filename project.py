from pico2d import *
from character import *
from background import *
from block import *
from monster import *
from title import *

def handle_events():
    global dir
    global prev_dir
    global jump
    global stop
    global title_count
    global game_state
    global stage
    global item
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                prev_dir=dir
                dir += 1
                check_dir()
            elif event.key == SDLK_LEFT:
                prev_dir=dir
                dir -= 1
                check_dir()
            elif event.key == SDLK_UP:
                if dir == 1:
                    mario.right_jump()
                elif dir == -1:
                    mario.left_jump()
                elif dir==0:
                    if prev_dir==1:
                        mario.right_jump()
                    elif prev_dir==-1:
                        mario.left_jump()
            elif event.key == SDLK_DOWN:
                #game_state=0
                pass
            elif event.key == SDLK_SPACE:
                if title_count == 0:
                    title_count = 1
                if game_state == 2:
                    if stage == 4:
                        close_canvas()
                        break
                    if title_count == 2:
                        stage += 1
                        game_state = 1
                        title_count = 1
                        restart()
                        break
                    title_count = 2
            elif event.key == SDLK_p:
                if title_count == 1:
                    title_count = 2
                elif title_count == 2:
                    title_count = 1
            elif event.key == SDLK_r:
                if game_state == 0:
                    restart()
            elif event.key == SDLK_1:
                if title_count == 2:
                    if life.coin_return() >= 1:
                        item.update_item(1)
                        life.coin_control(life.coin_return()-1)
            elif event.key == SDLK_2:
                if title_count == 2:
                    if life.coin_return() >= 3:
                        life.more_life()
                        life.coin_control(life.coin_return()-3)
            elif event.key == SDLK_3:
                if title_count == 2:
                    if life.coin_return() >= 3:
                        item.update_item(3)
                        life.coin_control(life.coin_return()-3)
            elif event.key == SDLK_4:
                if title_count == 2:
                    if life.coin_return() >= 5:
                        item.update_item(4)
                        life.coin_control(life.coin_return()-5)
            elif event.key == SDLK_a:
                if item.item_return() == 1:
                    mario.more_size()
                    item.update_item(0)
                elif item.item_return() == 3:
                    mario.more_size()
                    mario.mario_flower_state()
                    item.update_item(0)
                elif item.item_return() == 4:
                    mario.mario_star_state()
                    item.update_item(0)
            elif event.key==SDLK_ESCAPE:
                    close_canvas()
        elif event.type ==SDL_KEYUP:
            if event.key ==SDLK_RIGHT:
                prev_dir=dir
                dir -=1
                check_dir()
            elif event.key ==SDLK_LEFT:
                prev_dir=dir
                dir +=1
                check_dir()

def check_dir():
    if dir == 1:
         mario.right()
    elif dir==-1:
          mario.left()
    elif dir==0:
        if prev_dir>0:
            mario.stop_right()
        elif prev_dir<0:
            mario.stop_left()

def move_map():
    global map_left, map_bottom, map_right, map_top
    global mario_x, mario_y
    global dir
    if mario_x > 653 and 3805 <= 6000 + map_right and dir == 1:
        map_right += 650-mario_x
        if map_right < -2250:
            map_right = -2250
        for i in range(len(block)):
            block[i].update_block(650-mario_x)
        for i in range(len(coin)):
            coin[i].update_coin(650-mario_x)
        for i in range(len(monster1)):
            monster1[i].update_moster1(650-mario_x)
        for i in range(len(monster2)):
            monster2[i].update_moster2(650-mario_x)
        for i in range(len(mushroom1)):
            mushroom1[i].update_mushroom1(650-mario_x)
        for i in range(len(mushroom2)):
            mushroom2[i].update_mushroom2(650-mario_x)
        for i in range(len(flower)):
            flower[i].update_flower(650-mario_x)
        for i in range(len(star)):
            star[i].update_star(650-mario_x)
        for i in range(len(flag)):
            flag[i].update_flag(650-mario_x)
        mario.input_xy(mario_x, mario_y)

    elif mario_x < 245 and 0 < 3000-map_right and dir == -1:
        map_right += 249-mario_x
        if map_right > 3000:
            map_right = 3000
        for i in range(len(block)):
            block[i].update_block(249-mario_x)
        for i in range(len(coin)):
            coin[i].update_coin(249-mario_x)
        for i in range(len(monster1)):
            monster1[i].update_moster1(249-mario_x)
        for i in range(len(monster2)):
            monster2[i].update_moster2(249-mario_x)
        for i in range(len(mushroom1)):
            mushroom1[i].update_mushroom1(249-mario_x)
        for i in range(len(mushroom2)):
            mushroom2[i].update_mushroom2(249-mario_x)
        for i in range(len(flower)):
            flower[i].update_flower(249-mario_x)
        for i in range(len(star)):
            star[i].update_star(249-mario_x)
        for i in range(len(flag)):
            flag[i].update_flag(249-mario_x)
        mario.input_xy(mario_x, mario_y)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return 0
    if right_a < left_b: return 0
    if top_a < bottom_b: return 0
    if bottom_a > top_b: return 0

    if bottom_a < top_b:
        if bottom_a+10 > top_b:
            return 2

    if top_a > bottom_b:
        if top_a-10 < bottom_b:
            return 3
        
    if left_a < right_b:
        if left_a + 10 > right_b:
            return 4
        
    if right_a > left_b:
        if right_a-10 < left_b:
            return 5
    
    return 1

def restart():
    global game_state
    global mario
    global map
    global shop
    global life
    global over
    global stage
    global block
    global coin
    global monster1
    global monster2
    global mushroom1
    global mushroom2
    global flower
    global star
    global flag

    if game_state == 0:
        life.coin_control(0)
        life.less_life()
        
    game_state=1
    mario=Mario()
    map=Map()
    shop=Shop()
    over=Over()    
    block.clear()
    coin.clear()
    monster1.clear()
    monster2.clear()
    mushroom1.clear()
    mushroom2.clear()
    flower.clear()
    star.clear()
    flag.clear()

    if stage==1:
        block = []
        block.append(Block(500, 200))
        block.append(Block(550, 200))
        
        block.append(Block(600, 200))
        block.append(Block(1500, 200))
        block.append(Block(1550, 200))
        block.append(Block(2500, 200))
        block.append(Block(2550, 200))
        block.append(Block(2600, 200))
        block.append(Block(3550, 200))
        block.append(Block(3600, 200))
        block.append(Block(3650, 350))
        block.append(Block(3700, 200))
        block.append(Block(3750, 200))
        block.append(Block(4200, 200))
        block.append(Block(4250, 200))
        block.append(Block(4300, 200))
        block.append(Block(4800, 200))
        block.append(Block(4850, 200))
        block.append(Block(4900, 200))
        block.append(Block(5200, 200))
        block.append(Block(5250, 200))
        block.append(Block(5300, 200))

        coin = []

        coin.append(Coin(950, 200))
        coin.append(Coin(975, 225))
        coin.append(Coin(1000, 250))
        coin.append(Coin(1025, 225))
        coin.append(Coin(1050, 200))
        coin.append(Coin(2000, 200))
        coin.append(Coin(2025, 200))
        coin.append(Coin(2050, 200))
        coin.append(Coin(2075, 200))
        coin.append(Coin(2100, 200))
        coin.append(Coin(3050, 200))
        coin.append(Coin(3075, 200))
        coin.append(Coin(3100, 200))
        coin.append(Coin(3125, 200))
        coin.append(Coin(3150, 200))
        coin.append(Coin(3075, 250))
        coin.append(Coin(3100, 250))
        coin.append(Coin(3125, 250))
        coin.append(Coin(3100, 300))
        coin.append(Coin(4000, 200))
        coin.append(Coin(4025, 200))
        coin.append(Coin(4050, 200))
        coin.append(Coin(4075, 200))
        coin.append(Coin(4100, 200))
        coin.append(Coin(5000, 250))
        coin.append(Coin(5025, 250))
        coin.append(Coin(5050, 250))
        coin.append(Coin(5075, 250))
        coin.append(Coin(5100, 250))

        monster1 = []

        monster1.append(Monster1(600, 90))
        monster1.append(Monster1(800, 90))
        monster1.append(Monster1(1500, 90))
        monster1.append(Monster1(1750, 90))
        monster1.append(Monster1(2250, 90))
        monster1.append(Monster1(2500, 90))

        monster2 = []

        monster2.append(Monster2(1000, 94))
        monster2.append(Monster2(2000, 94))
        monster2.append(Monster2(3000, 94))
        monster2.append(Monster2(3250, 94))
        monster2.append(Monster2(4000, 94))
        monster2.append(Monster2(4750, 94))
        monster2.append(Monster2(5000, 94))

        mushroom1 = []

        mushroom1.append(Mushroom1(550,195))

        mushroom2 = []

        mushroom2.append(Mushroom2(1500,195))

        flower = []

        flower.append(Flower(2550,195))

        star = []

        star.append(Star(3650,350))

        flag = []

        flag.append(Flag(5800,254))
        
    elif stage==2:
        
        block = []
        block.append(Block(700, 200))
        block.append(Block(750, 200))
        block.append(Block(800, 200))
        block.append(Block(850, 200))
        block.append(Block(900, 200))
        block.append(Block(900, 150))
        block.append(Block(900, 100))
        
        block.append(Block(1700, 200))
        block.append(Block(1750, 200))
        block.append(Block(1800, 350))

        block.append(Block(2500, 200))
        block.append(Block(2450, 250))
        block.append(Block(2400, 300))
        block.append(Block(2550, 250))
        block.append(Block(2600, 300))
        block.append(Block(2450, 350))
        block.append(Block(2550, 350))
        block.append(Block(2500, 300))

        block.append(Block(3000, 200))
        block.append(Block(2950, 250))
        block.append(Block(2900, 300))
        block.append(Block(3050, 250))
        block.append(Block(3100, 300))
        block.append(Block(2950, 350))
        block.append(Block(3050, 350))
        block.append(Block(3000, 300))


        block.append(Block(3700, 200))
        block.append(Block(3750, 200))
        block.append(Block(3800, 200))
        block.append(Block(3850, 200))
        block.append(Block(3900, 200))
        block.append(Block(3950, 200))
        block.append(Block(4000, 200))
        block.append(Block(4050, 200))

        block.append(Block(4150, 300))
        block.append(Block(4200, 300))
        block.append(Block(4250, 300))
        block.append(Block(4300, 300))
        block.append(Block(4350, 300))
        block.append(Block(4400, 300))
        block.append(Block(4450, 300))
        block.append(Block(4500, 300))

        block.append(Block(4600, 400))
        block.append(Block(4650, 400))
        block.append(Block(4700, 400))
        block.append(Block(4750, 400))
        block.append(Block(4800, 400))
        
        block.append(Block(5400, 200))
        block.append(Block(5500, 300))
        block.append(Block(5600, 350))
        block.append(Block(5700, 450))
        block.append(Block(5700, 400))
        block.append(Block(5700, 350))
        block.append(Block(5700, 300))
        block.append(Block(5700, 250))
        block.append(Block(5700, 200))
        block.append(Block(5700, 150))
        block.append(Block(5700, 100))

        coin = []

        coin.append(Coin(1100, 200))
        coin.append(Coin(1150, 200))
        coin.append(Coin(1200, 200))
        coin.append(Coin(1250, 200))
        coin.append(Coin(1300, 200))

        coin.append(Coin(2100, 200))
        coin.append(Coin(2100, 250))
        coin.append(Coin(2150, 200)) 
        coin.append(Coin(2150, 250))
        coin.append(Coin(2200, 200))
        coin.append(Coin(2200, 250))
        
        coin.append(Coin(5200, 200))
        coin.append(Coin(5150, 250))
        coin.append(Coin(5100, 300))
        coin.append(Coin(5250, 250))
        coin.append(Coin(5300, 300))
        coin.append(Coin(5150, 350))
        coin.append(Coin(5250, 350))
        coin.append(Coin(5200, 300))

        monster1 = []

        monster1.append(Monster1(650, 90))
        monster1.append(Monster1(2000, 90))
        monster1.append(Monster1(2700, 90))
        monster1.append(Monster1(3300, 90))
        monster1.append(Monster1(4000, 90))
        
        monster2 = []

        monster2.append(Monster2(1000, 94))
        monster2.append(Monster2(1200, 94))
        monster2.append(Monster2(4500, 94))
        monster2.append(Monster2(5000, 94))

        mushroom1 = []

        mushroom1.append(Mushroom1(1800,345))

        mushroom2 = []

        mushroom2.append(Mushroom2(3800,195))

        flower = []

        flower.append(Flower(5400,195))

        star = []
        
        flag = []

        flag.append(Flag(5800,254))


    elif stage == 3:
        
        block = []
        block.append(Block(600, 200))
        block.append(Block(650, 200))
        block.append(Block(700, 200))
        block.append(Block(750, 200))

        block.append(Block(850, 300))
        block.append(Block(900, 300))
        block.append(Block(950, 300))
        block.append(Block(1000, 300))

        block.append(Block(1100, 200))
        block.append(Block(1150, 200))
        block.append(Block(1200, 200))
        block.append(Block(1250, 200))


        block.append(Block(1900, 100))
        block.append(Block(1900, 150))
        block.append(Block(1900, 200))

        block.append(Block(2500, 100))
        block.append(Block(2500, 150))
        block.append(Block(2500, 200))

        block.append(Block(3500, 200))
        block.append(Block(3550, 200))
        block.append(Block(3600, 200))

        block.append(Block(4100, 200))
        block.append(Block(4150, 200))
        block.append(Block(4200, 200))
        block.append(Block(4250, 200))
        block.append(Block(4300, 200))

        block.append(Block(4400, 300))
        block.append(Block(4450, 300))
        block.append(Block(4500, 300))
        block.append(Block(4550, 300))
        block.append(Block(4600, 300))

        block.append(Block(4700, 400))
        block.append(Block(4750, 400))
        block.append(Block(4800, 400))
        block.append(Block(4850, 400))
        block.append(Block(4900, 400))

        block.append(Block(5100, 200))
        block.append(Block(5150, 300))
        block.append(Block(5200, 200))
        
        

        coin = []

        coin.append(Coin(850, 200))
        coin.append(Coin(900, 200))
        coin.append(Coin(950, 200))
        coin.append(Coin(1000, 200))

        coin.append(Coin(1400, 250))
        coin.append(Coin(1450, 250))
        coin.append(Coin(1500, 250))
        coin.append(Coin(1600, 250))

        coin.append(Coin(4700, 400))
        coin.append(Coin(4750, 400))
        coin.append(Coin(4800, 400))
        coin.append(Coin(4850, 400))
        coin.append(Coin(4900, 400))

        coin.append(Coin(5150, 200))

        monster1 = []

        monster1.append(Monster1(900, 90))
        monster1.append(Monster1(1600, 90))
        monster1.append(Monster1(2200, 90))

        monster2 = []

        monster2.append(Monster2(4200, 94))
        monster2.append(Monster2(4300, 94))
        monster2.append(Monster2(4400, 94))
        monster2.append(Monster2(4500, 94))
        monster2.append(Monster2(4600, 94))
        monster2.append(Monster2(4700, 94))

        mushroom1 = []

        mushroom1.append(Mushroom1(600,195))

        mushroom2 = []

        mushroom2.append(Mushroom2(3550,195))

        flower = []

        flower.append(Flower(5150,295))

        star = []

        star.append(Star(4100,195))

        
        flag = []

        flag.append(Flag(5800,254))
        
        
    elif stage == 4:
        
        block = []
        block.append(Block(600, 200))
        block.append(Block(700, 250))
        block.append(Block(800, 200))
        block.append(Block(900, 250))
        block.append(Block(1000, 200))
        block.append(Block(1100, 250))
        block.append(Block(1200, 200))

        block.append(Block(1300, 300))
        block.append(Block(1350, 300))
        block.append(Block(1400, 300))
        block.append(Block(1450, 300))
        block.append(Block(1500, 300))
        block.append(Block(1550, 300))
        block.append(Block(1600, 300))
        block.append(Block(1650, 300))
        block.append(Block(1700, 300))
        block.append(Block(1750, 300))

        block.append(Block(1850, 400))
        block.append(Block(1900, 400))
        block.append(Block(1950, 400))
        block.append(Block(2000, 400))
        block.append(Block(2050, 400))
        block.append(Block(2100, 400))
        block.append(Block(2150, 400))
        block.append(Block(2200, 400))
        block.append(Block(2250, 400))
        block.append(Block(2300, 400))

        block.append(Block(2400, 200))
        block.append(Block(2450, 200))
        block.append(Block(2500, 200))
        block.append(Block(2500, 200))
        block.append(Block(2600, 200))
        block.append(Block(2650, 200))
        block.append(Block(2800, 200))

        block.append(Block(3200, 200))
        block.append(Block(3200, 150))
        block.append(Block(3200, 100))

        block.append(Block(3800, 200))
        block.append(Block(3800, 150))
        block.append(Block(3800, 100))

        block.append(Block(4100, 200))
        block.append(Block(4150, 200))
        block.append(Block(4200, 200))

        block.append(Block(4600, 200))
        block.append(Block(4650, 250))
        block.append(Block(4700, 300))

        block.append(Block(5200, 200))
        block.append(Block(5250, 300))
        block.append(Block(5300, 200))
        

        coin = []

        coin.append(Coin(600, 250))
        coin.append(Coin(700, 300))
        coin.append(Coin(800, 250))
        coin.append(Coin(900, 300))
        coin.append(Coin(1000, 250))
        coin.append(Coin(1100, 300))
        coin.append(Coin(1200, 250))
        
        coin.append(Coin(1850, 400))
        coin.append(Coin(1900, 400))
        coin.append(Coin(1950, 400))
        coin.append(Coin(2000, 400))
        coin.append(Coin(2050, 400))
        coin.append(Coin(2100, 400))
        coin.append(Coin(2150, 400))
        coin.append(Coin(2200, 400))
        coin.append(Coin(2250, 400))
        coin.append(Coin(2300, 400))

        coin.append(Coin(3400, 200))
        coin.append(Coin(3450, 200))
        coin.append(Coin(3500, 200))
        
        

        monster1 = []

        monster1.append(Monster1(700, 90))
        monster1.append(Monster1(900, 90))
        monster1.append(Monster1(1100, 90))
        monster1.append(Monster1(1300, 90))
        monster1.append(Monster1(1400, 90))
        
        monster1.append(Monster1(4200, 90))
        monster1.append(Monster1(4400, 90))

        monster2 = []

        monster2.append(Monster2(800, 94))
        monster2.append(Monster2(1000, 94))
        monster2.append(Monster2(1200, 94))
        monster2.append(Monster2(1500, 94))
        monster2.append(Monster2(16500, 94))
        monster2.append(Monster2(1700, 94))
        monster2.append(Monster2(1750, 94))
        monster2.append(Monster2(1800, 94))
        monster2.append(Monster2(1850, 94))
        monster2.append(Monster2(1900, 94))
        monster2.append(Monster2(1950, 94))
        monster2.append(Monster2(2000, 94))

        monster2.append(Monster2(3500, 94))
        monster2.append(Monster2(3600, 94))

        mushroom1 = []

        mushroom1.append(Mushroom1(2800,195))

        mushroom2 = []

        mushroom2.append(Mushroom2(4650,245))

        flower = []

        flower.append(Flower(5250,295))

        star = []

        star.append(Star(600,195))


        
        flag = []

        flag.append(Flag(5800,254))

        
open_canvas(800, 600)

mario = Mario()
map = Map()
title = Title()
shop = Shop()
life = Life()
over = Over()
clear = Clear()
item = Item()

block = []

block.append(Block(500, 200))
block.append(Block(550, 200))
block.append(Block(600, 200))
block.append(Block(1500, 200))
block.append(Block(1550, 200))
block.append(Block(2500, 200))
block.append(Block(2550, 200))
block.append(Block(2600, 200))
block.append(Block(3550, 200))
block.append(Block(3600, 200))
block.append(Block(3650, 350))
block.append(Block(3700, 200))
block.append(Block(3750, 200))
block.append(Block(4200, 200))
block.append(Block(4250, 200))
block.append(Block(4300, 200))
block.append(Block(4800, 200))
block.append(Block(4850, 200))
block.append(Block(4900, 200))
block.append(Block(5200, 200))
block.append(Block(5250, 200))
block.append(Block(5300, 200))

coin = []

coin.append(Coin(950, 200))
coin.append(Coin(975, 225))
coin.append(Coin(1000, 250))
coin.append(Coin(1025, 225))
coin.append(Coin(1050, 200))
coin.append(Coin(2000, 200))
coin.append(Coin(2025, 200))
coin.append(Coin(2050, 200))
coin.append(Coin(2075, 200))
coin.append(Coin(2100, 200))
coin.append(Coin(3050, 200))
coin.append(Coin(3075, 200))
coin.append(Coin(3100, 200))
coin.append(Coin(3125, 200))
coin.append(Coin(3150, 200))
coin.append(Coin(3075, 250))
coin.append(Coin(3100, 250))
coin.append(Coin(3125, 250))
coin.append(Coin(3100, 300))
coin.append(Coin(4000, 200))
coin.append(Coin(4025, 200))
coin.append(Coin(4050, 200))
coin.append(Coin(4075, 200))
coin.append(Coin(4100, 200))
coin.append(Coin(5000, 250))
coin.append(Coin(5025, 250))
coin.append(Coin(5050, 250))
coin.append(Coin(5075, 250))
coin.append(Coin(5100, 250))

monster1 = []

monster1.append(Monster1(600, 90))
monster1.append(Monster1(800, 90))
monster1.append(Monster1(1500, 90))
monster1.append(Monster1(1750, 90))
monster1.append(Monster1(2250, 90))
monster1.append(Monster1(2500, 90))

monster2 = []

monster2.append(Monster2(1000, 94))
monster2.append(Monster2(2000, 94))
monster2.append(Monster2(3000, 94))
monster2.append(Monster2(3250, 94))
monster2.append(Monster2(4000, 94))
monster2.append(Monster2(4750, 94))
monster2.append(Monster2(5000, 94))

mushroom1 = []

mushroom1.append(Mushroom1(550,195))

mushroom2 = []

mushroom2.append(Mushroom2(1500,195))

flower = []

flower.append(Flower(2550,195))

star = []

star.append(Star(3650,350))

flag = []

flag.append(Flag(5800,254))

dir = 0
prev_dir = 1
stop = 1
title_count = 0
game_state=1

stage = 1

while stop:
    handle_events()
    clear_canvas()
    if title_count == 1:
        map.update_stage_count(stage)
        map.draw()
        mario.draw()
        for i in range(len(coin)):
            coin[i].draw()
        for i in range(len(monster1)):
            monster1[i].draw()
        for i in range(len(monster2)):
            monster2[i].draw()
        for i in range(len(mushroom1)):
            mushroom1[i].draw()
        for i in range(len(mushroom2)):
            mushroom2[i].draw()
        for i in range(len(flower)):
            flower[i].draw()
        for i in range(len(star)):
            star[i].draw()
        for i in range(len(block)):
           block[i].draw()    
        for i in range(len(flag)):
            flag[i].draw()
        life.draw()
        item.draw()
        if game_state == 1:
            map_left, map_bottom, map_right, map_top=map.map_xy()
            mario_x, mario_y=mario.mario_xy()
            mario.update()
            move_map()
            map.update_map(map_left, map_bottom, map_right, map_top)
            for i in range(len(coin)):
                coin[i].update_frame_block()
            for i in range(len(monster1)):
                monster1[i].update_frame_moster1()
            for i in range(len(monster2)):
                monster2[i].update_frame_moster2()
                
            mario.update_floor(100)
            for i in range(len(block)):
                if collide(mario,block[i]) > 0:
                    if collide(mario,block[i]) == 1:
                        break
                    elif collide(mario,block[i]) == 2:
                        mario.update_floor(block[i].y+50)
                        break
                    elif collide(mario,block[i]) == 3:
                        if mario.mario_return_move_y() > 0:
                            mario.mario_move_y(0)
                            block[i].change_block()
                            if stage == 1:
                                if i == 1:
                                    for i in range(len(mushroom1)):
                                        if mushroom1[i].x == block[1].x:
                                            mushroom1[i].mushroom1_turn()
                                elif i == 3:
                                    for i in range(len(mushroom2)):
                                        if mushroom2[i].x == block[3].x:
                                            mushroom2[i].mushroom2_turn()
                                elif i == 6:
                                    for i in range(len(flower)):
                                        if flower[i].x == block[6].x:
                                            flower[i].flower_turn()
                                elif i == 10:
                                    for i in range(len(star)):
                                        if star[i].x == block[10].x:
                                            star[i].star_turn()
                            elif stage == 2:
                                if i == 9:
                                    for i in range(len(mushroom1)):
                                        if mushroom1[i].x == block[9].x:
                                            mushroom1[i].mushroom1_turn()
                                elif i == 28:
                                    for i in range(len(mushroom2)):
                                        if mushroom2[i].x == block[28].x:
                                            mushroom2[i].mushroom2_turn()
                                elif i == 47:
                                    for i in range(len(flower)):
                                        if flower[i].x == block[47].x:
                                            flower[i].flower_turn()
                            elif stage == 3:
                                if i == 0:
                                    for i in range(len(mushroom1)):
                                        if mushroom1[i].x == block[0].x:
                                            mushroom1[i].mushroom1_turn()
                                elif i == 19:
                                    for i in range(len(mushroom2)):
                                        if mushroom2[i].x == block[19].x:
                                            mushroom2[i].mushroom2_turn()
                                elif i == 37:
                                    for i in range(len(flower)):
                                        if flower[i].x == block[37].x:
                                            flower[i].flower_turn()
                                elif i == 21:
                                    for i in range(len(star)):
                                        if star[i].x == block[21].x:
                                            star[i].star_turn()
                            elif stage == 4:
                                if i == 33:
                                    for i in range(len(mushroom1)):
                                        if mushroom1[i].x == block[33].x:
                                            mushroom1[i].mushroom1_turn()
                                elif i == 44:
                                    for i in range(len(mushroom2)):
                                        if mushroom2[i].x == block[44].x:
                                            mushroom2[i].mushroom2_turn()
                                elif i == 47:
                                    for i in range(len(flower)):
                                        if flower[i].x == block[47].x:
                                            flower[i].flower_turn()
                                elif i == 0:
                                    for i in range(len(star)):
                                        if star[i].x == block[0].x:
                                            star[i].star_turn()
                            break
                    elif collide(mario,block[i]) == 4:
                        mario.input_xy(block[i].x+50,0)
                        break
                    elif collide(mario,block[i]) == 5:
                        mario.input_xy(block[i].x-50,0)
                        break
            for i in range(len(coin)):
                if collide(mario,coin[i]) > 0:
                    if collide(mario,coin[i]) == 1 or collide(mario,coin[i]) == 2:
                        del coin[i]
                        life.more_coin()
                        break
            for i in range(len(monster1)):
                if monster1[i].monster1_state() < 0:
                    del monster1[i]
                    break
                if collide(mario,monster1[i]) > 0:
                    if collide(mario,monster1[i]) == 1:
                        if mario.mario_state_return() == 0:
                            mario.less_size()
                        elif mario.mario_state_return() == 1 and mario.mario_stance_timer() == 0:
                            game_state=0
                        elif mario.mario_state_return() == 2:
                            monster1[i].change_monster1()
                            mario.mario_0_state()
                        elif mario.mario_state_return() == 3:
                            monster1[i].change_monster1()
                        break
                    elif collide(mario,monster1[i]) == 2:
                        monster1[i].change_monster1()
                        mario.mario_move_y(10)
                        break
            for i in range(len(monster2)):
                if collide(mario,monster2[i]) > 0:
                    if collide(mario,monster2[i]) == 1:
                        if mario.mario_state_return() == 0:
                            mario.less_size()
                        elif mario.mario_state_return() == 1 and mario.mario_stance_timer() == 0:
                            game_state=0
                        elif mario.mario_state_return() == 2 and monster2[i].monster2_state() != 2:
                            monster2[i].change_monster2()
                            mario.mario_0_state()
                        elif mario.mario_state_return() == 2 and monster2[i].monster2_state() == 2:
                            mario.mario_0_state()
                            del monster2[i]
                        elif mario.mario_state_return() == 3:
                            del monster2[i]
                        break
                    elif collide(mario,monster2[i]) == 2:
                        mario.mario_move_y(10)
                        if monster2[i].monster2_state() == 2:
                            del monster2[i]
                            break
                        monster2[i].change_monster2()
                        break
            for i in range(len(mushroom1)):
                if collide(mario,mushroom1[i]) > 0:
                    if collide(mario,mushroom1[i]) == 1 or collide(mario,mushroom1[i]) == 2:
                        mario.more_size()
                        del mushroom1[i]
                        break
            for i in range(len(mushroom2)):
                if collide(mario,mushroom2[i]) > 0:
                    if collide(mario,mushroom2[i]) == 1 or collide(mario,mushroom2[i]) == 2:
                        life.more_life()
                        del mushroom2[i]
                        break
            for i in range(len(flower)):
                if collide(mario,flower[i]) > 0:
                    if collide(mario,flower[i]) == 1 or collide(mario,flower[i]) == 2:
                        mario.more_size()
                        mario.mario_flower_state()
                        del flower[i]
                        break
            for i in range(len(star)):
                if collide(mario,star[i]) > 0:
                    if collide(mario,star[i]) == 1 or collide(mario,star[i]) == 2:
                        mario.mario_star_state()
                        del star[i]
                        break
            for i in range(len(flag)):
                if collide(mario,flag[i]) > 0:
                    if collide(mario,flag[i]) == 1 or collide(mario,flag[i]) == 2:
                        game_state=2
                        break
        elif game_state == 0:
            over.draw()
        elif game_state == 2:
            clear.draw()
    elif title_count == 0:
        title.draw()
    elif title_count == 2:
        shop.draw()
        life.draw()
        item.draw()
    update_canvas()
    delay(0.01)
