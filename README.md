# 🌏earth_wallpaper

### [English](https://github.com/ambition-echo/earth_wallpaper/blob/main/doc/README.md)

实时获取地球照片作为壁纸(Linux Only)

不仅仅是地球壁纸

[![Deb](https://github.com/ambition-echo/earth_wallpaper/actions/workflows/deb.yml/badge.svg)](https://github.com/ambition-echo/earth_wallpaper/actions/workflows/deb.yml)
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

Arch用户可以到[AUR](https://aur.archlinux.org/packages/earth-wallpaper-bin)下载

### 使用须知

第一次运行时会弹出设置窗口，点击```应用```即可开始运行

## 支持接口

- [x] 向日葵八号
- [x] 风云四号
- [x] 必应壁纸(调用 [@xCss](https://github.com/xCss/bing) API)
- [x] 动漫壁纸(调用 [waifu.im](https://waifu.im/) API)
- [x] 本地壁纸
- [x] 24h壁纸(灵感来自于[windynamicdesktop](https://github.com/t1m0thyj/windynamicdesktop))

> 24h壁纸推荐下载地址:
>
> [https://github.com/MiniBusiest/24Hour-Wallppe](https://github.com/MiniBusiest/24Hour-Wallppe)
>
> [https://windd.info/themes/index.html](https://windd.info/themes/index.html)

## 支持桌面环境

- [x] KDE Plasma
- [x] Deepin
- [x] GNOME
- [x] ubuntu:GNOME
- [x] Cinnamon
- [x] XFCE

## 依赖

- Qt5
- Python3
- qdbus
- python3-pil.imagetk
- python3-requests

## 手动编译安装

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

myip 获取ip地址：[https://myip.ipip.net](https://myip.ipip.net)

ipbase 获取ip地理位置：[https://api.ipbase.com](https://api.ipbase.com)

## 软件截图

![Image20220729131452](https://jihulab.com/ambition-echo/img_bed/raw/main/img/Image20220729131452.png)

![Image20220729131537](https://jihulab.com/ambition-echo/img_bed/-/raw/main/img/Image20220729131537.png)

![Image20220729131605](https://jihulab.com/ambition-echo/img_bed/raw/main/img/Image20220729131605.png)
