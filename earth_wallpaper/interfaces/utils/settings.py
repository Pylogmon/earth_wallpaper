from PySide6.QtCore import QSettings, QStandardPaths
from PySide6.QtWidgets import QApplication
import os


def trans(i: str) -> bool:
    if i == "true" or i == "True":
        return True
    if i == "false" or i == "False":
        return False


class Settings(object):

    def __init__(self):
        config_dir = QStandardPaths.writableLocation(
            QStandardPaths.ConfigLocation)
        config_path = os.path.join(config_dir,
                                   "earth-wallpaper/earth-wallpaper.conf")
        self.settings = QSettings(config_path, QSettings.IniFormat)

    def proxies(self) -> dict:
        type_list = ["None", "http", "socks5h"]
        prx_type = type_list[int(self.settings.value("System/proxy"))]
        prx_add = self.settings.value("System/proxyAdd")
        prx_port = self.settings.value("System/proxyPort")
        if prx_type == "None":
            proxies = {}
        else:
            proxies = {
                "http": f"{prx_type}://{prx_add}:{prx_port}",
                "https": f"{prx_type}://{prx_add}:{prx_port}"
            }
        return proxies

    def wallpaper_dir(self) -> str:
        return self.settings.value("APP/wallpaperDir")

    def wallpaper_file(self) -> str:
        return self.settings.value("APP/wallpaperFile")

    def earth_size(self) -> int:
        return int(self.settings.value("APP/earthSize"))

    def apikey(self) -> str:
        return self.settings.value("APP/apikey")

    def general(self):
        return trans(str(self.settings.value("APP/General")))

    def anime(self):
        return trans(str(self.settings.value("APP/Anime")))

    def people(self):
        return trans(str(self.settings.value("APP/People")))

    def sfw(self):
        return trans(str(self.settings.value("APP/SFW")))

    def sketchy(self):
        return trans(str(self.settings.value("APP/Sketchy")))

    def nsfw(self):
        return trans(str(self.settings.value("APP/NSFW")))

    def sorting(self):
        return self.settings.value("APP/sorting").lower().replace(" ", "_")

    def searchkey(self):
        return self.settings.value("APP/searchkey").replace(" ", "+")

    def color(self):
        return self.settings.value("APP/color").replace('#', '')

    def atleast(self):
        return self.settings.value("APP/atleast")

    @staticmethod
    def desktop_res() -> (int, int):
        desktop = QApplication.primaryScreen()
        desktop_rect = desktop.geometry()
        y = desktop_rect.height() + desktop_rect.top()
        x = desktop_rect.width() + desktop_rect.left()
        return x, y
