#include "thread.h"
#include <QDebug>

Thread::Thread(QSettings *settings)
{
    settings->beginGroup("APP");
    this->earthSource = settings->value("earthSource").toInt();
    this->updateTime = settings->value("updateTime").toInt();
    this->alwaysUpdate = settings->value("alwaysUpdate").toBool();
    settings->endGroup();
}

Thread::~Thread()
{
    this->stop();
    this->wait();
}

void Thread::run()
{
    while (this->runFlag)
    {
    }
}

void Thread::stop()
{
    this->runFlag = false;
}