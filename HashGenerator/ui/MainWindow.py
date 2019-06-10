#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
XulDebugTool

主页面

author: Kenshin
last edited: 2019.06.10
"""

import os
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtCore import Qt, pyqtSlot

from HashGenerator.ui.BaseWindow import BaseWindow
from HashGenerator.ui.widgets.ClickableLineEdit import ClickableLineEdit


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.dir = ""
        self.fileName = ""
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setFixedSize(460, 160)

        self.targetDir = QLabel(self)
        self.targetDir.setText("Target Dir:")
        self.targetDir.move(20, 28)

        self.targetDirLineEdit = ClickableLineEdit(self)
        self.targetDirLineEdit.resize(260, 28)
        self.targetDirLineEdit.move(130, 28)
        self.targetDirLineEdit.setReadOnly(True)
        self.targetDirLineEdit.clicked.connect(self.onTargetClicked)

        self.outputExcel = QLabel(self)
        self.outputExcel.setText("Output Excel:")
        self.outputExcel.move(20, 68)

        self.outputExcelLineEdit = ClickableLineEdit(self)
        self.outputExcelLineEdit.resize(260, 28)
        self.outputExcelLineEdit.move(130, 68)
        self.outputExcelLineEdit.setReadOnly(True)
        self.outputExcelLineEdit.clicked.connect(self.onOutputClicked)

        self.generatorButton = QPushButton(self)
        self.generatorButton.setText("Generator")
        self.generatorButton.move(180, 110)
        self.generatorButton.resize(100, 28)
        self.generatorButton.setEnabled(False)
        self.generatorButton.clicked.connect(self.onGeneratorClicked)

        # self.initMenuBar()
        # self.initLayout()
        super().initWindow()

    @pyqtSlot()
    def onTargetClicked(self):
        self.dir = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if self.dir != "":
            self.targetDirLineEdit.setText(self.dir)
        if self.dir != "" and self.fileName != "":
            self.generatorButton.setEnabled(True)

    @pyqtSlot()
    def onOutputClicked(self):
        self.fileName, self.fileType = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          os.getcwd(),
                                                          "Excel File (*.xlsx)")
        if self.fileName != "":
            self.outputExcelLineEdit.setText(self.fileName)
        if self.dir != "" and self.fileName != "":
            self.generatorButton.setEnabled(True)

    @pyqtSlot()
    def onGeneratorClicked(self):
        self.dir = self.targetDirLineEdit.text()
        self.fileName = self.outputExcelLineEdit.text()
        pass

