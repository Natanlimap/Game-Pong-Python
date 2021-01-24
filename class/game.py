import pygame
import sys
sys.path.append("class/")

from ball import *
from rectangle import *
COUNT = 0
WHITE = (255,255,255)
BLACK = (0,0,0)
RADIUS = 15

def start():
    global COUNT
    hitted = False
    pygame.init() 
    gameScreen = pygame.display.set_mode((1080, 720), 0)

    ball = Ball()
    rectangle = Rectangle()

    while ball.x >= 0:


        #Regas
        ball.increment()
        rectangle.increment()
        ball.ChangeVelIfAxisHittedWall()
        hitted = ball.hittedRect(rectangle)

        if hitted:
            COUNT = COUNT + 1
            rectangle.acelerate()


        #Pinta  
        gameScreen.fill(BLACK)
        pygame.draw.circle(gameScreen, WHITE, (5 + (int(ball.x)), 5 + int(ball.y)), RADIUS, 0)
        pygame.draw.rect(gameScreen, WHITE, pygame.Rect(30, int(rectangle.y), 20, 150))
        pygame.draw.rect(gameScreen, WHITE, pygame.Rect(540, 0, 20, 720))

        pygame.display.update()

        #Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    rectangle.moveDown()
                elif e.key == pygame.K_UP:
                    rectangle.moveUp() 
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    rectangle.resetVel()
    print(COUNT)