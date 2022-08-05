#include "trayicon.h"
#include "config.h"
#include "thread.h"
#include <QDebug>
#include <QDir>
#include <QFile>
#include <QMessageBox>
#include <QScreen>
#include <QStandardPaths>

TrayIcon::TrayIcon(QSystemTrayIcon *parent) : QSystemTrayIcon(parent)
{
    // 获取屏幕分辨率
    QScreen *desktop = QApplication::primaryScreen();
    QRect desktopRect = desktop->availableGeometry();
    this->height = desktopRect.height() + desktopRect.top();
    this->width = desktopRect.width() + desktopRect.left();
    initTrayIcon();
    initConnect();
    checkConfig();
}
TrayIcon::~TrayIcon()
{
    config->deleteLater();
    exit->deleteLater();
    trayIconMenu->deleteLater();
}
void TrayIcon::initConnect()
{
    // 退出程序
    connect(this->exit, &QAction::triggered, this, &TrayIcon::OnExit);
    // 打开设置页面
    connect(this->config, &QAction::triggered, this, &TrayIcon::showConfigPage);
    // 打开关于页面
    connect(this->about, &QAction::triggered, this, &TrayIcon::showAboutPage);
    // 刷新壁纸
    connect(this->refresh, &QAction::triggered, this, &TrayIcon::handle);
    // 保存壁纸
    connect(this->save, &QAction::triggered, this, &TrayIcon::saveCurrentImg);
    // 定时器
    connect(&this->timer, &QTimer::timeout, this, &TrayIcon::handle);
}
void TrayIcon::initTrayIcon()
{
    this->setIcon(QIcon(":/img/cn.huguoyang.earthwallpaper.png"));

    trayIconMenu = new QMenu();
    config = new QAction();
    exit = new QAction();
    refresh = new QAction();
    save = new QAction();
    about = new QAction();

    config->setText("设置");
    refresh->setText("更新壁纸");
    save->setText("保存当前壁纸");
    exit->setText("退出");
    about->setText("关于");

    trayIconMenu->addAction(save);
    trayIconMenu->addAction(refresh);
    trayIconMenu->addAction(config);
    trayIconMenu->addAction(about);
    trayIconMenu->addAction(exit);

    this->setContextMenu(trayIconMenu);

    this->show();
}

void TrayIcon::OnExit()
{
    qApp->exit(0);
}

void TrayIcon::showConfigPage()
{
    this->configPage = new Config;
    configPage->show();
    // 重载设置
    connect(this->configPage, &Config::configChanged, this, &TrayIcon::reloadSettings);
}

void TrayIcon::showAboutPage()
{
    this->aboutPage = new About;
    aboutPage->show();
}

void TrayIcon::checkConfig()
{
    QString path = QStandardPaths::writableLocation(QStandardPaths::ConfigLocation);
    path += "/earth-wallpaper/config";
    auto configFile = QFile(path);
    if (!configFile.exists())
    {
        qInfo() << "首次运行，打开设置页面";
        this->showConfigPage();
    }
    else
    {
        reloadSettings();
    }
}

void TrayIcon::reloadSettings()
{
    timer.stop();
    QString configPath = QStandardPaths::writableLocation(QStandardPaths::ConfigLocation);
    configPath += "/earth-wallpaper/config";
    delete settings;
    // 重新读取配置文件
    this->settings = new QSettings(configPath, QSettings::IniFormat);
    handle();
}
void TrayIcon::handle()
{
    qDebug() << "handling...";
    int earthSource = settings->value("APP/earthSource").toInt();
    QString earthSize = settings->value("APP/earthSize").toString();
    QString wallpaperDir = settings->value("APP/wallpaperDir").toString();
    QString wallpaperFile = settings->value("APP/wallpaperFile").toString();
    QString exePath = QCoreApplication::applicationDirPath();
    QString command = "";
    switch (earthSource)
    {
    case 0:
        command = "python3 " + exePath + "/scripts/" + "0.py " + QString::number(this->height) + " " +
                  QString::number(this->width) + " " + earthSize;
        break;
    case 1:
        command = "python3 " + exePath + "/scripts/" + "1.py " + QString::number(this->height) + " " +
                  QString::number(this->width) + " " + earthSize;
        break;
    case 2:
        command = "python3 " + exePath + "/scripts/" + "2.py";
        break;
    case 3:
        command = "python3 " + exePath + "/scripts/" + "3.py";
        break;
    case 4:
        command = "python3 " + exePath + "/scripts/" + "4.py";
        break;
    case 5:
        command = "python3 " + exePath + "/scripts/" + "5.py " + wallpaperDir;
        break;
    case 6:
        settings->setValue("APP/updateTime", "10");
        command = "python3 " + exePath + "/scripts/" + "6.py " + wallpaperFile;
        break;
    }

    // 根据设置下载、更新壁纸
    qDebug() << command;
    auto *thread = new Thread(command);
    thread->start();
    timer.start(60000 * settings->value("APP/updateTime").toInt());
}
void TrayIcon::saveCurrentImg()
{
    QString dirPath = "/tmp/earth-wallpaper";
    QDir dir(dirPath);
    QStringList nameFilters;
    nameFilters << "[1-9]*";
    dir.setNameFilters(nameFilters);
    QStringList files = dir.entryList(QDir::Files, QDir::Name);
    QString picturePath = QStandardPaths::writableLocation(QStandardPaths::PicturesLocation) + "/earth-wallpaper";
    if (!QDir(picturePath).exists())
    {
        QDir(picturePath).mkpath(picturePath);
    }
    QFile target = QFile("/tmp/earth-wallpaper/" + files[files.count() - 1]);
    if (target.copy(picturePath + "/" + files[files.count() - 1]))
    {
        QMessageBox::information(nullptr, "保存", "当前壁纸已保存到Picture目录", QMessageBox::Yes);
    }
}