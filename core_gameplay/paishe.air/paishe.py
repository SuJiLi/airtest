# -*- encoding=utf8 -*-
__author__ = "B27"

from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian,chonglian

dev = connect_device("Android:///Q2NVB21806000861")
os.path.dirname(os.path.abspath(__file__))

log_dir = r"D:\PiaoFang_Test\core_gameplay\paishe_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置
sleep(2)
touch(Template(r"tpl1744600009078.png", threshold=0.6, record_pos=(0.018, 0.952), resolution=(1080, 2220)))
sleep(5)
try:
    if exists(Template(r"tpl1744630226810.png", threshold=0.7)):
        print("电影满了")
        touch((61,1892))
        sleep(5)
        touch(Template(r"tpl1744623426320.png", record_pos=(0.27, 0.544), resolution=(1080, 2220)))
        sleep(5)
        touch(Template(r"tpl1744600009078.png", threshold=0.6, record_pos=(0.018, 0.952), resolution=(1080, 2220)))
except TargetNotFoundError:
        print("还有电影空位")
        
sleep(3)
touch(Template(r"tpl1744600034000.png", record_pos=(-0.286, 0.639), resolution=(1080, 2220)))
check_image1(r"tpl1744600199070.png")
sleep(2)
touch(Template(r"tpl1744600277942.png", threshold=0.3, record_pos=(-0.327, -0.018), resolution=(1080, 2220)))
check_image1(r"tpl1744600312096.png")
touch(Template(r"tpl1744600351534.png", threshold=0.4, record_pos=(0.217, 0.72), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744600394893.png", threshold=0.4, record_pos=(-0.002, 0.115), resolution=(1080, 2220)))
sleep(10)
try:
    if wait(Template(r"tpl1744600486269.png", threshold=0.8, record_pos=(-0.002, -0.131), resolution=(1080, 2220))):
        touch(Template(r"tpl1744600505972.png", record_pos=(0.381, -0.067), resolution=(1080, 2220)))
except TargetNotFoundError:
        print("没有屏蔽字")
check_image1(r"tpl1744602029233.png")
touch((994,1714))
sleep(5)
try:
    if wait(Template(r"tpl1744602083847.png")):
        touch(Template(r"tpl1744602104233.png", record_pos=(-0.004, -0.057), resolution=(1080, 2220)))
        sleep(5)
        if exists(Template(r"tpl1744802474311.png")):
            touch(Template(r"tpl1744802499175.png", record_pos=(-0.424, -0.345), resolution=(1080, 2220)))
            sleep(5)
            touch(Template(r"tpl1744802710381.png", record_pos=(0.002, 0.048), resolution=(1080, 2220)))
        else:
            sleep(5)
            try:
                            if wait(Template(r"tpl1744698977920.png", threshold=0.6)):
                                print("资源足够")
                                touch(Template(r"tpl1744602184076.png", record_pos=(0.239, -0.258), resolution=(1080, 2220)))
                                check_image1(r"tpl1744602209051.png")
                                touch(Template(r"tpl1744602276702.png", record_pos=(0.006, 0.321), resolution=(1080, 2220)))
                            elif wait(Template(r"tpl1744602083847.png")):
                                print("进入 if 分支，准备点击 tpl1744631103800.png")
                                touch(Template(r"tpl1744631103800.png", threshold=0.9, record_pos=(0.002, 0.051), resolution=(1080, 2220)))              
            except TargetNotFoundError:
                            print("编剧异常")
except TargetNotFoundError:
        print("没有编剧的剧本")


check_image1(r"tpl1744602305278.png")
sleep(3)
touch(Template(r"tpl1744602387131.png", record_pos=(-0.369, -0.322), resolution=(1080, 2220)))
sleep(10)
try:
    if exists(Template(r"tpl1744624183960.png", threshold=0.9)):
        touch(Template(r"tpl1744602521576.png", threshold=0.3, record_pos=(-0.378, -0.538), resolution=(1080, 2220)))
        check_image1(r"tpl1744609195702.png")
        touch(Template(r"tpl1745301639012.png", threshold=0.5, record_pos=(-0.294, -0.03), resolution=(1080, 2220)))
        sleep(3)
        touch(Template(r"tpl1744609346891.png", record_pos=(0.154, 0.746), resolution=(1080, 2220)))
        sleep(5)
        touch(Template(r"tpl1744609364886.png", record_pos=(0.002, 0.957), resolution=(1080, 2220)))
        check_image1(r"tpl1744609412633.png")
    else:
        touch(Template(r"tpl1744609610573.png", record_pos=(-0.001, 0.958), resolution=(1080, 2220)))
except TargetNotFoundError:
        print("拍摄异常")
sleep(2)
touch(Template(r"tpl1744609641760.png", record_pos=(0.0, 0.713), resolution=(1080, 2220)))
check_image1(r"tpl1744609667139.png")
touch(Template(r"tpl1744609911457.png", record_pos=(0.004, 0.641), resolution=(1080, 2220)))
sleep(20)
if exists(Template(r"tpl1744788511633.png", threshold=0.8)):
    touch(Template(r"tpl1744788528964.png", record_pos=(-0.002, 0.244), resolution=(1080, 2220)))
if exists(Template(r"tpl1745743474053.png",threshold=.3)):
    touch((893,1799)) 
sleep(5)
if wait(Template(r"tpl1744788559127.png", threshold=0.8, record_pos=(-0.003, -0.031), resolution=(1080, 2220))):
    touch(Template(r"tpl1744788573379.png", record_pos=(-0.005, 0.699), resolution=(1080, 2220)))
if exists(Template(r"tpl1744788511633.png", threshold=0.8)):
    touch(Template(r"tpl1744788528964.png", record_pos=(-0.002, 0.244), resolution=(1080, 2220)))
check_image1(r"tpl1744609974758.png")
touch((605,1110))
sleep(3)
touch(Template(r"tpl1744610053189.png", record_pos=(-0.002, 0.731), resolution=(1080, 2220)))
check_image1(r"tpl1744610088286.png")
if exists(Template(r"tpl1744788511633.png", threshold=0.8)):
    touch(Template(r"tpl1744788528964.png", record_pos=(-0.002, 0.244), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744610105466.png", record_pos=(0.297, -0.436), resolution=(1080, 2220)))
sleep(10)
if exists(Template(r"tpl1744788872800.png",threshold=0.9)):
    print("资源不足")
    
    touch(Template(r"tpl1744788884475.png", record_pos=(-0.425, -0.34), resolution=(1080, 2220)))
sleep(3)
touch(Template(r"tpl1744610122133.png", record_pos=(-0.002, 0.642), resolution=(1080, 2220)))
sleep(20)
try:
    if exists(Template(r"tpl1744610201164.png", threshold=0.9)):
        print("目标未达成")

        touch((836,1802))
    else:
        touch(Template(r"tpl1744615830450.png", record_pos=(-0.003, 0.243), resolution=(1080, 2220)))
except TargetNotFoundError:
        print("目标提前出现")
check_image1(r"tpl1744610284573.png")

touch(Template(r"tpl1744610300101.png", rgb=False, record_pos=(-0.005, 0.668), resolution=(1080, 2220)))
check_image1(r"tpl1744610325140.png")
sleep(10)
touch(Template(r"tpl1744610340933.png", threshold=0.85, record_pos=(-0.002, 0.66), resolution=(1080, 2220)))
check_image1(r"tpl1744610440575.png")
touch(Template(r"tpl1744610456639.png", record_pos=(0.341, -0.531), resolution=(1080, 2220)))
check_image1(r"tpl1744610476696.png")
touch(Template(r"tpl1744610500720.png", record_pos=(-0.001, 0.692), resolution=(1080, 2220)))
sleep(5)
touch((823,1747))
check_image1(r"tpl1744610544025.png")
touch(Template(r"tpl1744610562212.png", record_pos=(-0.001, 0.699), resolution=(1080, 2220)))
try:
    if wait(Template(r"tpl1744610613596.png"),timeout=100):
    
        touch(Template(r"tpl1744610725387.png", record_pos=(0.002, 0.207), resolution=(1080, 2220)))
except TargetNotFoundError:
        print("没有助手提示")
check_image1(r"tpl1744610874972.png")

simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)
chonglian()
sleep(30)


