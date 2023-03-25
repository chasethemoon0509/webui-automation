"""
群发测试结果邮件

以 QQ 邮箱为例
"""
import smtplib
from email.mime.text import MIMEText

from utils.log import log


def send_email(total=None, passed=None, failed=None, xfailed=None, skipped=None, receivers=None):
    host = 'smtp.qq.com'
    port = 465
    user = ''
    password = ''
    sender = ''
    receivers = ['接收者1', '接收者2', '接收者3', ...]

    message_content = f'''
        <p>此邮件为系统自动发送，无需回复。</p>
        <h3 style='color: red'>index.html 项目测试报告：</h3>
        <ul>
        <li>测试用例总数: {total}</li>
        <li>通过数: {passed}</li>
        <li>失败数: {failed}</li>
        <li>预期失败数: {xfailed}</li>
        <li>跳过数: {skipped}</li>
        <li>通过率: {format((passed / total) * 100, '.1f')}%</li>
        <li>失败率: {format((failed / total) * 100, '.1f')}%</li>
        </ul>
        详细测试报告 url: <a href='https://www.baidu.com'>https://www.baidu.com</a>
    '''
    message = MIMEText(message_content, 'html', 'utf-8')
    message['Subject'] = '测试报告'
    message['From'] = sender

    try:
        smtp_obj = smtplib.SMTP_SSL(host, port)
        smtp_obj.login(user, password)
        for i in receivers:
            message['To'] = i
            smtp_obj.sendmail(sender, i, message.as_string())
        smtp_obj.quit()
        log.info('邮件发送成功')
    except smtplib.SMTPException as e:
        log.error('邮件发送失败: {}', e)







