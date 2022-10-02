# 🌏earth_wallpaper

### [English](https://github.com/ambition-echo/earth_wallpaper/blob/main/doc/README.md)

实时获取地球照片作为壁纸

不仅仅是地球壁纸

[![Build](https://github.com/ambition-echo/earth_wallpaper/actions/workflows/build.yml/badge.svg)](https://github.com/ambition-echo/earth_wallpaper/actions/workflows/build.yml)
[![Aur](https://github.com/ambition-echo/earth_wallpaper/actions/workflows/aur.yml/badge.svg)](https://github.com/ambition-echo/earth_wallpaper/actions/workflows/aur.yml)
[![pipeline](https://jihulab.com/ambition-echo/earth_wallpaper/badges/main/pipeline.svg)](https://jihulab.com/ambition-echo/earth_wallpaper/commits/main)

[![downloads](https://img.shields.io/github/downloads/ambition-echo/earth_wallpaper/total)](https://github.com/ambition-echo/earth_wallpaper/releases)
[![Release](https://img.shields.io/github/v/release/ambition-echo/earth_wallpaper)](https://github.com/ambition-echo/earth_wallpaper/releases)
[![License](https://img.shields.io/github/license/ambition-echo/earth_wallpaper)](https://github.com/ambition-echo/earth_wallpaper/blob/main/LICENSE)

## 快速开始

### Deepin

到[发布页](https://jihulab.com/ambition-echo/earth_wallpaper/-/releases)下载```earth-wallpaper-deepin-amd64.deb```
安装包，双击安装即可

### Debian/Ubuntu

到[发布页](https://jihulab.com/ambition-echo/earth_wallpaper/-/releases)下载```earth-wallpaper-other-amd64.deb```
安装包，双击安装即可

### Arch

[![AUR version](https://img.shields.io/aur/version/earth-wallpaper-bin)](https://aur.archlinux.org/packages/earth-wallpaper-bin)
[![AUR version](https://img.shields.io/aur/version/earth-wallpaper-nightly)](https://aur.archlinux.org/packages/earth-wallpaper-nightly)

Arch用户可以到[AUR](https://aur.archlinux.org/packages/earth-wallpaper-bin)下载

注意```earth-wallpaper-git```包已经弃用，请安装```earth-wallpaper-nightly```或```earth-wallpaper-bin```包。

### 使用须知

第一次运行时会弹出设置窗口，点击```应用```即可开始运行

## 支持接口

- [x] 向日葵八号
- [x] 风云四号
- [x] 必应壁纸 (调用 [@xCss](https://github.com/xCss/bing) API)
- [x] 动漫壁纸 (调用 [waifu.im](https://waifu.im/) API)
- [x] 本地壁纸 (注：目前Windows下使用本地壁纸，路径需要全英文且无空格)
- [x] 24h壁纸 (灵感来自于[windynamicdesktop](https://github.com/t1m0thyj/windynamicdesktop))

> 24h壁纸推荐下载地址:
>
> [https://github.com/MiniBusiest/24Hour-Wallppe](https://github.com/MiniBusiest/24Hour-Wallppe)
>
> [https://windd.info/themes/index.html](https://windd.info/themes/index.html)

## 接口贡献指南

- 在scripts文件夹下新建python脚本，注意脚本开头写清楚脚本信息
- 第一行，```source```：接口名称
- 第二行，设置界面需要配置项，可选(updateTime/wallpaperDir/wallpaperFile)
- 可用 python 命令行参数：
    1. 屏幕分辨率高
    2. 屏幕分辨率宽
    3. 地球大小
    4. 壁纸文件夹路径
    5. 壁纸文件路径

示例代码：

```python
# source: 风景壁纸
# updateTime

from setWallpaper import set_wallpaper


# 1. 获取壁纸
def get_wallpaper():
    ...


# 2. 设置桌面壁纸
set_wallpaper(绝对路径)
```

## 支持桌面环境

### Linux
- [x] KDE Plasma
- [x] Deepin
- [x] GNOME
- [x] ubuntu:GNOME
- [x] Cinnamon
- [x] XFCE
- [x] MATE
- [x] Cutefish
- [x] LXQt (pcmanfm-qt)
- [x] LXDE (pcmanfm)

### Windows
- [x] Windows 10 (测试环境：Windows 10 专业版 21H1，其他版本自行测试)

## 依赖

- Qt5
- Python3
- qdbus
- python3-pil.imagetk
- python3-requests
- pywin32 (Windows 10 下需要，使用 `pip3 install pywin32` 安装)

## 手动编译安装 （Linux）

- 克隆仓库

```shell
git clone https://jihulab.com/ambition-echo/earth_wallpaper.git
cd earth_wallpaper
mkdir build && cd build
```

- 编译构建

```shell
cmake ..
make
```

- 打包安装

```shell
cd ../package
chmod +x ./package.sh
./package.sh
```

## 开放API

bing 壁纸: [https://github.com/xCss/bing](https://github.com/xCss/bing)

waifu.im 动漫壁纸: [https://waifu.im/](https://waifu.im/)

ipapi 获取ip地理位置：[https://ipapi.co](https://ipapi.co)

## 软件截图

![image-20220917003305855](https://jihulab.com/ambition-echo/img_bed/-/raw/main/img/image-20220917003305855.png)

![image-20220917003345620](https://jihulab.com/ambition-echo/img_bed/-/raw/main/img/image-20220917003345620.png)

![image-20220917003459088](https://jihulab.com/ambition-echo/img_bed/-/raw/main/img/image-20220917003459088.png)

![image-20220917003531050](https://jihulab.com/ambition-echo/img_bed/-/raw/main/img/image-20220917003531050.png)
