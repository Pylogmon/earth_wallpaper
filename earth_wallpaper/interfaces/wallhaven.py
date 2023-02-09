from .utils.platformInfo import PlatformInfo
from .utils.settings import Settings
from random import randint
import requests
import logging
import json

logger = logging.getLogger(__name__)


class Wallhaven(object):

    def __init__(self):
        self.proxies = Settings().proxies()
        self.search_url = "https://wallhaven.cc/api/v1/search?ratios=landscape"
        self.img_url = "https://wallhaven.cc/api/v1/w/"
        self.apikey = Settings().apikey()
        self.general = Settings().general()
        self.anime = Settings().anime()
        self.people = Settings().people()
        self.sfw = Settings().sfw()
        self.sketchy = Settings().sketchy()
        self.nsfw = Settings().nsfw()
        self.sorting = Settings().sorting()
        self.searchkey = Settings().searchkey()
        self.color = Settings().color()
        self.atleast = Settings().atleast()
        self.download_path = PlatformInfo().download_path(".png")

    def build_search_url(self):
        categories = ['0', '0', '0']
        if self.general:
            categories[0] = '1'
        if self.anime:
            categories[1] = '1'
        if self.people:
            categories[2] = '1'
        self.search_url += f"&categories={''.join(categories)}"
        purity = ['0', '0', '0']
        if self.sfw:
            purity[0] = '1'
        if self.sketchy:
            purity[1] = '1'
        if self.nsfw:
            purity[2] = '1'
        self.search_url += f"&purity={''.join(purity)}"
        self.search_url += f"&sorting={self.sorting}"
        self.search_url += f"&atleast={self.atleast}"
        if not len(self.searchkey) == 0:
            self.search_url += f"&q={self.searchkey}"
        if not self.color == "不选择":
            self.search_url += f"&colors={self.color}"
        if not len(self.apikey) == 0:
            self.search_url += f"&apikey={self.apikey}"
        logger.info(f"search_url构造完成:{self.search_url}")

    def get_img_url(self):
        img_info = requests.get(self.search_url, proxies=self.proxies)
        if img_info.ok:
            last_page = json.loads(
                img_info.content.decode())["meta"]["last_page"]
            page = randint(1, last_page)
            logger.info(f"获取到{last_page}页数据，现随机第{page}页数据")
            self.search_url += f"&pages={page}"
            logger.info(f"search_url构造完成:{self.search_url}")
            img_info = requests.get(self.search_url, proxies=self.proxies)
            if img_info.ok:
                img_info_json = json.loads(img_info.content.decode())["data"]
                self.img_url += img_info_json[randint(0,
                                                      len(img_info_json) -
                                                      1)]["id"]
                if not len(self.apikey) == 0:
                    self.img_url += f"?apikey={self.apikey}"
                logger.info(f"图像信息获取成功: {self.img_url}")
            else:
                logger.fatal(f"search_url请求失败: {img_info.status_code}")
        else:
            logger.fatal(f"search_url请求失败: {img_info.status_code}")

    def download(self):
        img_info = requests.get(self.img_url, proxies=self.proxies)
        if img_info.ok:
            download_url = json.loads(
                img_info.content.decode())["data"]["path"]
            logger.info(f"图像url获取成功: {download_url}")
            img = requests.get(download_url, proxies=self.proxies)
            if img.ok:
                logger.info("图像下载成功")
                return img.content
            else:
                logger.fatal(f"图像下载失败: {img.status_code}")
        else:
            logger.fatal(f"img_info请求失败: {img_info.status_code}")

    def run(self):
        self.build_search_url()
        self.get_img_url()
        return self.download()

    @staticmethod
    def name():
        return "wallhaven.cc"

    @staticmethod
    def layout():
        layout_list = [
            "updateTimeGroup", "apikeyGroup", "categoriesGroup", "purityGroup",
            "sortingGroup", "searchkeyGroup", "colorGroup", "atleastGroup"
        ]
        return layout_list
