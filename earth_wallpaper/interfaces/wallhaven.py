from .utils.platformInfo import PlatformInfo
from .utils.settings import Settings
from random import randint
import requests
import json


class Wallhaven(object):
    def __init__(self):
        self.proxies = Settings().proxies()
        self.search_url = "https://wallhaven.cc/api/v1/search"
        self.img_url = "https://wallhaven.cc/api/v1/w/"
        self.apikey = Settings().apikey()
        self.general = Settings().general()
        self.anime = Settings().anime()
        self.people = Settings().people()
        self.sfw = Settings().sfw()
        self.sketchy = Settings().sketchy()
        self.nsfw = Settings().nsfw()
        self.sorting = Settings().sorting()
        self.download_path = PlatformInfo().download_path(".png")

    def build_search_url(self):
        categories = ['0', '0', '0']
        if self.general:
            categories[0] = '1'
        if self.anime:
            categories[1] = '1'
        if self.people:
            categories[2] = '1'
        self.search_url += f"?categories={''.join(categories)}"
        purity = ['0', '0', '0']
        if self.sfw:
            purity[0] = '1'
        if self.sketchy:
            purity[1] = '1'
        if self.nsfw:
            purity[2] = '1'
        self.search_url += f"&purity={''.join(purity)}"
        self.search_url += f"&sorting={self.sorting}"
        if not len(self.apikey) == 0:
            self.search_url += f"&apikey={self.apikey}"
        print("列表json: " + self.search_url)

    def get_img_url(self):
        img_info = requests.get(self.search_url, proxies=self.proxies)
        if img_info.ok:
            img_info_json = json.loads(img_info.content.decode())["data"]
            self.img_url += img_info_json[randint(0, len(img_info_json) - 1)]["id"]
            if not len(self.apikey) == 0:
                self.img_url += f"?apikey={self.apikey}"
            print("图像信息json: " + self.img_url)

    def download(self):
        img_info = requests.get(self.img_url, proxies=self.proxies)
        if img_info.ok:
            download_url = json.loads(img_info.content.decode())["data"]["path"]
            print("图像url: " + download_url)
            img = requests.get(download_url, proxies=self.proxies)
            return img.content

    def run(self):
        self.build_search_url()
        self.get_img_url()
        return self.download()

    @staticmethod
    def name():
        return "wallhaven.cc"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup", "apikeyGroup", "categoriesGroup", "purityGroup", "sortingGroup"]
        return layout_list
