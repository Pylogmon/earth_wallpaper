# source: 动漫壁纸
# updateTime

from setWallpaper import set_wallpaper
from PlatformInfo import PlatformInfo
import requests
import datetime
import json
import os
import shutil

request_url = "https://api.waifu.im/random?orientation=LANDSCAPE"
global img_url


def get_img_url():
    res = requests.get(request_url).text
    res = json.loads(res)
    return {
        "img_url": res["images"][0]["url"],
        "img_ext": res["images"][0]["extension"]
    }


def download(url, ext):
    img = requests.get(url)
    today = datetime.datetime.utcnow()
    wallpaper_dir = PlatformInfo().getDownloadPath()
    if os.path.exists(wallpaper_dir):
        shutil.rmtree(wallpaper_dir)
    os.makedirs(wallpaper_dir)
    path = wallpaper_dir + today.strftime("%Y%m%d%H%M%S") + ext
    with open(path, "wb") as fwi:
        fwi.write(img.content)
    set_wallpaper(path)


def main():
    res = get_img_url()
    download(res["img_url"], res["img_ext"])


if __name__ == "__main__":
    main()
