# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

dev = connect_device("Android:///Q2NVB21806000861")

touch(Template(r"tpl1749109060222.png", record_pos=(0.276, -0.902), resolution=(1080, 2240)))
sleep(5)
touch(Template(r"tpl1749109092661.png", record_pos=(0.181, 0.639), resolution=(1080, 2240)))
sleep(50)
if wait(Template(r"tpl1749109161160.png")):
    print("已重启")
    







