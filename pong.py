# Simple Python Pong
import turtle

# Screen creation and definition
wind = turtle.Screen()
wind.title("Pong Game by @Angelion879")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Main game loop
while True:
    wind.update()