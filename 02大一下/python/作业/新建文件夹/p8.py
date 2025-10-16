# 五角星
import turtle
turtle.screensize(400,400,'red')

turtle.penup()
turtle.goto(-100,100)
turtle.pendown()

turtle.pencolor(1,0.84,0)
turtle.fillcolor(1,0.84,0)
 
turtle.begin_fill()
for i in range(5):
  turtle.forward(200)
  turtle.right(144)
turtle.end_fill()

