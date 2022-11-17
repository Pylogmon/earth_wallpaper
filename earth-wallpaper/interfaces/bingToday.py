from .utils.platformInfo import PlatformInfo
from PySide6.QtCore import QSettings, QStandardPaths
import requests
import os
from requests.structures import CaseInsensitiveDict
import json


class BingToday(object):
    def __init__(self, proxy="None"):
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
        self.bing_addr = "https://www.bing.com"
        self.request_url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
        self.download_path = PlatformInfo().download_path(".png")

    def get_img_url(self) -> str:
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"

        resp = requests.get(self.request_url, headers=headers, proxies=self.proxies)
        if resp.ok:
            web_json = json.loads(resp.content.decode())
            img_url = (self.bing_addr + web_json['images'][0]['url']).replace(
                "1920x1080", "UHD")
            return img_url

    def download(self):
        img_url = self.get_img_url()
        print(img_url)
        img = requests.get(img_url, proxies=self.proxies)
        return img.content

    def run(self):
        return self.download()

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
