import os


class XFCE(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        path = os.path.split(os.path.realpath(__file__))[0]
        os.system(path + "/xfce.sh {}".format(self.file))
