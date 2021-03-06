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
    y = randint(1,lens)
    x = int(list[y - 1])
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
    y = randint(1,lens)
    x = int(list[y - 1])
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
    shop_wait = 0
    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font/arcade.ttf", 44)
  
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
    background = Background("pic/shop.jpg")
    lif = int(life)
    check = 0
    i = 0
    while running:
        shop_wait = shop_wait + 1
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if i % 100 == 0:
            check = 0
        i = i + 1
        if pressed_keys[K_SPACE] and shop_wait > 100:
            check_level(lvl,life)
        if pressed_keys[K_1] and dollar >= 25 and check == 0 and lif > 10:
            check = 1
            lif = lif - 50
            dollar = dollar - 25
            write_id("life.txt",str(lif))
            write_id("money.txt", str(dollar))
            if lif < 10:
                write_id("life.txt","10")    
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
        if pressed_keys[K_5] and dollar >= 2000 and check == 0:
            check = 1
            dollar = dollar - 2000
            write_id("ship.txt","5")
            write_id("money.txt", str(dollar))
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        GAME_FONT.render_to(screen, (150, 45), str(dollar), (255,255,255))
        pygame.display.flip()
        clock.tick(30)




def stat_loop():
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('win.ogg'))
    death_k = print_file("loose_nbr.txt")
    win_k = print_file("win_nbr.txt")
    ship_k = print_file("ship_kill.txt")
    boss_k = print_file("boss_kill.txt")
    shoot_k = print_file("shoot_recieve.txt")
    death = int(death_k)
    win = int(win_k)
    ship = int(ship_k)
    boss = int(boss_k)
    shoot = int(shoot_k)
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    write_id("win.txt","1")
    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font/arcade.ttf", 44)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    background = Background("pic/stat.png")
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('m')]:
            menu_loop()
        if pressed_keys[ord("x")]:
            quit() 
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        GAME_FONT.render_to(screen, (230, 670), "Press    M    TO    GO    TO    THE    MENU    AND    X    TO    QUIT", (255,255,255))
        GAME_FONT.render_to(screen, (860 + + len(str(win)), 182), str(win), (255,255,255))
        GAME_FONT.render_to(screen, (880 + + len(str(death)), 254), str(death), (255,255,255))
        GAME_FONT.render_to(screen, (940 + len(str(ship)), 326), str(ship), (255,255,255))
        GAME_FONT.render_to(screen, (940 + len(str(boss)), 424), str(boss), (255,255,255))
        GAME_FONT.render_to(screen, (945 + len(str(shoot)), 516), str(shoot), (255,255,255))
        pygame.display.flip()
        clock.tick(30)

def how_to_play_loop():
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('win.ogg'))
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    write_id("win.txt","1")
    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font/arcade.ttf", 44)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    background = Background("pic/howtoplay.png")
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('m')]:
            menu_loop()
        if pressed_keys[ord("x")]:
            quit() 
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        GAME_FONT.render_to(screen, (230, 670), "Press    M    TO    GO    TO    THE    MENU    AND    X    TO    QUIT", (255,255,255))
        pygame.display.flip()
        clock.tick(30)

def level_loop():
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('win.ogg'))
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    write_id("win.txt","1")
    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font/arcade.ttf", 44)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    background = Background("pic/level.png")
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('e')]:
            write_id("difficulty.txt","1")
            check_level(1,10) 
        if pressed_keys[ord("m")]:
            write_id("difficulty.txt","2")
            check_level(1,10) 
        if pressed_keys[ord("h")]:
            write_id("difficulty.txt","3")
            check_level(1,10)  
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        pygame.display.flip()
        clock.tick(30)

def win_loop(lvl,life):
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('win.ogg'))
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    write_id("win.txt","1")
    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font/arcade.ttf", 44)
    write_id("enemy_life.txt","1")
    write_id("ship.txt","1")
    write_id("life.txt","10")
    write_id("money.txt","0")
    write_id("pos_y","100")
    write_id("level.txt","1")
    write_id("score.txt","0")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    background = Background("pic/win.png")
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('x')]:
            quit()
        if pressed_keys[ord("m")]:
            menu_loop()
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        GAME_FONT.render_to(screen, (230, 650), "Press    M    TO    GO    TO    THE    MENU    AND    X    TO    QUIT", (255,255,255))
        pygame.display.flip()
        clock.tick(30)



def menu_loop():
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('win.ogg'))
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    pygame.init()
    pygame.mixer.music.load("music/main.ogg")
    pygame.mixer.music.play(-1)
    #pygame.mixer.Channel(1).play(pygame.mixer.Sound('main.ogg'))
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font/arcade.ttf", 64)
    color = (0,0,0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2
    stop = 0
    clock = pygame.time.Clock()
    running = True
    background = Background("pic/menu.png")
    m_play = 0
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if int(pos[0]) > 470 and int(pos[0]) < 720 and int(pos[1]) > 248 and int(pos[1]) < 280:
                    write_id("enemy_life.txt","1")
                    write_id("ship.txt","1")
                    write_id("life.txt","10")
                    write_id("money.txt","0")
                    write_id("pos_y","100")
                    write_id("score.txt","0")
                    level_loop()
                if int(pos[0]) > 462 and int(pos[0]) < 595 and int(pos[1]) > 342 and int(pos[1]) < 385:
                    if int(print_file("level.txt")) != 11:
                        check_level(int(print_file("level.txt")),int(print_file("life.txt")))
                    if int(print_file("level.txt")) == 11:
                        level_loop()
                if int(pos[0]) > 425 and int(pos[0]) < 800 and int(pos[1]) > 548 and int(pos[1]) < 578:
                    how_to_play_loop()
                if int(pos[0]) > 450 and int(pos[0]) < 760 and int(pos[1]) > 448 and int(pos[1]) < 480:
                    stat_loop()
                if int(pos[0]) > 9 and int(pos[0]) < 82 and int(pos[1]) > 635 and int(pos[1]) < 707 and stop == 0:
                    pygame.mixer.music.stop()
                    stop = 1
                if stop == 1:
                    m_play = m_play + 1
                if int(pos[0]) > 9 and int(pos[0]) < 82 and int(pos[1]) > 635 and int(pos[1]) < 707 and stop == 1 and m_play > 1:
                    m_play = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play(-1)
                    stop = 0      
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('x')]:
            quit()
        if pressed_keys[K_SPACE]:
            check_level(lvl,life)
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        GAME_FONT.render_to(screen, (470, 250), "New Game", (255,255,255))
        GAME_FONT.render_to(screen, (460, 350), "Continue", (255,255,255))
        GAME_FONT.render_to(screen, (450, 450), "Statistic", (255,255,255))
        GAME_FONT.render_to(screen, (425, 550), "How    To    Play", (255,255,255))
        if stop == 1:
            pygame.draw.rect(screen, color, pygame.Rect(50,640, 50, 140))
        pygame.display.flip()
        clock.tick(30)

def end_loop(lvl,life):
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('win.ogg'))
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font/arcade.ttf", 44)
    write_id("enemy_life.txt","1")
    write_id("ship.txt","1")
    write_id("life.txt","10")
    write_id("money.txt","0")
    write_id("pos_y","100")
    write_id("level.txt","1")
    write_id("score.txt","0")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    background = Background("pic/loose.png")
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('x')]:
            quit()
        if pressed_keys[ord('m')]:
            menu_loop()
        screen.fill((0, 0, 0))
        screen.blit(background.surf,(0,0))
        GAME_FONT.render_to(screen, (230, 550), "Press    M    TO    GO    TO    THE    MENU    AND    X    TO    QUIT", (255,255,255))
        pygame.display.flip()
        clock.tick(30)

def make_score(time):
    x = 0
    if time <= 10:
        x = randint(100,200)
        return(x)
    if time < 30 and time > 10:
        x = randint(50,100)
        return(x)
    if time < 60 and time > 30:
        x = randint(25,50)
        return(x)
    if time < 100 and time > 60:
        x = randint(10,25)
        return(x)
    if time < 150 and time > 100:
        x = randint(5,10)
        return(x)
    if time < 200 and time > 150:
        x = 1
        return(x)

def check_win(list):
    win = 0
    for i in range(len(list)):
        if list[i] == -9999:
            win = win + 1
    if win == 5:
        return (1)  
def game_level(lvl,bullet_damage,damage,enemylife):
    death_k = print_file("loose_nbr.txt")
    death_nbr = int(death_k)
    win_k = print_file("win_nbr.txt")
    win_nbr = int(win_k)
    ship_k = print_file("ship_kill.txt")
    boss_k = print_file("boss_kill.txt")
    shoot_k = print_file("shoot_recieve.txt")
    ship_kills = int(shoot_k)
    boss_kills = int(boss_k)
    shoot_gots = int(shoot_k)
    dif = print_file("difficulty.txt")
    diff = int(dif)
    enemy_life = int(enemylife)
    #enemy_life = 10print
    write_id("level.txt",lvl)
    m = print_file("money.txt")
    high = print_file("highscore.txt")
    highscore = int(high)
    enemy_lifes = enemy_life
    level_life = print_file("life.txt")
    eee = print_file("life.txt")
    color = (255,255,255)
    color2 = (250,0,0)
    pygame.init()
    pygame.display.set_caption('Space Shooter')
    GAME_FONT = pygame.freetype.Font("font/arcade.ttf", 44)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = SCREEN_WIDTH/2
    Y = 630
    add_score = 0
    player = Ship("pic/ship.png")
    ship_lvl = print_file("ship.txt")
    speed_movement = 0
    double_bullet = 0
    menu_wait = 0
    big_bullet = 0
    if ship_lvl == "1":
        player = Ship("pic/ship.png")
        speed_movement = 5
        double_bullet = 0
        big_bullet = 0
        faster_bullet = 0
    if ship_lvl == "2":
        player = Ship("pic/ship2.png")
        speed_movement = 10
        double_bullet = 0
        big_bullet = 0
        faster_bullet = 0
    if ship_lvl == "3":
        player = Ship("pic/ship3.png")
        speed_movement = 10
        double_bullet = 1
        big_bullet = 0
        faster_bullet = 0
    if ship_lvl == "4":
        player = Ship("pic/ship4.png")
        speed_movement = 10
        double_bullet = 1
        big_bullet = 3
        faster_bullet = 0
    if ship_lvl == "5":
        player = Ship("pic/ship5.png")
        speed_movement = 10
        double_bullet = 1
        big_bullet = 3
        faster_bullet = 1
    more_damage = 0
    if lvl == 10:
        speed_follow = 3
    if lvl == 4 or lvl == 7:
        speed_follow = 0
    if lvl == 1 or lvl == 2:
        enemy = Ship("pic/eship.png")
        more_damage = 0
    if lvl == 3:
        enemy = Ship("pic/eship2.png")
        more_damage = 10
    if lvl == 5 or lvl == 6:
        enemy = Ship("pic/eship3.png")
        more_damage = 30
    if lvl == 8 or lvl == 9:
        enemy = Ship("pic/eship4.png")
        more_damage = 50
    if lvl == 4:
        enemy = Ship("pic/boss1.png")
    if lvl == 7:
        enemy = Ship("pic/boss2.png")
    if lvl == 10:
        enemy = Ship("pic/boss3.png")
    diff_damage = 0
    easy_bull = 0
    if diff == 1:
        diff_damage = 15
        easy_bull = 2
    if diff == 3:
        diff_damage = 15
    background = Background("pic/space.png")
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
    boss_follow = 0
    touch = 0
    rdm_y = randint(0,4)
    random_enemy = [320,420,520,620,720]
    rdm_shoot = random_shoot(0,d,5)
    random_shoot2 = 90
    dmg = int(damage)
    score_time = print_file("score.txt")
    score = int(score_time)
    time = 0
    up_score = 0
    if lvl != 4 and lvl != 7 and lvl != 10:
        while running:
            menu_wait = menu_wait + 1
            if move_up == 300:
                up_score = up_score + 1
            if up_score % 30 == 1:
                time = time + 1
            life = write_id("life.txt",str(dmg))
            y1 = [l2[0],l3[0],l4[0],l5[0]]
            y2 = [l2[1],l3[1],l4[1],l5[1]]
            y3 = [l2[2],l3[2],l4[2],l5[2]]
            y4 = [l2[3],l3[3],l4[3],l5[3]]
            y5 = [l2[4],l3[4],l4[4],l5[4]]
            bullet_speed = bullet_speed + bullet_damage
            if dmg > 1290:
                death_nbr = death_nbr + 1
                write_id("loose_nbr.txt",death_nbr)
                write_id("life.txt","10")
                end_loop(lvl,life)
            xpos = print_file("pos_y")
            pos = float(xpos)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    write_id("life.txt",str(level_life))
                    if event.key == K_ESCAPE:
                        quit()
                elif event.type == QUIT:
                    write_id("life.txt",str(level_life))
                    quit()
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
            if pressed_keys[ord('s')]:
                write_id("life.txt",str(level_life))
                quit()
            if menu_wait > 200:
                if pressed_keys[ord("m")]:
                    menu_loop()
            screen.fill((0, 0, 0))
            screen.blit(background.surf,(0,0))
            screen.blit(player.surf,(X,Y))
            display_enemy(screen,enemy,l,l2,l3,l4,l5,move_down,move_up)
            last_line = [l5[0],l5[1],l5[2],l5[3],l5[4]]
            move_up = move_up + 2
            #print(level_life)
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
            if time <= 10:
                add_score = randint(100,200)
            if time < 30 and time > 10:
                add_score = randint(50,100)
            if time < 60 and time > 30:
                add_score = randint(25,50)
            if time < 100 and time > 60:
                add_score = randint(10,25)
            if time < 150 and time > 100:
                add_score = randint(5,10)
            if time < 200 and time > 150:
                add_score = 1
            if space == 0:
                write_id("pos_y",str(X))
            if pressed_keys[K_SPACE] and  move_up == 300:
                space = 0
                space = space + 1
            if check_win(last_line) == 1:
                lvl = lvl + 1
                if diff == 1:
                    money = randint(80,100)
                    if money == 87 or money == 86 or money == 85 or money == 84 or money == 83:
                        money = 1
                    if money == 88:
                        money = 1000
                if diff == 2:
                    money = randint(50,70)
                    if money == 57 or money == 56 or money == 55 or money == 54 or money == 53:
                        money = 1
                    if money == 58:
                        money = 750
                if diff == 3:
                    money = randint(30,50)
                    if money == 47:
                        money = 1
                    if money == 48:
                        money = 500
                write_id("money.txt",str(int(money) + int(m)))
                if lvl != 11:
                    write_id("score.txt",str(score))
                    the_shoop(lvl,dmg)
                if lvl == 11:
                    win_nbr = win_nbr + 1
                    write_id("win_nbr.txt",win_nbr)
                    write_id("score.txt",str(score))
                    win_loop(lvl,life)
            if score > int(highscore):
                write_id("highscore.txt",str(score))
                high = print_file("highscore.txt")
                highscore = int(high)
            if move_up == 300:
                pygame.draw.rect(screen, color, pygame.Rect(rdm_shoot + 41,bullet_speed + random_shoot2, 5, 10))
            #pygame.draw.rect(screen, color, pygame.Rect(rdm_shoot + 41,random_shoot2, 5, 10))
            li2 = x2[randint(0,len(x2) - 1)]
            li3 = x3[randint(0,len(x3) - 1)]
            li4 = x4[randint(0,len(x4) - 1)]
            li5 = x5[randint(0,len(x5) - 1)]
            li6 = x6[randint(0,len(x6) - 1)]
            GAME_FONT.render_to(screen, (5, 5), "Level " + str(lvl), (255,255,255))
            GAME_FONT.render_to(screen, (5, 40), "Score " + str(score), (255,255,255))
            GAME_FONT.render_to(screen, (5, 75), "Highcore " + str(highscore), (255,255,255))
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
            player_rect = pygame.Rect(X, Y, 84, 67)
            bullet_rect = pygame.Rect(rdm_shoot, random_shoot2, 5, 20)
            #print(shoot_gots)
            if rdm_shoot >= X - 42 and rdm_shoot <= X + 42 and bullet_speed + random_shoot2 >= Y and bullet_speed + random_shoot2 <= Y + 67:
                if diff == 1:
                    dmg = dmg + 30 + more_damage - diff_damage
                    shoot_gots = shoot_gots + 1
                    write_id("shoot_recieve.txt",shoot_gots)
                if diff == 2:
                    dmg = dmg + 30 + more_damage
                    shoot_gots = shoot_gots + 1
                    write_id("shoot_recieve.txt",shoot_gots)
                if diff == 3:
                    dmg = dmg + 30 + more_damage + diff_damage
                    shoot_gots = shoot_gots + 1
                    write_id("shoot_recieve.txt",shoot_gots)
                bullet_speed = 0
            if pressed_keys[K_SPACE] and enemy_life < 1 and double_bullet == 0:
                enemy_life = enemy_lifes
                money = money + randint(0,5)
            if move_up == 300:
                for i in range(9):
                    if double_bullet == 0:
                        if pos_y < 385 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l2[int(i/2)] != -9999:
                            enemy_life = enemy_life - big_bullet - 1- easy_bull
                            space = 0
                            fire_speed = 10
                            if enemy_life <= 0:
                                score = score + add_score                                
                                l2[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                                ship_kills = ship_kills + 1
                                write_id("ship_kill.txt",ship_kills)
                            #print("og")
                        elif pos_y < 285 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l2[int(i/2)] == -9999 and l3[int(i/2)] != -9999:
                            enemy_life = enemy_life - big_bullet - 1- easy_bull
                            space = 0
                            fire_speed = 10
                            if enemy_life <= 0:
                                score = score + add_score                                
                                l3[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                                ship_kills = ship_kills + 1
                                write_id("ship_kill.txt",ship_kills)                
                                
                        elif pos_y < 185 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l3[int(i/2)] == -9999 and l4[int(i/2)] != -9999:
                            enemy_life = enemy_life - big_bullet - 1- easy_bull
                            space = 0
                            fire_speed = 10
                            money = money + randint(0,5)
                            if enemy_life <= 0:
                                score = score + add_score                                
                                l4[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                                ship_kills = ship_kills + 1
                                write_id("ship_kill.txt",ship_kills)                
                        elif pos_y < 85 and int(pos) >= enemy_x_pos[i] and int(pos) <= enemy_x_pos[i + 1] and l4[int(i/2)] == -9999 and l5[int(i/2)] != -9999:
                            enemy_life = enemy_life - big_bullet - 1- easy_bull
                            space = 0
                            fire_speed = 10
                            if enemy_life <= 0:
                                score = score + add_score                                
                                l5[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                                ship_kills = ship_kills + 1
                                write_id("ship_kill.txt",ship_kills)
                    if double_bullet == 1:
                        if (pos_y < 385 and int(pos) - 12 >= enemy_x_pos[i] and int(pos) -12 <= enemy_x_pos[i + 1] and l2[int(i/2)] != -9999) or (pos_y < 385 and int(pos) - 14 >= enemy_x_pos[i] and int(pos) - 14 <= enemy_x_pos[i + 1] and l2[int(i/2)] != -9999):
                            enemy_life = enemy_life - big_bullet - 2- easy_bull
                            space = 0
                            fire_speed = 10
                            if enemy_life  <= 0:
                                score = score + add_score                                
                                l2[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                                ship_kills = ship_kills + 1
                                write_id("ship_kill.txt",ship_kills)                
                                #print("go")
                        elif (pos_y < 285 and int(pos) -12 >= enemy_x_pos[i] and int(pos) -12 <= enemy_x_pos[i + 1] and l2[int(i/2)] == -9999 and l3[int(i/2)] != -9999) or (pos_y < 285 and int(pos) -14 >= enemy_x_pos[i] and int(pos) -14 <= enemy_x_pos[i + 1] and l2[int(i/2)] == -9999 and l3[int(i/2)] != -9999):
                            enemy_life = enemy_life - big_bullet - 2- easy_bull
                            space = 0
                            fire_speed = 10
                            if enemy_life <= 0:
                                score = score + add_score                                
                                l3[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                                ship_kills = ship_kills + 1
                                write_id("ship_kill.txt",ship_kills)                
                        elif (pos_y < 185 and int(pos) -12 >= enemy_x_pos[i] and int(pos) -12 <= enemy_x_pos[i + 1] and l3[int(i/2)] == -9999 and l4[int(i/2)] != -9999) or (pos_y < 185 and int(pos) -14 >= enemy_x_pos[i] and int(pos) -14 <= enemy_x_pos[i + 1] and l3[int(i/2)] == -9999 and l4[int(i/2)] != -9999):
                            enemy_life = enemy_life - big_bullet - 2- easy_bull
                            space = 0
                            fire_speed = 10
                            if enemy_life <= 0:
                                score = score + add_score                                
                                l4[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                                ship_kills = ship_kills + 1
                                write_id("ship_kill.txt",ship_kills)                
                        elif (pos_y < 85 and int(pos) -12 >= enemy_x_pos[i] and int(pos) -12 <= enemy_x_pos[i + 1] and l4[int(i/2)] == -9999 and l5[int(i/2)] != -9999) or (pos_y < 85 and int(pos) -14 >= enemy_x_pos[i] and int(pos) -14 <= enemy_x_pos[i + 1] and l4[int(i/2)] == -9999 and l5[int(i/2)] != -9999):
                            enemy_life = enemy_life - big_bullet - 2 - easy_bull
                            space = 0
                            fire_speed = 10
                            if enemy_life <= 0:
                                score = score + add_score                                
                                l5[int(i/2)] = -9999
                                enemy_life = enemy_lifes
                                ship_kills = ship_kills + 1
                                write_id("ship_kill.txt",ship_kills)                
                                        
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
            #print(int(pos),X)
    if lvl == 4 or lvl == 7 or lvl == 10:
        while running:
            menu_wait = menu_wait + 1
            if move_up == 300:
                up_score = up_score + 1
            if up_score % 30 == 1:
                time = time + 1
            if move_up == 300:
                if lvl == 7 or lvl == 10:
                    if boss_follow + 550 < X and X < 1175:
                        boss_follow = boss_follow + 2 + speed_follow
                    if boss_follow + 550 > X and X > 100:
                        boss_follow = boss_follow - 2 - speed_follow
                    if boss_follow == X:
                        boss_follow = boss_follow
            life = write_id("life.txt",str(dmg))
            bullet_speed = bullet_speed + bullet_damage
            if dmg > 1290:
                death_nbr = death_nbr + 1
                write_id("loose_nbr.txt",death_nbr)
                write_id("life.txt","10")
                end_loop(lvl,life)
            xpos = print_file("pos_y")
            pos = float(xpos)
            if boss == int(pos):
                boss_follow = boss_follow    
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        write_id("life.txt",str(level_life))
                        quit()
                elif event.type == QUIT:
                    write_id("life.txt",str(level_life))
                    quit()
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
            if pressed_keys[ord('s')]:
                write_id("life.txt",str(level_life))
                quit()
            if menu_wait > 200:
                if pressed_keys[ord("m")]:
                    menu_loop()
            screen.fill((0, 0, 0))
            screen.blit(background.surf,(0,0))
            screen.blit(player.surf,(X,Y))
            if lvl == 4:
                screen.blit(enemy.surf,(0 + move_up * 1.5,0))
            if (lvl == 7  or lvl == 10) and move_up < 300:
                screen.blit(enemy.surf,(0 + move_up * 1.5 ,0))
            if (lvl == 7 or lvl == 10) and move_up == 300:
                screen.blit(enemy.surf,(0 + move_up * 1.5 + boss_follow,0))
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
                boss_kills = boss_kills + 1
                write_id("boss_kill.txt",boss_kills)
                lvl = lvl + 1
                if diff == 1:
                    money = randint(500,1000)
                    if money == 87 or money == 86 or money == 85 or money == 84 or money == 83:
                        money = 1
                    if money == 88:
                        money = 5000
                if diff == 2:
                    money = randint(500,700)
                    if money == 57 or money == 56 or money == 55 or money == 54 or money == 53:
                        money = 1
                    if money == 58:
                        money = 5000
                if diff == 3:
                    money = randint(300,500)
                    if money == 47:
                        money = 1
                    if money == 48:
                        money = 5000
                write_id("money.txt",str(int(money) + int(m)))
                if lvl != 11:
                    write_id("score.txt",str(score))
                    the_shoop(lvl,dmg)
                if lvl == 11:
                    win_nbr = win_nbr + 1
                    write_id("win_nbr.txt",win_nbr)
                    write_id("score.txt",str(score))
                    win_loop(lvl,life)
            if score > int(highscore):
                write_id("highscore.txt",str(score))
                high = print_file("highscore.txt")
                highscore = int(high)
            if time <= 10:
                add_score = randint(100,200)
            if time < 30 and time > 10:
                add_score = randint(50,100)
            if time < 60 and time > 30:
                add_score = randint(25,50)
            if time < 100 and time > 60:
                add_score = randint(10,25)
            if time < 150 and time > 100:
                add_score = randint(5,10)
            if time < 200 and time > 150:
                add_score = 1
            
            if move_up == 300:
                pygame.draw.rect(screen, color, pygame.Rect(rdm_shoot + 41,bullet_speed + random_shoot2, 5, 10))
            #pygame.draw.rect(screen, color, pygame.Rect(rdm_shoot + 41,random_shoot2, 5, 10))
            GAME_FONT.render_to(screen, (5, 5), "Level " + str(lvl), (255,255,255))
            GAME_FONT.render_to(screen, (5, 40), "Score " + str(score), (255,255,255))
            GAME_FONT.render_to(screen, (5, 75), "Highcore " + str(highscore), (255,255,255))
            if bullet_speed > 610:
                bullet_speed = 0
                if enemy_life > 0:
                    if lvl == 4 or lvl == 7:
                        rdm_shoot = randint(boss_follow + 450,boss_follow + 600)
                    if lvl == 10:
                        rdm_shoot = randint(boss_follow + 500,boss_follow + 550)
                        dmg = dmg + 1
                    
            #        random_shoot2 = li2
            if rdm_shoot >= X - 42 and rdm_shoot <= X + 42 and bullet_speed + random_shoot2 >= Y and bullet_speed + random_shoot2 <= Y + 67:
                dmg = dmg + 100
                bullet_speed = 0
            if pressed_keys[K_SPACE] and enemy_life < 1 and double_bullet == 0:
                enemy_life = enemy_lifes
                money = money + randint(0,5)
            if move_up == 300:
                if double_bullet == 0:
                    #print("ok")
                    if int(pos) < 620 + boss_follow and int(pos) > 410 + boss_follow and Y  - fire_speed - 25 < 220:
                        enemy_life = enemy_life - big_bullet - 1- easy_bull
                        score = score + add_score
                        space = 0
                        fire_speed = 10
                        #print("og")
                if double_bullet == 1:
                    if int(pos) < 620 + boss_follow and int(pos) > 410 + boss_follow and Y  - fire_speed - 25 < 220:
                            enemy_life = enemy_life - big_bullet - 2- easy_bull
                            if ship_lvl == "3":
                                score = score + 2 * add_score
                            if ship_lvl == "4":
                                score = score + 3 * add_score
                            if ship_lvl == "5":
                                score = score + 4 * add_score
                            space = 0
                            fire_speed = 10
            #print(boss_follow + 450,X,enemy_life)           
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
        game_level(1,10,life,1)
    if lvl == 2:
        game_level(2,11,life,1)
    if lvl == 3:
        game_level(3,12,life,2)
    if lvl == 4:
        game_level(4,15,life,50)
    if lvl == 5:
        game_level(5,13,life,5)
    if lvl == 6:
        game_level(6,14,life,5)
    if lvl == 7:
        game_level(7,20,life,100)
    if lvl == 8:
        game_level(8,15,life,10)
    if lvl == 9:
        game_level(9,16,life,10)
    if lvl == 10:
        game_level(10,40,life,200)
    
system("clear")
#check_level(1,10)
life = print_file("life.txt")
#print(life)
#the_shoop(1,life)
menu_loop()