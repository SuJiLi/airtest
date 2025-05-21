import os
from airtest.core.api import *
from airtest.core.api import connect_device, start_app, stop_app
from airtest.report.report import simple_report, LogToHtml
def restart_mini_program():
    """模拟用户操作重新进入小程序"""
    try:
        # 1. 点击右上角三个点
        touch(Template(r"tpl1744793615178.png", record_pos=(0.279, -0.95), resolution=(1080, 2220)))  # 假设右上角位置（根据实际调整坐标）
        time.sleep(5)
        touch(Template(r"tpl1744793643021.png", record_pos=(0.093, 0.674), resolution=(1080, 2220)))
        if wait(Template(r"tpl1744793695052.png", record_pos=(-0.003, 0.049), resolution=(1080, 2220)),timeout=100):
            print("重启成功")
                
    except Exception as e:
        print(f"[WARNING] 重启小程序失败: {str(e)}")
        raise  # 如果重启失败则抛出异常

def run_scripts():
    # 初始化设备连接（可选）
    connect_device("Android:///")
    
    test_dir = r"D:\PiaoFang_Test\core_gameplay"
    modules = ["test.air","check_ui.air"]
    #, "shichang.air", "yiren.air"
    
    # 用于记录成功和失败的模块
    success_modules = []
    failed_modules = []
    for module in modules:
        script_path = os.path.join(test_dir, module)
        print(f"\n===== Running script: {module} =====")
        
        try:
            # 通过命令行调用 airtest run
            ret = os.system(f"airtest run {script_path} --device Android:///")
            if ret != 0:
                raise RuntimeError(f"脚本返回非零状态码: {ret}")
                
            # 如果执行成功，添加到成功列表
            success_modules.append(module)
            
        except Exception as e:
            print(f"[ERROR] 执行 {module} 时出错: {str(e)}", file=sys.stderr)
            # 添加到失败列表
            failed_modules.append(module)
            
            try:
                # 尝试重新进入小程序
                print("尝试重新进入小程序...")
                restart_mini_program()
            except Exception as restart_error:
                print(f"[CRITICAL] 小程序重启失败: {str(restart_error)}")
                continue  # 继续下一个模块

    # 所有模块运行完毕后输出结果
    print("\n===== 测试结果汇总 =====")
    print(f"成功执行的模块 ({len(success_modules)}个):")
    for module in success_modules:
        print(f"  - {module}")
    
    print(f"\n执行失败的模块 ({len(failed_modules)}个):")
    for module in failed_modules:
        print(f"  - {module}")
    
    # 如果有失败的模块，可以返回非零状态码
    if failed_modules:
        sys.exit(1)  

if __name__ == "__main__":
    run_scripts()
    
    
    
    
    
    