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
                for i in range(len(block)):
                    block[i].change_block()
                for i in range(len(monster1)):
                    monster1[i].change_monster1()
                for i in range(len(monster2)):
                    monster2[i].change_monster2()
            elif event.key == SDLK_SPACE:
                title_count = 1
            elif event.key == SDLK_p:
                if title_count == 1:
                    title_count = 2
                elif title_count == 2:
                    title_count = 1
            elif event.key==SDLK_ESCAPE:
                    stop=0
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
    
    return 1

open_canvas(800, 600)

mario = Mario()
map = Map()
title = Title()
shop = Shop()

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
block.append(Block(3600, 250))
block.append(Block(3650, 300))
block.append(Block(3700, 250))
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

mushroom1.append(Mushroom1(550,240))

mushroom2 = []

mushroom2.append(Mushroom2(1500,240))

flower = []

flower.append(Flower(2550,240))

star = []

star.append(Star(3650,340))

flag = []

flag.append(Flag(5800,254))

dir = 0
prev_dir = 1
stop = 1
title_count = 0

while stop:
    handle_events()
    clear_canvas()
    if title_count == 1:
        map.draw()
        mario.draw()
        for i in range(len(block)):
           block[i].draw()
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
        for i in range(len(flag)):
            flag[i].draw()
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
            

        for i in range(len(block)):
            if collide(mario,block[i]) > 0:
                if collide(mario,block[i]) == 1:
                    pass
                elif collide(mario,block[i]) == 2:
                    pass
        for i in range(len(coin)):
            if collide(mario,coin[i]) > 0:
                if collide(mario,coin[i]) == 1:
                    pass
                elif collide(mario,coin[i]) == 2:
                    pass
        for i in range(len(monster1)):
            if collide(mario,monster1[i]) > 0:
                if collide(mario,monster1[i]) == 1:
                    mario.less_size()
                    pass
                elif collide(mario,monster1[i]) == 2:
                    monster1[i].change_monster1()
                    pass
        for i in range(len(monster2)):
            if collide(mario,monster2[i]) > 0:
                if collide(mario,monster2[i]) == 1:
                    mario.less_size()
                    pass
                elif collide(mario,monster2[i]) == 2:
                    monster2[i].change_monster2()
                    pass
        for i in range(len(mushroom1)):
            if collide(mario,mushroom1[i]) > 0:
                if collide(mario,mushroom1[i]) == 1:
                    mario.more_size()
                    pass
                elif collide(mario,mushroom1[i]) == 2:
                    mario.more_size()
                    pass
        for i in range(len(mushroom2)):
            if collide(mario,mushroom2[i]) > 0:
                if collide(mario,mushroom2[i]) == 1:
                    pass
                elif collide(mario,mushroom2[i]) == 2:
                    pass
        for i in range(len(flower)):
            if collide(mario,flower[i]) > 0:
                if collide(mario,flower[i]) == 1:
                    pass
                elif collide(mario,flower[i]) == 2:
                    pass
        for i in range(len(star)):
            if collide(mario,star[i]) > 0:
                if collide(mario,star[i]) == 1:
                    pass
                elif collide(mario,star[i]) == 2:
                    pass
        for i in range(len(flag)):
            if collide(mario,flag[i]) > 0:
                if collide(mario,flag[i]) == 1:
                    pass
                elif collide(mario,flag[i]) == 2:
                    pass
                
    elif title_count == 0:
        title.draw()
    elif title_count == 2:
        shop.draw()
    update_canvas()
    delay(0.01)
