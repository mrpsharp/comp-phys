import math
from turtle import *
dt = 0.0

class Particle(Turtle):
    """Subclass of Turtle representing a body.

    Extra attributes:
    mass : mass in kg
    ax, ay: x, y accelerations in m/s^2
    vx, vy: x, y velocities in m/s
    px, py: x, y positions in m
    """
    mass = None
    vx = vy = 0
    px = 0.
    py = 0.

    def move(self, dt):
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.px += self.vx * dt
        self.py += self.vy * dt
        if self.py<0:
            self.py = -self.py
            self.vy = -self.vy
        self.goto(self.px*50, self.py*50)
        self.dot(3)

ball = Particle()
ball.hideturtle()
ball.mass = 1
ball.vx = 2
ball.vy = 10
ball.ax = 0
ball.ay = -9.81

ball.getscreen().delay(0)
while(True):
    ball.move(0.05)

ball.getscreen().exitonclick()
