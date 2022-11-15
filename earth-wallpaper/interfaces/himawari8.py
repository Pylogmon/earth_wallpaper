from PIL import Image
from .utils.setWallpaper import set_wallpaper
from .utils.PlatformInfo import PlatformInfo
from PySide6.QtCore import QSettings, QStandardPaths
from PySide6.QtWidgets import QApplication
import requests
import datetime
import os
import shutil


class Himawari8(object):
    def __init__(self):
        # 屏幕分辨率
        # QApplication()
        desktop = QApplication.primaryScreen()
        desktop_rect = desktop.geometry()
        self.Y = desktop_rect.height() + desktop_rect.top()
        self.X = desktop_rect.width() + desktop_rect.left()
        self.config_path = os.path.join(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation),
                                        "earth-wallpaper/config")
        self.settings = QSettings(self.config_path, QSettings.IniFormat)
        self.settings.beginGroup("APP")
        self.SIZE = int(self.settings.value("earthSize"))
        self.settings.endGroup()
        self.settings.beginGroup("System")
        type = ["None", "http", "socks"]
        self.prx_type = type[int(self.settings.value("proxy"))]
        self.prx_add = self.settings.value("proxyAdd")
        self.prx_port = self.settings.value("proxyPort")
        self.settings.endGroup()
        self.path = PlatformInfo().getDownloadPath()
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
        os.makedirs(self.path)
        self.today = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
        self.name_ = self.today.strftime("%Y%m%d%H%M%S") + ".png"
        self.path_today = ""

    # 下载图像
    def download(self, url):
        if self.prx_type == "None":
            img = requests.get(url)
        else:
            proxies = {"http": f"{self.prx_type}://{self.prx_add}:{self.prx_port}",
                       "https": f"{self.prx_type}://{self.prx_add}:{self.prx_port}"}
            img = requests.get(url, proxies=proxies)
        with open(self.path + self.name_, "wb") as fwi:
            fwi.write(img.content)

    # 填充黑色适配屏幕尺寸
    def fill_img(self):
        height = int(500.0 / (float(self.SIZE) * 0.01))
        width = int(height * (float(self.X) / float(self.Y)))
        img = Image.open(self.path + self.name_)
        new_img = Image.new(img.mode, (width, height), color='black')
        new_img.paste(img, (int(width / 2 - 250), int(height / 2 - 250)))

        new_img.save(self.path + self.name_)
        set_wallpaper(self.path + self.name_)

    def get_time_path(self):
        path_today_ = self.today.strftime("%Y/%m/%d/%H%M")
        temp_list = list(path_today_)
        temp_list[-1] = "0"
        self.path_today = "".join(temp_list)

    def run(self):
        self.get_time_path()
        url = f"https://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/{self.path_today}00_0_0.png"

        # name = "00_0_0.png"
        self.download(url)
        self.fill_img()

    @staticmethod
    def name():
        return "向日葵八号"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup", "earthSizeGroup"]
        return layout_list


if __name__ == '__main__':
    x = Himawari8()
    x.run()
