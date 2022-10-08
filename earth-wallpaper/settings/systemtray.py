from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QSystemTrayIcon, QMenu, QAction
import sys


class SystemTray(QSystemTrayIcon):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("resource/earth-wallpaper.png"))
        self.save = QAction("保存当前壁纸")
        self.update = QAction("更新壁纸")
        self.config = QAction("设置")
        self.about = QAction("关于")
        self.exit = QAction("退出")
        self.menu = QMenu()
        self.menu.addAction(self.save)
        self.menu.addAction(self.update)
        self.menu.addAction(self.config)
        self.menu.addAction(self.about)
        self.menu.addAction(self.exit)
        self.setContextMenu(self.menu)
        self.show()
        self.__connect__()

    def __connect__(self):
        self.exit.triggered.connect(sys.exit)
