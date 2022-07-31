from unicodedata import name
import pygame
from sys import exit
import random as r

pygame.init()

width = 500
height = 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ISN")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

perso_image = pygame.Surface((50,50))
fill_surface = pygame.Surface((200,50))
fill_surface.fill("White")

platform_width = 50
platform_height = 20
nb_platform = 7
space = (height - platform_height - nb_platform*platform_height)/nb_platform

colors = list(pygame.colordict.THECOLORS.keys())
background_color = r.choice(colors)

print(pygame.colordict.THECOLORS.keys())


class Character:
    def __init__(self,x,y,w,h):
        self.body = pygame.Rect(x,y,w,h)

    def draw(self):
        pygame.draw.rect(screen,"Red",self.body)
    
    def reset_position(self):
        self.body.x = width/2
        self.body.y = height-platform_height-50


class Platform:
    def __init__(self,x,y,w,h):
        self.body = pygame.Rect(x,y,w,h)

    def draw(self):
        pygame.draw.rect(screen,"Black",self.body)

class Platform_List:
    def __init__(self):
        self.sol = Platform(0,height-platform_height,width,platform_height) 
        self.list = []
        self.len = 0
    
    def draw_level(self):
        self.sol.draw()
        for i in range(self.len):
            self.list[i].draw()

    def restart(self):
        global background_color
        background_color = r.choice(colors)
        for i in range(self.len):
            self.list[i].body.x = r.randint(0,width-platform_width)

def create_level():
    platform_list = Platform_List()
    for i in range (nb_platform):
        plat_x = r.randint(0,width-platform_width)
        plat_y = (platform_list.sol.body.x)+(i+1)*space+platform_height
        platform_list.list.append(Platform(plat_x,plat_y,platform_width,platform_height))
        platform_list.len +=1

    return platform_list

def update_level():
    screen.fill(background_color)
    platform_list.draw_level()
    perso.draw()

def give_rect_for_collision():
    collision_list = []
    for p in platform_list.list:
        collision_list.append(p.body)
    return collision_list

def check_collisions(perso,platform,platform_list): #Explanations in the README.md
    #Right collision of character
    if (perso.right == platform.left and ((perso.top<=platform.top and perso.bottom>= platform.bottom) or (perso.top<=platform.top and perso.bottom>=platform.top) or (perso.top<=platform.bottom and perso.bottom>=platform.bottom))) or perso.right >= width:
        perso.right -=1
    #Left collision 
    elif (perso.left == platform.right and ((perso.top<=platform.top and perso.bottom>= platform.bottom) or (perso.top<=platform.top and perso.bottom>=platform.top) or (perso.top<=platform.bottom and perso.bottom>=platform.bottom))) or perso.left <= 0:
        perso.left +=1
    #Bottom collision (with ground too)
    elif (perso.bottom == platform.top and ((perso.left<=platform.left and perso.right >= platform.left) or (perso.left>=platform.left and perso.right<=platform.right) or (perso.left<=platform.right and perso.right>=platform.right))) or perso.bottom == platform_list.sol.body.top:
        perso.bottom -=1
    #Top collision
    elif (perso.top == platform.bottom and ((perso.left<=platform.left and perso.right >= platform.left) or (perso.left>=platform.left and perso.right<=platform.right) or (perso.left<=platform.right and perso.right>=platform.right))) or perso.top <= 0:
        perso.top +=1

platform_list = create_level()
collisions_list = give_rect_for_collision()
perso = Character(width/2,height-platform_height-50,20,50)
perso.draw()

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
        check_collisions(perso.body,p,platform_list)
    ############################# Character Movement #########################
    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        perso.body.x -= 1
    if keys[pygame.K_RIGHT]:
        perso.body.x += 1

    if keys[pygame.K_SPACE]:
        perso.body.bottom -= 1
    else:
        perso.body.bottom += 1

    ############################ Update screen ###################################
    update_level()
    pygame.display.update()
    clock.tick(300)
