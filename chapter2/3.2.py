# coding = utf-8
# 代码文件：chapter2/3.2.py
# 奥运五环

import turtle
import time

pen = turtle.Turtle()

pen.width(5)
pen.circle(60)

pen.penup()
pen.forward(140)
pen.pendown()
pen.color('red')  # 绘制红色的五环
pen.circle(60)

pen.penup()
pen.forward(140)
pen.pendown()
pen.color('yellow')  # 绘制黄色的五环
pen.circle(60)
pen.circle(60)

pen.penup()
pen.goto(210, -50)
pen.pendown()
pen.color('blue')  # 绘制蓝色的五环
pen.circle(60)

pen.penup()
pen.goto(60, -50)
pen.pendown()
pen.color('green')  # 绘制绿色的五环
pen.circle(60)

turtle.done()
