#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
HashGenerator

窗口基类, 设置窗口图标, 标题, 居中等属性

author: Kenshin
last edited: 2019.06.10
"""

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from HashGenerator.utils.IconTool import IconTool


class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'HashGenerator'

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(IconTool.buildQIcon('icon.png'))
        self.center()

    # 设置窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
