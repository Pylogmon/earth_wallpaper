#include "config.h"
#include "ui_config.h"
#include <QDebug>
#include <QDir>
#include <QFile>
#include <QMessageBox>
#include <QSettings>
#include <QStandardPaths>
#include <qfiledialog.h>

Config::Config(QWidget *parent) : QWidget(parent), ui(new Ui::Config)
{
    this->setAttribute(Qt::WA_DeleteOnClose);
    // 检查配置文件
    this->configPath = QStandardPaths::writableLocation(QStandardPaths::ConfigLocation);

    configPath += "/earth-wallpaper";
    QString path = configPath + "/config";
    auto configFile = new QFile(path);
    auto configDir = new QDir(configPath);
    if (!configFile->exists())
    {
        if (!configDir->exists())
        {
            configDir->mkpath(configPath);
        }
        QString exePath = QCoreApplication::applicationDirPath();
        auto tempFile = new QFile(exePath + "/template/config");
        tempFile->copy(path);
    }
    ui->setupUi(this);
    initUI();
    initConnect();
    readConfig();
    controlOption();
}

Config::~Config()
{
    settings->deleteLater();
    this->disconnect();
    delete ui;
}
void Config::initUI()
{
    this->setWindowIcon(QIcon(":/img/cn.huguoyang.earthwallpaper.png"));
    ui->earthSource->addItem("向日葵八号");
    ui->earthSource->addItem("风云四号");
    ui->earthSource->addItem("必应壁纸(随机)");
    ui->earthSource->addItem("必应壁纸(每日)");
    ui->earthSource->addItem("动漫壁纸");
    ui->earthSource->addItem("本地壁纸");
    ui->earthSource->addItem("24h壁纸");
    ui->updateTime->addItem("10");
    ui->updateTime->addItem("30");
    ui->updateTime->addItem("60");
    ui->updateTime->addItem("120");
    ui->updateTime->addItem("180");
    ui->updateTime->addItem("720");
}

void Config::initConnect()
{
    connect(ui->apply, &QPushButton::clicked, this, &Config::writeConfig);
    connect(ui->close, &QPushButton::clicked, this, &Config::close);
    connect(ui->earthSource, &QComboBox::currentTextChanged, this, &Config::controlOption);
    connect(ui->select, &QPushButton::clicked, this, &Config::selectDir);
    connect(ui->selectFile, &QPushButton::clicked, this, &Config::selectFile);
}
void Config::readConfig()
{
    this->settings = new QSettings(configPath + "/config", QSettings::IniFormat);
    settings->setIniCodec("UTF8");
    settings->beginGroup("APP");
    ui->earthSource->setCurrentIndex(settings->value("earthSource").toInt());
    ui->updateTime->setCurrentText(settings->value("updateTime").toString());
    ui->earthSize->setValue(settings->value("earthSize").toInt());
    ui->wallpaperDir->setText(settings->value("wallpaperDir").toString());
    ui->wallpaperFile->setText(settings->value("wallpaperFile").toString());
    settings->endGroup();
}
void Config::writeConfig()
{
    settings->beginGroup("APP");
    settings->setValue("earthSource", ui->earthSource->currentIndex());
    settings->setValue("updateTime", ui->updateTime->currentText());
    settings->setValue("earthSize", ui->earthSize->value());
    settings->setValue("wallpaperDir", ui->wallpaperDir->text());
    settings->setValue("wallpaperFile", ui->wallpaperFile->text());
    settings->endGroup();
    QMessageBox::information(this, tr("设置"), tr("设置保存成功！"));
    emit configChanged();
}
void Config::controlOption()
{
    if (ui->earthSource->currentIndex() == 0 || ui->earthSource->currentIndex() == 1)
    {
        ui->label_3->show();
        ui->earthSize->show();
    }
    else
    {
        ui->label_3->hide();
        ui->earthSize->hide();
    }
    if (ui->earthSource->currentIndex() == 5)
    {
        ui->label_4->show();
        ui->wallpaperDir->show();
        ui->select->show();
    }
    else
    {
        ui->label_4->hide();
        ui->wallpaperDir->hide();
        ui->select->hide();
    }
    if (ui->earthSource->currentIndex() == 6)
    {
        ui->label_5->show();
        ui->wallpaperFile->show();
        ui->selectFile->show();
        ui->updateTime->hide();
        ui->label_2->hide();
    }
    else
    {
        ui->label_5->hide();
        ui->wallpaperFile->hide();
        ui->selectFile->hide();
        ui->updateTime->show();
        ui->label_2->show();
    }
}
void Config::selectDir()
{
    QString dir = QFileDialog::getExistingDirectory(this, tr("选择壁纸文件夹"));
    ui->wallpaperDir->setText(dir);
}
void Config::selectFile()
{
    QString file =
        QFileDialog::getOpenFileName(this, "选择24h壁纸文件", "", "24h壁纸文件 (*.ddw *.zip);; 所有文件 (*.*);; ");
    ui->wallpaperFile->setText(file);
}