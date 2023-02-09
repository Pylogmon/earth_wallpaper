import os


class XFCE(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        output = os.popen("xfconf-query -c xfce4-desktop -p /backdrop -l")
        output = output.splitlines()
        for i in output:
            if "last-image" in i:
                os.system(
                    f"xfconf-query -c xfce4-desktop -p {i} -s {self.file}")
