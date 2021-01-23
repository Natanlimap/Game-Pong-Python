class Rectangle:
    x = 0
    y = 280
    vel_y = 0
    velocity = 1
    y_size = 170    

    def acelerate(self):
        self.velocity = self.velocity*1.000015
    def resetVel(self):
        self.vel_y = 0

    def increment(self):
        if(self.y < 0):
            self.resetVel()
            self.y = 0
        elif(self.y + self.y_size > 720):
            self.resetVel()
            self.y = 720 - self.y_size
        else:
            self.y = self.y + self.vel_y
    def moveDown(self):
        self.vel_y = self.velocity

    def moveUp(self):
        self.vel_y = -self.velocity
