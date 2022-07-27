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

    def draw(self):
        pygame.draw.rect(screen,"Red",self.body)
    
    def reset_position(self):
        self.body.x = width/2
        self.body.y = height-plateform_height-50

class plateform:
    def __init__(self,x,y,w,h):
        self.body = pygame.Rect(x,y,w,h)

    def draw(self):
        pygame.draw.rect(screen,"Black",self.body)

class Plateform_List:
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
            self.list[i].body.x = r.randint(0,width-plateform_width)

plateform_width = 50
plateform_height = 20
nb_plateform = 7
space = (height - plateform_height - nb_plateform*plateform_height)/nb_plateform

def create_level():
    plateform_list = Plateform_List()
    sol = plateform(0,height-plateform_height,width,plateform_height)
    plateform_list.sol = sol

    for i in range (nb_plateform):
        plateform_list.list.append(plateform(r.randint(0,width-plateform_width),(sol.body.x)+(i+1)*space+plateform_height,plateform_width,plateform_height))
        plateform_list.len +=1

    return plateform_list


def update_level():
    screen.fill("White")
    plateform_list.draw_level()
    perso.draw()



plateform_list = create_level()

perso = Character(width/2,height-plateform_height-50,20,50)
perso.draw()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                plateform_list.restart()
                perso.reset_position()
            elif event.key == pygame.K_SPACE:
                for i in range(200):
                    perso.body.y -= 1
                    perso.draw()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        perso.body.x -= 5
    elif keys[pygame.K_RIGHT]:
        perso.body.x += 5
    
    update_level()
    pygame.display.update()
    clock.tick(60)
