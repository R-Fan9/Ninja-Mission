import pygame, os, time
from pygame. locals import *

pygame.init()

WINDOWWIDTH = 500
WINDOWHEIGHT = 400

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Bouncy Ball')

BLACK = (0,0,0)

plx = 100
ply = 150
yspeed = 0
xspeed = 0.5
gravity = 0.1
 
player = pygame.image.load("player.png")
player.convert_alpha()
playerrect = player.get_rect()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(0)
            
    windowSurface.fill(BLACK)

    plx += xspeed

    if plx+player.get_width() > WINDOWWIDTH:
        xspeed *= -1
    elif plx < 0:
        xspeed *= -1
    
    
    ply += yspeed
    
    yspeed += gravity
    
    if ply+player.get_height() > WINDOWHEIGHT:
        yspeed *= -0.97

    playerrect.x = plx
    playerrect.y = ply

    windowSurface.blit(player, playerrect)
        
    pygame.display.update()
    
    time.sleep(0.02)
