# coding = utf-8
# 代码文件：chapter2/2.1.3.py
# 改变画笔

import turtle
import time

pen = turtle.Turtle()
pen.speed(0)
pen.ht()

pen.circle(80)
pen.penup()
pen.goto(100, 200)
time.sleep(2)

pen.pendown()

pen.pencolor('yellow')
pen.pensize(3)
pen.ht()

pen.circle(100, 80)

turtle.done()