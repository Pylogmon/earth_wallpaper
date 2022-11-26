import os


class Cinnamon(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        gs = f"gsettings set org.cinnamon.desktop.background picture-uri file://{self.file}"
        os.system(gs)
