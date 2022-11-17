import datetime
import platform
import os
import shutil


class PlatformInfo:

    def __init__(self):
        self.sys = platform.system().upper()

    def download_dir(self) -> str:
        if self.sys == "WINDOWS":
            appdata = os.getenv("APPDATA").replace("\\", "/")
            return appdata + "/earth-wallpaper/wallpaper/"
        elif self.sys == "LINUX":
            home = os.getenv("HOME")
            return home + '/.cache/earth-wallpaper/wallpaper/'

    def check(self):
        if os.path.exists(self.download_dir()):
            shutil.rmtree(self.download_dir())
        os.makedirs(self.download_dir())
