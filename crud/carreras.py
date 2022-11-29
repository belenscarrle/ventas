import pygame,sys
pygame.init()
from pygame.locals import*
import random
import math
import time 
screen = pygame.display.set_mode((798,600))
pygame.mixer.init()
pygame.display.set_caption('juego de autos')

logo = pygame.image.load("c:/Users/sistema/Downloads/crud/imagenes/logo.png")
pygame.display.set_icon(logo)
IntroFont = pygame.font.Font('freesansbold.ttf',38)

def intro(x,y):
    intro = pygame.image.load('c:/Users/sistema/Downloads/crud/imagenes/logo.png')
    screen.blit (intro,(x,y))

def play (x,y):
    playtext = IntroFont.render('jugar',True,(255,255,255))
    screen.blit (playtext,(x,y))

def pantatlladeinicio():
    run= True
    while run:
        screen.fill((0,0,0))
        intro(0,0)
        play(330,450)#coordenada del texto

        x,y = pygame.mouse.get_pos()
        button1 = pygame.Rect(300,440,195,50)

        pygame.draw.rect(screen, (255,255,255),button1,6)

        if button1.collidepoint(x,y):
            pygame.draw.rect(screen, (0,47,187), button1,6)

            if click:
                caracteristicas()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    click =True
        pygame.display.update()

def caracteristicas():
    font1= pygame.font.Font("freesansbold.ttf",25)

    with open ("","r") as f:
        highscore = f.read()
    def puntuacionmaxima(x,y):
        Hiscore_text = font1.render('puntuacion maxima: '+ str(highscore),True,(255,0,0))
        screen.blit (Hiscore_text,(x,y))
        pygame.display.update()

    def Gamerover():
        gameoverImg = pygame.image.load('')
        run =True
        while run:
            screen.blit(gameoverImg,(0,0))
            time.sleep(0,2)
            puntuacion(330,400)
            time.sleep(0,2)
            puntuacionmaxima(330,450)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        caracteristicas()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
bg = pygame.image.load('fondo.png')
#imagen del jugador 
maincar= pygame.image.load('c:/Users/sistema/Downloads/crud/imagenes/autoPlayer.png')
maincarX = 350
maincarY = 495
maincarX_change = 0
maincarY_change = 0

car1 = pygame.image.load('c:/Users/sistema/Downloads/crud/imagenes/autoPlayer.png')
car1X = random.randint(148,500)
car1Y =100
car1Ychange = 10
car2 = pygame.image.load('c:/Users/sistema/Downloads/crud/imagenes/enemigo1.png')
car2X = random.randint(155.505)
car2Y = 100
car2Ychange = 10
car3 = pygame.image.load('c:/Users/sistema/Downloads/crud/imagenes/enemigo2.png')
car3X = random.randint(145.495)
car3Y = 100
car3Ychange = 10

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                maincarX_change += 5
            if event.Key == pygame.K_LEFT:
                maincarX_change += 5
            if event.Key == pygame.K_UP:
                maincarY_change += 5
            if event.Key == pygame.K_DOWN:
                maincarY_change += 5
        if event.type == pygame.KEYUP:
            if event.Key == pygame.K_RIGHT:
                maincarX_change += 0
            if event.Key == pygame.K_LEFT:
                maincarX_change += 0
            if event.Key == pygame.K_UP:
                maincarY_change += 0
            if event.Key == pygame.K_DOWN:
                maincarY_change += 0
    if maincarX < 178:
        maincarX = 178
    if maincarX > 490:
        maincarX = 490
    if maincarY < 0:
        maincarY = 0
    if maincarY > 495:
        maincarY = 495
    
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    screen.blit(maincar,(maincarX,maincarY))
    screen.blit(car1,(car1X,car1Y))
    screen.blit(car1,(car2X,car2Y))
    screen.blit(car1,(car3X,car3Y))

    puntuacion=(570,280)
    puntuaciomaxima =(0,0)
    maincarX += maincarX_change
    maincarY += maincarY_change
    car1Y +=2
    car2Y +=2
    car3Y +=2
    if car1Y > 670:
        car1Y = -11
        car1X = random.randint(178.490)
    if car2Y > 670:
        car2Y = -200
        car2X = random.randint(178.490)
    if car3Y > 670:
        car3Y = -300
        car3X = random.randint(178.490)

    def collision(car1X,car1Y,maincarX,maincarY):
        distance = math.sqrt(math.pow(car1X-maincarX,2)+ math.pow(car1Y-maincarY,2))

        if distance < 30:
            return True
        else:
            return False
    def collision(car2X,car2Y,maincarX,maincarY):
        distance = math.sqrt(math.pow(car2X-maincarX,2)+math.pow(car2Y-maincarY))
        if distance < 30:
            return True
        else:
            return False
    def collision(car3X,car3Y,maincarX,maincarY):
        distance = math.sqrt(math.pow(car3X-maincarX,2)+math.pow(car3Y-maincarY))
        if distance < 30:
            return True
        else:
            return False
    coll1 = collision(car1X,car1Y,maincarX,maincarY)
    coll2 = collision(car2X,car2Y,maincarX,maincarY)
    coll3 = collision(car3X,car3Y,maincarX,maincarY)
    if coll1:
        car1Ychange = 0
        car2Ychange = 0
        car3Ychange = 0
        car1Y = 0
        car2Y = 0
        car3Y = 0
        maincarX_change = 0
        maincarY_change = 0
        time.sleep(1)
        Gameover()
    if coll2:
        car1Ychange = 0
        car2Ychange = 0
        car3Ychange = 0
        car1Y = 0
        car2Y = 0
        car3Y = 0
        maincarX_change = 0
        maincarY_change = 0
        time.sleep(1)
        Gameover()
    if coll3:
        car1Ychange = 0
        car2Ychange = 0
        car3Ychange = 0
        car1Y = 0
        car2Y = 0
        car3Y = 0
        maincarX_change = 0
        maincarY_change = 0
        time.sleep(1)
        Gameover()
    if car1Ychange == 0 and car2Ychange == 0 and car3Ychange == 0:
        pass

    pygame.display.update()
pantatlladeinicio()
    