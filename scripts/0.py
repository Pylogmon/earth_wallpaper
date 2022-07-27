from PIL import Image
import requests
import datetime
import sys
import os
# 屏幕分辨率
Y = int(sys.argv[1])
X = int(sys.argv[2])
SIZE = int(sys.argv[3])
DE = os.getenv('XDG_CURRENT_DESKTOP')
# 存储路径
path = '/tmp/'

name = '0.png'


# 下载图像
def download(url, path):
    img = requests.get(url)
    with open(path, "wb") as fwi:
        fwi.write(img.content)


# 填充黑色适配屏幕尺寸
def fill_img(path):
    global X, Y  # 屏幕分辨率
    height = int(500.0 / (float(SIZE) * 0.01))
    width = int(height * (float(X) / float(Y)))
    img = Image.open(path)
    new_img = Image.new(img.mode, (width, height), color='black')
    new_img.paste(img, (int(width / 2 - 250), int(height / 2 - 250)))
    today = datetime.datetime.utcnow()
    name = today.strftime("%Y%m%d%H%M%s")
    new_img.save(path + name + ".png")
    set_wallpaper(path + name + ".png")


def get_time_path():
    global today, path_today

    today = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
    path_today = today.strftime("%Y/%m/%d/%H%M")
    temp_list = list(path_today)
    temp_list[-1] = "0"
    path_today = "".join(temp_list)


def set_wallpaper(file):
    if (DE == "Deepin"):
        os.system("export primary_screen=\
                (xrandr|grep 'connected primary'|awk '{print $1}')"                                                                   )
        primary_screen = os.getenv('primary_screen')
        dbus = f"dbus-send --dest=com.deepin.daemon.Appearance \
            /com/deepin/daemon/Appearance --print-reply \
                com.deepin.daemon.Appearance.SetMonitorBackground \
                    string:\"{primary_screen}\" string:\"file:/{file}\""

        os.system(dbus)
    elif (DE == "KDE"):
        print(file)
        dbus = f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {{d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file://{file}\")}}'"
        os.system(dbus)
    else:
        print("该桌面环境暂不支持")


def main():
    global today, path_today, path, name

    get_time_path()
    url = f"https://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/{path_today}00_0_0.png"

    # name = "00_0_0.png"
    download(url, path + name)
    fill_img(path + name)


if __name__ == '__main__':
    main()
