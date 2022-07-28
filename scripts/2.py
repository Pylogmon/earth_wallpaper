from PIL import Image
from setWallpaper import set_wallpaper
import requests
import datetime
import sys
import json

api_url = "https://api.waifu.im/random"


def get_img_url():
    res = requests.get(api_url).text
    print(res)
    res_json = json.loads(requests.get(api_url).text)
    return [res_json["images"][0]["url"], res_json["images"][0]["extension"]]


def download(url, path):
    img = requests.get(url)
    with open(path, "wb") as fwi:
        fwi.write(img.content)


def main():
    today = datetime.datetime.utcnow()
    img_info = get_img_url()
    name = "/tmp/" + today.strftime("%Y%m%d%H%M%s") + img_info[1]
    download(img_info[0], name)


if __name__ == '__main__':
    main()
