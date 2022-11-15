import os
from .utils.setWallpaper import set_wallpaper
from PySide6.QtCore import QSettings, QStandardPaths


class LocalWallpaper(object):

    def __init__(self):
        self.config_path = os.path.join(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation),
                                        "earth-wallpaper/config")
        self.settings = QSettings(self.config_path, QSettings.IniFormat)
        self.settings.beginGroup("APP")
        self.wallpaperDir = self.settings.value("wallpaperDir")
        self.currentFile = self.wallpaperDir + "/current.txt"
        self.currentWallpaper = "None"
        self.exts = [".png", ".jpg", "jpeg", ".gif"]

    def run(self):
        if os.path.exists(self.currentFile):
            with open(self.currentFile, 'r') as f:
                self.currentWallpaper = f.readline()
        else:
            files = os.listdir(self.wallpaperDir)
            for i in files:
                if i[-4:] in self.exts:
                    set_wallpaper(self.wallpaperDir + "/" + i)
                    with open(self.currentFile, 'w') as f:
                        f.write(i)
                    break
                else:
                    continue

        files = os.listdir(self.wallpaperDir)
        flag = False
        for i in files:
            if flag:
                if i[-4:] in self.exts:
                    set_wallpaper(self.wallpaperDir + "/" + i)
                    with open(self.currentFile, 'w') as f:
                        f.write(i)
                    break
                else:
                    continue
            else:
                if i == self.currentWallpaper:
                    flag = True
        else:
            for i in files:
                if i[-4:] in self.exts:
                    set_wallpaper(self.wallpaperDir + "/" + i)
                    with open(self.currentFile, 'w') as f:
                        f.write(i)
                    break
                else:
                    continue

    @staticmethod
    def name():
        return "本地壁纸"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup", "wallpaperDirGroup"]
        return layout_list
