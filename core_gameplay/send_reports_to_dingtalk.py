# -*- coding: utf-8 -*-
import os
import requests
import json
import glob
from datetime import datetime

def collect_test_reports(workspace_path):
    reports = []
    scripts = ["lianjieshebei", "check_ui", "jingying", "guanli", "shejiao", "cangku", "renwu"]
    
    for script in scripts:
        log_dir = os.path.join(workspace_path, f"{script}_log")
        if os.path.exists(log_dir):
            html_reports = glob.glob(os.path.join(log_dir, "*.html"))
            if html_reports:
                latest_report = max(html_reports, key=os.path.getmtime)
                reports.append({
                    'script_name': script,
                    'report_path': latest_report
                })
                print(f"Found report for: {script}")
    
    return reports

def main():
    # 替换为你的钉钉token
    DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN"
    
    WORKSPACE = r'C:\ProgramData\Jenkins\.jenkins\workspace\Piaofangdamaiwang\core_gameplay'
    
    print("Collecting test reports...")
    reports = collect_test_reports(WORKSPACE)
    
    script_list = "\n".join([f"- {r['script_name']}" for r in reports])
    
    message = {
        "msgtype": "markdown",
        "markdown": {
            "title": "测试报告",
            "text": f"""Airtest测试完成
时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
脚本数量: {len(reports)}

执行的脚本:
{script_list}

所有测试已完成，请查看相应日志目录获取详细报告。"""
        }
    }
    
    try:
        response = requests.post(DINGTALK_WEBHOOK, json=message, timeout=10)
        if response.status_code == 200:
            print("Message sent to DingTalk successfully")
        else:
            print(f"Failed to send: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()