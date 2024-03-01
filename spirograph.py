import turtle
import math

class Spiro:
    def __init__(self, x_pos, y_pos, col, R, r, l) -> None:
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.step = 5
        self.complete = False
        self.setparam(x_pos, y_pos, col, R, r, l)
        self.restart()
        #setter
    def setparam(self, x_pos, y_pos, col, R, r, l):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.col = col
        self.R = int(R)
        self.r = int(r)
        self.l = l
        gcd = gcd(self.r, self.R)
        self.n_rotation = r//gcd #// floor divisior
        self.k = r/float(R)
        self.t.color(*col)
        self.theta = 0

    def restart(self):
        self.complete = False
        self.t.showturtle()
        #go to first point
        self.t.up()
        R,k,l = self.R, self.k, self.l
        theta=0
        x = R*((1-k)*math.cos(theta)+l*k*math.cos((1-k)*theta/k))
        y = R*((1-k)*math.sin(theta)+l*k*math.sin((1-k)*theta/k))
        self.t.setpos(self.x_pos, +x, self.y_pos+y)
        self.t.down()

    def draw(self):
        R,k,l = self.R, self.k, self.l
    


