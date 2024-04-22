# coding=utf-8
# 代码文件：chapter3/3.4.2.py
# 键盘事件

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyWindow(QWidget):
    def __init__(self) :
        super().__init__()
        self.label = None
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.move(600, 300)
        self.setWindowTitle('键盘事件')
        self.label = QLabel(self)
        self.label.setText('Hello World!')
        self.label.move(100, 120)

    #  重写键盘按下函数
    def keyPressEvent(self, event):
        self.label.setText('键盘按下')

    #  重写键盘释放函数
    def keyReleaseEvent(self, event):
        self.label.setText('键盘释放')


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
