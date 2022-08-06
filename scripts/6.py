import os
import sys
import json
import time
import math
from setWallpaper import set_wallpaper
from sunCalculator import SunCalculator, DateTime
import requests

file = sys.argv[1]
unpackDir = "/tmp/" + file.split("/")[-1].split(".")[0]


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
    dt = DateTime()
    sunCalculator = SunCalculator(dt.Y, dt.M, dt.D, la, lo)
    st = sunCalculator.getSunTimes()
    sunrise_time = int(st.sunrise)
    sunset_time = int(st.sunset)

    sunrise = list(range(sunrise_time, sunrise_time + 4))
    day = list(range(sunrise_time + 4, sunset_time))
    sunset = [x % 24 for x in range(sunset_time, sunset_time + 4)]
    if sunset[-1] < sunrise_time:
        night = list(range(sunset[-1], sunrise_time))
    else:
        night = list(range(sunset_time + 4, 24)) + list(range(0, sunrise_time))
    read_json(sunrise, day, sunset, night)


def read_json(sunrise, day, sunset, night):
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
