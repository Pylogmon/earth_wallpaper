# source: 风云四号
# updateTime earthSize
from PIL import Image
from setWallpaper import set_wallpaper
from PlatformInfo import PlatformInfo
import requests
import datetime
import sys
import os
import shutil

# 屏幕分辨率
Y = int(sys.argv[1])
X = int(sys.argv[2])
SIZE = int(sys.argv[3])

wallpaper_dir = PlatformInfo().getDownloadPath()
if os.path.exists(wallpaper_dir):
    shutil.rmtree(wallpaper_dir)
os.makedirs(wallpaper_dir)
path = wallpaper_dir
name = '1.png'


def download(url, path):

    header = {
        'user-agent':
        'Mozilla/5.0 (X11; Linux x86_64; rv:102.0)Gecko/20100101 Firefox/102.0'
    }
    if (sys.argv[6] == "None"):
        img = requests.get(url, headers=header)
    else:
        proxies = {"http": str(sys.argv[6]), "https": str(sys.argv[6])}
        img = requests.get(url, headers=header, proxies=proxies)
    with open(path, "wb") as fwi:
        fwi.write(img.content)


def concat_images(image_names, name, path):
    image_files = []
    for index in range(2 * 2):
        image_files.append(Image.open(path + image_names[index]))
    target = Image.new('RGB', (687 * 2, 687 * 2))

    for row in range(2):
        for col in range(2):
            target.paste(image_files[2 * row + col],
                         (0 + 687 * col, 0 + 687 * row))
    target.save(path + name, quality=100)  # 成品图保存


def fill_img(download_path, name):
    global X, Y  # 屏幕分辨率
    global SIZE
    height = int(1374.0 / (float(SIZE) * 0.01))
    width = int(height * (float(X) / float(Y)))
    img = Image.open(download_path + name)
    new_img = Image.new(img.mode, (width, height), color='black')
    new_img.paste(img, (int(width / 2 - 687), int(height / 2 - 687)))
    today = datetime.datetime.utcnow()
    name = today.strftime("%Y%m%d%H%M%S")
    new_img.save(path + name + ".png")
    set_wallpaper(path + name + ".png")


def get_time_path():
    global today, path_today

    today = datetime.datetime.utcnow()
    path_today = today.strftime("%Y%m%d%H%M")
    path_today = str((int(path_today) - 10000) -
                     (int(path_today) - 10000) % 100)


def main():
    global today, path_today, path, name
    get_time_path()
    url1 = f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{path_today}00/jpg/1/0/0.png"

    url2 = f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{path_today}00/jpg/1/0/1.png"

    url3 = f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{path_today}00/jpg/1/1/0.png"

    url4 = f"http://rsapp.nsmc.org.cn/swapQuery/public/tileServer/getTile/fy-4a/full_disk/NatureColor/{path_today}00/jpg/1/1/1.png"

    download(url1, path + '1' + name)
    download(url2, path + '2' + name)
    download(url3, path + '3' + name)
    download(url4, path + '4' + name)

    concat_images(['1' + name, '2' + name, '3' + name, '4' + name], name, path)
    fill_img(path, name)


if __name__ == '__main__':
    main()
