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

def write_id(path,x):  
    f = open(path, "a")
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
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)

def main_loop():
    pygame.init()
    pygame.display.set_caption('Space Shooter')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = SCREEN_WIDTH/2
    Y = 630
    player = Ship("ship.png")
    background = Background("space.png")
    boss = Boss()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] and Y > 530:
            Y = Y - 10
        if pressed_keys[K_DOWN] and Y < 650:
            Y = Y + 10
        if pressed_keys[K_LEFT] and X > 10:
            X = X - 10
        if pressed_keys[K_RIGHT] and X < 1190:
            X = X + 10
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        screen.blit(player.surf,(X,Y))
        pygame.display.flip()
        clock.tick(30)
        print(X,Y)
main_loop()