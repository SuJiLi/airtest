# -*- encoding=utf8 -*-
__author__ = "B27"

from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian
auto_setup()

os.path.dirname(os.path.abspath(__file__))

log_dir = r"D:\PiaoFang_Test\core_gameplay\shichang_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置  
touch(Template(r"tpl1760586474670.png", record_pos=(0.143, 1.024), resolution=(1264, 2736)))
sleep(5)
try:
    if exists(Template(r"tpl1744715356027.png")):
        touch(Template(r"tpl1744700381999.png", record_pos=(0.302, 0.675), resolution=(1080, 2220)))
except TargetNotFoundError:
        print("没有收益可以领取")
sleep(15)
try:
    if exists(Template(r"tpl1744700505592.png")):
        touch(Template(r"tpl1744700545157.png", record_pos=(0.002, 0.628), resolution=(1080, 2220)))
    else:
        check_image1(r"tpl1760595981483.png")
except TargetNotFoundError:
        print("没有升级界面弹出")
sleep(10)
touch(Template(r"tpl1760595724518.png", record_pos=(-0.408, -0.93), resolution=(1264, 2736)))
check_zhujiemian()
    
    
simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)




