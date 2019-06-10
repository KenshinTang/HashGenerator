from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLineEdit


class ClickableLineEdit(QLineEdit):
    clicked = pyqtSignal() # signal when the text entry is left clicked

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: self.clicked.emit()
        else: super().mousePressEvent(event)

