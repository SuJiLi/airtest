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
    if not exists(Template(r"tpl1745907542094.png")):
        print("存在就关闭")
        touch(Template(r"tpl1744872751817.png", record_pos=(-0.421, -0.664), resolution=(1080, 2220)))
        sleep(5)
        if exists(Template(r"tpl1745907542094.png", record_pos=(0.014, 0.956), resolution=(1080, 2220))):
            
            touch(Template(r"tpl1744872751817.png", record_pos=(-0.421, -0.664), resolution=(1080, 2220)))
def shengji():
    if exists(Template(r"tpl1745478669410.png", threshold=0.9)):
        touch(Template(r"tpl1745478853818.png", record_pos=(0.002, 0.631), resolution=(1080, 2220)))

def renwu():
    if exists(Template(r"tpl1745479096513.png")):
        touch(Template(r"tpl1745479096513.png", record_pos=(0.425, 0.771), resolution=(1080, 2220)))


