#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from main import MainWindow


if __name__ == '__main__':

    # HiDPI Support
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

    # Create application and initialize
    app = QApplication(sys.argv)
    window = MainWindow()

    # Running
    window.show()
    sys.exit(app.exec_())
