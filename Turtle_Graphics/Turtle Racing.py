from turtle import Turtle,Screen
import random
import time
raphael= Turtle()
donny= Turtle()
leo= Turtle()
michael= Turtle()
finishLine= Turtle()

TMNT=[]
raphael.shape("turtle")
raphael.color("red")
TMNT.append(raphael)
donny.shape("turtle")
donny.color("purple")
TMNT.append(donny)

leo.shape("turtle")
leo.color("blue")
TMNT.append(leo)
michael.shape("turtle")
michael.color("orange")
TMNT.append(michael)

finishLine.shape("square")
finishLine.color("green")
finishLine.shapesize(100,0.001,12)
finishLine.penup()
finishLine.setpos(300, 2*30)
index=0
for turtle in TMNT:
    turtle.penup()
    turtle.setpos(-300, index*30)
    
    turtle.pendown()
    index+=1
GameLoop=True
while GameLoop==True:
    for turtle in TMNT:
        turtle.penup()
        turtleX=turtle.xcor()
        turtleY=turtle.ycor()
        turtle.setpos(turtleX+random.randint(10,20), turtleY)

        if turtleX>=290:
            GameLoop=False
            print("Winner: " + str(turtle.color()))
            break
   


screen = Screen()
screen.title('Kame musume')
screen.exitonclick()