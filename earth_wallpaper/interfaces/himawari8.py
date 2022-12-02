from .utils.platformInfo import PlatformInfo
from .utils.settings import Settings
from os.path import join
from PIL import Image
import requests
import datetime
import logging

logger = logging.getLogger(__name__)


class Himawari8(object):
    def __init__(self):
        self.Y = Settings.desktop_res()[1]
        self.X = Settings.desktop_res()[0]
        self.earth_size = Settings().earth_size()
        self.proxies = Settings().proxies()
        self.temp_dir = PlatformInfo.temp_dir()
        self.path_today = None
        self.download_path = PlatformInfo.download_path(".png")

    # 下载图像
    def download(self):
        url = f"https://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/{self.path_today}00_0_0.png"

        img = requests.get(url, proxies=self.proxies)
        if img.ok:
            logger.info("图像himawari.png下载成功")
            with open(join(self.temp_dir, "himawari.png"), "wb") as f:
                f.write(img.content)
        else:
            logger.fatal(f"图像下载失败: {img.status_code}")

    # 填充黑色适配屏幕尺寸
    def fill_img(self):
        height = int(500.0 / (float(self.earth_size) * 0.01))
        width = int(height * (float(self.X) / float(self.Y)))
        img = Image.open(join(self.temp_dir, "himawari.png"))
        new_img = Image.new(img.mode, (width, height), color='black')
        new_img.paste(img, (int(width / 2 - 250), int(height / 2 - 250)))
        new_img.save(join(self.temp_dir, "himawari.png"))
        with open(join(self.temp_dir, "himawari.png"), "rb") as f:
            data = f.read()
        return data

    def get_time_path(self):
        today = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
        path_today_ = today.strftime("%Y/%m/%d/%H%M")
        temp_list = list(path_today_)
        temp_list[-1] = "0"
        self.path_today = "".join(temp_list)

    def run(self):
        self.get_time_path()
        self.download()
        return self.fill_img()

    @staticmethod
    def name():
        return "向日葵八号"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup", "earthSizeGroup"]
        return layout_list


if __name__ == '__main__':
    x = Himawari8()
    x.run()
