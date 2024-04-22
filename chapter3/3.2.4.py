# coding=utf-8
# 代码文件： chapter3/3.2.3.py
# 编写你的第一个PyQt GUI程序

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.move(600, 300)

        self.setWindowTitle('你好Qt!')


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
