# source: 本地壁纸
# updateTime wallpaperDir
import sys
import os
from setWallpaper import set_wallpaper

wallpaperDir = sys.argv[4]
currentFile = wallpaperDir + "/current.txt"

currentWallpaper = "None"
exts = [".png", ".jpg", "jpeg", ".gif"]

if os.path.exists(currentFile):
    with open(currentFile, 'r') as f:
        currentWallpaper = f.readline()
else:
    files = os.listdir(wallpaperDir)
    for i in files:
        if i[-4:] in exts:
            set_wallpaper(wallpaperDir + "/" + i)
            with open(currentFile, 'w') as f:
                f.write(i)
            break
        else:
            continue

files = os.listdir(wallpaperDir)
flag = False
for i in files:
    if flag:
        if i[-4:] in exts:
            set_wallpaper(wallpaperDir + "/" + i)
            with open(currentFile, 'w') as f:
                f.write(i)
            break
        else:
            continue
    else:
        if i == currentWallpaper:
            flag = True
else:
    for i in files:
        if i[-4:] in exts:
            set_wallpaper(wallpaperDir + "/" + i)
            with open(currentFile, 'w') as f:
                f.write(i)
            break
        else:
            continue
