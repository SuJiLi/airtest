# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian

log_dir = r"D:\PiaoFang_Test\core_gameplay\cangku_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置
dev = connect_device("Android:///Q2NVB21806000861")

check_image1(r"tpl1744883377895.png")
touch(Template(r"tpl1744883794540.png", record_pos=(0.419, 0.967), resolution=(1080, 2220)))
check_image1(r"tpl1744883830711.png")
sleep(5)
if exists(Template(r"tpl1749173610440.png")):
    touch(Template(r"tpl1749173610440.png", record_pos=(-0.331, -0.47), resolution=(1080, 2240)))
else:  
    check_image1(r"tpl1744883873852.png")
sleep(5)
touch(Template(r"tpl1744883899896.png", record_pos=(0.0, -0.505), resolution=(1080, 2220)))
check_image1(r"tpl1744883938151.png")
sleep(5)
touch(Template(r"tpl1744883966324.png", record_pos=(0.166, -0.505), resolution=(1080, 2220)))
check_image1(r"tpl1744883987410.png")
sleep(5)
touch(Template(r"tpl1744884033036.png", record_pos=(0.331, -0.507), resolution=(1080, 2220)))
check_image1(r"tpl1744884069163.png")
touch(Template(r"tpl1744884084964.png", record_pos=(-0.394, -0.599), resolution=(1080, 2220)))
check_zhujiemian()
simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)





















