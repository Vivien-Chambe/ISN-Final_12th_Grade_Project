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
test_font = pygame.font.Font(None, 50)

perso_image = pygame.Surface((50,50))


class Character:
    def __init__(self,x,y,w,h):
        self.body = pygame.Rect(x,y,w,h)
        self.relative_height = 0
        self.falling = False

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
        self.sol = None 
        self.list = []
        self.len = 0
    
    def draw_level(self):
        self.sol.draw()
        for i in range(self.len):
            self.list[i].draw()

    def restart(self):
        for i in range(self.len):
            self.list[i].body.x = r.randint(0,width-platform_width)

platform_width = 50
platform_height = 20
nb_platform = 7
space = (height - platform_height - nb_platform*platform_height)/nb_platform

def create_level():
    platform_list = Platform_List()
    sol = Platform(0,height-platform_height,width,platform_height)
    platform_list.sol = sol

    for i in range (nb_platform):
        platform_list.list.append(Platform(r.randint(0,width-platform_width),(sol.body.x)+(i+1)*space+platform_height,platform_width,platform_height))
        platform_list.len +=1

    return platform_list


def update_level():
    screen.fill("White")
    platform_list.draw_level()
    perso.draw()



platform_list = create_level()

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
    

    ############################# Character Movement #########################
    keys = pygame.key.get_pressed()

    if (sum(keys) == 0 and perso.relative_height > 0) or perso.falling == True : # No key pressed
        perso.body.y += 5
        perso.relative_height -= 5
        if perso.relative_height == 0:
            perso.falling = False

    if keys[pygame.K_LEFT]:
        perso.body.x -= 5
    if keys[pygame.K_RIGHT]:
        perso.body.x += 5
    if keys[pygame.K_SPACE] and perso.relative_height<150 and perso.falling == False:
        perso.body.y -= 5
        perso.relative_height += 5
        if perso.relative_height == 150:
            perso.falling = True
    else:pass
    ############################ Update screen ###################################
    update_level()
    pygame.display.update()
    clock.tick(100)
