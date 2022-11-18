from PySide6.QtCore import QSettings, QStandardPaths
from PySide6.QtWidgets import QApplication
import os


class Settings(object):
    def __init__(self):
        config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        config_path = os.path.join(config_dir, "earth-wallpaper/config")
        self.settings = QSettings(config_path, QSettings.IniFormat)

    def proxies(self) -> dict:
        type_list = ["None", "http", "socks"]
        prx_type = type_list[int(self.settings.value("System/proxy"))]
        prx_add = self.settings.value("System/proxyAdd")
        prx_port = self.settings.value("System/proxyPort")
        if prx_type == "None":
            proxies = {}
        else:
            proxies = {"http": f"{prx_type}://{prx_add}:{prx_port}",
                       "https": f"{prx_type}://{prx_add}:{prx_port}"}
        return proxies

    def wallpaper_dir(self) -> str:
        return self.settings.value("APP/wallpaperDir")

    def wallpaper_file(self) -> str:
        return self.settings.value("APP/wallpaperFile")

    def earth_size(self) -> int:
        return int(self.settings.value("APP/earthSize"))

    @staticmethod
    def desktop_res() -> (int, int):
        desktop = QApplication.primaryScreen()
        desktop_rect = desktop.geometry()
        y = desktop_rect.height() + desktop_rect.top()
        x = desktop_rect.width() + desktop_rect.left()
        return x, y
