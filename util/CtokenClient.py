import requests

class CtokenClient:
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
