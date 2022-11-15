from .utils.setWallpaper import set_wallpaper
from .utils.PlatformInfo import PlatformInfo
from PySide6.QtCore import QSettings, QStandardPaths
import requests
import datetime
import os
import shutil
import json
import hashlib


class BingRand(object):
    def __init__(self):
        self.config_path = os.path.join(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation),
                                        "earth-wallpaper/config")
        self.settings = QSettings(self.config_path, QSettings.IniFormat)
        type = ["None", "http", "socks"]
        self.settings.beginGroup("System")
        self.prx_type = type[int(self.settings.value("proxy"))]
        self.prx_add = self.settings.value("proxyAdd")
        self.prx_port = self.settings.value("proxyPort")
        self.api_url = "https://bing.ioliu.cn/v1/rand?type=json"

    def download(self, path):
        headers = {
            "user-agent":
                "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        img_json = requests.get(self.api_url, headers=headers)

        img_url = json.loads(img_json.content.decode())["data"]["url"]
        img_url = img_url.replace("http://h1.ioliu.cn/bing/",
                                  "https://www.bing.com/th?id=OHR.")
        img_url = img_url.replace("1920x1080", "UHD")
        img_url = img_url[:-10]
        print(img_url)

        if self.prx_type == "None":
            img = requests.get(img_url, headers=headers)
        else:
            proxies = {"http": f"{self.prx_type}://{self.prx_add}:{self.prx_port}",
                       "https": f"{self.prx_type}://{self.prx_add}:{self.prx_port}"}
            img = requests.get(img_url, headers=headers, proxies=proxies)
        with open(path, "wb") as fwi:
            fwi.write(img.content)
        with open(path, 'rb') as fp:
            data = fp.read()
        md5 = hashlib.md5(data).hexdigest()
        if md5 == "f0f7d2c575a576fcbe5904900906e27a":
            return False
        else:
            return True

    def run(self):
        today = datetime.datetime.utcnow()
        wallpaper_dir = PlatformInfo().getDownloadPath()
        if os.path.exists(wallpaper_dir):
            shutil.rmtree(wallpaper_dir)
        os.makedirs(wallpaper_dir)
        name = wallpaper_dir + today.strftime("%Y%m%d%H%M%S") + ".png"  # windows S
        while True:
            if self.download(name):
                break
        set_wallpaper(name)

    @staticmethod
    def name():
        return "必应壁纸(随机)"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup"]
        return layout_list


if __name__ == '__main__':
    x = BingRand()
    x.run()
