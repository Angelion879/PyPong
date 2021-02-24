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
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Key binding
wind.listen()
wind.onkeypress(left_paddle_up, 'w')
wind.onkeypress(right_paddle_up, 'Up')
wind.onkeypress(left_paddle_down, 's')
wind.onkeypress(right_paddle_down, 'Down')


# Main game loop
while True:
    wind.update()