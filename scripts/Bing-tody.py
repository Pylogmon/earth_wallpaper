# source: 必应壁纸(今日)
# updateTime
from setWallpaper import set_wallpaper
from PlatformInfo import PlatformInfo
import requests
import datetime
import os
import shutil
from requests.structures import CaseInsensitiveDict
import json
import sys

bing_addr = "https://www.bing.com"
json_link = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"


def download(path):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    if (sys.argv[6] == "None"):
        resp = requests.get(json_link, headers=headers)
    else:
        proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
        resp = requests.get(json_link, headers=headers, proxies=proxies)
    if resp.ok:
        webjson = json.loads(resp.content.decode())
        imageurl = (bing_addr + webjson['images'][0]['url']).replace(
            "1920x1080", "UHD")
        if (sys.argv[6] == "None"):
            imager = requests.get(imageurl)
        else:
            proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
            imager = requests.get(imageurl, proxies=proxies)

        with open(path, 'wb') as f:
            f.write(imager.content)
    else:
        raise ValueError('Fetching website failed.')


def main():
    today = datetime.datetime.utcnow()
    wallpaper_dir = PlatformInfo().getDownloadPath()
    if os.path.exists(wallpaper_dir):
        shutil.rmtree(wallpaper_dir)
    os.makedirs(wallpaper_dir)
    name = wallpaper_dir + today.strftime("%Y%m%d%H%M%S") + ".png"
    download(name)
    set_wallpaper(name)


if __name__ == '__main__':
    main()
