#include "trayicon.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QApplication::setQuitOnLastWindowClosed(false); //最后一个窗口关闭时，禁止退出应用程序
    TrayIcon tray;
    return a.exec();
}
