# Simple Python Pong
import turtle
import time

# Screen creation and definition
wind = turtle.Screen()
wind.title("Pong Game by @Angelion879")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Objects in the screen:


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__(shape='square')
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
        self.dx = 0.3
        self.dy = 0.3


class Text(turtle.Turtle):
    def __init__(self, position, message, l_size):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(message, align="center", font=("Courier", l_size, "normal"))


class SelectionArrow(turtle.Turtle):
    def __init__(self, position, direction):
        super().__init__(shape='arrow')
        self.speed(0)
        self.color('white')
        self.penup()
        self.goto(position)
        self.left(direction)


class Option(turtle.Turtle):
    def __init__(self, position, message):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(message, align="center", font=("Courier", 20, "normal"))


menu = Text((0, 20), "PRESS SPACE TO START", 35)
exit_message = Text((0, -290), "PRESS ESC TO EXIT", 10)
left_paddle = Paddle((-360, 0))
right_paddle = Paddle((360, 0))
ball = Ball((0, 0))
start = False

# AI Starter
single = Option((-150, -50), "SINGLEPLAYER")
multi = Option((150, -50), "MULTIPLAYER")
right_arrow = SelectionArrow((-35, -35), 180)
left_arrow = SelectionArrow((-265, -35), 0)
pc_play = False

# Point Writing
score_left = 0
score_right = 0
points = Text(
    (0, 260), f"A: {score_left}\t\t\t\t\tB: {score_right}", 20)

# Functions


def start_game():
    global start
    start = True


def exit_game():
    turtle.bye()


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


def ai_paddle_down():
    y = left_paddle.ycor()
    y -= 10
    left_paddle.sety(y)


def ai_paddle_up():
    y = left_paddle.ycor()
    y += 10
    left_paddle.sety(y)


def selection_move_right():
    rx = 255
    lx = 40
    right_arrow.setx(rx)
    left_arrow.setx(lx)


def selection_move_left():
    rx = -35
    lx = -265
    right_arrow.setx(rx)
    left_arrow.setx(lx)


def game_mode():
    if right_arrow.xcor() < 0:
        global pc_play
        pc_play = True
    else:
        pc_play = False


# Key binding
wind.listen()
wind.onkeypress(left_paddle_up, 'w')
wind.onkeypress(right_paddle_up, 'Up')
wind.onkeypress(left_paddle_down, 's')
wind.onkeypress(right_paddle_down, 'Down')
wind.onkeypress(start_game, 'space')
wind.onkeypress(exit_game, 'Escape')
wind.onkeypress(selection_move_right, 'Right')
wind.onkeypress(selection_move_left, 'Left')


# Main game loop
while True:
    wind.update()
    game_mode()

    # Ball moving
    if start:
        menu.clear()
        single.clear()
        multi.clear()
        right_arrow.hideturtle()
        left_arrow.hideturtle()
        wind.onkeypress(None, 'Right')
        wind.onkeypress(None, 'Left')
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

    # Border colision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        points.clear()
        points.write(f"A: {score_left}\t\t\t\t\tB: {score_right}",
                     align="center", font=("Courier", 20, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        points.clear()
        points.write(f"A: {score_left}\t\t\t\t\tB: {score_right}",
                     align="center", font=("Courier", 20, "normal"))

    # Paddle colision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (right_paddle.ycor() + 50) and ball.ycor() > (right_paddle.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < (left_paddle.ycor() + 50) and ball.ycor() > (left_paddle.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1

    # AI Player
    if pc_play == True:
        if ball.xcor() < 0 and left_paddle.ycor() < ball.ycor() and abs(left_paddle.ycor() - ball.ycor()) > 20:
            ai_paddle_up()
        elif ball.xcor() < 0 and left_paddle.ycor() > ball.ycor() and abs(left_paddle.ycor() - ball.ycor()) > 20:
            ai_paddle_down()

    # Winning condition
    if (score_left >= 5) or (score_right >= 5):
        start = False
        if score_left > score_right:
            menu.write(f"PLAYER A WINS", align="center",
                       font=("Courier", 35, "normal"))
        else:
            menu.write(f"PLAYER B WINS", align="center",
                       font=("Courier", 35, "normal"))
