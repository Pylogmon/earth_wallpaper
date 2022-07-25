from PIL import Image
import requests
import datetime
import sys
import os
# 屏幕分辨率
Y = sys.argv[1]
X = sys.argv[2]
SIZE = sys.argv[3]
DE = os.getenv('XDG_CURRENT_DESKTOP')
path = '/tmp/'
name = '1.png'


def download(url, path):
    img = requests.get(
        url,
        headers={
            'user-agent':
            'Mozilla/5.0 (X11; Linux x86_64; rv:102.0)Gecko/20100101 Firefox/102.0'
        })
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


def fill_img(path, name):
    global X, Y  # 屏幕分辨率
    global SIZE
    height = int(float(Y) / (float(SIZE) * 0.01))
    width = int(height * (float(X) / float(Y)))
    img = Image.open(path + name)
    new_img = Image.new(img.mode, (width, height), color='black')
    new_img.paste(img, (int(width / 2 - 687), int(height / 2 - 687)))
    today = datetime.datetime.utcnow()
    name = today.strftime("%Y%m%d%H%M%s")
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


def set_wallpaper(file):
    if (DE == "Deepin"):
        os.system("export primary_screen=\
                (xrandr|grep 'connected primary'|awk '{print $1}')")
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


if __name__ == '__main__':
    main()
