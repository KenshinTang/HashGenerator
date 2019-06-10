#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
HashGenerator

应用入口

author: Kenshin
last edited: 2019.06.10
"""

import sys

from PyQt5.QtWidgets import QApplication

from HashGenerator.ui.MainWindow import MainWindow


class App(object):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
