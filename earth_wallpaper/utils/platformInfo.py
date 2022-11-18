from PySide6.QtCore import QStandardPaths
import platform
import shutil
import os


class PlatformInfo:

    def __init__(self):
        self.sys = platform.system().upper()

    @staticmethod
    def download_dir() -> str:
        cache = QStandardPaths.writableLocation(QStandardPaths.GenericCacheLocation)
        return os.path.join(cache, 'earth-wallpaper/wallpaper/')

    def check(self):
        if os.path.exists(self.download_dir()):
            shutil.rmtree(self.download_dir())
        os.makedirs(self.download_dir())
    
    def get_os(self):
        return self.sys
