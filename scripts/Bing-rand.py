# source: 必应壁纸(随机)
# updateTime
from setWallpaper import set_wallpaper
from PlatformInfo import PlatformInfo
import requests
import datetime
import os
import shutil
import sys
import json
import hashlib

api_url = "https://bing.ioliu.cn/v1/rand?type=json"


def download(path):
    headers = {
        "user-agent":
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    if (sys.argv[6] == "None"):
        imgjson = requests.get(api_url, headers=headers)
    else:
        proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
        imgjson = requests.get(api_url, headers=headers, proxies=proxies)
    img_url = json.loads(imgjson.content.decode())["data"]["url"]
    img_url = img_url.replace("http://h1.ioliu.cn/bing/",
                              "https://www.bing.com/th?id=OHR.")
    img_url = img_url.replace("1920x1080", "UHD")
    img_url = img_url[:-10]
    print(img_url)

    if (sys.argv[6] == "None"):
        img = requests.get(img_url, headers=headers)
    else:
        proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
        img = requests.get(img_url, headers=headers, proxies=proxies)
    with open(path, "wb") as fwi:
        fwi.write(img.content)
    with open(path, 'rb') as fp:
        data = fp.read()
    md5 = hashlib.md5(data).hexdigest()
    if (md5 == "f0f7d2c575a576fcbe5904900906e27a"):
        return False
    else:
        return True


def main():
    today = datetime.datetime.utcnow()
    wallpaper_dir = PlatformInfo().getDownloadPath()
    if os.path.exists(wallpaper_dir):
        shutil.rmtree(wallpaper_dir)
    os.makedirs(wallpaper_dir)
    name = wallpaper_dir + today.strftime("%Y%m%d%H%M%S") + ".png"  # windows S
    while (True):
        if (download(name)):
            break
    set_wallpaper(name)


if __name__ == '__main__':
    main()
