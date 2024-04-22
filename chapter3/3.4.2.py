# coding=utf-8
# 代码文件：chapter3/3.4.2.py
# 鼠标事件

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.move(600, 300)
        self.setWindowTitle('鼠标事件')
        self.label = QLabel(self)
        self.label.setText('Hello World!')
        self.label.move(180, 120)

    #  重写鼠标按下函数
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText('鼠标左键按下')
        elif event.button() == Qt.RightButton:
            self.label.setText('鼠标右键按下')
        else:
            self.label.setText('鼠标未知按下')

    #  重写鼠标释放函数
    def mouseReleaseEvent(self, event):
        self.label.setText('鼠标释放')


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
