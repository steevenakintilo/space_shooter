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
import sys
import pygame.freetype 
from lib import *
sys.setrecursionlimit(1000000)

    
def random_shoot(no,list,lens):
    val = 0
    #print(list)
    y = randint(1,lens)
    #l = [1,2,3,4,5]
    x = int(list[y - 1])
    #print(list,x)
    #if x == no:
    #    l.pop(no - 1)
    #    newy = randint(1,4)
    #    x = int(l[newy - 1])
    #print(list,no,lens)        
    #if no == 0:
    #    x = randint(1,5)
    if x == 1:
        val = 320
    if x == 2:
        val = 420
    if x == 3:
        val = 520
    if x == 4:
        val = 620
    if x == 5:
        val = 720
    return(val)

def srandom_shoot(no,list,lens):
    val = 0
    #print(list)
    y = randint(1,lens)
    #l = [1,2,3,4,5]
    x = int(list[y - 1])
    #print(list,x)
    #if x == no:
    #    l.pop(no - 1)
    #    newy = randint(1,4)
    #    x = int(l[newy - 1])
    #print(list,no,lens)        
    #if no == 0:
    #    x = randint(1,5)
    if x == 1:
        val = 320
    if x == 2:
        val = 330
    if x == 3:
        val = 340
    if x == 4:
        val = 350
    if x == 5:
        val = 360
    return(val)

def the_shoop(lvl,life):
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('win.ogg'))
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 44)
  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2
    money = print_file("money.txt")
    #dollar = int(money)
    #l = len(money)
    #money = money[:l-1]
    dollar = int(money)
    clock = pygame.time.Clock()
    running = True
    background = Background("shop.jpg")
    lif = int(life)
    check = 0
    i = 0
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if i % 100 == 0:
            check = 0
        i = i + 1
        if pressed_keys[K_SPACE]:
            check_level(lvl,life)
        if pressed_keys[K_1] and dollar >= 25 and check == 0:
            check = 1
            lif = lif - 50
            dollar = dollar - 25
            write_id("life.txt",str(lif))
            write_id("money.txt", str(dollar))
        if pressed_keys[K_2] and dollar >= 250 and check == 0:
            check = 1
            dollar = dollar - 250
            write_id("ship.txt","2")
            write_id("money.txt", str(dollar))
        if pressed_keys[K_3] and dollar >= 500 and check == 0:
            check = 1
            dollar = dollar - 500
            write_id("ship.txt","3")
            write_id("money.txt", str(dollar))
        if pressed_keys[K_4] and dollar >= 1000 and check == 0:
            check = 1
            dollar = dollar - 1000
            write_id("ship.txt","4")
            write_id("money.txt", str(dollar))
        if pressed_keys[K_5] and dollar >= 2500 and check == 0:
            check = 1
            dollar = dollar - 2500
            write_id("ship.txt","5")
            write_id("money.txt", str(dollar))
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        GAME_FONT.render_to(screen, (150, 45), str(dollar), (255,255,255))
        pygame.display.flip()
        clock.tick(30)


def end_loop(lvl,life):
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('win.ogg'))
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 44)
  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    background = Background("win.png")
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            check_level(lvl,life)
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        pygame.display.flip()
        clock.tick(30)

def check_win(list):
    win = 0
    for i in range(len(list)):
        if list[i] == -9999:
            win = win + 1
    if win == 5:
        return (1)  
def level1(lvl,bullet_damage,damage,enemylife):
    enemy_life = int(enemylife)
    #enemy_life = 10print
    m = print_file("money.txt")
    enemy_lifes = enemy_life
    eee = print_file("life.txt")
    color = (255,255,255)
    color2 = (250,0,0)
    pygame.init()
    pygame.display.set_caption('Space Shooter')
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 44)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = SCREEN_WIDTH/2
    Y = 630
    player = Ship("ship.png")
    ship_lvl = print_file("ship.txt")
    speed_movement = 0
    double_bullet = 0
    big_bullet = 0
    if ship_lvl == "1":
        player = Ship("ship.png")
        speed_movement = 5
        double_bullet = 0
        big_bullet = 0
        faster_bullet = 0
    if ship_lvl == "2":
        player = Ship("ship2.png")
        speed_movement = 10
        double_bullet = 0
        big_bullet = 0
        faster_bullet = 0
    if ship_lvl == "3":
        player = Ship("ship3.png")
        speed_movement = 10
        double_bullet = 1
        big_bullet = 0
        faster_bullet = 0
    if ship_lvl == "4":
        player = Ship("ship4.png")
        speed_movement = 10
        double_bullet = 1
        big_bullet = 3
        faster_bullet = 0
    if ship_lvl == "5":
        player = Ship("ship5.png")
        speed_movement = 10
        double_bullet = 1
        big_bullet = 3
        faster_bullet = 1
    if lvl != 4:
        enemy = Ship("eship.png")
    if lvl == 4:
        enemy = Ship("boss1.png")
    background = Background("space.png")
    boss = Boss()
    running = True
    fire_speed = 0
    space = 0
    move_up = 0
    move_down = 0
    #int(damage) = int(life)
    bullet_speed = 0
    enemy_x_pos = [280,360,380,460,480,560,580,660,680,760]
    l = [20,120,220,320,420]
    l2 = [l[0],l[1],l[2],l[3],l[4]]
    l3 = [l[0],l[1],l[2],l[3],l[4]]
    l4 = [l[0],l[1],l[2],l[3],l[4]]
    l5 = [l[0],l[1],l[2],l[3],l[4]]
    x2 = [90,180,270,360]
    x3 = [90,180,270,360]
    x4 = [90,180,270,360]
    x5 = [90,180,270,360]
    x6 = [90,180,270,360]
    d = ["1","2","3","4","5"]
    money = 0
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0
    f5 = 0
    pop11 = 0
    pop12 = 0
    pop13 = 0
    pop21 = 0
    pop22 = 0
    pop23 = 0
    pop31 = 0
    pop32 = 0
    pop33 = 0
    pop41 = 0
    pop42 = 0
    pop43 = 0
    pop51 = 0
    pop52 = 0
    pop53 = 0
    revive = 0
    touch = 0
    rdm_y = randint(0,4)
    random_enemy = [320,420,520,620,720]
    rdm_shoot = random_shoot(0,d,5)
    random_shoot2 = 90
    dmg = int(damage)
    if lvl != 4:
        while running:
            life = write_id("life.txt",str(dmg))
            y1 = [l2[0],l3[0],l4[0],l5[0]]
            y2 = [l2[1],l3[1],l4[1],l5[1]]
            y3 = [l2[2],l3[2],l4[2],l5[2]]
            y4 = [l2[3],l3[3],l4[3],l5[3]]
            y5 = [l2[4],l3[4],l4[4],l5[4]]
            bullet_speed = bullet_speed + bullet_damage
            if dmg > 1290:
                write_id("life.txt","10")
                quit()
            xpos = print_file("pos_y")
            pos = float(xpos)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
            pos_y =  Y  - fire_speed - 25
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP] and Y > 530:
                Y = Y - speed_movement
            if pressed_keys[K_DOWN] and Y < 640:
                Y = Y + speed_movement
            if pressed_keys[K_LEFT] and X > 10:
                X = X - speed_movement
            if pressed_keys[K_RIGHT] and X < 1190:
                X = X + speed_movement
            screen.fill((0, 0, 0))
            screen.blit(background.surf,(0,0))
            screen.blit(player.surf,(X,Y))
            display_enemy(screen,enemy,l,l2,l3,l4,l5,move_down,move_up)
            last_line = [l5[0],l5[1],l5[2],l5[3],l5[4]]
            move_up = move_up + 2
            if move_up < 300:
                dmg = int(eee)
            if move_up > 300:
                move_up = 300
            if space != 0:
                if faster_bullet == 0:
                    fire_speed = fire_speed + 10
                if faster_bullet == 1:
                    fire_speed = fire_speed + 20
                if pos_y < 0:
                    space = 0
                    fire_speed = 10
                if double_bullet == 0:
                    shoot_fire(screen,color,int(pos),Y,fire_speed)
                if double_bullet == 1:
                    shoot_fire(screen,color,int(pos) -12,Y,fire_speed)
                    shoot_fire(screen,color,int(pos)  -14+ 20,Y,fire_speed)
            if space == 0:
                write_id("pos_y",str(X))
            if pressed_keys[K_SPACE] and  move_up == 300:
                space = 0
                space = space + 1
            if check_win(last_line) == 1:
                lvl = lvl + 1
                money = randint(30,50)
                if money == 47:
                    money = 1
                if money == 48:
                    money = 500
                write_id("money.txt",str(int(money) + int(m)))
                the_shoop(lvl,dmg)
            if move_up == 300:
                pygame.draw.rect(screen, color, pygame.Rect(rdm_shoot + 41,bullet_speed + random_shoot2, 5, 10))
            pygame.draw.rect(screen, color, pygame.Rect(rdm_shoot + 41,random_shoot2, 5, 10))
            li2 = x2[randint(0,len(x2) - 1)]
            li3 = x3[randint(0,len(x3) - 1)]
            li4 = x4[randint(0,len(x4) - 1)]
            li5 = x5[randint(0,len(x5) - 1)]
            li6 = x6[randint(0,len(x6) - 1)]
            GAME_FONT.render_to(screen, (5, 5), "Level " + str(lvl), (255,255,255))
            if bullet_speed > 610:
                bullet_speed = 0
                if check_win(last_line) != 1:
                    rdm_shoot = random_shoot(0,d,len(d))
                    random_shoot2 = li2
                if l5[0] == -9999 and r1 == 0 and check_win(last_line) != 1:
                    r1 = 1
                    rdm_shoot = random_shoot(1,d,len(d))
                    random_shoot2 = li2
                if l5[1] == -9999 and r2 == 0 and check_win(last_line) != 1:
                    r2 = 1
                    rdm_shoot = random_shoot(2,d,len(d))
                    random_shoot2 = li3
                if l5[2] == -9999 and r3 == 0 and check_win(last_line) != 1:
                    r3 = 1
                    rdm_shoot = random_shoot(3,d,len(d))
                    random_shoot2 = li4
                if l5[3] == -9999 and r4 == 0 and check_win(last_line) != 1:
                    r4 = 1
                    rdm_shoot = random_shoot(4,d,len(d))
                    random_shoot2 = li5
                if l5[4] == -9999 and r5 == 0 and check_win(last_line) != 1:
                    r5 = 1
                    rdm_shoot = random_shoot(5,d,len(d))
                    random_shoot2 = li6
            if rdm_shoot >= int(pos) - 42 and rdm_shoot <= int(pos) + 42 and bullet_speed + random_shoot2 >= Y and bullet_speed + random_shoot2 <= Y + 67:
                dmg = dmg + 30
                bullet_speed = 0
            if pressed_keys[K_SPACE] and enemy_life < 1 and double_bullet == 0:
                enemy_life = enemy_lifes
                money = money + randint(0,5)
            if move_up == 300:
                for i in range(9):
                    if double_bullet == 0:
                        if pos_y < 385 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l2[int(i/2)] != -9999:
                            enemy_life = enemy_life - big_bullet - 1
                            space = 0
                            fire_speed = 10
                            if enemy_life == 0:
                                l2[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                            #print("og")
                        elif pos_y < 285 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l2[int(i/2)] == -9999 and l3[int(i/2)] != -9999:
                            enemy_life = enemy_life - big_bullet - 1
                            space = 0
                            fire_speed = 10
                            if enemy_life == 0:
                                l3[int(i/2)] = -9999
                                enemy_life = enemy_lifes                            
                                
                        elif pos_y < 185 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l3[int(i/2)] == -9999 and l4[int(i/2)] != -9999:
                            enemy_life = enemy_life - big_bullet - 1
                            space = 0
                            fire_speed = 10
                            money = money + randint(0,5)
                            if enemy_life == 0:
                                l4[int(i/2)] = -9999
                                enemy_life = enemy_lifes                            
                        elif pos_y < 85 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l4[int(i/2)] == -9999 and l5[int(i/2)] != -9999:
                            enemy_life = enemy_life - big_bullet - 1
                            space = 0
                            fire_speed = 10
                            if enemy_life == 0:
                                l5[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                    if double_bullet == 1:
                        if (pos_y < 385 and int(pos) - 12 >= enemy_x_pos[i] and int(pos) -12 <= enemy_x_pos[i + 1] and l2[int(i/2)] != -9999) or (pos_y < 385 and int(pos) - 14 >= enemy_x_pos[i] and int(pos) - 14 <= enemy_x_pos[i + 1] and l2[int(i/2)] != -9999):
                            enemy_life = enemy_life - big_bullet - 2
                            space = 0
                            fire_speed = 10
                            if enemy_life == 0:
                                enemy_life = enemy_lifes                            
                                l2[int(i/2)] = -9999
                                #print("go")
                        elif (pos_y < 285 and int(pos) -12 >= enemy_x_pos[i] and int(pos) -12 <= enemy_x_pos[i + 1] and l2[int(i/2)] == -9999 and l3[int(i/2)] != -9999) or (pos_y < 285 and int(pos) -14 >= enemy_x_pos[i] and int(pos) -14 <= enemy_x_pos[i + 1] and l2[int(i/2)] == -9999 and l3[int(i/2)] != -9999):
                            enemy_life = enemy_life - big_bullet - 2
                            space = 0
                            fire_speed = 10
                            if enemy_life == 0:
                                enemy_life = enemy_lifes                            
                                l3[int(i/2)] = -9999
                        elif (pos_y < 185 and int(pos) -12 >= enemy_x_pos[i] and int(pos) -12 <= enemy_x_pos[i + 1] and l3[int(i/2)] == -9999 and l4[int(i/2)] != -9999) or (pos_y < 185 and int(pos) -14 >= enemy_x_pos[i] and int(pos) -14 <= enemy_x_pos[i + 1] and l3[int(i/2)] == -9999 and l4[int(i/2)] != -9999):
                            enemy_life = enemy_life - big_bullet - 2
                            space = 0
                            fire_speed = 10
                            if enemy_life == 0:
                                enemy_life = enemy_lifes                                
                                l4[int(i/2)] = -9999
                        elif (pos_y < 85 and int(pos) -12 >= enemy_x_pos[i] and int(pos) -12 <= enemy_x_pos[i + 1] and l4[int(i/2)] == -9999 and l5[int(i/2)] != -9999) or (pos_y < 85 and int(pos) -14 >= enemy_x_pos[i] and int(pos) -14 <= enemy_x_pos[i + 1] and l4[int(i/2)] == -9999 and l5[int(i/2)] != -9999):
                            enemy_life = enemy_life - big_bullet - 2
                            space = 0
                            fire_speed = 10
                            if enemy_life == 0:
                                enemy_life = enemy_lifes                                
                                l5[int(i/2)] = -9999
                                        
            if y1[0] == -9999 and pop11 == 0:
                x2.pop(len(x2) - 1)
                pop11 = 1
            if y1[1] == -9999 and pop12 == 0:
                x2.pop(len(x2) - 1)
                pop12 = 1
            if y1[2] == -9999 and pop13 == 0:
                x2.pop(len(x2) - 1)
                pop13 = 1
            
            if y2[0] == -9999 and pop21 == 0:
                x3.pop(len(x3) - 1)
                pop21 = 1
            if y2[1] == -9999 and pop22 == 0:
                x3.pop(len(x3) - 1)
                pop22 = 1
            if y2[2] == -9999 and pop23 == 0:
                x3.pop(len(x3) - 1)
                pop23 = 1
            
            if y3[0] == -9999 and pop31 == 0:
                x4.pop(len(x4) - 1)
                pop31 = 1
            if y3[1] == -9999 and pop32 == 0:
                x4.pop(len(x4) - 1)
                pop32 = 1
            if y3[2] == -9999 and pop33 == 0:
                x4.pop(len(x4) - 1)
                pop33 = 1
            
            if y4[0] == -9999 and pop41 == 0:
                x5.pop(len(x5) - 1)
                pop41 = 1
            if y4[1] == -9999 and pop42 == 0:
                x5.pop(len(x5) - 1)
                pop42 = 1
            if y4[2] == -9999 and pop43 == 0:
                x5.pop(len(x5) - 1)
                pop43 = 1
            
            if y5[0] == -9999 and pop51 == 0:
                x6.pop(len(x6) - 1)
                pop51 = 1
            if y5[1] == -9999 and pop52 == 0:
                x6.pop(len(x6) - 1)
                pop52 = 1
            if y5[2] == -9999 and pop53 == 0:
                x6.pop(len(x6) - 1)
                pop53 = 1
            
            pygame.draw.rect(screen, color, pygame.Rect(0,705,1290,30))
            pygame.draw.rect(screen, color2, pygame.Rect(0,705,1290 - dmg,30))
            pygame.display.flip()
            clock.tick(30)
            #print(y1,y2,y3,y4,y5)
            write_id("life.txt",str(dmg))
            dz = print_file("life.txt")
            #print(enemy_life,enemy_lifes)
            if l5[0] == -9999 and f1 == 0:
                f1 = 1
                d.remove("1")
            elif l5[1] == -9999 and f2 == 0:
                f2 = 1
                d.remove("2")
            elif l5[2] == -9999 and f3 == 0:
                f3 = 1
                d.remove("3")
            elif l5[3] == -9999 and f4 == 0:
                f4 = 1
                d.remove("4")
            elif l5[4] == -9999 and f5 == 0 and len(d) > 1:
                f5 = 1
                d.remove("5")
            #print(money)
            #print(d)
    if lvl == 4:
        while running:
            life = write_id("life.txt",str(dmg))
            bullet_speed = bullet_speed + bullet_damage
            if dmg > 1290:
                write_id("life.txt","10")
                quit()
            xpos = print_file("pos_y")
            pos = float(xpos)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
            pos_y =  Y  - fire_speed - 25
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP] and Y > 530:
                Y = Y - speed_movement
            if pressed_keys[K_DOWN] and Y < 640:
                Y = Y + speed_movement
            if pressed_keys[K_LEFT] and X > 10:
                X = X - speed_movement
            if pressed_keys[K_RIGHT] and X < 1190:
                X = X + speed_movement
            screen.fill((0, 0, 0))
            screen.blit(background.surf,(0,0))
            screen.blit(player.surf,(X,Y))
            screen.blit(enemy.surf,(0 + move_up * 1.5,0))
            #display_enemy(screen,enemy,l,l2,l3,l4,l5,move_down,move_up)
            move_up = move_up + 2
            if move_up < 300:
                dmg = int(eee)
            if move_up > 300:
                move_up = 300
            if space != 0:
                if faster_bullet == 0:
                    fire_speed = fire_speed + 10
                if faster_bullet == 1:
                    fire_speed = fire_speed + 20
                if pos_y < 0:
                    space = 0
                    fire_speed = 10
                if double_bullet == 0:
                    shoot_fire(screen,color,int(pos),Y,fire_speed)
                if double_bullet == 1:
                    shoot_fire(screen,color,int(pos) -12,Y,fire_speed)
                    shoot_fire(screen,color,int(pos)  -14+ 20,Y,fire_speed)
            if space == 0:
                write_id("pos_y",str(X))
            if pressed_keys[K_SPACE] and  move_up == 300:
                space = 0
                space = space + 1
            if enemy_life <= 0:
                lvl = lvl + 1
                money = randint(30,50)
                if money == 47:
                    money = 1
                if money == 48:
                    money = 500
                write_id("money.txt",str(int(money) + int(m)))
                the_shoop(lvl,dmg)
            if move_up == 300:
                pygame.draw.rect(screen, color, pygame.Rect(rdm_shoot + 41,bullet_speed + random_shoot2, 5, 10))
            pygame.draw.rect(screen, color, pygame.Rect(rdm_shoot + 41,random_shoot2, 5, 10))
            GAME_FONT.render_to(screen, (5, 5), "Level " + str(lvl), (255,255,255))
            if bullet_speed > 610:
                bullet_speed = 0
                if enemy_life > 0:
                    rdm_shoot = randint(400,600)
            #        random_shoot2 = li2
            if rdm_shoot >= int(pos) - 42 and rdm_shoot <= int(pos) + 42 and bullet_speed + random_shoot2 >= Y and bullet_speed + random_shoot2 <= Y + 67:
                dmg = dmg + 30
                bullet_speed = 0
            if pressed_keys[K_SPACE] and enemy_life < 1 and double_bullet == 0:
                enemy_life = enemy_lifes
                money = money + randint(0,5)
            if move_up == 300:
                if double_bullet == 0:
                    #print("ok")
                    if int(pos) < 620 and int(pos) > 410 and Y  - fire_speed - 25 < 220:
                        enemy_life = enemy_life - big_bullet - 1
                        space = 0
                        fire_speed = 10
                        #print("og")
                if double_bullet == 1:
                    if int(pos) < 620 and int(pos) > 410 and Y  - fire_speed - 25 < 220:
                            enemy_life = enemy_life - big_bullet - 2
                            space = 0
                            fire_speed = 10
            print(enemy_life,enemy_lifes)           
            pygame.draw.rect(screen, color, pygame.Rect(0,705,1290,30))
            pygame.draw.rect(screen, color2, pygame.Rect(0,705,1290 - dmg,30))
            pygame.display.flip()
            clock.tick(30)
            #print(y1,y2,y3,y4,y5)
            write_id("life.txt",str(dmg))
            dz = print_file("life.txt")
            #print(enemy_life,enemy_lifes)
            #print(money)
            #print(d)
    

def check_level(lvl,life):
    life = print_file("life.txt")
    enemy_life = print_file("enemy_life.txt")
    if lvl == 1:
        level1(1,10,life,enemy_life)
    if lvl == 2:
        level1(2,11,life,enemy_life)
    if lvl == 3:
        level1(3,12,life,enemy_life)
    if lvl == 4:
        level1(4,12,life,enemy_life)
    
#write_id("enemy_life.txt","1")
write_id("ship.txt","5")
write_id("life.txt","10")
write_id("money.txt","0")
write_id("pos_y","100")
system("clear")
check_level(4,10)
life = print_file("life.txt")
print(life)
the_shoop(1,life)