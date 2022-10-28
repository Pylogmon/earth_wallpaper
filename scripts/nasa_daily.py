# NASA Image of the Day
import requests
import shutil
import sys
import datetime
import os
from setWallpaper import set_wallpaper
from PlatformInfo import PlatformInfo
import xml.etree.ElementTree as ET


def download(path):
    page_link = "https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss"
    rqst = requests.get(page_link)
    if rqst.ok:
        content = rqst.content.decode().strip()
        root = ET.fromstring(content)
        elements = root[0]
        newitem = elements.find('item')
        imginfo = newitem.find('enclosure').attrib
        imageurl = imginfo['url']
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
