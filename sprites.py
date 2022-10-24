import pygame, sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

graphics_dir = resource_path("Graphics")

#### Sprites loading ######
menu = pygame.image.load(graphics_dir + "/menu.jpg")

perso_sprite_left_1 =pygame.image.load(graphics_dir + "/sprite_left1.bmp")
perso_sprite_left_1.set_colorkey("White")

perso_sprite_left_2 =pygame.image.load(graphics_dir + "/sprite_left2.bmp")
perso_sprite_left_2.set_colorkey("White")

perso_sprite_right_1 =pygame.image.load(graphics_dir + "/sprite_right1.bmp")
perso_sprite_right_1.set_colorkey("White")

perso_sprite_right_2 =pygame.image.load(graphics_dir + "/sprite_right2.bmp")
perso_sprite_right_2.set_colorkey("White")

back1 = pygame.image.load(graphics_dir + "/back1.jpg")
back3 = pygame.image.load(graphics_dir + "/back3.jpg")
back4 = pygame.image.load(graphics_dir + "/back4.jpg")

flag_sprite = pygame.image.load(graphics_dir + "/flag.jpg")
flag_sprite.set_colorkey("White")

platforme_sprite = pygame.image.load(graphics_dir + "/platforme.jpg")
sol_sprite = pygame.image.load(graphics_dir + "/sol.jpg")

#############################