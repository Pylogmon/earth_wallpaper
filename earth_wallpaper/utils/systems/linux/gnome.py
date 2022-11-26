import os


class Gnome(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        gs1 = f"gsettings set org.gnome.desktop.background picture-uri {self.file}"
        gs2 = f"gsettings set org.gnome.desktop.background picture-uri-dark {self.file}"
        os.system(gs1)
        os.system(gs2)
