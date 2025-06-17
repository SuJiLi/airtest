# -*- encoding=utf8 -*-
__author__ = "B27"

from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian

dev = connect_device("Android:///Q2NVB21806000861")
os.path.dirname(os.path.abspath(__file__))

log_dir = r"D:\PiaoFang_Test\core_gameplay\shichang_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置

sleep(10)
touch(Template(r"tpl1744700009905.png", threshold=0.5, record_pos=(0.144, 0.953), resolution=(1080, 2220)))
try:
    if wait(Template(r"tpl1744715356027.png")):
        touch(Template(r"tpl1744700381999.png", record_pos=(0.302, 0.675), resolution=(1080, 2220)))
except TargetNotFoundError:
        print("没有收益可以领取")
sleep(15)
try:
    if exists(Template(r"tpl1744700505592.png")):
        touch(Template(r"tpl1744700545157.png", record_pos=(0.002, 0.628), resolution=(1080, 2220)))
except TargetNotFoundError:
        print("没有升级界面弹出")
sleep(5)
if not exists(Template(r"tpl1744710655776.png",threshold=0.8)):
    swipe((888,634),(207,629))
    touch((626,644))
else:
    print("它在这个界面")
    
try:
    if wait(Template(r"tpl1744700855355.png")):
        print("已经在宣传界面")
        sleep(2)
        if exists(Template(r"tpl1744701004844.png", threshold=0.6)):
            sleep(2)
            touch(Template(r"tpl1744701040175.png", threshold=0.7, record_pos=(0.271, 0.304), resolution=(1080, 2220)))
            sleep(5)
            touch(Template(r"tpl1744701199054.png", record_pos=(0.019, 0.74), resolution=(1080, 2220)))
            sleep(5)
            touch(Template(r"tpl1745917404350.png", record_pos=(-0.392, -0.654), resolution=(1080, 2220)))
            try:
                if exists(Template(r"tpl1744701751946.png")):
                    touch((1002,1419))  
                    sleep(5)
                    touch(Template(r"tpl1744715644037.png", record_pos=(-0.389, -0.649), resolution=(1080, 2220)))         
            except TargetNotFoundError:                    
                print("没有宣传完成")
                touch((921,1797))
                sleep(5)
                touch(Template(r"tpl1744701448744.png", record_pos=(-0.408, -0.526), resolution=(1080, 2220)))
                sleep(3)
                touch(Template(r"tpl1744701479236.png", record_pos=(-0.389, -0.652), resolution=(1080, 2220)))
        elif exists(Template(r"tpl1744702098648.png",threshold=0.5)):
            touch(Template(r"tpl1744703296053.png", record_pos=(-0.018, 0.057), resolution=(1080, 2220)))
            sleep(5)
            touch(Template(r"tpl1744703322271.png", record_pos=(-0.002, 0.931), resolution=(1080, 2220)))
            sleep(5)
            touch((908,1768))
            sleep(5)
            touch(Template(r"tpl1744703364273.png", record_pos=(-0.002, 0.726), resolution=(1080, 2220)))
            sleep(5)
            touch(Template(r"tpl1744703382370.png", record_pos=(-0.389, -0.648), resolution=(1080, 2220)))
            sleep(5)
            if exists(Template(r"tpl1744710355799.png")):
                touch(Template(r"tpl1744710380390.png", record_pos=(-0.407, -0.518), resolution=(1080, 2220)))
except TargetNotFoundError:
        print("不在宣传界面")
sleep(5)
check_zhujiemian()
    
    
simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)






