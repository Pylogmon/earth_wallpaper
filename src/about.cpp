#include "about.h"
#include "ui_about.h"
#include <qapplication.h>
#include <qpushbutton.h>

About::About(QWidget *parent) : QWidget(parent), ui(new Ui::About)
{
    this->setAttribute(Qt::WA_DeleteOnClose);
    ui->setupUi(this);
    initUI();
    initConnect();
}
About::~About()
{
}

void About::initUI()
{
    ui->version->setText(VERSION);
}

void About::initConnect()
{
    connect(ui->aboutQt, &QPushButton::clicked, qApp, &QApplication::aboutQt);
}