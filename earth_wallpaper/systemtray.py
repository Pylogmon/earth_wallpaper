from PySide6.QtCore import QStandardPaths, QTimer, QSettings, QDir, QFile
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QMessageBox
from earth_wallpaper.utils.platformInfo import PlatformInfo
from earth_wallpaper.config import Config
from earth_wallpaper.thread import Thread
from PySide6.QtGui import QIcon, QAction
from earth_wallpaper.about import About
import logging
import sys
import os

logger = logging.getLogger(__name__)


class SystemTray(QSystemTrayIcon):

    def __init__(self):
        super(SystemTray, self).__init__()
        self.threads = []
        self.config_page = None
        self.about_page = None
        self.config_path = PlatformInfo.config_path()
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
        self.timer = QTimer()
        self._connect_()
        self.check_config()

    def _connect_(self):
        self.exit.triggered.connect(sys.exit)
        self.about.triggered.connect(self.show_about)
        self.config.triggered.connect(self.show_config)
        self.timer.timeout.connect(self.start_timer)
        self.update.triggered.connect(self.start_timer)
        self.save.triggered.connect(self.save_current_img)

    def show_about(self):
        self.about_page = About()

    def show_config(self):
        self.config_page = Config()
        self.config_page.configChanged.connect(self.start_timer)

    def check_config(self):
        if not os.path.exists(self.config_path):
            logger.info("首次运行，打开设置页面")
            self.config_page = Config()
            self.config_page.configChanged.connect(self.start_timer)
        else:
            self.start_timer()

    def start_timer(self):
        settings = QSettings(self.config_path, QSettings.IniFormat)

        for t in self.threads:
            t.stop()
            if t.isFinished():
                t.deleteLater()
                self.threads.remove(t)

        self.threads.append(Thread(settings.value("APP/wallpaperSource")))
        self.threads[-1].start()
        self.timer.start(60000 * int(settings.value("APP/updateTime")))

    @staticmethod
    def save_current_img():
        img_dir = PlatformInfo.download_dir()

        dir_ = QDir(img_dir)
        name_filters = ["[1-9]*"]
        dir_.setNameFilters(name_filters)
        files = dir_.entryList(sort=QDir.Name)
        picture_dir = QStandardPaths.writableLocation(QStandardPaths.PicturesLocation) + "/earth-wallpaper"
        if not QDir(picture_dir).exists():
            QDir(picture_dir).mkpath(picture_dir)
        source = QFile(os.path.join(img_dir, files[-1]))

        target = QFile(os.path.join(picture_dir, files[-1]))
        message = QMessageBox()
        if not target.exists():
            if source.copy(target.fileName()):
                logger.info(f"保存{os.path.join(img_dir, files[-1])}到{os.path.join(picture_dir, files[-1])}")
                QMessageBox.information(message, "保存", "保存成功，已保存到用户Picture目录", QMessageBox.Yes)
            else:
                logger.warning("保存失败，原因未知")
                QMessageBox.warning(message, "保存", "保存失败，原因未知（懒）", QMessageBox.Yes)

        else:
            logger.info("当前壁纸已存在")
            QMessageBox.information(message, "保存", "当前壁纸已存在，未做任何处理", QMessageBox.Yes)
