# Simple Python Pong
import turtle

# Screen creation and definition
wind = turtle.Screen()
wind.title("Pong Game by @Angelion879")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Objects in the screen:
class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__(shape = 'square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(position)
class Ball(turtle.Turtle):
    def __init__(self, position):
        super().__init__(shape='square')
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(position)

left_paddle = Paddle((-360,0))
right_paddle = Paddle((360,0))
ball = Ball((0,0))

# Functions

# Main game loop
while True:
    wind.update()