# -*- encoding=utf8 -*-
__author__ = "B27"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

# script content
def check_image1(image_path):
    try:
        pic = wait(Template(image_path, record_pos=(0.003, -0.009), resolution=(1080, 2220)), timeout=40)
        if pic:
            print("界面正常")
    except TargetNotFoundError:
            print("界面不正常")
#检查很严谨的界面     
def check_image2(image_path):
    try:
        pic = wait(Template(image_path, record_pos=(0.003, -0.009), resolution=(1080, 2220),threshold=0.95), timeout=40)
        if pic:
            print("界面正常")
    except TargetNotFoundError:
            print("界面不正常")
#检查某些界面返回主界面时会打开建筑界面
def check_zhujiemian():
    sleep(3)
    if not exists(Template(r"tpl1745907542094.png", threshold=0.6)):
        print("存在异常界面就关闭")
        touch(Template(r"tpl1744872751817.png", record_pos=(-0.421, -0.664), resolution=(1080, 2220)))
def shengji():
    sleep(3)
    if exists(Template(r"tpl1745478669410.png", threshold=0.9)):
        touch(Template(r"tpl1745478853818.png", record_pos=(0.002, 0.631), resolution=(1080, 2220)))

def renwu():
    sleep(3)
    if exists(Template(r"tpl1745479096513.png")):
        touch(Template(r"tpl1745479096513.png", record_pos=(0.425, 0.771), resolution=(1080, 2220)))
        
def chonglian():
    touch(Template(r"tpl1749109060222.png", record_pos=(0.276, -0.902), resolution=(1080, 2240)))
    sleep(5)
    touch(Template(r"tpl1749109092661.png", record_pos=(0.181, 0.639), resolution=(1080, 2240)))
    sleep(50)
    if wait(Template(r"tpl1749109161160.png")):
        print("已重启")
         



