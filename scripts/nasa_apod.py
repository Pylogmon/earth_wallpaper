# source: NASA每日天文图片
# updateTime
import requests
import shutil
import sys
import datetime
import os
from setWallpaper import set_wallpaper
from PlatformInfo import PlatformInfo
from html.parser import HTMLParser


class MyParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.mytag = []
        self.myattr = []
        self.mydata = []

    def handle_starttag(self, tag, attrs):
        self.mytag.append(tag)
        self.myattr.append(attrs)

    def handle_data(self, data):
        self.mydata.append(data)


def download(path):
    page_link = "https://apod.nasa.gov/apod/"
    if (sys.argv[6] == "None"):
        rqst = requests.get(page_link)
    else:
        proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
        rqst = requests.get(page_link, proxies=proxies)
    if rqst.ok:
        content = rqst.content.decode().strip()
        parser = MyParser()
        parser.feed(content)
        imgattr = [b for a, b in zip(parser.mytag, parser.myattr) if a == 'img'][0]
        imageurl = page_link + [b for a, b in imgattr if a == 'src'][0]
        if (sys.argv[6] == "None"):
            imager = requests.get(imageurl)
        else:
            proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
            imager = requests.get(imageurl, proxies=proxies)
        with open(path, 'wb') as f:
            f.write(imager.content)
    else:
        raise ValueError('Fetching website failed.')
    return


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
