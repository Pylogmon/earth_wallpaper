#include "thread.h"
#include <QDebug>

Thread::Thread(QString command)
{
    this->command = std::move(command);
}

Thread::~Thread() = default;

void Thread::run()
{
    int ret = system(this->command.toUtf8());
    if (ret == 0)
    {
        qDebug() << "脚本执行成功！";
    }
    else
    {
        qDebug() << "脚本执行失败，返回值 " << ret;
    }
}