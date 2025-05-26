import os
import sys
import time
from airtest.core.api import *
from airtest.report.report import simple_report, LogToHtml
from airtest.core.settings import Settings as ST  # 显式导入Settings

def restart_mini_program():
    """模拟用户操作重新进入小程序（使用绝对路径引用图片）"""
    try:
        # 获取当前脚本所在目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 1. 点击右上角三个点（使用绝对路径）
        touch(Template(os.path.join(script_dir, "tpl1744793615178.png"), 
                      record_pos=(0.279, -0.95), 
                      resolution=(1080, 2220)))
        time.sleep(5)
        
        # 2. 点击重新进入按钮
        touch(Template(os.path.join(script_dir, "tpl1744793643021.png"),
                      record_pos=(0.093, 0.674),
                      resolution=(1080, 2220)))
        
        # 3. 验证是否重启成功
        if wait(Template(os.path.join(script_dir, "tpl1744793695052.png"),
                       record_pos=(-0.003, 0.049),
                       resolution=(1080, 2220)), timeout=100):
            print("重启成功")
            return True
                
    except Exception as e:
        print(f"[WARNING] 重启小程序失败: {str(e)}")
        return False
def is_locked():
    """
    通过adb检测设备是否锁屏
    返回True表示锁屏，False表示未锁屏
    """
    output = shell("dumpsys window")
    return "mDreamingLockscreen=true" in output or "isShowing=true" in output

if __name__ == "__main__":
    
    dev = connect_device("Android:///TPC7N18515001155")
        # 设置工作目录为脚本所在位置
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        if is_locked():
            keyevent("POWER")  # 唤醒屏幕
            swipe((551,1800),(543,470))
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
    touch(Template(r"tpl1747623798740.png", threshold=0.5, record_pos=(-0.342, -0.298), resolution=(1080, 2240)))
    sleep(60)