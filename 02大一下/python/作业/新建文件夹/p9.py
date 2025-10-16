# 鹦鹉螺
from turtle import *
speed(5)
bgcolor("white")  
pencolor("black")
h = 10
for j in  range(360):
    for i in range(4):
        forward(h)
        right(90)

    right(3)
    h = h*1.01

