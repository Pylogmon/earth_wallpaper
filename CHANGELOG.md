# CHANGELOG
## 1.8.0 (2022-09-14)

### New feature:

- **about**: 添加检查更新功能([`69c031a`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/69c031ad7083bafab21bf54bd4353e8226f77228)) (by ambition_echo)

- **scripts**: 添加Windows10支持([`#8`](https://github.com/ambition-echo/earth_wallpaper/pull/8)) (by Ccslykx)

### Bugs fixed:

- **scripts**: 修复timeout问题([`21a4015`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/21a40155d6d3267950e908f7d323d5ae4e23f113)) (by ambition_echo)

## 1.7.6 (2022-09-09)

### New feature:

- **scripts**: 添加XFQT桌面支持([`e28fc11`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/e28fc11cc3b5ef7209f172465339db06ebd93966)) (by ambition_echo)

### Bugs fixed:

- **scripts/package**: 删除LXQt,修复dbus-python依赖([`f74ceab`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/f74ceab9f83f9100f688d0886de4110b7bb6c648)) (by ambition_echo)

## 1.7.5 (2022-09-05)

### New feature:

- **scripts**: 支持MATE桌面环境([`1942db0`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/1942db060c44f38c2c27e32cdcebb29cfd2d0312)) (by ambition_echo)

### Bugs fixed:

- **scripts**: 修复MATE桌面设置壁纸失败([`2cece82`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/2cece821e6130fda689f37b4a75648e093e1d38d)) (by ambition_echo)
- **scripts**: 修复dbus导入错误([`4fb73ee`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/4fb73eeb41a59209b3bd047ca10457f6abc01ce6)) (by ambition_echo)
- **scripts**: 修复24h壁纸无网络状态下更新失败([`f1e557f`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/f1e557f547f5f2086667458de20caa95ba1526e0)) (by ambition_echo)

## 1.7.4 (2022-09-01)

### Bugs fixed:

- **package**: 修复aur nightly包依赖缺失([`0528648`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/05286483f6649470eabb622824ebaa2eb719a335)) (by ambition_echo)

## 1.7.3 (2022-08-12)

### Bugs fixed:

- **scripts**: 删除无效引用([`b3b0403`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/b3b0403bc57999dbee7392eb956fc550b5ddc60c)) (by ambition_echo)
- **scripts**: 删除无用import([`10bb4fd`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/10bb4fdf955336955df14446a72f22fb023c7345)) (by ambition_echo)
- **scripts/src**: 获取Ipv4地址([`3cd11d6`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/3cd11d685b97ba21e0b43aba3547c68a20c209e7)) (by ambition_echo)

## 1.7.2 (2022-08-09)

### Bugs fixed:

- **scripts/src**: 修改当前壁纸保存路径，防止重启后壁纸消失([`46206b9`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/46206b9fe4ffe3ac92fecb199cd96f06ddb094fc)) (by ambition_echo)

### Performance improves:

- **scripts**: 删除获取ip步骤，改为api自动获取([`4540524`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/4540524c22e394c2af9a8e87d89fd2ba85bb3136)) (by ambition_echo)

## 1.7.1 (2022-08-08)

### Bugs fixed:

- **scripts**: 更换获取公网ip接口([`09475da`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/09475da13743b33e56d069aef0971ff04e0a65e6)) (by ambition_echo)
- **scripts**: 修复某些IP无法获取到坐标的问题([`2f6d837`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/2f6d837f9b8866ad23511d08a808922a08ec58d6)) (by ambition_echo)

## 1.6.5 (2022-08-07)

### Bugs fixed:

- **scripts**: 修改IP地理位置api为ipapi.co([`2d771ee`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/2d771eef1c20a808a7c55582165829b290beccfa)) (by ambition_echo)
- **scripts**: 修复ipbase API失效问题([`080c283`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/080c283cd19218eb3b12cabbf943c783455a82cd)) (by ambition_echo)

### Performance improves:

- **scripts**: 删除时间进位([`0ba2072`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/0ba20726911a7c014265dd8b7ef29a679bfabce7)) (by ambition_echo)

## 1.6.4 (2022-08-06)

### Bugs fixed:

- **scripts**: 修复时段计算错误([`cadbbc5`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/cadbbc59b26b4d58d7eebb522cafb2a8e043fa06)) (by ambition_echo)

## 1.6.3 (2022-08-06)

### Bugs fixed:

- **scripts**: 识别其他命名json文件([`c9f30ba`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/c9f30bac478062bd993bb2f10ba87de918bbbbc6)) (by ambition_echo)

### Performance improves:

- **scripts**: 修改区间计算算法([`f9d5681`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/f9d56816f0420bba7f555f95317e0fcfce4477cf)) (by ambition_echo)

## 1.6.2 (2022-08-05)

### Bugs fixed:

- **package**: 修复aur包名([`8a593b6`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/8a593b60fb041ab930e677871420c4390247ae91)) (by ambition_echo)

## 1.6.1 (2022-08-05)

### New feature:

- **scripts**: 添加根据ip获取日出日落时间([`de1debe`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/de1debe5dde1fc5be7115c19cee99ee594477bf2)) (by ambition_echo)

### Bugs fixed:

- **package**: 修复aur二进制包命名相同无法更新的问题([`6fbe3ef`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/6fbe3ef2649c35ca52689c57a6b4e50f19a1658c)) (by ambition_echo)

### Performance improves:

- **Config**: 修改24h壁纸时的更新频率为10分钟([`8d9cef5`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/8d9cef543434e49203b954ea6d25f32152665c04)) (by ambition_echo)
- **scripts**: 修改时段计算方法，提升效率([`3d50835`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/3d50835bd84106e9a8bd40f4ca7cd0e169558edc)) (by ambition_echo)

## 1.6.0 (2022-08-05)

### New feature:

- **scripts**: 添加24h壁纸选项([`21f4ef1`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/21f4ef149aeabb2af79651dfc24fdf1c03e8ea8e)) (by ambition_echo)

### Bugs fixed:

- **Config**: 修复设置路径问题([`b5cbdd5`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/b5cbdd5a051cf85d34d47e5be467c236fa9f3606)) (by ambition_echo)

### BREAKING CHANGES:

- 兼容常规24h壁纸json格式