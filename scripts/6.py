import os
import sys
import json
import time
import math
from setWallpaper import set_wallpaper

file = sys.argv[1]
unpackDir = "/tmp/" + file.split("/")[-1].split(".")[0]

sunrise = [5, 6, 7, 8]
day = [9, 10, 11, 12, 13, 14, 15, 16, 17]
sunset = [18, 19, 20]
night = [21, 22, 23, 0, 1, 2, 3, 4]


def check():
    if not os.path.exists(unpackDir):
        unpack()


def unpack():
    import zipfile
    with zipfile.ZipFile(file) as zf:
        zf.extractall(unpackDir)


def main():
    check()
    read_json()


def read_json():
    with open(unpackDir + "/theme.json", "r") as f:
        theme = json.load(f)

    hour = time.localtime(time.time()).tm_hour
    minute = time.localtime(time.time()).tm_min

    if minute > 30:
        hour += 1

    if hour in sunrise:
        num = math.ceil(len(sunrise) / len(theme["sunriseImageList"]))
        index = sunrise.index(hour) // num
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace("*", str(theme["sunriseImageList"][index])))
    elif hour in day:
        num = math.ceil(len(day) / len(theme["dayImageList"]))
        index = day.index(hour) // num
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace("*", str(theme["dayImageList"][index])))
    elif hour in sunset:
        num = math.ceil(len(sunset) / len(theme["sunsetImageList"]))
        index = sunset.index(hour) // num
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace("*", str(theme["sunsetImageList"][index])))
    elif hour in night:
        num = math.ceil(len(night) / len(theme["nightImageList"]))
        index = night.index(hour) // num
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace("*", str(theme["nightImageList"][index])))
    else:
        print("Error")


if __name__ == "__main__":
    main()
