from PySide6.QtCore import QStandardPaths
import datetime
import platform
import os


class PlatformInfo:

    def __init__(self):
        self.sys = platform.system().upper()

    @staticmethod
    def download_dir() -> str:
        cache = QStandardPaths.writableLocation(QStandardPaths.GenericCacheLocation)
        return os.path.join(cache, 'earth-wallpaper/wallpaper/')

    @staticmethod
    def config_path() -> str:
        config = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        return os.path.join(config, 'earth-wallpaper/earth-wallpaper.conf')

    @staticmethod
    def log_path() -> str:
        today = datetime.datetime.utcnow()
        cache = QStandardPaths.writableLocation(QStandardPaths.GenericCacheLocation)
        log_dir = os.path.join(cache, 'earth-wallpaper/logs/')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        file_name = today.strftime("%Y-%m-%d") + ".log"
        log_path = os.path.join(log_dir, file_name)
        if not os.path.exists(log_path):
            open(log_path, 'w').write('')
        return log_path

    def check(self):
        if os.path.exists(self.download_dir()):
            pass
        else:
            os.makedirs(self.download_dir())

    def get_os(self):
        return self.sys
