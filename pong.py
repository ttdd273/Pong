# Simple pong game

import turtle

# Score
score_a = 0
score_b = 0


window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width = 800, height = 600)
# Stops the window from updating, speeds up the game
window.tracer(0)

# Paddle Left
paddle_r = turtle.Turtle()
# Animation speed, draw it instantly
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_r.color("white")
paddle_r.penup()
# Initalize
paddle_r.goto(-350, 0)

# Paddle Right
paddle_l = turtle.Turtle()
paddle_l = turtle.Turtle()
# Animation speed, draw it instantly
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_l.color("white")
paddle_l.penup()
# Initalize
paddle_l.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball = turtle.Turtle()
# Animation speed, draw it instantly
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
# Initalize
ball.goto(0, 0)
# Ball movement
ball.dx = 0.25
ball.dy = 0.25

# CoolDown in seconds
cooldown = 0.2

# Functions
def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)

def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

# Keyboard binding
window.listen()
if cooldown <= 0.2:
    window.onkeypress(paddle_r_up, 'w')
    window.onkeypress(paddle_r_down, 's')
    window.onkeypress(paddle_l_up, 'Up')
    window.onkeypress(paddle_l_down, 'Down')

def writeScore(score_a, score_b):
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align= 'center', font= ('Courier', 24, 'normal'))

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
writeScore(score_a, score_b)

# Main game loop
while True:
    window.update()
    if cooldown > 0.2:
        cooldown -= 0.2
    # Move the Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    # Border check
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1
    # Player left wins
    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        writeScore(score_a, score_b)

    # Player right wins
    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        writeScore(score_a, score_b)

    # Collision, we want the ball to be in the y coordinates of the paddle_l
    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_l.ycor()+40 and ball.ycor()\
    > paddle_l.ycor()-40:
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_r.ycor()+40 and ball.ycor()\
    > paddle_r.ycor()-40:
        ball.setx(-340)
        ball.dx *= -1
