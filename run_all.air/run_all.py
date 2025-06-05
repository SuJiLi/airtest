import os
import sys
import time
from airtest.core.api import *
from airtest.report.report import simple_report, LogToHtml
from airtest.core.settings import Settings as ST  # 显式导入Settings
from airtest.cli.runner import AirtestCase, run_script
from airtest.cli.parser import runner_parser
import traceback

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
    
    
    
def call_multiple_air_scripts_with_recovery(script_paths):
    """
    按顺序调用多个AIR脚本，带有错误恢复机制
    
    参数:
        script_paths: 要调用的AIR脚本路径列表
    
    返回:
        dict: 包含每个脚本调用结果的字典
    """
    original_dir = os.getcwd()
    results = {}
    
    for idx, script_path in enumerate(script_paths, 1):
        script_name = os.path.basename(script_path)
        script_dir = os.path.dirname(script_path)
        
        try:
            # 切换到目标目录
            os.chdir(script_dir)
            print(f"\n[{idx}/{len(script_paths)}] 切换到目录: {script_dir}")
            
            # 调用脚本 - 使用更可靠的调用方式
            print(f"开始调用脚本: {script_name}")
            
            # 创建并配置运行参数
            args = runner_parser.parse_args([])
            args.script = script_name
            args.device = []  # 确保device参数存在
            
            # 初始化AirtestCase
            test_case = AirtestCase(args)
            test_case.setUpClass()
            
            # 运行脚本
            run_script(args, test_case)
            
            # 记录成功结果
            results[script_name] = {
                'status': 'success',
                'message': '脚本调用成功',
                'recovery_executed': False
            }
            print(f"脚本 {script_name} 调用成功")
            
        except Exception as e:
            # 记录原始错误信息
            error_msg = str(e)
            print(f"\n脚本 {script_name} 调用失败: {error_msg}")
            print("尝试执行恢复操作...")
            
            # 执行恢复方法
            recovery_success = restart_mini_program()
            
            # 记录失败结果（包含恢复信息）
            results[script_name] = {
                'status': 'failed',
                'message': error_msg,
                'recovery_executed': True,
                'recovery_success': recovery_success,
                'traceback': traceback.format_exc()
            }
            
            print(f"恢复操作执行{'成功' if recovery_success else '失败'}，将继续执行下一个脚本")
            
        finally:
            # 每个脚本调用后都恢复原始目录
            os.chdir(original_dir)
            try:
                test_case.tearDownClass()
            except:
                pass
    
    # 最终汇总报告
    print("\n所有脚本调用完成，结果汇总:")
    for name, result in results.items():
        status = result['status']
        msg = result['message']
        if result['status'] == 'failed':
            recovery_info = "（已执行恢复）" if result['recovery_executed'] else ""
            print(f"{name}: {status}{recovery_info} - {msg}")
        else:
            print(f"{name}: {status} - {msg}")
    
    return results

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
    sleep(5)
    touch(Template(r"tpl1747623798740.png", threshold=0.5, record_pos=(-0.342, -0.298), resolution=(1080, 2240)))
    sleep(60)
    test_sequence = [
        r"D:\PiaoFang_Test\core_gameplay\check_ui.air",
    ]
    
    # 调用带恢复功能的顺序执行方法
    final_results = call_multiple_air_scripts_with_recovery(test_sequence)
    
    # 分析最终结果
    failed_scripts = [name for name, res in final_results.items() if res['status'] == 'failed']
    if not failed_scripts:
        print("\n✅ 所有脚本执行成功！")
    else:
        print(f"\n⚠️ 有 {len(failed_scripts)} 个脚本执行失败: {', '.join(failed_scripts)}")