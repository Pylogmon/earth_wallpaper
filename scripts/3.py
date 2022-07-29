from setWallpaper import set_wallpaper
from checkWakkpaperDir import check
import requests
import datetime
import sys

height = int(sys.argv[1])
width = int(sys.argv[2])

api_url = "http://bing.ioliu.cn/v1"


def download(path):
    headers = {
        "user-agent":
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    body = {"w": width * 2, "h": height * 2}
    img = requests.get(api_url, headers=headers, data=body)
    with open(path, "wb") as fwi:
        fwi.write(img.content)


def main():
    check()
    today = datetime.datetime.utcnow()
    name = "/tmp/earth-wallpaper/" + today.strftime("%Y%m%d%H%M%s") + ".png"
    download(name)
    set_wallpaper(name)


if __name__ == '__main__':
    main()
