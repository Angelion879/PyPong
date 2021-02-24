# Simple Python Pong
import turtle

# Screen creation and definition
wind = turtle.Screen()
wind.title("Pong Game by @Angelion879")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Menu
menu = turtle.Turtle()
menu.speed(0)
menu.color("white")
menu.penup()
menu.hideturtle()
menu.goto(0,15)
menu.write("PRESS SPACE TO START", align="center", font=("Courier", 35, "normal"))

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
        self.dx = 0.2
        self.dy = 0.2

left_paddle = Paddle((-360,0))
right_paddle = Paddle((360,0))
ball = Ball((0,0))
start = False

# Point Writing
score_left = 0
score_right = 0
points = turtle.Turtle()
points.speed(0)
points.color("white")
points.penup()
points.hideturtle()
points.goto(0,260)
points.write(f"Player A: {score_left}\t\t\tPlayer B: {score_right}", align="center", font=("Courier", 20, "normal"))

# Functions
def start_game():
    global start
    start = True
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
wind.onkeypress(start_game, 'space')


# Main game loop
while True:
    wind.update()

    # Ball moving
    if start:
        menu.clear()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

    # Border colision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *=-1
    elif ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_left += 1
        points.clear()
        points.write(f"Player A: {score_left}\t\t\tPlayer B: {score_right}", align="center", font=("Courier", 20, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_right +=1
        points.clear()
        points.write(f"Player A: {score_left}\t\t\tPlayer B: {score_right}", align="center", font=("Courier", 20, "normal"))

    # Paddle colision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (right_paddle.ycor() +50) and ball.ycor() > (right_paddle.ycor() -50)):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < (left_paddle.ycor() +50) and ball.ycor() > (left_paddle.ycor() -50)):
        ball.setx(-340)
        ball.dx *= -1

    # Winning condition
    if (score_left >= 3) or (score_right >= 3):
        start = False
        if score_left > score_right:
            menu.write(f"PLAYER A WINS", align="center", font=("Courier", 35, "normal"))
        else:
            menu.write(f"PLAYER B WINS", align="center", font=("Courier", 35, "normal"))