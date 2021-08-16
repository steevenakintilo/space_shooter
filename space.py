#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

# Import the pygame module
import pygame
from random import randint
from os import system

def write_id(path,x):  
    f = open(path, "w")
    f.write(str(x))    
    f.close            

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_SPACE,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Background(pygame.sprite.Sprite):
    def __init__(self,path):
        super(Background, self).__init__()
        self.surf = pygame.image.load(path).convert_alpha()
        self.rect = self.surf.get_rect()

class Ship(pygame.sprite.Sprite):
    def __init__(self,path):
        super(Ship, self).__init__()
        self.surf = pygame.image.load(path).convert_alpha()
        self.rect = self.surf.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 255, 255))
        self.rect = self.surf.get_rect()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super(Boss, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

def display_all(screen,x,y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y), 1)

def shoot_fire(screen,color,X,Y,fire_speed):
    pos_y = Y  - fire_speed - 25
    pygame.draw.rect(screen, color, pygame.Rect(X + 41,pos_y, 5, 20))
    #print(pos_y)

def level1(screen,enemy,list,list2,list3,list4,list5,up,down):
    color = (0,0,0)
    #l2 = [list[0],list[1],list[2],list[3],list[4]]
    for i in range(5):
        screen.blit(enemy.surf,(list5[i]+down,20+up))
        screen.blit(enemy.surf,(list4[i]+down,120+up))
        screen.blit(enemy.surf,(list3[i]+down,220+up))
        screen.blit(enemy.surf,(list2[i]+down,320+up))
        
        
def main_loop():
    color = (255,255,255)
    color2 = (250,0,0)
    pygame.init()
    pygame.display.set_caption('Space Shooter')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = SCREEN_WIDTH/2
    Y = 630
    player = Ship("ship.png")
    enemy = Ship("ship2.png")
    background = Background("space.png")
    boss = Boss()
    running = True
    fire_speed = 0
    space = 0
    move_up = 0
    move_down = 0
    damage = 10
    enemy_x_pos = [310,360,380,460,480,560,580,660,680,760]
    l = [20,120,220,320,420]
    l2 = [l[0],l[1],l[2],l[3],l[4]]
    l3 = [l[0],l[1],l[2],l[3],l[4]]
    l4 = [l[0],l[1],l[2],l[3],l[4]]
    l5 = [l[0],l[1],l[2],l[3],l[4]]
    while running:
        if damage > 1290:
            quit()
        damage = damage + 10
        xpos = print_file("pos_y")
        pos = float(xpos)
        #space = 0
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pos_y =  Y  - fire_speed - 25
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] and Y > 530:
            Y = Y - 10
        if pressed_keys[K_DOWN] and Y < 640:
            Y = Y + 10
        if pressed_keys[K_LEFT] and X > 10:
            X = X - 10
        if pressed_keys[K_RIGHT] and X < 1190:
            X = X + 10
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        screen.blit(player.surf,(X,Y))
        level1(screen,enemy,l,l2,l3,l4,l5,move_down,move_up)
        
        move_up = move_up + 2
        if move_up > 300:
            move_up = 300
        if space != 0:
            fire_speed = fire_speed + 10
            if pos_y < 0:
                space = 0
                fire_speed = 10
            shoot_fire(screen,color,int(pos),Y,fire_speed)
        pygame.draw.rect(screen, color, pygame.Rect(0,705,1290,30))
        pygame.draw.rect(screen, color2, pygame.Rect(0,705,1290 - damage,30))
            #pygame.draw.rect(screen, color, pygame.Rect(X + 41, Y  - fire_speed - 25, 5, 20))
        if space == 0:
            write_id("pos_y",str(X))
        if pressed_keys[K_SPACE]:
            space = 0
            space = space + 1
            #shoot_fire(screen,color,X,Y,fire_speed)
        #print(space, X)
        if move_up == 300:
            for i in range(9):
                if pos_y < 385 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l2[int(i/2)] != -9999:
                    l2[int(i/2)] = -9999
                    space = 0
                    fire_speed = 10
                elif pos_y < 285 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l2[int(i/2)] == -9999 and l3[int(i/2)] != -9999:
                    l3[int(i/2)] = -9999
                    space = 0
                    fire_speed = 10
                elif pos_y < 185 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l3[int(i/2)] == -9999 and l4[int(i/2)] != -9999:
                    l4[int(i/2)] = -9999
                    space = 0
                    fire_speed = 10
                elif pos_y < 85 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l4[int(i/2)] == -9999 and l5[int(i/2)] != -9999:
                    l5[int(i/2)] = -9999
                    space = 0
                    fire_speed = 10
                #else:
            #    print("ok")
        #print(pos_y)
        pygame.display.flip()
        clock.tick(30)
        print(damage)

system("clear")
main_loop()