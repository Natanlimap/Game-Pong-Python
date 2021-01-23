import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)
RADIUS = 30

class Rectangle:
    x = 0
    y = 180
    vel_y = 0
    velocity = 1
    y_size = 170    

    def resetVel(self):
        self.vel_y = 0

    def increment(self):
        self.y = self.y + self.vel_y

    def moveDown(self):
        self.vel_y = self.velocity

    def moveUp(self):
        self.vel_y = -self.velocity

class Ball:
    x = 200
    y = 180 
    velocity = 1
    vel_x = 1
    vel_y = 1.0
    
    def changeYVel(self):
        if self.vel_y == -1:
            self.vel_y = + self.velocity
            return
        self.vel_y = -self.velocity

    def changeXVel(self):
        if self.vel_x == -1:
            self.vel_x = + self.velocity
            return
        self.vel_x = -self.velocity

    def hittedRect(self, rect  ):
        if self.x < 60:
            if rect.y - rect.y_size  <= self.y <= rect.y + rect.y_size:
                self.changeXVel()
        else:
            return
    def ChangeVelIfAxisHittedWall(self):
        if self.x > 1080:
            self.changeXVel()
        
        if self.y > 720 or self.y == 0:
            self.changeYVel()

    def increment(self):
        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y


pygame.init() 
gameScreen = pygame.display.set_mode((1080, 720), 0)

ball = Ball()
rectangle = Rectangle()
while ball.x >= 0:


    #Regas
    ball.increment()
    rectangle.increment()
    ball.ChangeVelIfAxisHittedWall()
    ball.hittedRect(rectangle)
    #Pinta  
    gameScreen.fill(BLACK)
    pygame.draw.circle(gameScreen, WHITE, (5 + (int(ball.x)), 5 + int(ball.y)), RADIUS, 0)
    pygame.draw.rect(gameScreen, WHITE, pygame.Rect(30, int(rectangle.y), 20, 150))

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
          
