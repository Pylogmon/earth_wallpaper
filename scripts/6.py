import os
import sys
import json
import time
import math
from setWallpaper import set_wallpaper
import requests

file = sys.argv[1]
unpackDir = "/tmp/" + file.split("/")[-1].split(".")[0]
hours = list(range(0, 24))
sunrise = []
day = []
sunset = []
night = []


def check():
    if not os.path.exists(unpackDir):
        unpack()


def unpack():
    import zipfile
    with zipfile.ZipFile(file) as zf:
        zf.extractall(unpackDir)


def get_location():
    ip = requests.get('https://myip.ipip.net', timeout=5).text.split(" ")[1][3:]
    loc = json.loads(
        requests.get('https://api.ipbase.com/v2/info?apikey=hNJIYCzO8Enm5SiGtas9o6WAHpl33TR5xLDt2QtP&ip=' + ip,
                     timeout=5).text)
    latitude = loc["data"]["location"]["latitude"]
    longitude = loc["data"]["location"]["longitude"]
    calculate_sun(latitude, longitude)


def calculate_sun(la, lo):
    # TODO calculate the sunrise time and sunset time

    sunrise_time = 5
    sunset_time = 18  # 由上面计算得出
    for i in hours:
        if i < sunrise_time:
            night.append(i)
        elif sunrise_time <= i < sunrise_time + 4:
            sunrise.append(i)
        elif sunrise_time + 4 <= i < sunset_time:
            day.append(i)
        elif sunset_time <= i < sunset_time + 4:
            sunset.append(i)
        else:
            night.append(i)
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
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace(
            "*", str(theme["sunriseImageList"][index])))
    elif hour in day:
        num = math.ceil(len(day) / len(theme["dayImageList"]))
        index = day.index(hour) // num
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace(
            "*", str(theme["dayImageList"][index])))
    elif hour in sunset:
        num = math.ceil(len(sunset) / len(theme["sunsetImageList"]))
        index = sunset.index(hour) // num
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace(
            "*", str(theme["sunsetImageList"][index])))
    elif hour in night:
        num = math.ceil(len(night) / len(theme["nightImageList"]))
        index = night.index(hour) // num
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace(
            "*", str(theme["nightImageList"][index])))
    else:
        print("Error")


def main():
    check()
    get_location()


if __name__ == "__main__":
    main()
