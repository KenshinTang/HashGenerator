#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
XulDebugTool

主页面

author: Kenshin
last edited: 2019.06.10
"""
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from HashGenerator.ui.BaseWindow import BaseWindow


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setFixedSize(460, 150)

        # self.initMenuBar()
        # self.initLayout()
        super().initWindow()

