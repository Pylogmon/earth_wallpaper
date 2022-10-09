# source: 必应壁纸(今日)
# updateTime
from .utils.setWallpaper import set_wallpaper
from .utils.PlatformInfo import PlatformInfo
import requests
import datetime
import os
import shutil
from requests.structures import CaseInsensitiveDict
import json
import sys


class BingToday(object):
    def __init__(self, proxy="None"):
        self.proxy = proxy
        self.bing_addr = "https://www.bing.com"
        self.json_link = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

    def download(self, path):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        if self.proxy == "None":
            resp = requests.get(self.json_link, headers=headers)
        else:
            proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
            resp = requests.get(self.json_link, headers=headers, proxies=proxies)
        if resp.ok:
            web_json = json.loads(resp.content.decode())
            image_url = (self.bing_addr + web_json['images'][0]['url']).replace(
                "1920x1080", "UHD")
            if self.proxy == "None":
                imager = requests.get(image_url)
            else:
                proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
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
