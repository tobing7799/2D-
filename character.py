from pico2d import *


class Mario():
    def __init__(self):
        self.image = load_image('mario-side.png')
        self.flowerimage = load_image('mario-side-flower.png')
        self.star1 = load_image('mario-side-star1.png')
        self.star2 = load_image('mario-side-star2.png')
        self.star3 = load_image('mario-side-star3.png')
        self.star4 = load_image('mario-side-star4.png')
        self.star5 = load_image('mario-side-star5.png')
        self.star6 = load_image('mario-side-star6.png')
        
        self.x,self.y=100,100 #시작 좌표
        self.frame=0 #프레임 조절
        self.frame_size_x=27 #프레임 가로 길이 조절
        self.frame_empty_x=16 #이미지 앞에 빈공간 없애주기
        self.size_x=29 #이미지 가로 사이즈
        self.size_y=40 #이미지 세로 사이즈
        self.frame_y=2465 #이미지 세로 위치 조절
        #캐릭터의 움직임 속도
        self.move_x=0
        self.move_y=0
        # delay와 속도 조절
        self.frame_control=0
        self.frame_control_jump=0
        #현재 캐릭터의 움직임 속도
        self.speed=0
        self.dir=0
        #캐릭터 움직임
        self.jump=False
        self.after_jump=0
        self.run=0.05
        self.run_count=0
        #캐릭터 크기
        self.mario_size_x=44
        self.mario_size_y=60
        #충돌 타이머
        self.timer=0
        #마리오의 현재 상태
        self.state = 0 #0은바닥 1은 블럭위
        self.floor = 100 #바닥 좌표
        self.power = 0 #0 기본 상태,1 미니 상태, 2 꽃 먹은 상태,3 별 상태
        self.star_timer=0
        
    def draw(self):
        if self.x < 20:
            self.x = 20
        if self.x > 780:
            self.x = 780
        if self.timer > 0:
            self.timer-=100
            if self.timer%1000 != 0 and self.timer%500 != 0:
                self.image.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
        elif self.timer == 0:
            if self.power == 0 or self.power == 1:
                self.image.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
            elif self.power == 2:
                self.flowerimage.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
            elif self.power == 3:
                if self.star_timer > 0:
                    self.star_timer-=200
                    if self.star_timer%60000 < 10000:
                        self.star1.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
                    elif self.star_timer%50000 < 10000:
                        self.star2.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
                    elif self.star_timer%40000 < 10000:
                        self.star3.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
                    elif self.star_timer%30000 < 10000:
                        self.star4.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
                    elif self.star_timer%20000 < 10000:
                        self.star5.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
                    elif self.star_timer%10000 < 10000:
                        self.star6.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
                elif self.star_timer <= 0:
                    self.power = 0
                
    def update(self):
        if self.frame_control==10:
            if self.dir==0:
                if self.jump == True:
                    self.frame_control_jump+=1
                    if self.frame_control_jump<2:
                        self.frame = 0
                    elif self.frame_control_jump<3:
                        self.frame = 1
                    elif self.frame_control_jump<4:
                        self.frame = 2
                    elif self.frame_control_jump<7:
                        self.frame = (self.frame+1)%6
                        #self.move_y=0
                    if self.frame_control_jump==7:
                        self.frame_control_jump=0
                        self.jump = False
                        self.after()
                elif self.jump == False:
                    self.frame = (self.frame+1) % 6
            elif self.dir==1:
                self.frame = (self.frame-1) % 6
            self.frame_control=0
            
        self.frame_control+=1
        
        self.x += self.move_x*2
        self.y += self.move_y
       # if self.jump==True:
       #     if self.frame_control_jump<3:
       #         self.move_y-=0.8
       #     elif self.frame_control_jump<4:
       #          self.move_y-=0.8
       #     elif self.frame_control_jump==4:
       #         self.move_y=0
       # elif self.jump=False:
       
      #  if self.state == 0: 
       #    if self.mario_size_y == 30:
       #        if self.y <= 85:
       #            self.y=85
       #            self.move_y=0
       #        elif self.y > 85:
       #             self.move_y-=0.8
       #    elif self.mario_size_y == 60:
       #         if self.y <= 100:
       #             self.y=100
       #             self.move_y=0
       #         elif self.y > 100:
       #             self.move_y-=0.8
        if self.mario_size_y == 30:
            if self.y < self.floor-15:
                self.y = self.floor-15
                self.move_y = 0
            elif self.y > self.floor-15:
                    self.move_y-=0.8           
        elif self.mario_size_y == 60:
            if self.y < self.floor:
                self.y = self.floor
                self.move_y=0
            elif self.y > self.floor:
                self.move_y-=0.8
            


                    
        if self.move_x >=0.5 and self.move_x<=3:
            self.move_x+=self.run
        elif self.move_x<=-0.5 and self.move_x>=-3:
            self.move_x-=self.run
                
    def right(self):
        self.speed=0.5
        self.move_x+=self.speed
        self.after_jump=1
        if self.jump==True:
            self.frame_size_x=31
            self.frame_empty_x=14
            self.size_x=31
            self.size_y=43
            self.frame_y=2401
        if self.jump == False:
            self.frame=0
            self.frame_size_x=34
            self.frame_empty_x=10
            self.size_x=34
            self.size_y=40
            self.frame_y=2340
            
    def left(self):
        self.speed=0.5
        self.move_x-=self.speed
        self.after_jump=2
        if self.jump==True:
            self.frame_size_x= -31
            self.frame_empty_x=1059
            self.size_x=31
            self.size_y=43
            self.frame_y=2401
        if self.jump == False:
            self.frame=0
            self.frame_size_x= -34
            self.frame_empty_x=1060
            self.size_x=34
            self.size_y=40
            self.frame_y=2340
        
    def stop_right(self):
        self.speed=0
        self.move_x=0
        self.after_jump=3
        if self.jump == False:
            #self.move_y=0
            self.frame=0
            self.frame_y=2465
            self.frame_empty_x=16
            self.frame_size_x=27
            self.size_x=29
            self.size_y=40

    def stop_left(self):
        self.speed=0
        self.move_x=0
        self.after_jump=4
        if self.jump == False:
            #self.move_y=0
            self.frame=0
            self.frame_y=2465
            self.frame_empty_x=1059
            self.frame_size_x=-27
            self.size_x=29
            self.size_y=40

    def left_jump(self):
        if self.jump == False:
            self.frame_control=-1
            self.move_y=16
            self.frame=0
            self.frame_size_x= -31
            self.frame_empty_x=1059
            self.size_x=31
            self.size_y=43
            self.frame_y=2401
            self.jump=True
    
    def right_jump(self):
        if self.jump == False:
            self.frame_control=-1
            self.move_y=16
            self.frame=0
            self.frame_size_x=31
            self.frame_empty_x=14
            self.size_x=31
            self.size_y=43
            self.frame_y=2401
            self.jump=True
        
    def after(self):
        if self.after_jump==1:
            self.frame=0
            self.frame_size_x=34
            self.frame_empty_x=10
            self.size_x=34
            self.size_y=40
            self.frame_y=2340
        elif self.after_jump==2:
            self.frame=0
            self.frame_size_x= -34
            self.frame_empty_x=1060
            self.size_x=34
            self.size_y=40
            self.frame_y=2340
        elif self.after_jump==3:
            #self.move_y=0
            self.frame=0
            self.frame_y=2465
            self.frame_empty_x=16
            self.frame_size_x=27
            self.size_x=29
            self.size_y=40
        elif self.after_jump==4:
            #self.move_y=0
            self.frame=0
            self.frame_y=2465
            self.frame_empty_x=1059
            self.frame_size_x=-27
            self.size_x=29
            self.size_y=40
            
    def mario_xy(self):
        return self.x,self.y

    def input_xy(self,x,y):
        self.x=x
        
    def get_bb(self):
        return self.x-self.mario_size_x/2,self.y-self.mario_size_y/2,self.x+self.mario_size_x/2,self.y+self.mario_size_y/2

    def less_size(self):
        if self.timer > 0:
            return 0
        if self.power == 0:
            self.mario_size_x=22
            self.y-=15
            self.mario_size_y=30
            self.power = 1
        elif self.power == 1:
            pass
        elif self.power == 2:
            self.power = 1
        elif self.power == 3:
            self.power = 1
            
        self.timer=20000
        
    def more_size(self):
        if self.power == 1:
            self.mario_size_x=44
            self.y+=15
            self.mario_size_y=60
            self.power = 0

    def update_floor(self,y):
        self.floor = y

    def mario_return_move_y(self):
        return self.move_y

    def mario_move_y(self,y):
        self.move_y = y

    def mario_0_state(self):
        self.power = 0
        self.timer=20000

    def mario_flower_state(self):
        self.power = 2

    def mario_star_state(self):
        self.power = 3
        self.star_timer=70000

    def mario_state_return(self):
        return self.power

    def mario_stance_timer(self):
        return self.timer

    def mario_jump_state(self):
        return self.jump





    
