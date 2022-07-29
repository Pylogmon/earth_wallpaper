import os


def check():
    dirs = '/tmp/earth-wallpaper/'
    if not os.path.exists(dirs):
        os.makedirs(dirs)
