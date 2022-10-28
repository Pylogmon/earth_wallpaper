#include "thread.h"
#include <QDebug>
#include <QProcess>

Thread::Thread(QStringList command)
{
    this->command = command;
}

Thread::~Thread() = default;

void Thread::run()
{
    QProcess process(0);
    process.start("python3",command);
    process.waitForStarted();
    process.waitForFinished();

    QStringList output = QString::fromLocal8Bit(process.readAllStandardOutput()).split("\n");
    foreach(QString i,output){
        if(!i.isEmpty())
        {
            qDebug() << "[python3]" << i;
        }
    }
}
