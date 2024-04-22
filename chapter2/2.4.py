# coding = utf-8
# 代码文件：chapter2/2.1.3.py
# 好漂亮的一棵树

import turtle

def y(sz, level):
    """定义y函数，sz表示树的尺寸，level表示树的层次级别"""
    if level > 0:
        #  按照树的层次级别设置树的颜色
        pen.pencolor(0, 255 // level, 0)  # //整数除法取比结果大的最接近的整数
        pen.fd(sz)
        pen.rt(angle)

        #  递归调用y函数，绘制右边的子树
        y(0.8 * sz, level - 1)
        pen.pencolor(0, 255 // level, 0)  # //整数除法取比结果大的最接近的整数
        pen.left(2 * angle)

        #  递归调用y函数，绘制左边的子树
        y(0.8 * sz, level - 1)
        pen.pencolor(0, 255 // level, 0)  # //整数除法取比结果大的最接近的整数
        pen.right(angle)
        pen.forward(-sz)


if __name__ == '__main__':
    pen = turtle.Turtle()

    #  设置绘图速度
    pen.speed('fastest')

    #  设置颜色模式为255，即颜色范围是0-255
    turtle.colormode(255)

    #  设置画笔朝向
    pen.right(-90)

    # 设置树杈的角度
    angle = 30

    #  创建尺寸为80且层次级别为7的树
    y(80, 7)

    turtle.done()  # 结束绘图
