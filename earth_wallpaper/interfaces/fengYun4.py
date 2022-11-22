from .utils.platformInfo import PlatformInfo
from .utils.settings import Settings
from os.path import join
from PIL import Image
import requests
import datetime
import logging

logger = logging.getLogger(__name__)


class FengYun4(object):
    def __init__(self):
        self.Y = Settings.desktop_res()[1]
        self.X = Settings.desktop_res()[0]
        self.earth_size = Settings().earth_size()
        self.proxies = Settings().proxies()
        self.temp_dir = PlatformInfo.temp_dir()
        self.path_today = None
        self.download_path = PlatformInfo.download_path(".png")

    def get_time_path(self):
        today = datetime.datetime.utcnow()
        path_today_ = today.strftime("%Y%m%d%H%M")
        self.path_today = str((int(path_today_) - 10000) -
                              (int(path_today_) - 10000) % 100)

    def download(self):
        header = {
            'user-agent':
                'Mozilla/5.0 (X11; Linux x86_64; rv:102.0)Gecko/20100101 Firefox/102.0'
        }
        img_urls = [
            f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{self.path_today}00/jpg/1/0/0.png",

            f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{self.path_today}00/jpg/1/0/1.png",

            f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{self.path_today}00/jpg/1/1/0.png",

            f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{self.path_today}00/jpg/1/1/1.png",
        ]
        for i in range(4):
            img = requests.get(img_urls[i], headers=header, proxies=self.proxies)
            if img.ok:
                logger.info(f"图像fenyun{i}.png下载成功")
                with open(join(self.temp_dir, f"fenYun{i}.png"), "wb") as f:
                    f.write(img.content)
            else:
                logger.fatal(f"图像fenyun{i}.png下载失败: {img.status_code}")

    def concat_images(self, image_files):
        target = Image.new('RGB', (687 * 2, 687 * 2))
        for row in range(2):
            for col in range(2):
                target.paste(image_files[2 * row + col], (0 + 687 * col, 0 + 687 * row))
        target.save(join(self.temp_dir, "fenYun.png"), quality=100)  # 成品图保存

    def fill_img(self):
        height = int(1374.0 / (float(self.earth_size) * 0.01))
        width = int(height * (float(self.X) / float(self.Y)))
        img = Image.open(join(self.temp_dir, "fenYun.png"))
        new_img = Image.new(img.mode, (width, height), color='black')
        new_img.paste(img, (int(width / 2 - 687), int(height / 2 - 687)))
        new_img.save(join(self.temp_dir, "fenYun.png"))
        with open(join(self.temp_dir, "fenYun.png"), "rb") as f:
            data = f.read()
        return data

    def run(self):
        self.get_time_path()
        self.download()
        image_files = [
            Image.open(join(self.temp_dir, "fenYun0.png")),
            Image.open(join(self.temp_dir, "fenYun1.png")),
            Image.open(join(self.temp_dir, "fenYun2.png")),
            Image.open(join(self.temp_dir, "fenYun3.png")),
        ]
        self.concat_images(image_files)
        return self.fill_img()

    @staticmethod
    def name():
        return "风云四号"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup", "earthSizeGroup"]
        return layout_list


if __name__ == '__main__':
    x = FengYun4()
    x.run()
