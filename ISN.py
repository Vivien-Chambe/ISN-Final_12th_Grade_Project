from turtle import left
from unicodedata import name
import pygame,os,sys
from sys import exit
import random as r
from sprites import *
from classes import *

pygame.init()

width = 500
height = 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ISN")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
fill_surface = pygame.Surface((200,50))


backs = [back1,back3,back4]


platform_width = 50
platform_height = 20
nb_platform = 7
space = (height - platform_height - nb_platform*platform_height)/nb_platform
max_height = 180



def create_level():
    platform_list = Platform_List()
    for i in range (nb_platform):
        plat_x = r.randint(0,width-platform_width)
        if i>0:
            gap = 0
            while gap > 250 or gap < 2*platform_width :
                plat_x = r.randint(0,width-platform_width)
                if plat_x < platform_list.list[i-1].body.x:
                    gap =  platform_list.list[i-1].body.left - plat_x + platform_width
                elif plat_x > platform_list.list[i-1].body.right:
                    gap = plat_x - platform_list.list[i-1].body.left
        plat_y = (platform_list.sol.body.x)+(i+1)*space+platform_height
        platform_list.list.append(Platform(plat_x,plat_y,platform_width,platform_height,"Black"))
        platform_list.len +=1
        
    platform_list.flag.body.x = (platform_list.list[0].body.left)+(platform_width/2)
    platform_list.flag.body.bottom = platform_list.list[0].body.top
    return platform_list

def update_level():
    screen.blit(random_background,(0,0))
    platform_list.draw_level()
    perso.draw()
    

def give_rect_for_collision():
    collision_list = []
    for p in platform_list.list:
        collision_list.append(p.body)
    return collision_list

def check_collisions(perso,platform,platform_list): #Explanations in the README.md
    perso.body.clamp_ip(pygame.display.get_surface().get_rect()) #Keep Character within the windows

    #Right collision of character
    if (perso.body.right == platform.left and ((perso.body.top<=platform.top and perso.body.bottom>= platform.bottom) or (perso.body.top<=platform.top and perso.body.bottom>=platform.top) or (perso.body.top<=platform.bottom and perso.body.bottom>=platform.bottom))):# or perso.right >= width:
        perso.body.right -=1
    #Left collision 
    elif (perso.body.left == platform.right and ((perso.body.top<=platform.top and perso.body.bottom>= platform.bottom) or (perso.body.top<=platform.top and perso.body.bottom>=platform.top) or (perso.body.top<=platform.bottom and perso.body.bottom>=platform.bottom))):# or perso.left <= 0:
        perso.body.left +=1
    #Bottom collision (with ground too)
    elif (perso.body.bottom == platform.top and ((perso.body.left<=platform.left and perso.body.right >= platform.left) or (perso.body.left>=platform.left and perso.body.right<=platform.right) or (perso.body.left<=platform.right and perso.body.right>=platform.right))) or perso.body.bottom == platform_list.sol.body.top:
        perso.body.bottom -=1
        perso.falling = False
        perso.jump_height = 0
        perso.can_jump = True
    #Top collision
    elif (perso.body.top == platform.bottom and ((perso.body.left<=platform.left and perso.body.right >= platform.left) or (perso.body.left>=platform.left and perso.body.right<=platform.right) or (perso.body.left<=platform.right and perso.body.right>=platform.right))):# or perso.top <= 0:
        perso.body.top +=1
    
    elif pygame.Rect.colliderect(perso.body,platform_list.flag.body):
        print("Victory")
        platform_list.restart()
        perso.reset_position()


platform_list = create_level()
random_background = r.choice(backs)
collisions_list = give_rect_for_collision()
perso = Character(width/2,height-platform_height-50,30,50)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                platform_list.restart()
                perso.reset_position()

    
    for p in collisions_list:    
        check_collisions(perso,p,platform_list)

    ############################# Character Movement #########################
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        perso.body.x -= 1
        perso.update_frame()
        perso.direction = "left"
    if keys[pygame.K_d]:
        perso.body.x += 1
        perso.update_frame()
        perso.direction = "right"

    if keys[pygame.K_SPACE] and (not perso.falling) and perso.can_jump:
        perso.body.bottom -= 1
        perso.jump_height += 1
        if perso.jump_height >= max_height: 
            perso.falling = True
            perso.can_jump = False
    else:
        perso.body.bottom += 1

    ############################ Update screen ###################################
    update_level()
    pygame.display.update()
    clock.tick(300)
