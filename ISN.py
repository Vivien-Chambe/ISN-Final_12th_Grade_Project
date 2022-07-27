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
    def __init__(self,x,y,image):
        self.x = x
        self.y = y 
        self.image = image

class Platform:
    def __init__(self,x,y,w,h):
        self.body = pygame.Rect(x,y,w,h)

    def draw(self):
        pygame.draw.rect(screen,"Black",self.body)

platform_width = 50
platform_height = 20
nb_platform = 8
platform_list = []
space = (height - platform_height - nb_platform*platform_height)/nb_platform

def create_level():
    sol = Platform(0,height-platform_height,width,platform_height)
    sol.draw()

    for i in range (nb_platform):
        platform_list.append(Platform(r.randint(0,width-platform_width),(sol.body.x)+(i+1)*space+platform_height,platform_width,platform_height))
        platform_list[i].draw()

screen.fill("White")
create_level()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                platform_list = []
                screen.fill("White")
                create_level()
        
    pygame.display.update()
    clock.tick(60)
