# coding = utf-8
# 代码文件：chapter2/2.1.3.py
# 设置画笔

import turtle

pen = turtle.Turtle()

pen.speed(9)

pen.hideturtle()
pen.penup()

pen.pencolor('red')
pen.fillcolor('red')

pen.goto(-100, 150)
pen.begin_fill()

for i in range(5):
    pen.pendown()
    pen.fd(200)
    pen.right(144)

pen.end_fill()

turtle.done()