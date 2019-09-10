import pygame, os, random, time
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 500
WINDOWHEIGHT = 400

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Moving Character')

BLACK = (0,0,0)
WHITE = (255, 255, 255)

moveLeft = False
moveRight = False
spaceBar = False

RightMotion = [pygame.image.load('RM1.png').convert_alpha(), pygame.image.load('RM2.png').convert_alpha(),pygame.image.load('RM3.png').convert_alpha(),pygame.image.load('RM4.png').convert_alpha(),pygame.image.load('RM5.png').convert_alpha()]
LeftMotion = [pygame.image.load('LM1.png').convert_alpha(), pygame.image.load('LM2.png').convert_alpha(),pygame.image.load('LM3.png').convert_alpha(),pygame.image.load('LM4.png').convert_alpha(),pygame.image.load('LM5.png').convert_alpha()]

MOVESPEED = 3

FRAMERATE = 45

walknums = 0

x = 210
y = 317

left = False

def DrawMovements():
    global walknums
    windowSurface.fill(BLACK)

    if walknums + 1 >= 15:
        walknums = 0

    if moveLeft:
        windowSurface.blit(LeftMotion[walknums//3], (x,y))
        walknums += 1
        
    elif moveRight:
        windowSurface.blit(RightMotion[walknums//3], (x,y))
        walknums += 1

    else:
        if left:
            windowSurface.blit(LeftMotion[0], (x,y))
        else:
            windowSurface.blit(RightMotion[0], (x,y))

    pygame.display.update()


class bullets():
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = image
            
    def display(self, windowSurface):
        windowSurface.blit(self.image, (self.x, self.y))

        pygame.display.update()


NStar = pygame.image.load('NStar.png')
wspeed = 5 #weapon speed

weapons = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)
        elif event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                spaceBar = False
                moveLeft = True
            elif event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                spaceBar = False
                moveRight = True
            elif event.key == K_SPACE:
                moveLeft = False
                moveRight = False
                spaceBar = True
            
                
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                os._exit(1)
                
            elif event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            elif event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            elif event.key == K_SPACE:
                spaceBar = False

    if moveRight and x+RightMotion[0].get_width() < WINDOWWIDTH:
        left = False
        x += MOVESPEED
    elif moveLeft and x > 0:
        left = True
        x -= MOVESPEED
    else:
        moveLeft = False
        moveRight = False
        walknums = 0

    if spaceBar:
        weapons.append(bullets(round(x+(RightMotion[0].get_width()//2)-15), round(y-RightMotion[0].get_height()//2), NStar))

        
    for weapon in weapons:
        if weapon.y > 0 and weapon.y < WINDOWHEIGHT:
            weapon.y -= wspeed
        else:
            weapons.remove(weapon)

    for weapon in weapons:
        weapon.display(windowSurface)

    DrawMovements()
    
    mainClock.tick(FRAMERATE)
