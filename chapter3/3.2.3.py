# coding=utf-8
# 代码文件： chapter3/3.2.3.py
# 编写你的第一个PyQt GUI程序

import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)    # 创建应用程序对象

window = QWidget()
window.resize(400, 300)
window.move(600, 300)

window.setWindowTitle('你好Qt!')  # 设置窗口的标题
window.show()   # 显示窗口

sys.exit(app.exec_())