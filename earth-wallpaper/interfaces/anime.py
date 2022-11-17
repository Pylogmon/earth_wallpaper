from PySide6.QtCore import QSettings, QStandardPaths
from .utils.platformInfo import PlatformInfo
import requests
import json
import os


class Anime(object):
    def __init__(self):
        config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        config_path = os.path.join(config_dir, "earth-wallpaper/config")
        settings = QSettings(config_path, QSettings.IniFormat)
        type_list = ["None", "http", "socks"]
        prx_add = settings.value("System/proxyAdd")
        prx_port = settings.value("System/proxyPort")
        self.prx_type = type_list[int(settings.value("System/proxy"))]
        if self.prx_type == "None":
            self.proxies = {}
        else:
            self.proxies = {"http": f"{self.prx_type}://{prx_add}:{prx_port}",
                            "https": f"{self.prx_type}://{prx_add}:{prx_port}"}
        self.request_url = "https://api.waifu.im/random?orientation=LANDSCAPE"
        self.download_dir = PlatformInfo().download_dir()
        self.download_path = None
        self.img_url = None

    def get_img_url(self):
        res = requests.get(self.request_url, proxies=self.proxies)
        res = json.loads(res.text)
        self.img_url = res["images"][0]["url"]
        img_ext = res["images"][0]["extension"]
        self.download_path = PlatformInfo().download_path(img_ext)

    def download(self):
        img = requests.get(self.img_url, proxies=self.proxies)
        return img.content

    def run(self):
        self.get_img_url()
        return self.download()

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
