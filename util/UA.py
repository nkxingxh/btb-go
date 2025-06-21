import random

class UAGenerator:
    def __init__(self):
        self.common_resolutions = [
            # 常见手机竖屏分辨率(宽x高)
            "360x800", "375x812", "390x844",  # 中低端安卓/iPhone mini
            "414x896", "428x926",  # iPhone 11/12/13
            "393x873", "430x932",  # iPhone 14/15
            "412x915", "360x780",  # 主流安卓手机
            "412x869", "360x800"   # 常见安卓手机
        ]

    def generate_mobile_ua(self):
        """
        生成手机客户端User-Agent
        :return: 生成的User-Agent字符串
        """
        # 随机选择手机类型和浏览器
        phone_type = random.choice(["iPhone", "Android"])
        browser = random.choice(["Chrome", "Safari", "Edge"])
        resolution = random.choice(self.common_resolutions)

        if phone_type == "iPhone":
            ios_version = f"{random.randint(13,16)}_0"
            safari_version = f"{random.randint(600,605)}.1.15"
            return f"Mozilla/5.0 ({phone_type}; CPU {phone_type} OS {ios_version} like Mac OS X) AppleWebKit/{safari_version} (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/{safari_version}"
        else:  # Android
            android_version = f"{random.randint(9,12)}.0"
            if browser == "Chrome":
                chrome_version = f"{random.randint(90,120)}.0.{random.randint(1000,9999)}.{random.randint(100,999)}"
                return f"Mozilla/5.0 (Linux; Android {android_version}; {resolution}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"
            elif browser == "Edge":
                edge_version = f"{random.randint(90,120)}.0.{random.randint(1000,9999)}.{random.randint(100,999)}"
                return f"Mozilla/5.0 (Linux; Android {android_version}; {resolution}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{edge_version} Mobile Safari/537.36 EdgA/{edge_version}"
            else:  # Safari
                return f"Mozilla/5.0 (Linux; Android {android_version}; {resolution}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{android_version} Mobile Safari/537.36"

# 示例用法
if __name__ == "__main__":
    ua_gen = UAGenerator()
    print("iPhone UA:", ua_gen.generate_mobile_ua())
    print("Android UA:", ua_gen.generate_mobile_ua())