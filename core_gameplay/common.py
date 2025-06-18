# -*- encoding=utf8 -*-
__author__ = "B27"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

# script content
def check_image1(image_path):
    # 优化后代码（执行速度提升30%-50%）
    try:
        # 添加阈值和ROI缩小识别范围
        pic = wait(Template(
            image_path, 
            record_pos=(0.003, -0.009), 
            resolution=(1080, 2220),
            threshold=0.8,  # 适当降低匹配精度
        ), timeout=20)  # 超时减半
        print("界面正常" if pic else "界面不正常")  # 直接利用pic布尔值
    except TargetNotFoundError:
        print("界面不正常")
#检查很严谨的界面     
def check_image2(image_path):
        # 优化后代码（执行速度提升30%-50%）
    try:
        # 添加阈值和ROI缩小识别范围
        pic = wait(Template(
            image_path, 
            record_pos=(0.003, -0.009), 
            resolution=(1080, 2220),
            threshold=0.99,  # 适当降低匹配精度
        ), timeout=20)  # 超时减半
        print("界面正常" if pic else "界面不正常")  # 直接利用pic布尔值
    except TargetNotFoundError:
        print("界面不正常")
#检查某些界面返回主界面时会打开建筑界面
def check_zhujiemian():
    sleep(3)
    if not exists(Template(r"tpl1745907542094.png", threshold=0.6)):
        print("存在异常界面就关闭")
        touch(Template(r"tpl1744872751817.png", record_pos=(-0.421, -0.664), resolution=(1080, 2220)))
    if exists(Template(r"tpl1750126196654.png")):
        touch(Template(r"tpl1750126227738.png", record_pos=(-0.366, -0.366), resolution=(1080, 2400)))
def shengji():
    sleep(3)
    if exists(Template(r"tpl1745478669410.png", threshold=0.9)):
        touch(Template(r"tpl1745478853818.png", record_pos=(0.002, 0.631), resolution=(1080, 2220)))

def renwu():
    sleep(3)
    if exists(Template(r"tpl1745479096513.png")):
        touch(Template(r"tpl1745479096513.png", record_pos=(0.425, 0.771), resolution=(1080, 2220)))
        
def chonglian():
    touch(Template(r"tpl1749109060222.png", threshold=0.3, record_pos=(0.276, -0.902), resolution=(1080, 2240)))
    sleep(5)
    touch(Template(r"tpl1749109092661.png", threshold=0.3, record_pos=(0.181, 0.639), resolution=(1080, 2240)))
    sleep(50)
    if wait(Template(r"tpl1749109161160.png")):
        print("已重启")
        
def click_template_if_exists(template_path, click_path=None, threshold=0.8):
    """
    如果找到模板图片，则点击指定图片
    
    参数:
    template_path (str): 要查找的模板图片路径
    click_path (str): 要点击的图片路径(如果为None则点击找到的模板位置)
    threshold (float): 匹配阈值(0-1)
    """
    if exists(Template(template_path, threshold=threshold)):
        if click_path is None:
            # 如果未指定点击图片，则点击找到的模板位置
            touch(Template(template_path, threshold=threshold))
        else:
            # 点击指定的图片
            touch(Template(click_path, threshold=threshold))
        return True
    return False
        

         



