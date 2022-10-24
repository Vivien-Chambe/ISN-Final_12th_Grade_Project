from turtle import left
from unicodedata import name
import pygame,os,sys
from sys import exit
import random as r
from sprites import *
from classes import *
from fonctions import *

pygame.init()

width = 500
height = 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ISN")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
fill_surface = pygame.Surface((200,50))


backs = [back1,back3,back4]
random_background = r.choice(backs)
platform_width = 50
platform_height = 20
nb_platform = 7
space = (height - platform_height - nb_platform*platform_height)/nb_platform
max_height = 180

platform_list = create_level(nb_platform,platform_width,platform_height,space,width,height)
random_background = r.choice(backs)
collisions_list = give_rect_for_collision(platform_list)
perso = Character(width/2,height-platform_height-50,30,50)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                platform_list.restart()
                random_background = r.choice(backs)
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
    update_level(screen,platform_list,perso,random_background,width,height)
    pygame.display.update()
    clock.tick(300)
