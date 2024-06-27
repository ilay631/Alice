import os


def wol_pc():
    os.system("sudo etherwake -i eth0 D8:43:AE:21:83:87")

