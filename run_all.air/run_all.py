import os
import sys
import time
from airtest.core.api import *
from airtest.core.api import connect_device
from airtest.report.report import simple_report, LogToHtml
from airtest.core.settings import Settings as ST

def get_image_dir():
    """智能获取图片目录路径（兼容新旧版Airtest）"""
    try:
        # 方案1：优先使用Airtest推荐路径
        from airtest.core.settings import Settings as ST
        if hasattr(ST, "TEMPLATE_DIR"):
            return os.path.join(ST.TEMPLATE_DIR, "img")
    except:
        pass
    
    """直接返回脚本所在目录（不强制要求img子目录）"""
    return os.path.dirname(__file__)

def restart_mini_program():
    """模拟用户操作重新进入小程序"""
    try:
        # 1. 点击右上角三个点（直接引用同级目录图片）
        touch(Template(r"tpl1744793615178.png", 
                      record_pos=(0.279, -0.95), 
                      resolution=(1080, 2220)))
        time.sleep(5)
        
        # 2. 点击重新进入按钮
        touch(Template(r"tpl1744793643021.png",
                      record_pos=(0.093, 0.674),
                      resolution=(1080, 2220)))
        
        # 3. 验证是否重启成功
        if wait(Template(r"tpl1744793695052.png",
                       record_pos=(-0.003, 0.049),
                       resolution=(1080, 2220)), timeout=100):
            print("重启成功")
            return True
                
    except Exception as e:
        print(f"[WARNING] 重启小程序失败: {str(e)}")
        return False
    
def run_test_script(script_path, device_uri="Android:///"):
    """执行单个测试脚本"""
    try:
        print(f"\n[INFO] 开始执行脚本: {os.path.basename(script_path)}")
        
        # 动态获取图片目录并验证
        image_dir = get_image_dir()
        if not os.path.exists(image_dir):
            raise FileNotFoundError(f"图片目录不存在: {image_dir}")
        
        # 连接设备
        connect_device(device_uri)
        
        # 通过命令行调用 airtest run
        ret = os.system(f"airtest run {script_path} --device {device_uri} --log ./logs")
        if ret != 0:
            raise RuntimeError(f"脚本返回非零状态码: {ret}")
            
        return True
        
    except Exception as e:
        print(f"[ERROR] 执行脚本出错: {str(e)}", file=sys.stderr)
        return False

def main():
    # 配置初始化
    test_dir = r"D:\PiaoFang_Test\core_gameplay"
    modules = ["test.air", "check_ui.air"]  # 可扩展其他模块
    device_uri = "Android:///TPC7N18515001155"  # 使用你的设备ID
    
    success_modules = []
    failed_modules = []
    
    for module in modules:
        script_path = os.path.join(test_dir, module)
        
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
    
    # 如果有失败的模块则返回非零状态码
    if failed_modules:
        sys.exit(1)

if __name__ == "__main__":
    # 设置工作目录为脚本所在位置
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()