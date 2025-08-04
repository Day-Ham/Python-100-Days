# Import the turtle library for 
# drawing the required curve
from turtle import Turtle,Screen
screen = Screen()
pencil= Turtle()
def move_forward():
    pencil.forward(10)
def move_back():
    pencil.backward(10)
def rotate_clockwise():
    pencil.setheading( pencil.heading() + 10) 
def rotate_counter_clockwise():
    pencil.setheading( pencil.heading() - 10) 


screen.listen()
screen.onkeypress(move_forward,'w')
screen.onkeypress(move_back,'s')
screen.onkeypress(rotate_clockwise,'a')
screen.onkeypress(rotate_counter_clockwise,'d')

screen.title('Sketch Down')
screen.exitonclick()