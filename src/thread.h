#pragma once

#include <QThread>

class Thread : public QThread
{
  public:
    QString command;
    Thread(QString command);
    ~Thread();

    void run();
};
