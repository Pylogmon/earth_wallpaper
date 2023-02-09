# CHANGELOG

## 2.2.0 (2023-02-09)

### New feature:

- wallhaven 添加最小尺寸选择，扩展wallhaven壁纸随机范围([`e1b4139`](https://github.com/ambition-echo/earth_wallpaper/commit/e1b413903bddbc8147d5b828edd38ade25fcf010)) (by ambition-echo)

### Bugs fixed:

- 适配最新版gnome([`1c317cb`](https://github.com/ambition-echo/earth_wallpaper/commit/1c317cbb18a82a63793e00171b442f7781fe4194)) (by ambition-echo)

## 2.1.9 (2023-02-01)

### Bugs fixed:

- 修复windows无法保存壁纸的问题([`cf6229e`](https://github.com/ambition-echo/earth_wallpaper/commit/cf6229e1c391918e068f029d9872cecade9f89ae)) (by ambition-echo)
- 修复多显示器设置失败问题([`3d86a0c`](https://github.com/ambition-echo/earth_wallpaper/commit/3d86a0ce829c004546ab3f36d135da4e05a1805e)) (by ambition_echo)

## 2.1.7 (2022-12-02)

### Bugs fixed:

- 修复向日葵八号获取不到图片的问题([`3a558aa`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/3a558aa5f4da9812952c1a9b8b3d5897b28999c4)) (by 派了个萌)
- 修复向日葵八号壁纸没有填充的问题([`2bab7a0`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/2bab7a0c00377d0830d77dc76c628ce326eff12a)) (by 派了个萌)
- 修复对话框没有图标([`2b0d15d`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/2b0d15d5af5f7a508f2f0b193ada935c7987caa5)) (by ambition_echo)
- 修复windows壁纸设置失效的问题([`576b55f`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/576b55f806f424dc18b51431d34c8d2fafbcedf1)) (by ambition_echo)

## 2.1.6 (2022-11-27)

### New feature:

- 添加缓存大小显示功能([`5800aad`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/5800aada1e60d970e0096af92e0512d9aa7bab0d)) (by ambition_echo)

### Bugs fixed:

- 修复windows任务栏图标问题([`46a7984`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/46a7984d40f4828f6167b10bbb4b4e5c6fc0acd4)) (by ambition_echo)

## 2.1.5 (2022-11-26)

### Bugs fixed:

- **about**: 完善主线程异常处理([`3e8c7c2`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/3e8c7c21df5c1898e163a3e1d32b4369ae6cc72e)) (by ambition_echo)
- **main**: 修复import路径([`da12a01`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/da12a01eba11df49d9aab48b58a2a4a5210f852f)) (by ambition_echo)

### Revert:

- revert [`1af7849`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/1af7849e), refactor: 改用pyside2([`e7f00a8`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/e7f00a886fb755760187f6390aa3ad573e4a01be))

## 2.1.4 (2022-11-24)

### New feature:

- **setWallpaper**: 添加外部脚本，解决无法识别的桌面的壁纸设置问题([`e62ae07`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/e62ae076fa3b34ef079853d5c03d115e2faa661d)) (by ambition_echo)

### Bugs fixed:

- **ci**: 改用ubuntu20.04进行打包([`60d791a`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/60d791a95707e5f4e2f2a9369ce8852afe3388dc)) (by 派了个萌)

## 2.1.3 (2022-11-23)

### New feature:

- **wallhaven**: 添加搜索关键词和颜色选项([`879296f`](https://github.com/ambition-echo/earth_wallpaper/commit/879296fc690c4e583daec69a030cc5042622ebe8)) (by ambition_echo)

### Bugs fixed:

- **proxy**: 修复socks5代理设置无效的问题([`2594125`](https://github.com/ambition-echo/earth_wallpaper/commit/2594125281010940a62d94ad28a87d8e45e0698f)) (by ambition_echo)

## 2.1.2 (2022-11-22)

### New feature:

- **config**: 新增删除缓存功能([`d484a42`](https://github.com/ambition-echo/earth_wallpaper/commit/d484a42ca7cb2a371ec8ba8fe97fcbb4f45564c1)) (by ambition_echo)

### Bugs fixed:

- **deb**: 修复control格式([`97b410f`](https://github.com/ambition-echo/earth_wallpaper/commit/97b410fa174a6596220a51b7a95ca6810b83cfa1)) (by ambition_echo)
- **package**: 修复deb包依赖([`aa3b7df`](https://github.com/ambition-echo/earth_wallpaper/commit/aa3b7df50cc20be946ab400eb6bfef52d63c2bb3)) (by ambition_echo)
- **wallhaven**: 只获取横版图片([`c8771a0`](https://github.com/ambition-echo/earth_wallpaper/commit/c8771a02aad12023c6b8e1c6d0e5f654b2d4e603)) (by ambition_echo)

## 2.1.1 (2022-11-22)

### Bugs fixed:

- **ci**: 修复打包脚本导致的版本异常问题([`8632db8`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/8632db88a2ecf174100e2e829bbdc13ee52c0236)) (by ambition_echo)

## 2.1.0 (2022-11-22)

### New feature:

- **save_img**: 不再每次删除cache([`5be4c88`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/5be4c884fa234add28adeeb7995b1e8497c1b6fb)) (by ambition_echo)
- **ALL**: 新增日志记录系统([`cc6317f`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/cc6317f4a8e8789297edbe4bf345d865f3ad376a)) (by ambition_echo)
- **about**: 动态调节设置页面大小([`9f6715c`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/9f6715ca550a6e87cc73d9d171b118361151f76c)) (by ambition_echo)
- **about**: 添加启动时检查更新([`9148af4`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/9148af46e16e68a9a7b260a0f1056128089cf6f9)) (by ambition_echo)
- **about**: 新增检查更新功能([`fdb12d0`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/fdb12d0e1e3f8522347200cf064d7bafad67dcb6)) (by ambition_echo)

## 2.0.9 (2022-11-21)

### Bugs fixed:

- **wallhaven**: 修复wallhaven随机列表不生效的问题([`2970adb`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/2970adb5d64c31466e2bce3de0c8c05ea4ca21fe)) (by ambition_echo)

## 2.0.8 (2022-11-21)

### Bugs fixed:

- **wallhaven**: 修复没有更新时间设置项([`293f7fa`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/293f7fa947557f586bd2d54f102e17bc87e43429)) (by ambition_echo)

## 2.0.7 (2022-11-21)

### New feature:

- **interfaces**: 添加wallhaven网站接口([`59e97e0`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/59e97e068e95f1f3b5181d6ddf939166aa6a79c5)) (by ambition_echo)

## 2.0.4 (2022-11-20)

### Bugs fixed:

- **interfaces**: 修复随机壁纸资源占用过高的问题([`59a8bc9`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/59a8bc91618020e4df768e7c58bcfa970f7b64b0)) (by ambition_echo)

## 2.0.1 (2022-11-18)

### New feature:

- **ALL**: 完全使用PySide6重构 (by ambition_echo)
- **interfaces**: 完成接口重构([`e7c69ef`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/e7c69eff21eb150f7440def2209c8e31b94a36bf)) (by ambition_echo)
- **somewhere**: 完善线程安全([`0af698e`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/0af698e4ddd5613e2f3c3fcbc9a732f96f1511bc)) (by ambition_echo)
- **somewhere**: 完善基本功能([`9df4c46`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/9df4c469be48599477394b898cb2ae7b1bd6a44c)) (by ambition_echo)

## 1.8.5 (2022-09-29)

### New feature:

- **scripts**: 增加对 Linux 桌面环境 Cutefish 的支持([`#9`](https://github.com/ambition-echo/earth_wallpaper/pull/9)) (by [lisuke](https://github.com/lisuke))

## 1.8.4 (2022-09-19)

### New feature:

- **scripts**: 必应随机壁纸获取高清壁纸而不是1080p([`1654643`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/165464355dc4fb3e0c036792eef71516ef092518)) (by ambition_echo)
- **scripts**: 必应每日壁纸改用官方高清壁纸([`70ffe79`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/70ffe792153f5cc17c22bfb09f46661317d3be98)) (by ambition_echo)

## 1.8.3 (2022-09-18)

### Bugs fixed:

- **scripts**: 修复没有设置代理时下载壁纸下载失败的问题([`6c9c0d2`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/6c9c0d28ddb1883e5d93fe40626982d4408ed257)) (by ambition_echo)

## 1.8.2 (2022-09-16)

### New feature:

- **config**: 添加设置网络代理功能([`ff61407`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/ff614071836e8928317d324ec74c43389662ad56)) (by ambition_echo)

## 1.8.1 (2022-09-14)

### Bugs fixed:

- **thread**: 改用QProcess调用代替system,解决windows运行弹出cmd窗口的问题([`2ede6f5`](https://jihulab.com/ambition-echo/earth_wallpaper/commit/2ede6f53d129259dc1faa9b4b87d0deb5372db01)) (by ambition_echo)

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