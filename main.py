import time
from turtle import *
from random import random

def circle(obj):
    obj.speed(800)
    for i in range(120):
        obj.pencolor(random(),random(),random())
        obj.left(3)
        obj.circle(200)

timmy = Turtle()
time.sleep(2)
timmy.shape("turtle")
circle(timmy)

screen = Screen()
screen.exitonclick()
