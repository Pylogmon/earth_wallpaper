#include "thread.h"
#include <QDebug>

Thread::Thread(QString command)
{
    this->command = command;
}

Thread::~Thread()
{
}

void Thread::run()
{
    int result = system(this->command.toUtf8());
}