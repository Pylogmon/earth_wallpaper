#!/bin/python3
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QSharedMemory
from earth_wallpaper.systemtray import SystemTray
import sys


def main():
    app = QApplication()

    QApplication.setQuitOnLastWindowClosed(False)

    lock = QSharedMemory("earth-wallpaper-PySide6")
    if lock.attach():
        message = QMessageBox()
        QMessageBox.information(message, "警告", "程序已经运行", QMessageBox.Yes)
        sys.exit(0)
    lock.create(10)

    tray = SystemTray()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
