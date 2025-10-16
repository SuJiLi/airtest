import os
import requests
import json
import glob
from datetime import datetime

def collect_test_reports(workspace_path):
    """
    收集所有测试脚本的报告信息
    """
    reports = []
    script_dirs = [
        "lianjieshebei", "check_u1", "jingying", "guanli", 
        "shejiao", "cangku", "renwu"
    ]
    
    for script in script_dirs:
        log_dir = os.path.join(workspace_path, f"{script}_log")
        if os.path.exists(log_dir):
            # 查找最新的报告文件
            html_reports = glob.glob(os.path.join(log_dir, "*.html"))
            log_files = glob.glob(os.path.join(log_dir, "*.txt"))
            
            if html_reports:
                # 按修改时间排序，取最新的报告
                latest_report = max(html_reports, key=os.path.getmtime)
                reports.append({
                    'script_name': script,
                    'report_path': latest_report,
                    'log_path': log_files[0] if log_files else None,
                    'status': 'SUCCESS' if '成功' in script else 'UNKNOWN'
                })
    
    return reports

def generate_dingtalk_message(reports, workspace_path, build_info=None):
    """
    生成钉钉消息内容
    """
    total_scripts = len(reports)
    success_count = sum(1 for r in reports if r['status'] == 'SUCCESS')
    failed_count = total_scripts - success_count
    
    # 构建消息内容
    message = {
        "msgtype": "markdown",
        "markdown": {
            "title": "Airtest 自动化测试报告",
            "text": f"""## 🧪 Airtest 核心玩法测试报告
**📊 测试概况**
- 执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 总脚本数: {total_scripts} 个
- 成功脚本: {success_count} 个
- 失败脚本: {failed_count} 个
- 成功率: {success_count/total_scripts*100:.1f}%

**📋 脚本执行详情**
{generate_script_details(reports)}

**🔗 报告访问**
- Jenkins 构建: {build_info.get('jenkins_url', 'N/A') if build_info else 'N/A'}
- 工作目录: {workspace_path}

**💡 说明**
- 点击脚本名称查看详细报告
- 绿色 ✅ 表示成功，红色 ❌ 表示失败
"""
        }
    }
    return message

def generate_script_details(reports):
    """
    生成脚本执行详情
    """
    details = []
    for report in reports:
        status_icon = "✅" if report['status'] == 'SUCCESS' else "❌"
        script_name = report['script_name']
        
        # 这里可以添加报告文件的链接（如果有web服务器的话）
        report_link = f"file://{report['report_path']}"  # 本地文件链接
        
        details.append(f"- {status_icon} **{script_name}** - [查看报告]({report_link})")
    
    return "\n".join(details)

def send_to_dingtalk(webhook_url, message):
    """
    发送消息到钉钉
    """
    try:
        response = requests.post(
            webhook_url,
            json=message,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ 报告已成功推送到钉钉")
            return True
        else:
            print(f"❌ 推送失败，状态码: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ 推送出错: {e}")
        return False

def main():
    # 钉钉机器人 webhook URL
    DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=d93115cbf7b839a6e78d457230a9cb29efb0b3ec75560609519dcac8c6f86312"
    
    # Jenkins 工作空间路径
    WORKSPACE = os.getenv('WORKSPACE', r'C:\ProgramData\Jenkins\.jenkins\workspace\Piaofangdamaiwang\core_gameplay')
    
    # 构建信息
    build_info = {
        'jenkins_url': os.getenv('BUILD_URL', ''),
        'build_number': os.getenv('BUILD_NUMBER', ''),
        'job_name': os.getenv('JOB_NAME', '')
    }
    
    print("开始收集测试报告...")
    
    # 收集所有报告
    reports = collect_test_reports(WORKSPACE)
    
    if not reports:
        print("❌ 未找到任何测试报告")
        return
    
    print(f"✅ 共收集到 {len(reports)} 个测试报告")
    
    # 生成钉钉消息
    message = generate_dingtalk_message(reports, WORKSPACE, build_info)
    
    # 发送到钉钉
    print("正在推送报告到钉钉...")
    send_to_dingtalk(DINGTALK_WEBHOOK, message)

if __name__ == "__main__":
    main()