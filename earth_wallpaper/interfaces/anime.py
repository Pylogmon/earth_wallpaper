from .utils.platformInfo import PlatformInfo
from .utils.settings import Settings
import requests
import json


class Anime(object):
    def __init__(self):
        self.proxies = Settings().proxies()
        self.download_dir = PlatformInfo().download_dir()
        self.download_path = None
        self.request_url = "https://api.waifu.im/random?orientation=LANDSCAPE"
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
