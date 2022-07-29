# earth_wallpaper

实时获取地球照片作为壁纸(Linux Only)

## 快速开始

到[发布页](https://jihulab.com/ambition-echo/earth_wallpaper/-/releases)下载最新版安装包，双击安装即可

第一次运行时会弹出设置窗口，点击```应用```即可开始运行

## 基础功能

- [x] 自动获取地球照片
- [x] 设置地球显示大小
- [x] 定时更新壁纸

## 支持接口

- [x] 向日葵八号
- [x] 风云四号
- [x] 必应壁纸([@xCss](https://github.com/xCss/bing)提供接口)

## 支持桌面环境

- [x] KDE
- [x] Deepin
- [x] Gnome

## 依赖

- Qt5
- Python3
  - pillow
  - requests

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

bing: [https://github.com/xCss/bing](https://github.com/xCss/bing)

## 软件截图

![image-20220725124921280](https://jihulab.com/ambition-echo/img_bed/raw/main/img/image-20220725124921280.png)

![image-20220725124950954](https://jihulab.com/ambition-echo/img_bed/raw/main/img/image-20220725124950954.png)