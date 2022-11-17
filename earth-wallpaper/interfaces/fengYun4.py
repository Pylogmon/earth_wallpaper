from PIL import Image
from PySide6.QtWidgets import QApplication
from .utils.platformInfo import PlatformInfo
from PySide6.QtCore import QSettings, QStandardPaths
import requests
import datetime
import os
import shutil


class FengYun4(object):
    def __init__(self):
        # 屏幕分辨率
        # QApplication()
        desktop = QApplication.primaryScreen()
        desktop_rect = desktop.geometry()
        self.Y = desktop_rect.height() + desktop_rect.top()
        self.X = desktop_rect.width() + desktop_rect.left()
        self.config_path = os.path.join(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation),
                                        "earth-wallpaper/config")
        self.settings = QSettings(self.config_path, QSettings.IniFormat)
        self.settings.beginGroup("APP")
        self.SIZE = int(self.settings.value("earthSize"))
        self.settings.endGroup()
        self.settings.beginGroup("System")
        type = ["None", "http", "socks"]
        self.prx_type = type[int(self.settings.value("proxy"))]
        self.prx_add = self.settings.value("proxyAdd")
        self.prx_port = self.settings.value("proxyPort")
        self.settings.endGroup()
        wallpaper_dir = PlatformInfo().download_dir()
        if os.path.exists(wallpaper_dir):
            shutil.rmtree(wallpaper_dir)
        os.makedirs(wallpaper_dir)
        self.path = wallpaper_dir
        self.today = datetime.datetime.utcnow()
        self.name_ = self.today.strftime("%Y%m%d%H%M%S") + ".png"
        self.path_today = ""
        self.download_path = PlatformInfo().download_path(".png")

    def download(self, url, path_):
        header = {
            'user-agent':
                'Mozilla/5.0 (X11; Linux x86_64; rv:102.0)Gecko/20100101 Firefox/102.0'
        }
        if self.prx_type == "None":
            img = requests.get(url, headers=header)
        else:
            proxies = {"http": f"{self.prx_type}://{self.prx_add}:{self.prx_port}",
                       "https": f"{self.prx_type}://{self.prx_add}:{self.prx_port}"}
            img = requests.get(url, headers=header, proxies=proxies)
        with open(path_, "wb") as fwi:
            fwi.write(img.content)

    def concat_images(self, image_names):
        image_files = []
        for index in range(2 * 2):
            image_files.append(Image.open(self.path + image_names[index]))
        target = Image.new('RGB', (687 * 2, 687 * 2))

        for row in range(2):
            for col in range(2):
                target.paste(image_files[2 * row + col],
                             (0 + 687 * col, 0 + 687 * row))
        target.save(self.path + self.name_, quality=100)  # 成品图保存

    def fill_img(self, download_path, name):
        height = int(1374.0 / (float(self.SIZE) * 0.01))
        width = int(height * (float(self.X) / float(self.Y)))
        img = Image.open(download_path + self.name_)
        new_img = Image.new(img.mode, (width, height), color='black')
        new_img.paste(img, (int(width / 2 - 687), int(height / 2 - 687)))

        return new_img.tobytes()

    def get_time_path(self):
        path_today_ = self.today.strftime("%Y%m%d%H%M")
        self.path_today = str((int(path_today_) - 10000) -
                              (int(path_today_) - 10000) % 100)

    def run(self):
        self.get_time_path()
        url1 = f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{self.path_today}00/jpg/1/0/0.png"

        url2 = f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{self.path_today}00/jpg/1/0/1.png"

        url3 = f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{self.path_today}00/jpg/1/1/0.png"

        url4 = f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{self.path_today}00/jpg/1/1/1.png"

        self.download(url1, self.path + '1' + self.name_)
        self.download(url2, self.path + '2' + self.name_)
        self.download(url3, self.path + '3' + self.name_)
        self.download(url4, self.path + '4' + self.name_)

        self.concat_images(['1' + self.name_, '2' + self.name_, '3' + self.name_, '4' + self.name_])
        return self.fill_img(self.path, self.name_)

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
