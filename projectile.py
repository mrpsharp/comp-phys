import turtle

ball = turtle.Turtle()
wn = turtle.Screen()
ball.hideturtle()
vx=10
vy=40
x=0
y=0
dt=0.1
ax=0
ay=-9.81

while(1):
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    ball.goto(x, y)
    ball.dot(3)
    if(y<0):
        vy = -0.8*vy
wn.mainloop()             # Wait for user to close window
