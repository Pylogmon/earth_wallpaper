from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from .about import About
import sys
import os


class SystemTray(QSystemTrayIcon):

    def __init__(self):
        super(SystemTray, self).__init__()
        self.path = os.path.split(os.path.realpath(__file__))[0]
        self.setIcon(QIcon(os.path.join(self.path, "../resource/earth-wallpaper.png")))
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
        self._connect_()

    def _connect_(self):
        self.exit.triggered.connect(sys.exit)
        self.about.triggered.connect(self.show_about)

    def show_about(self):
        self.about_page = About()
