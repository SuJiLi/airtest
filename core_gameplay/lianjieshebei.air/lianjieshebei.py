# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

def is_locked():
    """
    通过adb检测设备是否锁屏
    返回True表示锁屏，False表示未锁屏
    """
    output = shell("dumpsys window")
    return "mDreamingLockscreen=true" in output or "isShowing=true" in output



dev = connect_device("Android:///Q2NVB21806000861")
try:
    dev = connect_device("Android:///Q2NVB21806000861")
    if not dev:
        raise RuntimeError("设备连接失败")
    print("设备连接成功")
except Exception as e:
    print(f"设备连接异常: {str(e)}")
    sys.exit(1)  # 非零退出码会标记构建失败:ml-citation{ref="6" data="citationList
    
max_retries = 3
retry_count = 0
while retry_count < max_retries:
    if is_locked():
        keyevent("POWER")  # 唤醒屏幕
        swipe((551,2124),(543,470))
            # 再次检查是否仍然锁定
        if is_locked():
            keyevent("POWER")
            swipe((551,1800),(543,470))  # 滑动解锁
            break  # 解锁成功则退出循环
        else:
            retry_count += 1
            print(f"屏幕又息屏了，重试 {retry_count}/{max_retries}")
    else:
        print("设备已解锁")
        break
else:
    print("达到最大重试次数，解锁失败")
sleep(5)
start_app("com.tencent.mm")
sleep(10)
swipe((501,334),(567,1539))
sleep(5)
touch(Template(r"tpl1747623798740.png", threshold=0.5, record_pos=(-0.342, -0.298), resolution=(1080, 2240)))
sleep(60)
