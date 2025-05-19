# -*- encoding=utf8 -*-
__author__ = "Administrator"
import os
from airtest.core.api import *
from airtest.core.api import connect_device, start_app, stop_app
import subprocess
from airtest.report.report import simple_report, LogToHtml

from airtest.core.api import *

# 或者指定设备序列号（adb devices 获取）
dev = connect_device("Android:///TPC7N18515001155")  # 替换为你的设备号
sleep(5)
def is_locked():
    """
    通过adb检测设备是否锁屏
    返回True表示锁屏，False表示未锁屏
    """
    output = shell("dumpsys window")
    return "mDreamingLockscreen=true" in output or "isShowing=true" in output
if is_locked():
    keyevent("POWER")  # 唤醒屏幕
    swipe((551,1800),(543,470))  # 滑动解锁
else:
    print("设备已解锁")
touch(Template(r"tpl1747380949540.png", record_pos=(0.0, 0.261), resolution=(1080, 2240)))
sleep(10)
swipe((501,334),(567,1539))
touch(Template(r"tpl1747623798740.png", record_pos=(-0.342, -0.298), resolution=(1080, 2240)))
sleep(60)




