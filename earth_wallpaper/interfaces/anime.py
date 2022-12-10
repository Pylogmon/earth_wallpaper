from .utils.platformInfo import PlatformInfo
from .utils.settings import Settings
import requests
import logging
import json

logger = logging.getLogger(__name__)


class Anime(object):
    def __init__(self):
        self.proxies = Settings().proxies()
        self.download_dir = PlatformInfo().download_dir()
        self.download_path = None
        self.request_url = "https://api.waifu.im/search?orientation=LANDSCAPE"
        self.img_url = None

    def get_img_url(self):
        headers = {'Accept-Version': 'v4'}
        res = requests.get(self.request_url, headers=headers, proxies=self.proxies)
        if res.ok:
            res = json.loads(res.text)
            self.img_url = res["images"][0]["url"]
            logger.info(f"img_url获取成功: {self.img_url}")
            img_ext = res["images"][0]["extension"]
            self.download_path = PlatformInfo().download_path(img_ext)
        else:
            logger.fatal(f"img_url获取失败: {res.status_code}")

    def download(self):
        img = requests.get(self.img_url, proxies=self.proxies)
        if img.ok:
            logger.info("图像下载成功")
            return img.content
        else:
            logger.fatal(f"图像下载失败: {img.status_code}")

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
