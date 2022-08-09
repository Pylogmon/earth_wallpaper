# source: 必应壁纸(随机)
# updateTime
from setWallpaper import set_wallpaper
import requests
import datetime
import os
import shutil

api_url = "https://bing.ioliu.cn/v1/rand"


def download(path):
    headers = {
        "user-agent":
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    img = requests.get(api_url, headers=headers)
    with open(path, "wb") as fwi:
        fwi.write(img.content)


def main():
    today = datetime.datetime.utcnow()
    home = os.getenv("HOME")
    wallpaper_dir = home + '/.cache/earth-wallpaper/wallpaper/'
    if os.path.exists(wallpaper_dir):
        shutil.rmtree(wallpaper_dir)
    os.makedirs(wallpaper_dir)
    name = wallpaper_dir + today.strftime("%Y%m%d%H%M%s") + ".png"
    download(name)
    set_wallpaper(name)


if __name__ == '__main__':
    main()
