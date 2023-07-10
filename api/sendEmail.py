import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendEmailAPI:
    def __init__(self):
        pass

    def send_email(self, subject, message, sender_email, receiver_email, password):
        smtp_server = 'smtp.163.com'
        smtp_port = 465

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = Header(subject, 'utf-8')

        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())


# 创建SendEmailAPI实例
email_api = SendEmailAPI()

# 调用send_email方法发送邮件
email_api.send_email(
    subject='邮件主题1',
    message='邮件内容1',
    sender_email='guoqiang0507@163.com',
    receiver_email='373648449@qq.com',
    password='HUDZQIWQJGJDYLNQ'
)
