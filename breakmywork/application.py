#!/usr/bin/env python

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QDesktopWidget, QLabel


class BreakMyWork(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('breakmywork')
        self.addLabel()
        self.center()
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(
                self,
                'Message',
                "Are you sure to quit?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def addLabel(self):
        self.label1 = QLabel("Welcome to breakmywork!", self)
        self.label1.setGeometry(0, 0, 250, 150)
        self.label1.setAlignment(Qt.AlignCenter)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    ex = BreakMyWork()
    sys.exit(app.exec_())
