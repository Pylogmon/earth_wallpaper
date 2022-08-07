import os
import sys
import json
import time
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
    session = requests.Session()
    session.trust_env = False
    try:
        ip = session.get('https://myip.ipip.net').text.split(" ")[1][3:]
        loc = requests.get("https://ipapi.co/{}/json/".format(ip)).json()
        latitude = loc["latitude"]
        longitude = loc["longitude"]
        calculate_sun(latitude, longitude)
    except ConnectionResetError:
        print("使用默认时间")
        calculate_time(5, 18)
    except KeyError:
        print("使用默认时间")
        calculate_time(5, 18)


def calculate_sun(la, lo):
    dt = DateTime()
    sunCalculator = SunCalculator(dt.Y, dt.M, dt.D, la, lo)
    st = sunCalculator.getSunTimes()
    calculate_time(int(st.sunrise), int(st.sunset))


def calculate_time(sunrise_time, sunset_time):
    sunrise = list(range(sunrise_time, sunrise_time + 4))
    day = list(range(sunrise_time + 4, sunset_time))
    sunset = [x % 24 for x in range(sunset_time, sunset_time + 4)]
    if sunset[-1] < sunrise_time:
        night = list(range(sunset[-1], sunrise_time))
    else:
        night = list(range(sunset_time + 4, 24)) + list(range(0, sunrise_time))
    read_json(sunrise, day, sunset, night)


def read_json(sunrise, day, sunset, night):
    json_name = str(
        os.popen(
            "cd {} && ls *.json".format(unpackDir)).read().splitlines()[0])
    with open(unpackDir + "/" + json_name, "r") as f:
        theme = json.load(f)

    hour = time.localtime(time.time()).tm_hour

    if hour in sunrise:
        print(sunrise)
        num = len(sunrise) // len(theme["sunriseImageList"])
        index = sunrise.index(hour) // num
        if index >= len(theme["sunriseImageList"]):
            index = -1
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace(
            "*", str(theme["sunriseImageList"][index])))
    elif hour in day:
        print(day)
        num = len(day) // len(theme["dayImageList"])
        index = day.index(hour) // num
        if index >= len(theme["dayImageList"]):
            index = -1
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace(
            "*", str(theme["dayImageList"][index])))
    elif hour in sunset:
        print(sunset)
        num = len(sunset) // len(theme["sunsetImageList"])
        index = sunset.index(hour) // num
        if index >= len(theme["sunsetImageList"]):
            index = -1
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace(
            "*", str(theme["sunsetImageList"][index])))
    elif hour in night:
        print(night)
        num = len(night) // len(theme["nightImageList"])
        index = night.index(hour) // num
        if index >= len(theme["nightImageList"]):
            index = -1
        set_wallpaper(unpackDir + "/" + theme["imageFilename"].replace(
            "*", str(theme["nightImageList"][index])))
    else:
        print("Error")


def main():
    check()
    get_location()


if __name__ == "__main__":
    main()
