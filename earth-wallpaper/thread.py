from PySide6.QtCore import QThread
import interfaces


def get_class_name(name: str):
    for i in dir(interfaces):
        if getattr(interfaces, i).name() == name:
            return i


class Thread(QThread):

    def __init__(self, name):
        super(Thread, self).__init__()
        self.class_name = get_class_name(name)

    def run(self):
        x = getattr(interfaces, self.class_name)()
        print(f"Start run {x.name()}...")
        x.run()
        print("Run completed!")
