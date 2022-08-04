#include "thread.h"
#include <QDebug>

Thread::Thread(QString command)
{
    this->command = std::move(command);
}

Thread::~Thread() = default;

void Thread::run()
{
    qDebug() << system(this->command.toUtf8());
}