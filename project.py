from pico2d import *
from character import *
from background import *

def handle_events():
    global dir
    global prev_dir
    global jump
    global stop
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key ==SDLK_RIGHT:
                prev_dir=dir
                dir +=1
                check_dir()
            elif event.key ==SDLK_LEFT:
                prev_dir=dir
                dir -=1
                check_dir()
            elif event.key ==SDLK_UP:
                if dir==1:
                    mario.right_jump()
                elif dir==-1:
                    mario.left_jump()
            #elif event.key==SDLK_DOWN:
            #    stop=0
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
    global map_left,map_bottom,map_right,map_top
    global mario_x,mario_y
    global dir
    if mario_x>653 and 1250<=2500-map_right and dir==1:
        map_right+=650-mario_x
        print(mario_x,map_right)
        mario.input_xy(mario_x,mario_y)
    elif mario_x<245 and 0<1250-map_right and dir==-1:
        map_right+= 250-mario_x
        if map_right>1250:
            map_right=1250
        print(mario_x,map_right)
        mario.input_xy(mario_x,mario_y)
      
    #print(mario_x,map_right)
open_canvas(800,600)

mario=Mario()
map=Map()

dir = 0
prev_dir=0
stop=1

while stop:
    handle_events()
    clear_canvas()
    map.draw()
    mario.draw()
    map_left,map_bottom,map_right,map_top=map.map_xy()
    mario_x,mario_y=mario.mario_xy()
    mario.update()
    move_map()
    map.update_map(map_left,map_bottom,map_right,map_top)
    update_canvas()
    delay(0.01)
