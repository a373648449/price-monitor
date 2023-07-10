import requests
from bs4 import BeautifulSoup
import time
import re
from api.sendEmail import SendEmailAPI

# 创建SendEmailAPI实例
email_api = SendEmailAPI()

def get_product_price(url, sender_email, receiver_email, password):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    script_tag = soup.find('script', text=re.compile(r'window._itemInfo'))

    if script_tag:
        script_text = script_tag.text
        match = re.search(r'"p":"(\d+\.\d+)"', script_text)
        if match:
            price = match.group(1)
            return price
    return None


# 监控的产品链接
product_url = 'https://item.m.jd.com/product/100021529017.html?&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share&utm_user=plusmember&gx=RnAomTM2bTLanc0S-4J0XFdOllGsJA4&gxd=RnAolmVbPDXezZgVp9ZwVVxnOibys4sCL_TxonECFciNdqkNAvHdrqhSTufCAi8'

# 监控的价格阈值
target_price = 6100.00

# 邮件相关信息
sender_email = 'guoqiang0507@163.com'
receiver_email = '373648449@qq.com'
password = 'HUDZQIWQJGJDYLNQ'

while True:
    price = get_product_price(product_url, sender_email, receiver_email, password)
    print(f'当前价格：{price}')
    if float(price) <= target_price:
        subject = '产品价格监控提醒'
        message = f'当前价格低于或等于目标价格：{target_price}，赶快购买！'
        email_api.send_email(subject, message, sender_email, receiver_email, password)  # 调用send_email方法
        break
    time.sleep(60)  # 每分钟检查一次价格
