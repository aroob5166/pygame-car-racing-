import pygame

import random
import time
pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Car Game')
colors = {'grey': (118,119,110), 'black': (0,0,0)}

backgroundLeft = pygame.image.load('images/left.png')
backgroundRight = pygame.image.load('images/right.png')
carImg = pygame.image.load('images/car1.png')
def background():
    screen.blit(backgroundLeft, (0,0))
    screen.blit(backgroundRight, (700,0))
def displayMessage(text):
    largeText = pygame.font.Font("freesansbold.ttf",80)
    textsurf = largeText.render(text, True, colors['black'])
    textrect = textsurf.get_rect()
    textrect.center = ((400,300))
    screen.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    loop()



def policeCar(police_starX, police_startY, police):
        if police == 0:
             policeCar = pygame.image.load('images/car2.png')
        if police == 1:
             policeCar = pygame.image.load('images/car3.png')     
        if police == 2:
             policeCar = pygame.image.load('images/car1.png')
        screen.blit(policeCar,(police_starX,police_startY))

def car(x,y):
    screen.blit(carImg, (x,y))

def loop():
    x,y= 400,540
    xchange = 0
    carWidth = 23
    carHeight= 47
    
    police_startY= -600
    police_startX = random.randrange(130, 700-carWidth)
    police =random.randrange(0, 2)
    policeCarSpeed = 5
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xchange = -5
                if event.key == pygame.K_RIGHT:
                    xchange = 5
            if event.type == pygame.KEYUP:
                xchange = 0
        x += xchange
        screen.fill(colors['grey'])
        background()
        policeCar(police_startX,police_startY,police)
        police_startY+=policeCarSpeed
        if police_startY > 600:
            police_startY = -600
            police_startX = random.randrange(130, 700-carWidth)
            police = random.randrange(0,2)
        if x < 130 or x> 700-carWidth:
            displayMessage('Car Crashed') 
        if y < police_startY-carHeight:
           if x > police_startX and x < police_startX+carWidth or x+carWidth >police_startX and x+carWidth<police_startX+carWidth:
            displayMessage('Car Crashed')  
        car(x,y)
        pygame.display.update()
loop()