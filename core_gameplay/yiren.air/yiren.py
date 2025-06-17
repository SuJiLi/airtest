# -*- encoding=utf8 -*-
__author__ = "B27"

from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian

dev = connect_device("Android:///Q2NVB21806000861")
os.path.dirname(os.path.abspath(__file__))

log_dir = r"D:\PiaoFang_Test\core_gameplay\yiren_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置

sleep(10)
touch(Template(r"tpl1744715809929.png", record_pos=(-0.138, 0.968), resolution=(1080, 2220)))
sleep(5)
touch((541,1012))
sleep(5)
touch(Template(r"tpl1744716085795.png", record_pos=(-0.231, -0.453), resolution=(1080, 2220)))

sleep(5)
touch(Template(r"tpl1744716152497.png", record_pos=(-0.226, 0.111), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744716105965.png", record_pos=(-0.006, 0.299), resolution=(1080, 2220)))
sleep(5)

if exists(Template(r"tpl1744716643164.png")):
    touch(Template(r"tpl1744716675999.png", record_pos=(-0.424, -0.652), resolution=(1080, 2220)))
else:
    sleep(5)
    touch((911,1556))
sleep(5)
touch(Template(r"tpl1744716428373.png", record_pos=(0.344, -0.333), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1745830267535.png")):
    touch((952,1359))
    
sleep(5)
if not exists(Template(r"tpl1744716461316.png")):
    touch(Template(r"tpl1744774004071.png", threshold=0.8, record_pos=(-0.396, -0.183), resolution=(1080, 2220)))
touch(Template(r"tpl1744716461316.png", record_pos=(-0.005, 0.187), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744716797234.png", record_pos=(-0.304, 0.597), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1744774506106.png", threshold=0.9)):
        touch(Template(r"tpl1744774531636.png", record_pos=(-0.428, -0.343), resolution=(1080, 2220)))
        sleep(5)
        touch(Template(r"tpl1744774555695.png", record_pos=(-0.447, -0.843), resolution=(1080, 2220)))
elif exists(Template(r"tpl1744716821809.png",threshold=0.9)):   
        print("有资源")
        touch(Template(r"tpl1744716839504.png", record_pos=(-0.001, 0.887), resolution=(1080, 2220)))
        sleep(5)
        touch(Template(r"tpl1744716858898.png", record_pos=(-0.449, -0.843), resolution=(1080, 2220)))
else:
    touch(Template(r"tpl1745304632687.png", record_pos=(-0.448, -0.842), resolution=(1080, 2220)))
sleep(10)
if exists(Template(r"tpl1745829848051.png")):
        touch(Template(r"tpl1745829871553.png", record_pos=(-0.423, -0.661), resolution=(1080, 2220)))
touch(Template(r"tpl1744716967732.png", threshold=0.8, record_pos=(-0.262, -0.185), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1744716985509.png")):
    touch(Template(r"tpl1744716985509.png", record_pos=(0.307, 0.241), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744717012882.png", threshold=0.8, record_pos=(-0.131, -0.184), resolution=(1080, 2220)))

sleep(5)
touch(Template(r"tpl1744717031918.png", record_pos=(0.331, 0.125), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1744717969781.png", rgb=False)):
    print("资源不足")
    touch(Template(r"tpl1744718075974.png", rgb=True, record_pos=(-0.413, -0.325), resolution=(1080, 2220)))
else:
    sleep(5)
    touch(Template(r"tpl1744717247738.png", record_pos=(-0.005, 0.226), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744772896288.png", threshold=0.8, record_pos=(-0.002, -0.184), resolution=(1080, 2220)))
check_image1(r"tpl1744772975701.png")
sleep(5)
touch(Template(r"tpl1744773022278.png", threshold=0.8, record_pos=(0.13, -0.184), resolution=(1080, 2220)))
check_image1(r"tpl1744773042314.png")
sleep(5)
touch(Template(r"tpl1744773088533.png", threshold=0.8, record_pos=(0.264, -0.185), resolution=(1080, 2220)))
check_image1(r"tpl1744773115365.png")
touch(Template(r"tpl1744773217080.png", record_pos=(-0.004, 0.466), resolution=(1080, 2220)))
check_image1(r"tpl1744773234369.png")
touch(Template(r"tpl1744773397390.png", record_pos=(-0.309, -0.51), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1744773416300.png",threshold=0.9)):
    touch(Template(r"tpl1744773416300.png", threshold=0.8, record_pos=(0.396, -0.187), resolution=(1080, 2220)))
    check_image1(r"tpl1744773557111.png")
sleep(2)
touch(Template(r"tpl1744773579588.png", record_pos=(-0.421, -0.67), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744783006323.png", record_pos=(-0.399, 0.96), resolution=(1080, 2220)))
sleep(5)
check_image1(r"tpl1744783090152.png")
touch(Template(r"tpl1744773610572.png", record_pos=(-0.452, -0.85), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1744783208035.png")):
    touch(Template(r"tpl1744783208035.png", record_pos=(0.179, 0.96), resolution=(1080, 2220)))
check_image1(r"tpl1744783238542.png")
sleep(5)
if exists(Template(r"tpl1744783329438.png")):
    touch(Template(r"tpl1744783329438.png", record_pos=(-0.234, 0.963), resolution=(1080, 2220)))
    check_image1(r"tpl1744783359238.png")
    touch(Template(r"tpl1744783621162.png", rgb=True, record_pos=(-0.402, -0.32), resolution=(1080, 2220)))

sleep(5)
touch(Template(r"tpl1743062331959.png", record_pos=(-0.419, -0.301), resolution=(1080, 2220)))
check_image1(r"tpl1744785638557.png")
sleep(2)
touch(Template(r"tpl1743062395485.png", record_pos=(0.19, 0.678), resolution=(1080, 2220)))
sleep(3)
touch(Template(r"tpl1743062424777.png", record_pos=(-0.001, 0.378), resolution=(1080, 2220)))
sleep(15)
try:
    
    while exists(Template(r"tpl1744785707426.png", threshold=0.8)):
        touch(Template(r"tpl1743062487704.png", record_pos=(-0.005, 0.796), resolution=(1080, 2220)))
        sleep(5)
        touch(Template(r"tpl1743131937133.png", record_pos=(0.169, 0.204), resolution=(1080, 2220)))
        sleep(3)
        touch((810,1514))
        sleep(3)
        touch((934,1582))
        sleep(7)
    else:
        print(11111222333)
        touch((963,1737))
        sleep(5)
        
        touch(Template(r"tpl1743062676068.png", record_pos=(-0.458, -0.855), resolution=(1080, 2220)))
        
except TargetNotFoundError:
        print("外星人入侵")
sleep(2)
touch(Template(r"tpl1743062709358.png", record_pos=(-0.243, -0.297), resolution=(1080, 2220)))
sleep(5)
check_image1(r"tpl1744785784520.png")
sleep(2)
touch((621,533))
check_image1(r"tpl1744785840864.png")
sleep(5)
touch(Template(r"tpl1743063051114.png", record_pos=(-0.445, -0.837), resolution=(1080, 2220)))
sleep(3)
touch(Template(r"tpl1743063082917.png", record_pos=(-0.446, -0.837), resolution=(1080, 2220)))
sleep(3)
touch(Template(r"tpl1743063102443.png", record_pos=(-0.07, -0.301), resolution=(1080, 2220)))
sleep(5)
check_image1(r"tpl1744785870426.png")
sleep(2)
touch(Template(r"tpl1743063168630.png", record_pos=(-0.449, -0.846), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1743063313609.png", record_pos=(0.095, -0.3), resolution=(1080, 2220)))
sleep(5)
check_image1(r"tpl1744785900149.png")
swipe((787,1864),(782,771))
sleep(3)
touch(Template(r"tpl1743066674770.png", record_pos=(0.002, -0.749), resolution=(1080, 2220)))
check_image1(r"tpl1744785946101.png")
sleep(3)
touch(Template(r"tpl1743066741246.png", record_pos=(0.2, -0.744), resolution=(1080, 2220)))
check_image1(r"tpl1744785991174.png")
sleep(2)
touch(Template(r"tpl1743066811062.png", record_pos=(-0.465, -0.86), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1743066851197.png", record_pos=(0.257, -0.298), resolution=(1080, 2220)))
check_image1(r"tpl1744786014925.png")
sleep(5)
touch(Template(r"tpl1743066926158.png", record_pos=(-0.405, -0.663), resolution=(1080, 2220)))
touch(Template(r"tpl1744773610572.png", record_pos=(-0.452, -0.85), resolution=(1080, 2220)))
check_zhujiemian()
simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)

















