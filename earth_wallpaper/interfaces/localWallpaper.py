from .utils.settings import Settings
from PySide6.QtCore import QDir
import logging
import os

logger = logging.getLogger(__name__)


class LocalWallpaper(object):

    def __init__(self):
        self.wallpaper_dir = Settings().wallpaper_dir()
        self.files = None
        self.currentFile = self.wallpaper_dir + "/current.txt"
        self.currentWallpaper = None

    def get_files(self):
        wallpaper_dir = QDir(self.wallpaper_dir)
        name_filter = ["*.png", "*.jpg", "*.jpeg", "*.gif"]
        wallpaper_dir.setNameFilters(name_filter)
        self.files = wallpaper_dir.entryList(QDir.Files, QDir.Name)

    def check(self):
        if os.path.exists(self.currentFile):
            with open(self.currentFile, 'r') as f:
                self.currentWallpaper = f.readline()
                logger.info(f"当前壁纸为 {self.currentWallpaper}")
        else:
            with open(self.currentFile, 'w') as f:
                f.write(self.files[0])

    def find_next(self):
        for i in range(len(self.files)):
            if self.files[i] == self.currentWallpaper:
                if self.files[i] == self.files[-1]:
                    with open(self.currentFile, 'w') as f:
                        f.write(self.files[0])
                    return os.path.join(self.wallpaper_dir, self.files[0])
                else:
                    with open(self.currentFile, 'w') as f:
                        f.write(self.files[i + 1])
                    return os.path.join(self.wallpaper_dir, self.files[i + 1])

    def run(self):
        self.get_files()
        self.check()
        return self.find_next()

    @staticmethod
    def name():
        return "本地壁纸"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup", "wallpaperDirGroup"]
        return layout_list


if __name__ == "__main__":
    x = LocalWallpaper()
    x.run()
