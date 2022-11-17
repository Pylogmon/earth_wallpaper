from .utils.platformInfo import PlatformInfo
from PySide6.QtCore import QSettings, QStandardPaths
import requests
import os
import json
import hashlib


class BingRand(object):
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
        self.request_url = "https://bing.ioliu.cn/v1/rand?type=json"
        self.download_path = PlatformInfo().download_path(".png")

    def get_img_url(self) -> str:
        headers = {
            "user-agent":
                "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        img_json = requests.get(self.request_url, headers=headers, proxies=self.proxies)
        img_url = json.loads(img_json.content.decode())["data"]["url"]
        img_url = img_url.replace("http://h1.ioliu.cn/bing/",
                                  "https://cn.bing.com/th?id=OHR.")
        img_url = img_url.replace("1920x1080", "UHD")
        img_url = img_url[:-10]
        return img_url

    def download(self):
        headers = {
            "user-agent":
                "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        while True:
            img_url = self.get_img_url()
            print(img_url, end=" ")
            img = requests.get(img_url, headers=headers, proxies=self.proxies)
            md5 = hashlib.md5(img.text.encode('utf-8')).hexdigest()
            print(md5)
            # 检测无效数据
            if md5 == "6d0b9d149a0c9a1da30920e84e5581a0":
                print("数据无效，重新下载")
                pass
            else:
                return img.content

    def run(self):
        return self.download()

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
