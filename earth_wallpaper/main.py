#!/bin/python3
import sys, os
# 添加path路径，否则有可能会找不到模块
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from PySide6.QtWidgets import QApplication, QMessageBox
from earth_wallpaper.systemtray import SystemTray
from PySide6.QtCore import QSharedMemory

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
