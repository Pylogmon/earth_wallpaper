#pragma once

#include <QSettings>
#include <QThread>

class Thread : public QThread
{
  public:
    int earthSource;
    int updateTime;
    bool alwaysUpdate;

    bool runFlag = true;
    Thread(QSettings *settings);
    ~Thread();

    void run();
    void stop();
};
