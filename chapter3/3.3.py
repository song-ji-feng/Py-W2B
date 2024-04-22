# coding=utf-8
# 代码文件： chapter3/3.3.py
# 在窗口中添加控件

import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = None
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.move(600, 300)

        self.setWindowTitle('信号与槽机')

        self.label = QLabel(self)
        self.label.setText('Hello World!')
        self.label.move(180, 120)

        button = QPushButton('OK', self)
        button.clicked.connect(self.click_success)  # 连接信号与槽
        button.move(170, 160)

    def click_success(self):
        self.label.setText('世界你好！')
    # def click_success(self):
    #     print('点我啦！！！')
    #     QMessageBox.about(self, '提示', '点我啦啦')


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
