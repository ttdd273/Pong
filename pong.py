# Simple pong game

import turtle

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width = 750, height = 600)
# Stops the window from updating, speeds up the game
window.tracer(0)

# Paddle Right
paddle_r = turtle.Turtle()
# Animation speed, draw it instantly
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_r.color("white")
paddle_r.penup()
# Initalize
paddle_r.goto(-350, 0)

# Paddle Left
paddle_l = turtle.Turtle()
paddle_l = turtle.Turtle()
# Animation speed, draw it instantly
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_l.color("white")
paddle_l.penup()
# Initalize
paddle_l.goto(330, 0)

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

# Main game loop
while True:
    window.update()
