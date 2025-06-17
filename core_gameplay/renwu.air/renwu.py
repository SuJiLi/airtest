# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian


dev = connect_device("Android:///Q2NVB21806000861")
os.path.dirname(os.path.abspath(__file__))

log_dir = r"D:\PiaoFang_Test\core_gameplay\renwu_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置

touch(Template(r"tpl1744884610836.png", threshold=0.3, record_pos=(0.422, 0.761), resolution=(1080, 2220)))
check_image1(r"tpl1744884652799.png")

timeout = 60  # Set timeout in seconds
start_time = time.time()

try:
    while exists(Template(r"tpl1744884683461.png")):
        # Check if timeout has been reached
        if time.time() - start_time > timeout:
            print("操作超时")
            break
            
        touch(Template(r"tpl1744884702855.png", record_pos=(0.335, -0.306), resolution=(1080, 2220)))
        sleep(5)
        if not exists(Template(r"tpl1744884726210.png")):
            break
        sleep(1)
except TargetNotFoundError:
    print("无可领取奖励")
sleep(5)
touch(Template(r"tpl1743046587009.png", record_pos=(-0.409, -0.736), resolution=(1080, 2220)))
check_zhujiemian()




simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)
stop_app("com.tencent.mm")
keyevent("POWER")
