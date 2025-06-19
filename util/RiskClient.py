import requests
from typing import Optional, Dict, List, Any

class RiskClient:
    def __init__(self, server_url):
        self.server_url = server_url.rstrip('/')

    def get_ctoken(self):
        """获取ctoken"""
        try:
            response = requests.get(f"{self.server_url}/api/ctoken")
            response.raise_for_status()
            return response.json().get('ctoken', '')
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

    def get_cookie_ticket(self, user_agent: str, cookies: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        通过API获取Cookie_ticket

        参数:
            user_agent (str): 用户代理字符串
            cookies (List[Dict[str, str]]): Cookie数组，每个元素包含name、value等字段

        返回:
            Dict[str, Any]: API响应结果

        异常:
            requests.exceptions.RequestException: 当请求失败时抛出
        """
        url = f"{self.server_url}/getticket"
        payload = {
            "user_agent": user_agent,
            "cookies": cookies
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # 检查HTTP错误
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"获取Cookie_ticket失败: {str(e)}")
