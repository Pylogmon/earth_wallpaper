import os


class LXQT(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        os.system("pcmanfm-qt -w {}".format(self.file))
