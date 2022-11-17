import platform
import os
import datetime


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

    def download_path(self, ext: str) -> str:
        today = datetime.datetime.utcnow()
        file_name = today.strftime("%Y%m%d%H%M%S")
        return self.download_dir() + file_name + ext

    def get_os(self) -> str:
        return self.sys
