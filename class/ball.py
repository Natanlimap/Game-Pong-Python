class Ball:
    x = 200
    y = 180 
    velocity = 1
    vel_x = 1
    vel_y = 1.0
        
    def acelerateVelX(self):
        self.velocity = self.velocity*1.015

    def changeYVel(self):
        if self.vel_y < 0:
            self.vel_y = + self.velocity
            return
        self.vel_y = -self.velocity

    def changeXVel(self):
        if self.vel_x < 0:
            self.vel_x = + self.velocity
            return
        self.vel_x = -self.velocity

    def hittedRect(self, rect):
        if 30< self.x < 60:
            if rect.y <= self.y <= rect.y + rect.y_size:
                self.changeXVel()
                return True
        else:
            return
    def ChangeVelIfAxisHittedWall(self):
        if self.x > 1080:
            self.acelerateVelX()
            self.acelerateVelX()
            self.changeXVel()
        
        if self.y > 720 or self.y < 0:
            self.changeYVel()

    def increment(self):
        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y
