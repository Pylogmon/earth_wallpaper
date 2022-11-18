from PySide6.QtCore import QStandardPaths, QTimer, QSettings, QSysInfo, QDir, QFile
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QMessageBox
from earth_wallpaper.about import About
from earth_wallpaper.config import Config
from earth_wallpaper.thread import Thread
import sys
import os


class SystemTray(QSystemTrayIcon):

    def __init__(self):
        super(SystemTray, self).__init__()
        self.threads = []
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
        self.update.triggered.connect(self.start_timer)
        self.save.triggered.connect(self.save_current_img)

    def show_about(self):
        self.about_page = About()

    def show_config(self):
        self.config_page = Config()
        self.config_page.configChanged.connect(self.start_timer)

    def check_config(self):
        if not os.path.exists(self.config_path):
            print("首次运行，打开设置页面")
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

        self.threads.append(Thread(settings.value("APP/earthSource")))
        self.threads[-1].start()
        self.timer.start(60000 * int(settings.value("APP/updateTime")))

    def save_current_img(self):
        if QSysInfo.productType() == "windows":
            dir_path = QStandardPaths.writableLocation(
                QStandardPaths.HomeLocation) + "/AppData/Roaming/earth-wallpaper/wallpaper/"
        else:
            dir_path = QStandardPaths.writableLocation(
                QStandardPaths.HomeLocation) + "/.cache/earth-wallpaper/wallpaper/"

        dir_ = QDir(dir_path)
        name_filters = ["[1-9]*"]
        dir_.setNameFilters(name_filters)
        files = dir_.entryList(QDir.Files, QDir.Name)
        picturePath = QStandardPaths.writableLocation(QStandardPaths.PicturesLocation) + "/earth-wallpaper"
        if not QDir(picturePath).exists():
            QDir(picturePath).mkpath(picturePath)
        source = QFile(dir_path + files[0])

        target = QFile(picturePath + "/" + files[len(files) - 1])
        message = QMessageBox()
        if not target.exists():
            if source.copy(target.fileName()):
                QMessageBox.information(message, "保存", "保存成功，已保存到用户Picture目录", QMessageBox.Yes)
            else:
                QMessageBox.warning(message, "保存", "保存失败，原因未知（懒）", QMessageBox.Yes)

        else:
            QMessageBox.information(message, "保存", "当前壁纸已存在，未做任何处理", QMessageBox.Yes)
