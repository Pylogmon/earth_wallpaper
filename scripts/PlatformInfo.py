import platform
import os

class PlatformInfo:

    def __init__(self):
        self.sys = platform.system().upper()
        if self.sys == "WINDOWS":
            print("Current OS is Windows.")
            
        elif self.sys == "LINUX":
            print("Current OS is Linux.")

    def getDownloadPath(self) -> str:
        if self.sys == "WINDOWS":
            appdata = os.getenv("APPDATA").replace("\\", "/")
            return appdata + "/earth-wallpaper/wallpaper/"
        elif self.sys == "LINUX":
            home = os.getenv("HOME")
            return home + '/.cache/earth-wallpaper/wallpaper/'

    def getOS(self) -> str:
        return self.sys