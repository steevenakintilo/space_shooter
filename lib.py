#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

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

def display_enemy(screen,enemy,list,list2,list3,list4,list5,up,down):
    color = (0,0,0)
    #l2 = [list[0],list[1],list[2],list[3],list[4]]
    for i in range(5):
        screen.blit(enemy.surf,(list5[i]+down,20+up))
        screen.blit(enemy.surf,(list4[i]+down,120+up))
        screen.blit(enemy.surf,(list3[i]+down,220+up))
        screen.blit(enemy.surf,(list2[i]+down,320+up))
