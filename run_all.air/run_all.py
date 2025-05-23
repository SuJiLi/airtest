import os
import sys
import time
from airtest.core.api import *
from airtest.report.report import simple_report, LogToHtml
from airtest.core.settings import Settings as ST  # 显式导入Settings

# 修复ST.IMAGE_DIR问题（关键修改）
if not hasattr(ST, 'IMAGE_DIR'):
    ST.IMAGE_DIR = os.path.join(os.path.dirname(__file__), "..")  # 指向上级目录

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

def run_test_script(script_path, device_uri="Android:///"):
    """执行单个测试脚本（增加路径验证）"""
    try:
        print(f"\n[INFO] 开始执行脚本: {os.path.basename(script_path)}")
        
        # 验证脚本路径是否存在
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"脚本路径不存在: {script_path}")
        
        # 连接设备（增加重试机制）
        for i in range(3):
            try:
                connect_device(device_uri)
                break
            except Exception as e:
                if i == 2:
                    raise
                print(f"[RETRY] 设备连接失败，正在重试... ({i+1}/3)")
                time.sleep(2)
        
        # 执行脚本（使用绝对路径）
        cmd = f'airtest run "{script_path}" --device "{device_uri}" --log ./logs'
        print(f"执行命令: {cmd}")
        ret = os.system(cmd)
        
        if ret != 0:
            raise RuntimeError(f"脚本执行失败，返回码: {ret}")
            
        return True
        
    except Exception as e:
        print(f"[ERROR] 执行脚本出错: {str(e)}", file=sys.stderr)
        return False

def main():
    # 配置初始化
    test_dir = os.path.join(os.path.dirname(__file__), "..", "core_gameplay")  # 使用相对路径
    modules = ["check_ui.air"]  # 可扩展其他模块
    device_uri = "Android:///235424b0b00c7ece"
    
    # 初始化日志目录
    os.makedirs("./logs", exist_ok=True)
    
    success_modules = []
    failed_modules = []
    
    for module in modules:
        script_path = os.path.join(test_dir, module)
        print(f"\n{'='*30}\n开始处理模块: {module}\n{'='*30}")
        
        # 验证模块路径
        if not os.path.exists(script_path):
            print(f"[ERROR] 模块不存在: {script_path}")
            failed_modules.append(module)
            continue
            
        # 首次尝试执行
        if run_test_script(script_path, device_uri):
            success_modules.append(module)
            continue
            
        # 如果失败，尝试恢复操作
        print("[WARNING] 尝试恢复测试环境...")
        if restart_mini_program():
            # 恢复后重试
            if run_test_script(script_path, device_uri):
                success_modules.append(module)
                continue
                
        # 仍然失败则记录
        failed_modules.append(module)
    
    # 生成测试报告
    print("\n===== 测试结果汇总 =====")
    print(f"成功模块 ({len(success_modules)}个):")
    for m in success_modules: print(f"  - {m}")
    
    print(f"\n失败模块 ({len(failed_modules)}个):")
    for m in failed_modules: print(f"  - {m}")
    
    # 生成HTML报告
    try:
        simple_report(__file__, logpath="./logs")
    except Exception as e:
        print(f"[WARNING] 生成报告失败: {str(e)}")
    
    # 如果有失败的模块则返回非零状态码
    if failed_modules:
        sys.exit(1)
        
def is_locked():
    """
    通过adb检测设备是否锁屏
    返回True表示锁屏，False表示未锁屏
    """
    output = shell("dumpsys window")
    return "mDreamingLockscreen=true" in output or "isShowing=true" in output

if __name__ == "__main__":
    
    dev = connect_device("Android:///235424b0b00c7ece")
    if is_locked():
        keyevent("POWER")  # 唤醒屏幕
        swipe((551,1800),(543,470))  # 滑动解锁
    else:
        print("设备已解锁")
    sleep(5)
    start_app("com.tencent.mm")
    sleep(10)
    swipe((501,334),(567,1539))
    touch(Template(r"tpl1747623798740.png", threshold=0.5, record_pos=(-0.342, -0.298), resolution=(1080, 2240)))
    sleep(60)
    # 设置工作目录为脚本所在位置
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 打印关键路径信息（调试用）
    print(f"当前工作目录: {os.getcwd()}")
    print(f"ST.IMAGE_DIR: {getattr(ST, 'IMAGE_DIR', '未设置')}")
    main()