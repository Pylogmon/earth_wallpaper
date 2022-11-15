from .utils.setWallpaper import set_wallpaper
from .utils.PlatformInfo import PlatformInfo
from PySide6.QtCore import QSettings, QStandardPaths
import requests
import datetime
import os
import shutil
from requests.structures import CaseInsensitiveDict
import json


class BingToday(object):
    def __init__(self, proxy="None"):
        self.config_path = os.path.join(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation),
                                        "earth-wallpaper/config")
        self.settings = QSettings(self.config_path, QSettings.IniFormat)
        type = ["None", "http", "socks"]
        self.settings.beginGroup("System")
        self.prx_type = type[int(self.settings.value("proxy"))]
        self.prx_add = self.settings.value("proxyAdd")
        self.prx_port = self.settings.value("proxyPort")
        self.bing_addr = "https://www.bing.com"
        self.json_link = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

    def download(self, path):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        if self.prx_type == "None":
            resp = requests.get(self.json_link, headers=headers)
        else:
            proxies = {"http": f"{self.prx_type}://{self.prx_add}:{self.prx_port}",
                       "https": f"{self.prx_type}://{self.prx_add}:{self.prx_port}"}
            resp = requests.get(self.json_link, headers=headers, proxies=proxies)
        if resp.ok:
            web_json = json.loads(resp.content.decode())
            image_url = (self.bing_addr + web_json['images'][0]['url']).replace(
                "1920x1080", "UHD")
            if self.prx_type == "None":
                imager = requests.get(image_url)
            else:
                proxies = {"http": f"{self.prx_type}://{self.prx_add}:{self.prx_port}",
                           "https": f"{self.prx_type}://{self.prx_add}:{self.prx_port}"}
                imager = requests.get(image_url, proxies=proxies)

            with open(path, 'wb') as f:
                f.write(imager.content)
        else:
            raise ValueError('Fetching website failed.')

    def run(self):
        today = datetime.datetime.utcnow()
        wallpaper_dir = PlatformInfo().getDownloadPath()
        if os.path.exists(wallpaper_dir):
            shutil.rmtree(wallpaper_dir)
        os.makedirs(wallpaper_dir)
        name = wallpaper_dir + today.strftime("%Y%m%d%H%M%S") + ".png"
        self.download(name)
        set_wallpaper(name)

    @staticmethod
    def name():
        return "必应壁纸(今日)"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup"]
        return layout_list


if __name__ == '__main__':
    x = BingToday()
    x.run()
