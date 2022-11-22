from .utils.sunCalculator import SunCalculator, DateTime
from .utils.platformInfo import PlatformInfo
from .utils.settings import Settings
import requests
import logging
import json
import time
import os

logger = logging.getLogger(__name__)


def find_first_json(dir_):
    files = os.listdir(dir_)
    for file in files:
        if file.endswith(".json"):
            return file
    else:
        logger.fatal("找不到json文件")


class Wallpaper24(object):
    def __init__(self):
        self.wallpaperFile = Settings().wallpaper_file()
        self.cache = PlatformInfo().download_dir()
        self.download_path = PlatformInfo().download_path(".png")
        self.unpackDir = self.cache + self.wallpaperFile.split("/")[-1].split(".")[0]

    def check(self):
        if not os.path.exists(self.cache):
            os.makedirs(self.cache)
        if not os.path.exists(self.unpackDir):
            self.unpack()

    def unpack(self):
        import zipfile
        with zipfile.ZipFile(self.wallpaperFile) as zf:
            zf.extractall(self.unpackDir)

    def get_location(self):
        session = requests.Session()
        session.trust_env = False
        i = 0
        while i < 3:
            try:
                ip = session.get("https://checkip.amazonaws.com/",
                                 timeout=5).text.strip()
                logger.info(f"ip获取成功: {ip}")
                loc = session.get("https://ipapi.co/{}/json/".format(ip),
                                  timeout=5).json()
                latitude = float(loc["latitude"])
                longitude = float(loc["longitude"])
                logger.info(f"经纬度获取成功: ({latitude},{longitude})")
                i = 3
                return self.calculate_sun(latitude, longitude)
            except ConnectionResetError:
                logger.warning(f"本机IP获取失败，第{i + 1}次重试")
                if i == 3:
                    return self.calculate_time(5, 18)
                else:
                    i += 1
            except KeyError:
                logger.warning("API响应错误，使用默认时间")
                i = 3
                return self.calculate_time(5, 18)
            except TypeError:
                logger.warning("该IP获取不到地理坐标，使用默认时间")
                i = 3
                return self.calculate_time(5, 18)
            except requests.exceptions.ReadTimeout:
                logger.warning(f"请求超时,第{i + 1}次重试...")
                if i == 3:
                    return self.calculate_time(5, 18)
                else:
                    i += 1
            except requests.exceptions.ConnectionError:
                logger.warning("无网络连接,使用默认时间")
                i = 3
                return self.calculate_time(5, 18)

    def calculate_sun(self, la, lo):
        dt = DateTime()
        sun_calculator = SunCalculator(dt.Y, dt.M, dt.D, la, lo)
        st = sun_calculator.getSunTimes()
        return self.calculate_time(int(st.sunrise), int(st.sunset))

    def calculate_time(self, sunrise_time, sunset_time):
        sunrise = list(range(sunrise_time, sunrise_time + 4))
        day = list(range(sunrise_time + 4, sunset_time))
        sunset = [x % 24 for x in range(sunset_time, sunset_time + 4)]
        if sunset[-1] < sunrise_time:
            night = list(range(sunset[-1], sunrise_time))
        else:
            night = list(range(sunset_time + 4, 24)) + list(range(0, sunrise_time))
        return self.read_json(sunrise, day, sunset, night)

    def read_json(self, sunrise, day, sunset, night):
        json_name = find_first_json(self.unpackDir)
        with open(self.unpackDir + "/" + json_name, "r") as f:
            theme = json.load(f)

        hour = time.localtime(time.time()).tm_hour

        if hour in sunrise:
            print('sunrise')
            num = len(sunrise) // len(theme["sunriseImageList"])
            index = sunrise.index(hour) // num
            if index >= len(theme["sunriseImageList"]):
                index = -1
            with open(self.unpackDir + "/" + theme["imageFilename"].replace(
                    "*", str(theme["sunriseImageList"][index])), 'rb') as fp:
                data = fp.read()
                return data
        elif hour in day:
            num = len(day) // len(theme["dayImageList"])
            index = day.index(hour) // num
            if index >= len(theme["dayImageList"]):
                index = -1
            with open(self.unpackDir + "/" + theme["imageFilename"].replace(
                    "*", str(theme["dayImageList"][index])), 'rb') as fp:
                data = fp.read()
            return data
        elif hour in sunset:
            num = len(sunset) // len(theme["sunsetImageList"])
            index = sunset.index(hour) // num
            if index >= len(theme["sunsetImageList"]):
                index = -1
            with open(self.unpackDir + "/" + theme["imageFilename"].replace(
                    "*", str(theme["sunsetImageList"][index])), 'rb') as fp:
                data = fp.read()
            return data
        elif hour in night:
            num = len(night) // len(theme["nightImageList"])
            index = night.index(hour) // num
            if index >= len(theme["nightImageList"]):
                index = -1
            with open(self.unpackDir + "/" + theme["imageFilename"].replace(
                    "*", str(theme["nightImageList"][index])), 'rb') as fp:
                data = fp.read()
            return data
        else:
            logger.fatal("壁纸解析出错")

    def run(self):
        self.check()
        return self.get_location()

    @staticmethod
    def name():
        return "24h壁纸"

    @staticmethod
    def layout():
        layout_list = ["updateTimeGroup", "wallpaperFileGroup"]
        return layout_list


if __name__ == "__main__":
    x = Wallpaper24()
    x.run()
