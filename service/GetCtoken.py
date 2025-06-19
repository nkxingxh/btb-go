import requests
from typing import Optional, Dict

class CtokenClient:
    """
    Ctoken客户端，用于获取和刷新ctoken
    
    参数:
        server_url (str): ctoken服务器地址
    """
    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip('/')  # 移除末尾的斜杠
    
    def get_ctoken(self, screen_width: int = 360, screen_height: int = 640) -> Dict[str, str]:
        """
        获取初始ctoken和ctkid
        
        参数:
            screen_width (int): 屏幕宽度，默认360(手机尺寸)
            screen_height (int): 屏幕高度，默认640(手机尺寸)
            
        返回:
            Dict[str, str]: 包含ctkid和ctoken的字典
            
        异常:
            requests.exceptions.RequestException: 当请求失败时抛出
        """
        url = f"{self.server_url}/generate"
        payload = {
            "screen_width": screen_width,
            "screen_height": screen_height
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # 检查HTTP错误
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"获取ctoken失败: {str(e)}")
    
    def refresh_ctoken(self, ctkid: str) -> Dict[str, str]:
        """
        通过ctkid刷新ctoken
        
        参数:
            ctkid (str): 之前获取的ctkid
            
        返回:
            Dict[str, str]: 包含新ctoken的字典
            
        异常:
            requests.exceptions.RequestException: 当请求失败时抛出
        """
        url = f"{self.server_url}/get/{ctkid}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查HTTP错误
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"刷新ctoken失败: {str(e)}")

# 示例用法
if __name__ == "__main__":
    # 示例服务器地址，实际使用时应该从用户界面传入
    SERVER_URL = "http://localhost:8080"
    
    client = CtokenClient(SERVER_URL)
    
    try:
        # 获取初始ctoken
        init_result = client.get_ctoken()
        print("获取ctoken成功:", init_result)
        
        # 刷新ctoken
        if "ctkid" in init_result:
            refresh_result = client.refresh_ctoken(init_result["ctkid"])
            print("刷新ctoken成功:", refresh_result)
    except Exception as e:
        print("发生错误:", str(e))
