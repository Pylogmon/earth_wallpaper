#include "trayicon.h"
#include "config.h"
#include "src/thread.h"
#include "thread.h"
#include <QDebug>
#include <QFile>
#include <QScreen>
#include <QStandardPaths>

TrayIcon::TrayIcon(QSystemTrayIcon *parent)
{
    //获取屏幕分辨率
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
    //退出程序
    connect(this->exit, &QAction::triggered, this, &TrayIcon::OnExit);
    //打开设置页面
    connect(this->config, &QAction::triggered, this, &TrayIcon::showConfigPage);
    //定时器
    connect(&this->timer, &QTimer::timeout, this, &TrayIcon::handle);
}
void TrayIcon::initTrayIcon()
{
    this->setIcon(QIcon(":/img/icon.png"));

    trayIconMenu = new QMenu();
    config = new QAction();
    exit = new QAction();
    config->setText("设置");
    exit->setText("退出");

    trayIconMenu->addAction(config);
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
    //重载设置
    connect(this->configPage, &Config::configChanged, this, &TrayIcon::reloadSettings);
}

void TrayIcon::checkConfig()
{
    QString path = QStandardPaths::writableLocation(QStandardPaths::ConfigLocation);
    path += "/earth_wallpaper/config_user";
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
    configPath += "/earth_wallpaper/config_user";
    if (settings != nullptr)
    {
        delete settings;
    }
    //重新读取配置文件
    this->settings = new QSettings(configPath, QSettings::IniFormat);
    handle();
}
void TrayIcon::handle()
{
    qDebug() << "handling...";
    QString earthSource = settings->value("APP/earthSource").toString();
    QString earthSize = settings->value("APP/earthSize").toString();
    QString command = "python scripts/" + earthSource + ".py " + QString::number(this->height) + " " +
                      QString::number(this->width) + " " + earthSize;
    // 根据设置下载、更新壁纸
    qDebug() << command;
    Thread *thread = new Thread(command);
    thread->start();
    timer.start(60000 * settings->value("APP/updateTime").toInt());
}