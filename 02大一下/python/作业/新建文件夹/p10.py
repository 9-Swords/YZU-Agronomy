# 太阳花
import turtle
turtle.tracer(False)
turtle.color("red", "yellow")  # 同时设置pencolor和fillcolor
turtle.begin_fill()
for i in range(50):
    turtle.forward(400)
    turtle.left(170)
turtle.end_fill()
 

