from .utils.platformInfo import PlatformInfo
from .utils.settings import Settings
import requests
import logging
import json

logger = logging.getLogger(__name__)


class BingRand(object):
    def __init__(self):
        self.proxies = Settings().proxies()
        self.request_url = "https://bing.ioliu.cn/v1/rand?type=json"
        self.download_path = PlatformInfo().download_path(".png")

    def get_img_url(self) -> str:
        headers = {
            "user-agent":
                "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        img_json = requests.get(self.request_url, headers=headers, proxies=self.proxies)
        if img_json.ok:
            img_url = json.loads(img_json.content.decode())["data"]["url"]
            img_url = img_url.replace("http://h1.ioliu.cn/bing/",
                                      "https://cn.bing.com/th?id=OHR.")
            img_url = img_url.replace("1920x1080", "UHD")
            img_url = img_url[:-10]
            logger.info(f"img_url获取成功: {img_url}")
            return img_url
        else:
            logger.fatal(f"img_url请求失败: {img_json.status_code}")

    def download(self):
        headers = {
            "user-agent":
                "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        while True:
            img_url = self.get_img_url()
            img = requests.get(img_url, headers=headers, proxies=self.proxies)
            if img.ok:
                logger.info("图像下载成功")
                return img.content
            else:
                logger.fatal(f"图像下载失败: {img.status_code}")

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
