import sys
import os
import time
import requests
import json
import hmac
import hashlib
import base64
import urllib.parse
from airtest.core.api import *

auto_setup(__file__)

def send_dingtalk_message(message, is_error=False):
    """
    发送钉钉机器人通知
    """
    try:
        # 钉钉机器人配置 - 请替换为实际的token和secret
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=d93115cbf7b839a6e78d457230a9cb29efb0b3ec75560609519dcac8c6f86312"
        secret = "SECf6190e5b6c84fac45da19cdec2d2524c00d9a7f6cb2e1743a3de8ed1f33c909f"
        
        # 生成签名
        timestamp = str(round(time.time() * 1000))
        string_to_sign = f"{timestamp}\n{secret}"
        hmac_code = hmac.new(
            secret.encode('utf-8'), 
            string_to_sign.encode('utf-8'), 
            digestmod=hashlib.sha256
        ).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        
        # 构建完整的webhook URL
        webhook_url = f"{webhook}&timestamp={timestamp}&sign={sign}"
        
        # 消息内容
        title = "❌ 服务器状态异常告警"
        text = f"""### {title}
        
**环境**: Jenkins自动化检测
**状态**: {message}
**时间**: {time.strftime('%Y-%m-%d %H:%M:%S')}
**设备**: AYATVB5528001633

@所有人 **请及时处理！**"""
        
        # 构建消息数据
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": text
            },
            "at": {
                "isAtAll": True
            }
        }
        
        # 发送请求
        headers = {'Content-Type': 'application/json'}
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✓ 钉钉消息发送成功")
            return True
        else:
            print(f"✗ 钉钉消息发送失败: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"✗ 发送钉钉消息异常: {e}")
        return False

def is_locked():
    """
    通过adb检测设备是否锁屏
    返回True表示锁屏，False表示未锁屏
    """
    try:
        output = shell("dumpsys window")
        return "mDreamingLockscreen=true" in output or "isShowing=true" in output
    except Exception as e:
        print(f"锁屏检测异常: {e}")
        return True

def unlock_device():
    """
    解锁设备
    """
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        if is_locked():
            print("设备已锁屏，尝试解锁...")
            keyevent("POWER")  # 唤醒屏幕
            sleep(2)
            swipe((551, 2124), (543, 470))  # 滑动解锁
            sleep(2)
            
            # 再次检查是否仍然锁定
            if is_locked():
                print("第一次解锁失败，再次尝试...")
                keyevent("POWER")
                sleep(2)
                swipe((551, 1800), (543, 470))  # 滑动解锁
                sleep(2)
            else:
                print("✓ 设备解锁成功")
                return True
        else:
            print("✓ 设备已解锁")
            return True
            
        retry_count += 1
        print(f"解锁失败，重试 {retry_count}/{max_retries}")
        sleep(3)
    
    print("✗ 达到最大重试次数，解锁失败")
    return False

def check_server_status():
    """
    检查服务器状态主流程
    """
    try:
        # 连接设备
        print("正在连接设备...")
        dev = connect_device("Android:///AYATVB5528001633")
        if not dev:
            raise RuntimeError("设备连接失败")
        print("✓ 设备连接成功")
        
        # 解锁设备
        if not unlock_device():
            send_dingtalk_message("设备解锁失败，无法进行服务器状态检测")
            return False
        
        # 启动微信应用
        print("启动微信应用...")
        start_app("com.tencent.mm")
        sleep(10)
        
        # 滑动操作
        swipe((501, 334), (567, 1539))
        sleep(5)
        
        # 点击目标位置
        touch(Template(r"tpl1747623798740.png", threshold=0.5, record_pos=(-0.342, -0.298), resolution=(1080, 2240)))
        sleep(50)
        
        # 检查服务器状态图像
        print("检查服务器状态...")
        tpl = Template(r"tpl1760320820379.png", threshold=0.5)
        
        if exists(tpl):
            print("✓ 服务器状态正常")
            # 正常状态不发送钉钉通知
            return True
        else:
            print("✗ 服务器状态异常")
            send_dingtalk_message("服务器状态异常，检测到服务不可用，请立即检查！")
            return False
            
    except Exception as e:
        error_msg = f"检测过程中发生异常: {str(e)}"
        print(f"✗ {error_msg}")
        send_dingtalk_message(error_msg)
        return False

if __name__ == "__main__":
    print("开始服务器状态检测...")
    
    success = check_server_status()
    
    if success:
        print("✓ 检测完成 - 状态正常")
        sys.exit(0)
    else:
        print("✗ 检测完成 - 状态异常")
        # 在退出前确保钉钉通知已发送
        sys.exit(1)