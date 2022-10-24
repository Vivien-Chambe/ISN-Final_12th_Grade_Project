import pygame
import random as r
import classes as c
import sprites as s

def create_level(nb_platform,platform_width,platform_height,space,width,height):
    platform_list = c.Platform_List(height,width,platform_height)
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
        platform_list.list.append(c.Platform(plat_x,plat_y,platform_width,platform_height,"Black"))
        platform_list.len +=1
        
    platform_list.flag.body.x = (platform_list.list[0].body.left)+(platform_width/2)
    platform_list.flag.body.bottom = platform_list.list[0].body.top
    return platform_list

def update_level(screen,platform_list,perso,random_background,width,height):
    screen.blit(random_background,(0,0))
    platform_list.draw_level(screen,width,height)
    perso.draw(screen)
    

def give_rect_for_collision(platform_list):
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