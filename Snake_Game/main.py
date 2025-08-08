# Import the turtle library for 
# drawing the required curve
from turtle import Turtle,Screen
import time
screen = Screen()
Head= Turtle()
GameLoop=True


def move_forward():
    Head.setheading( 90) 
def move_back():
    Head.setheading(-90) 
def rotate_clockwise():
    Head.setheading(180) 
    print(Head.heading)
def rotate_counter_clockwise():
    Head.setheading(0) 
    print(Head.heading)

screen.listen()
screen.onkeypress(move_forward,'w')
screen.onkeypress(move_back,'s')
screen.onkeypress(rotate_clockwise,'a')
screen.onkeypress(rotate_counter_clockwise,'d')
while GameLoop:
    
    screen.listen() 
    screen.update()
    time.sleep(0.11)
    Head.forward(20)

screen.title('Sketch Down')
screen.exitonclick()