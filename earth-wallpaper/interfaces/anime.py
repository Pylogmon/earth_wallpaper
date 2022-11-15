import sys
from PySide6.QtCore import QSettings, QStandardPaths
from .utils.setWallpaper import set_wallpaper
from .utils.PlatformInfo import PlatformInfo
import requests
import datetime
import json
import os
import shutil


class Anime(object):
    def __init__(self):
        self.config_path = os.path.join(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation),
                                        "earth-wallpaper/config")
        self.settings = QSettings(self.config_path, QSettings.IniFormat)
        type = ["None", "http", "socks"]
        self.settings.beginGroup("APP")
        self.prx_type = int(self.settings.value("proxy"))
        self.prx_add = self.settings.value("proxyAdd")
        self.prx_port = self.settings.value("proxyPort")
        self.request_url = "https://api.waifu.im/random?orientation=LANDSCAPE"
        self.img_url = ""
        self.img_ext = ""

    def get_img_url(self):
        if self.prx_type == "None":
            res = requests.get(self.request_url).text
        else:
            proxies = {"http": f"{self.prx_type}://{self.prx_add}:{self.prx_port}",
                       "https": f"{self.prx_type}://{self.prx_add}:{self.prx_port}"}
            res = requests.get(self.request_url, proxies=proxies).text
        res = json.loads(res)

        self.img_url = res["images"][0]["url"]
        self.img_ext = res["images"][0]["extension"]

    def download(self):
        if self.prx_type == "None":
            img = requests.get(self.img_url)
        else:
            proxies = {"http": f"{self.prx_type}://{self.prx_add}:{self.prx_port}",
                       "https": f"{self.prx_type}://{self.prx_add}:{self.prx_port}"}
            img = requests.get(self.img_url, proxies=proxies)
        today = datetime.datetime.utcnow()
        wallpaper_dir = PlatformInfo().getDownloadPath()
        if os.path.exists(wallpaper_dir):
            shutil.rmtree(wallpaper_dir)
        os.makedirs(wallpaper_dir)
        path = wallpaper_dir + today.strftime("%Y%m%d%H%M%S") + self.img_ext
        with open(path, "wb") as fwi:
            fwi.write(img.content)
        set_wallpaper(path)

    def run(self):
        self.get_img_url()
        self.download()

    @staticmethod
    def name():
        return "动漫壁纸"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup"]
        return layout_list


if __name__ == "__main__":
    x = Anime()
    x.run()
