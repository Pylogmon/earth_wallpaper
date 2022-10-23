from PySide6.QtCore import QStandardPaths, QTimer, QSettings
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from about import About
from config import Config
from thread import Thread
import sys
import os


class SystemTray(QSystemTrayIcon):

    def __init__(self):
        super(SystemTray, self).__init__()
        self.config_path = os.path.join(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation),
                                        "earth-wallpaper/config")
        self.path = os.path.split(os.path.realpath(__file__))[0]
        self.setIcon(QIcon(os.path.join(self.path, "resource/earth-wallpaper.png")))
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
        self.timer = QTimer()
        self._connect_()
        self.check_config()

    def _connect_(self):
        self.exit.triggered.connect(sys.exit)
        self.about.triggered.connect(self.show_about)
        self.config.triggered.connect(self.show_config)
        self.timer.timeout.connect(self.start_timer)

    def show_about(self):
        self.about_page = About()

    def show_config(self):
        self.config_page = Config()

    def check_config(self):
        if not os.path.exists(self.config_path):
            print("首次运行，打开设置页面")
            self.config_page = Config()

        else:
            self.start_timer()

    def start_timer(self):
        settings = QSettings(self.config_path, QSettings.IniFormat)
        
        self.thread = Thread(settings.value("APP/earthSource"))
        self.thread.start()

        self.timer.start(60000 * int(settings.value("APP/updateTime")))
