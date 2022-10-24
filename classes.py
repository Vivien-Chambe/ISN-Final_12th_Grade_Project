import pygame 
from sprites import *
from ISN import width,height,platform_height

class Character:
    def __init__(self,x,y,w,h):
        self.body = pygame.Rect(x,y,w,h)
        self.jump_height = 0
        self.falling = False
        self.can_jump = True
        self.direction = "right"
        self.frame = 0
        self.sprite = 1

    def draw(self,screen):
        if self.direction == "right":
            if self.sprite == 1: screen.blit(perso_sprite_right_1,self.body)
            elif self.sprite == 2 : screen.blit(perso_sprite_right_2,self.body)
        elif self.direction == "left":
            if self.sprite == 1: screen.blit(perso_sprite_left_1,self.body)
            elif self.sprite == 2 : screen.blit(perso_sprite_left_2,self.body)
        
    def update_frame(self):
        self.frame += 1
        if self.frame >= 0 and self.frame <50: self.sprite = 1
        elif self.frame >= 50 and self.frame <100: self.sprite =2
        elif self.frame >= 100 :self.frame =0
        else: print("Not a valid frame")

    def reset_position(self):
        self.body.x = width/2
        self.body.y = height-platform_height-50


class Platform:
    def __init__(self,x,y,w,h,color):
        self.body = pygame.Rect(x,y,w,h)
        self.color = color
    def draw(self,screen):
        if self.body.width == width:
            screen.blit(sol_sprite,self.body)
        else:
            screen.blit(platforme_sprite,self.body)

class Platform_List:
    def __init__(self):
        self.sol = Platform(0,height-platform_height,width,platform_height,"Black") 
        self.list = []
        self.len = 0
        self.flag = Platform(0,0,10,30,"Green")
    
    def draw_level(self,screen):
        self.sol.draw()
        for i in range(self.len):
            self.list[i].draw()
        screen.blit(flag_sprite,self.flag.body)

    def restart(self):
        global random_background
        random_background = r.choice(backs)
        for i in range(self.len):
            new_x = r.randint(0,width-platform_width)
            if i>0:
                gap = 0
                while gap > 250 or gap < 2*platform_width : # I check if platforms are not too close from the previous one or too far away
                    new_x = r.randint(0,width-platform_width)
                    if new_x < self.list[i-1].body.x:
                        gap = self.list[i-1].body.left - new_x + platform_width
                    elif new_x > self.list[i-1].body.right:
                        gap = new_x - self.list[i-1].body.left
            
            self.list[i].body.x = new_x


        self.flag.body.x = (self.list[0].body.left)+(platform_width/2)
        self.flag.body.bottom = self.list[0].body.top