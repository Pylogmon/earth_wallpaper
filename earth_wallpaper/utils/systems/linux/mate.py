import os


class MATE(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        gs = f"gsettings set org.mate.background picture-filename {self.file}"
        os.system(gs)
