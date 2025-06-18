# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from airtest.core.settings import Settings as ST 
from common import check_image1,check_image2,check_zhujiemian

dev = connect_device("Android:///Q2NVB21806000861")
sleep(10)
log_dir = r"D:\PiaoFang_Test\core_gameplay\check_ui_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置
os.path.dirname(os.path.abspath(__file__))

if exists(Template(r"tpl1747623526623.png", threshold=0.5)):
    sleep(5)
    if exists(Template(r"tpl1747623606770.png")):
        touch(Template(r"tpl1747623606770.png", record_pos=(0.219, 0.716), resolution=(1080, 2240)))
        sleep(5)
        touch(Template(r"tpl1747623642976.png", record_pos=(-0.004, 0.194), resolution=(1080, 2240)))
    
        sleep(5)
        touch((762,1852))
    elif exists(Template(r"tpl1749692298465.png")):
        touch(Template(r"tpl1749692298465.png", record_pos=(0.217, 0.719), resolution=(1080, 2240)))
        sleep(5)
        touch(Template(r"tpl1747623642976.png", record_pos=(-0.004, 0.194), resolution=(1080, 2240)))
    
        sleep(5)
        touch((762,1852))
check_zhujiemian()
touch(Template(r"tpl1744944382976.png", record_pos=(0.446, 0.569), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1745307989339.png")):
    touch(Template(r"tpl1745308006347.png", record_pos=(-0.17, 0.203), resolution=(1080, 2220)))
check_image1(r"tpl1744944406386.png")

sleep(5)
touch(Template(r"tpl1744944529252.png", record_pos=(-0.388, -0.65), resolution=(1080, 2220)))
sleep(5)
check_zhujiemian()
touch(Template(r"tpl1744944565443.png", record_pos=(0.445, 0.46), resolution=(1080, 2220)))
check_image2(r"tpl1744944585710.png")
touch(Template(r"tpl1744944642422.png", record_pos=(-0.441, -0.678), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1744944669943.png", record_pos=(0.329, -0.037), resolution=(1080, 2220)))
check_image2(r"tpl1744944813330.png")
touch(Template(r"tpl1744944844414.png", record_pos=(-0.439, -0.832), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1744944889017.png", record_pos=(0.447, -0.363), resolution=(1080, 2220)))
check_image2(r"tpl1744944910440.png")
touch(Template(r"tpl1744945173513.png", record_pos=(-0.44, -0.842), resolution=(1080, 2220)))
check_zhujiemian()
if exists(Template(r"tpl1744945213348.png")):
    touch(Template(r"tpl1744945213348.png", record_pos=(0.33, -0.151), resolution=(1080, 2220)))
    if exists(Template(r"tpl1750133454661.png", record_pos=(-0.025, 0.913), resolution=(1080, 2400))):
        check_image2(r"tpl1744945261635.png")
        touch(Template(r"tpl1744945292173.png", record_pos=(-0.455, -0.835), resolution=(1080, 2220)))
        check_zhujiemian()
if exists(Template("tpl1744945333212.png")):
    touch(Template(r"tpl1744945361578.png", record_pos=(0.322, -0.26), resolution=(1080, 2220)))
    check_image2(r"tpl1744945397397.png")
    touch(Template(r"tpl1744945650437.png", record_pos=(-0.431, -0.687), resolution=(1080, 2220)))
    check_zhujiemian()
if exists(Template(r"tpl1744945764812.png")):
    touch(Template(r"tpl1744945764812.png", record_pos=(0.444, -0.26), resolution=(1080, 2220)))
    check_image2(r"tpl1744945807761.png")
    touch(Template(r"tpl1744945825593.png", record_pos=(-0.422, -0.825), resolution=(1080, 2220)))
    check_zhujiemian()
if exists(Template(r"tpl1744945893958.png")):
    touch(Template(r"tpl1744945914679.png", record_pos=(0.325, -0.363), resolution=(1080, 2220)))
    check_image2(r"tpl1744945942858.png")
    touch(Template(r"tpl1744945965192.png", record_pos=(-0.41, -0.519), resolution=(1080, 2220)))
    check_zhujiemian()
if exists(Template(r"tpl1744946291817.png")):
        touch(Template(r"tpl1744946291817.png", record_pos=(0.328, -0.473), resolution=(1080, 2220)))
        check_image2(r"tpl1744946500734.png")
        touch(Template(r"tpl1744946517732.png", record_pos=(-0.456, -0.846), resolution=(1080, 2220)))
        check_zhujiemian()
if exists(Template(r"tpl1744946645159.png")):
    touch(Template(r"tpl1744946673348.png", record_pos=(0.327, -0.577), resolution=(1080, 2220)))
    check_image2(r"tpl1744946697536.png")
    touch(Template(r"tpl1744946721091.png", record_pos=(-0.431, -0.635), resolution=(1080, 2220)))
    check_zhujiemian()
touch(Template(r"tpl1744947016683.png", record_pos=(0.445, -0.463), resolution=(1080, 2220)))
check_image2(r"tpl1744947039122.png")
touch(Template(r"tpl1744947063027.png", record_pos=(-0.432, -0.756), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1744947083376.png", record_pos=(0.442, -0.575), resolution=(1080, 2220)))
check_image2(r"tpl1744947210878.png")
sleep(5)
touch(Template(r"tpl1744947364456.png", record_pos=(-0.002, -0.714), resolution=(1080, 2220)))
check_image2(r"tpl1744947586047.png")
check_image2(r"tpl1744947620040.png")
if exists(Template(r"tpl1744947683824.png")):
    touch(Template(r"tpl1744947705778.png", record_pos=(0.257, -0.704), resolution=(1080, 2220)))
    check_image1(r"tpl1744947723689.png")
    touch(Template(r"tpl1744947745686.png", record_pos=(-0.435, -0.838), resolution=(1080, 2220)))
    check_zhujiemian()
else:
    touch(Template(r"tpl1745734189447.png", record_pos=(-0.431, -0.843), resolution=(1080, 2220)))
touch(Template(r"tpl1744947786818.png", record_pos=(0.446, -0.684), resolution=(1080, 2220)))
check_image2(r"tpl1744947824629.png")
swipe((134,554),(807,559))
if exists(Template(r"tpl1744955147726.png")):
    touch(Template(r"tpl1744955166361.png", record_pos=(-0.136, -0.517), resolution=(1080, 2220)))
    check_image2(r"tpl1744955257353.png")
if exists(Template(r"tpl1744955412526.png")):
    touch(Template(r"tpl1744955412526.png", record_pos=(0.064, -0.539), resolution=(1080, 2220)))
    check_image2(r"tpl1744955441201.png")
if exists(Template(r"tpl1744955492467.png")):
    touch(Template(r"tpl1744955507853.png", record_pos=(0.271, -0.531), resolution=(1080, 2220)))
    check_image2(r"tpl1744955526472.png")
swipe((807,559),(134,554))
if exists(Template(r"tpl1744955606877.png")):
    touch(Template(r"tpl1744955606877.png", record_pos=(0.136, -0.517), resolution=(1080, 2220)))
    check_image2(r"tpl1744955639336.png")
if exists(Template(r"tpl1744955665152.png")):
    touch(Template(r"tpl1744955665152.png", record_pos=(0.338, -0.517), resolution=(1080, 2220)))
    check_image2(r"tpl1744955697660.png")
touch(Template(r"tpl1748311551886.png", record_pos=(-0.435, 0.946), resolution=(1080, 2240)))
check_zhujiemian()
touch(Template(r"tpl1744957295444.png", record_pos=(-0.22, -0.447), resolution=(1080, 2220)))
check_image2(r"tpl1744957319202.png")
sleep(5)
touch(Template(r"tpl1744957346956.png", record_pos=(-0.079, 0.934), resolution=(1080, 2220)))
check_image2(r"tpl1744957455968.png")
touch(Template(r"tpl1744957496807.png", record_pos=(-0.435, -0.843), resolution=(1080, 2220)))
check_zhujiemian()
if exists(Template(r"tpl1744957972178.png")):
    touch(Template(r"tpl1744958279194.png", record_pos=(-0.327, -0.449), resolution=(1080, 2220)))
    check_image2(r"tpl1744958329568.png")
    touch(Template(r"tpl1744958351687.png", record_pos=(-0.344, -0.721), resolution=(1080, 2220)))
    check_zhujiemian()
touch(Template(r"tpl1744958377854.png", record_pos=(-0.435, -0.447), resolution=(1080, 2220)))
check_image1(r"tpl1744958548874.png")
touch(Template(r"tpl1744958596282.png", record_pos=(-0.212, -0.356), resolution=(1080, 2220)))
check_image1(r"tpl1744958618526.png")
touch(Template(r"tpl1744958815859.png", record_pos=(-0.454, -0.847), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744958896792.png", record_pos=(-0.444, -0.843), resolution=(1080, 2220)))
check_zhujiemian()
check_zhujiemian()
simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)





    




    
    

    

 