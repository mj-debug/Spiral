# program to draw a spiral ring

from turtle import *
from math import *
pensize(10)
pencolor("blue")
penup()
radius = 10
goto(radius,0)
pendown()
for i in range(1, 350):
    newangle = 2 * i * pi/100
    goto( radius * cos(newangle), radius * sin(newangle))
    radius = radius + 1
