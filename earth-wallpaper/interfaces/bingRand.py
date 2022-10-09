# source: 必应壁纸(随机)
# updateTime
from .utils.setWallpaper import set_wallpaper
from .utils.PlatformInfo import PlatformInfo
import requests
import datetime
import os
import shutil
import sys
import json
import hashlib


class BingRand(object):
    def __init__(self, proxy="None"):
        self.proxy = proxy
        self.api_url = "https://bing.ioliu.cn/v1/rand?type=json"

    def download(self, path):
        headers = {
            "user-agent":
                "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        if self.proxy == "None":
            img_json = requests.get(self.api_url, headers=headers)
        else:
            proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
            img_json = requests.get(self.api_url, headers=headers, proxies=proxies)
        img_url = json.loads(img_json.content.decode())["data"]["url"]
        img_url = img_url.replace("http://h1.ioliu.cn/bing/",
                                  "https://www.bing.com/th?id=OHR.")
        img_url = img_url.replace("1920x1080", "UHD")
        img_url = img_url[:-10]
        print(img_url)

        if self.proxy == "None":
            img = requests.get(img_url, headers=headers)
        else:
            proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
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
