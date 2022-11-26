import os


class LXDE(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        os.system("pcmanfm -w {}".format(self.file))
