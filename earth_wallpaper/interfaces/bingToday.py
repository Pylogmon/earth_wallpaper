from requests.structures import CaseInsensitiveDict
from .utils.platformInfo import PlatformInfo
from .utils.settings import Settings
import requests
import logging
import json

logger = logging.getLogger(__name__)


class BingToday(object):
    def __init__(self):
        self.proxies = Settings().proxies()
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
            logger.info(f"img_url获取成功: {img_url}")
            return img_url
        else:
            logger.fatal(f"img_url获取失败: {resp.status_code}")

    def download(self):
        img_url = self.get_img_url()
        img = requests.get(img_url, proxies=self.proxies)
        if img.ok:
            logger.info("图像下载成功")
            return img.content
        else:
            logger.fatal(f"图像下载失败: {img.status_code}")

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
