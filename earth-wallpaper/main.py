#!/bin/python3
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QSharedMemory
from settings.systemtray import SystemTray
import sys

if __name__ == "__main__":
    app = QApplication()

    QApplication.setQuitOnLastWindowClosed(False)

    lock = QSharedMemory("earth-wallpaper-PySide2")
    if lock.attach():
        message = QMessageBox()
        QMessageBox.information(message, "警告", "程序已经运行", QMessageBox.Yes)
        sys.exit(0)
    lock.create(10)

    tray = SystemTray()
    sys.exit(app.exec_())
