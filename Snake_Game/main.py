from turtle import Screen,Turtle
import time
screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snek')
screen.tracer(0)


starting_position=[(0,0),(-20,0),(-40,0)]
GameLoop=True;

Body=[]
Head= Turtle()
Head.shape("square")
Head.color("white")

for pos in starting_position:
    segment= Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    segment.setpos(pos)
    Body.append(segment)

screen.update()

while GameLoop:
    screen.update()
    time.sleep(0.11)


    #for seg in Body:
    #   seg.forward(20)




















screen.exitonclick()