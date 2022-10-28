#include "about.h"
#include "ui_about.h"
#include <QDesktopServices>
#include <QUrl>

About::About(QWidget *parent) : QWidget(parent), ui(new Ui::About)
{
    this->setAttribute(Qt::WA_DeleteOnClose);
    ui->setupUi(this);
    initUI();
    initConnect();
}
About::~About() { delete ui; };

void About::initUI()
{
    this->setWindowIcon(QIcon(":/img/cn.huguoyang.earthwallpaper.png"));
    ui->version->setText(VERSION);
}

void About::initConnect()
{
    connect(ui->aboutQt, &QPushButton::clicked, qApp, &QApplication::aboutQt);
    connect(ui->checkUpdate, &QPushButton::clicked, this, &About::checkUpdate);
}

void About::checkUpdate()
{
    QDesktopServices::openUrl(QUrl(QString("https://github.com/ambition-echo/earth_wallpaper/releases")));
}

void About::closeEvent(QCloseEvent *event)
{
    emit closed();
}
