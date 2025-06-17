# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian


dev = connect_device("Android:///Q2NVB21806000861")
os.path.dirname(os.path.abspath(__file__))

log_dir = r"D:\PiaoFang_Test\core_gameplay\jingying_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置

check_image1(r"tpl1744869478330.png")
touch(Template(r"tpl1744869568363.png", record_pos=(-0.419, 0.963), resolution=(1080, 2220)))
sleep(5)
if not exists(Template(r"tpl1744869970239.png")):
    touch(Template(r"tpl1744870016123.png", record_pos=(-0.421, 0.967), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744870041029.png", record_pos=(-0.421, -0.131), resolution=(1080, 2220)))
check_image1(r"tpl1744870061053.png")
sleep(5)
touch(Template(r"tpl1744870096811.png", record_pos=(-0.448, -0.837), resolution=(1080, 2220)))
sleep(5)
check_zhujiemian()
sleep(5)
touch(Template(r"tpl1744870127601.png", record_pos=(-0.421, -0.008), resolution=(1080, 2220)))
check_image1(r"tpl1744870162987.png")
sleep(5)
touch(Template(r"tpl1744870260577.png", record_pos=(-0.079, -0.818), resolution=(1080, 2220)))
sleep(15)
if exists(Template(r"tpl1744870310635.png")):
    touch(Template(r"tpl1744870328478.png", record_pos=(-0.001, 0.248), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744870407170.png", record_pos=(-0.274, -0.114), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1744870439420.png")):
    touch(Template(r"tpl1744870566337.png", record_pos=(-0.001, 0.246), resolution=(1080, 2220)))

sleep(5)
touch(Template(r"tpl1744870601773.png", record_pos=(-0.455, -0.848), resolution=(1080, 2220)))
sleep(5)
check_zhujiemian()
sleep(5)

touch(Template(r"tpl1744870887785.png", record_pos=(-0.419, 0.133), resolution=(1080, 2220)))
sleep(5)
check_image1(r"tpl1744871205027.png")
sleep(5)
if exists(Template(r"tpl1744871515827.png")):
    touch(Template(r"tpl1744871515827.png", record_pos=(0.385, 0.967), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1745913130523.png")):
    touch(Template(r"tpl1745913367230.png", record_pos=(-0.374, -0.293), resolution=(1080, 2220)))
    
if exists(Template(r"tpl1744871554374.png", threshold=0.6)):
    touch((960,1786))
    
sleep(5)
touch(Template(r"tpl1744872000598.png", record_pos=(0.191, 0.968), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744872025786.png", record_pos=(-0.441, -0.86), resolution=(1080, 2220)))
sleep(5)
check_zhujiemian()
sleep(5)
touch(Template(r"tpl1744873064643.png", record_pos=(-0.416, 0.26), resolution=(1080, 2220)))
check_image1(r"tpl1744873153265.png")
sleep(80)
sleep(5)
touch(Template(r"tpl1744873322640.png", threshold=0.6, record_pos=(-0.42, 0.541), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1744873343758.png")):
    print("有会议内容")
    check_image1(r"tpl1744873343758.png")
    sleep(5)
    if exists(Template(r"tpl1744873390458.png")):
        touch(Template(r"tpl1744873390458.png", record_pos=(0.385, -0.158), resolution=(1080, 2220)))
    sleep(5)
    if exists(Template(r"tpl1744873577354.png")):
        touch((766,1687))#这里要改，会点到大楼ui
    else:
        touch(Template(r"tpl1744874165641.png", record_pos=(-0.445, -0.84), resolution=(1080, 2220)))
    sleep(5)
sleep(5)
touch(Template(r"tpl1744873733101.png", record_pos=(-0.421, 0.669), resolution=(1080, 2220)))
sleep(5)
check_image1(r"tpl1744874097100.png")
touch(Template(r"tpl1744874165641.png", record_pos=(-0.445, -0.84), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1744874223614.png", record_pos=(-0.419, 0.786), resolution=(1080, 2220)))
check_image1(r"tpl1744874248077.png")
sleep(5)
touch(Template(r"tpl1744874271886.png", record_pos=(-0.456, -0.85), resolution=(1080, 2220)))
check_zhujiemian()
sleep(5)

touch(Template(r"tpl1744873262934.png", record_pos=(-0.421, 0.394), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1749175511564.png")):
    touch(Template(r"tpl1749175511564.png", record_pos=(0.183, 0.294), resolution=(1080, 2240)))
    sleep(5)
    touch((475,452))
sleep(5)
touch(Template(r"tpl1744881944457.png", record_pos=(-0.419, 0.96), resolution=(1080, 2220)))
check_zhujiemian()
simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)



    





