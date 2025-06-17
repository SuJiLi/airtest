# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian

dev = connect_device("Android:///Q2NVB21806000861")
os.path.dirname(os.path.abspath(__file__))

log_dir = r"D:\PiaoFang_Test\core_gameplay\shejiao_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置

check_image1(r"tpl1744883195768.png")
touch(Template(r"tpl1744882477333.png", record_pos=(0.282, 0.962), resolution=(1080, 2220)))
if not exists(Template(r"tpl1744882523919.png")):
    touch(Template(r"tpl1744882477333.png", record_pos=(0.282, 0.962), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744882840714.png", record_pos=(0.28, 0.539), resolution=(1080, 2220)))
check_image1(r"tpl1744882862804.png")
touch(Template(r"tpl1744882883691.png", record_pos=(-0.449, -0.842), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1744882907175.png", record_pos=(0.279, 0.662), resolution=(1080, 2220)))
check_image1(r"tpl1744882929875.png")
touch(Template(r"tpl1744882948253.png", record_pos=(-0.45, -0.842), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1744883007417.png", record_pos=(0.277, 0.802), resolution=(1080, 2220)))
check_image1(r"tpl1744883032814.png")
touch(Template(r"tpl1744883049200.png", record_pos=(-0.405, -0.606), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1744883069267.png", record_pos=(0.279, 0.965), resolution=(1080, 2220)))
simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)

    
