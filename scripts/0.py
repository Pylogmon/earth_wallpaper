from PIL import Image
import requests
import datetime
import sys

# 屏幕分辨率
Y = sys.argv[2]
X = sys.argv[3]
# 存储路径
path = '/home/hgy/Desktop/'

name = 'wallpaper.png'


# 下载图像
def download(url, path):
    img = requests.get(url)
    with open(path, "wb") as fwi:
        fwi.write(img.content)


# 填充黑色适配屏幕尺寸
def fill_img(path):
    global X, Y  # 屏幕分辨率

    img = Image.open(path)
    new_img = Image.new(img.mode, (X, Y), color='black')
    new_img.paste(img, (int(X / 2 - 250), int(Y / 2 - 250)))
    new_img.save(path)


def get_time_path():
    global today, path_today

    today = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
    path_today = today.strftime("%Y/%m/%d/%H%M")
    temp_list = list(path_today)
    temp_list[-1] = "0"
    path_today = "".join(temp_list)


def main():
    global today, path_today, path, name

    get_time_path()
    url = f"https://himawari8-dl.nict.go.jp/himawari8/\
        img/D531106/1d/550/{path_today}00_0_0.png"

    # name = "00_0_0.png"
    download(url, path + name)
    fill_img(path + name)


if __name__ == '__main__':
    main()
