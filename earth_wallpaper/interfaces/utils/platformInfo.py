from PySide6.QtCore import QStandardPaths
import platform
import datetime
import os


class PlatformInfo:

    def __init__(self):
        self.sys = platform.system().upper()

    @staticmethod
    def download_dir() -> str:
        cache = QStandardPaths.writableLocation(QStandardPaths.GenericCacheLocation)
        return os.path.join(cache, 'earth-wallpaper/wallpaper/')

    @staticmethod
    def download_path(ext: str) -> str:
        today = datetime.datetime.utcnow()
        cache = QStandardPaths.writableLocation(QStandardPaths.GenericCacheLocation)
        download_dir = os.path.join(cache, 'earth-wallpaper/wallpaper/')
        file_name = today.strftime("%Y%m%d%H%M%S")
        return download_dir + file_name + ext

    @staticmethod
    def temp_dir() -> str:
        temp = QStandardPaths.writableLocation(QStandardPaths.TempLocation)
        return temp

    def get_os(self) -> str:
        return self.sys
