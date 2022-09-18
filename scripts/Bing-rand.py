# source: 必应壁纸(随机)
# updateTime
from setWallpaper import set_wallpaper
from PlatformInfo import PlatformInfo
import requests
import datetime
import os
import shutil
import sys

api_url = "https://bing.ioliu.cn/v1/rand"


def download(path):
    headers = {
        "user-agent":
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    if (sys.argv[6] == "None"):
        img = requests.get(api_url, headers=headers)
    else:
        proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
        img = requests.get(api_url, headers=headers, proxies=proxies)
    with open(path, "wb") as fwi:
        fwi.write(img.content)


def main():
    today = datetime.datetime.utcnow()
    wallpaper_dir = PlatformInfo().getDownloadPath()
    if os.path.exists(wallpaper_dir):
        shutil.rmtree(wallpaper_dir)
    os.makedirs(wallpaper_dir)
    name = wallpaper_dir + today.strftime("%Y%m%d%H%M%S") + ".png"  # windows S
    download(name)
    set_wallpaper(name)


if __name__ == '__main__':
    main()
