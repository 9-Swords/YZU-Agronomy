#窗花
from turtle import *
pensize(10)
speed(8)

#自定义画圆弧函数
def arc(initial_degree,range_num,step,rotate_degree):
    setheading(initial_degree)
    for n in range(range_num):
        forward(step)
        right(rotate_degree)

#绘制窗花
for i in range(9):
    pu()
    home()
    pd()
    pencolor("red")
    arc(40*i,100,3,3)
