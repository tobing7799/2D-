from pico2d import *


class Mario():
    def __init__(self):
        self.image = load_image('mario-side.png')
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
        
    def draw(self):
        if self.x < 20:
            self.x = 20
        if self.x > 780:
            self.x = 780
        draw_rectangle(*self.get_bb())
        if self.timer > 0:
            self.timer-=100
            if self.timer%1000 != 0 and self.timer%500 != 0:
                self.image.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
        elif self.timer == 0:
            self.image.clip_draw(self.frame * self.frame_size_x+self.frame_empty_x, self.frame_y, self.size_x, self.size_y, self.x, self.y,self.mario_size_x,self.mario_size_y)
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
                        self.move_y=0
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
        if self.jump==True:
            if self.frame_control_jump<3:
                self.move_y-=0.8
            elif self.frame_control_jump<4:
                 self.move_y-=0.8
            elif self.frame_control_jump==4:
                self.move_y=0
           
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
            self.move_y=0
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
            self.move_y=0
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
            self.move_y=0
            self.frame=0
            self.frame_y=2465
            self.frame_empty_x=16
            self.frame_size_x=27
            self.size_x=29
            self.size_y=40
        elif self.after_jump==4:
            self.move_y=0
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
        if self.mario_size_x !=22:
            self.mario_size_x=22
            self.y-=15
            self.mario_size_y=30
            self.timer=20000
        
    def more_size(self):
        if self.mario_size_x !=44:
            self.mario_size_x=44
            self.y+=15
            self.mario_size_y=60






    
