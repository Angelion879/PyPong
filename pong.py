# Simple Python Pong
import turtle

# Screen creation and definition
wind = turtle.Screen()
wind.title("Pong Game by @Angelion879")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Objects in the screen:

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0) #Animation speed, not movement speed
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.color("white")
left_paddle.penup()
left_paddle.goto(-360,0) 
# Right Paddle
right_padle = turtle.Turtle()
right_padle.speed(0) #Animation speed, not movement speed
right_padle.shape("square")
right_padle.shapesize(stretch_wid=5, stretch_len=1)
right_padle.color("white")
right_padle.penup()
right_padle.goto(360,0)
# Ball
ball = turtle.Turtle()
ball.speed(0) #Animation speed, not movement speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

# Main game loop
while True:
    wind.update()