<p align="center">
  <a href="#">
  </a>
  <p align="center">
   <img width="150" height="150" src="../assets/earth-wallpaper.png" alt="Logo">
  </p>
  <h1 align="center"><b>earth-wallpaper</b></h1>
  <p align="center">
  Simple and easy to use multifunctional wallpaper software
    <br />
  </p>
</p>
<div align="center">

[![downloads](https://img.shields.io/github/downloads/ambition-echo/earth_wallpaper/total)](https://github.com/ambition-echo/earth_wallpaper/releases)
[![Release](https://img.shields.io/github/v/release/ambition-echo/earth_wallpaper)](https://github.com/ambition-echo/earth_wallpaper/releases)
[![License](https://img.shields.io/github/license/ambition-echo/earth_wallpaper)](https://github.com/ambition-echo/earth_wallpaper/blob/main/LICENSE)
[![Visitor](https://visitor-badge.glitch.me/badge?page_id=ambition-echo.earth_wallpaper)](https://github.com/ambition-echo/earth_wallpaper)

[![PyPI](https://img.shields.io/pypi/v/earth-wallpaper?logo=python)](https://pypi.org/project/earth-wallpaper/)
[![AUR version](https://img.shields.io/aur/version/earth-wallpaper-bin?label=earth-wallpaper-bin&logo=archlinux)](https://aur.archlinux.org/packages/earth-wallpaper-bin)
[![AUR version](https://img.shields.io/aur/version/earth-wallpaper-nightly?label=earth-wallpaper-nightly&logo=archlinux)](https://aur.archlinux.org/packages/earth-wallpaper-nightly)
## [中文](https://github.com/ambition-echo/earth_wallpaper#readme)
</div>
<br/>

## Install

### Linux

#### Debian

Download `earth-wallpaper-amd64.deb` and install via apt or dpkg

#### Arch

Install from [AUR](https://aur.archlinux.org/packages?O=0&K=earth-wallpaper-)

### Windows

Install via pip
need python3 installed

```shell
pip install earth-wallpaper # install
pip install earth-wallpaper --upgrade #update
```

### Usage Notice

When you run it for the first time, the settings window will pop up, click ```Apply``` to start running

## Support Interface

- [x] Himawari-8 (Weather satellites from Japan)
- [x] FY-4A (Weather satellites from China)
- [x] Bing Wallpaper (Call [@xCss](https://github.com/xCss/bing) API)
- [x] Anime Wallpaper (Call [waifu.im](https://waifu.im/) API)
- [x] Local Wallpaper
- [x] 24h Wallpaper (Inspired by [windynamicdesktop](https://github.com/t1m0thyj/windynamicdesktop))
- [x] wallhaven.cc ([wallhaven.cc](https://wallhaven.cc))

> 24h Wallpaper recommended download address:
>
> [https://github.com/MiniBusiest/24Hour-Wallppe](https://github.com/MiniBusiest/24Hour-Wallppe)
>
> [https://windd.info/themes/index.html](https://windd.info/themes/index.html)

## Supported Desktop Environment

### Linux

- [x] KDE Plasma
- [x] Deepin
- [x] GNOME
- [x] ubuntu:GNOME
- [x] Cinnamon
- [x] XFCE
- [x] MATE
- [x] Cutefish
- [x] LXQt (pcmanfm-qt 或者 pcmanfm)
- [x] LXDE (pcmanfm)
- [x] Custom script

### Windows

- [x] Windows 10

## Depends

- Pillow
- PySide6
- requests
- setuptools
- pywin32 (Only Windows)

## Install Manually

```shell
git clone https://jihulab.com/ambition-echo/earth_wallpaper.git
cd earth_wallpaper
python3 setup.py install
```

## Public API

bing: [https://github.com/xCss/bing](https://github.com/xCss/bing)

waifu.im: [https://waifu.im/](https://waifu.im/)

ipapi: [https://ipapi.co](https://ipapi.co)

wallhaven: [https://wallhaven.cc/help/api](https://wallhaven.cc/help/api)

## ScreenShot

![bing](./assets/bing.png)

![wallpaper24](./assets/wallpaper24.png)

![fengyun4](./assets/fengyun4.png)

![wallhaven](./assets/wallhaven.png)