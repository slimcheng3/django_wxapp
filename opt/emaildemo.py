#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import django, os
import smtplib
from test_weather import settings
from email.mime.text import MIMEText

os.environ.setdefault('DJANGO__SETTINGS_MODULE', 'test_weather.settings')
django.setup()

def mail():
    msg = MIMEText("邮件测试", "plain", 'utf-8')
    msg["FROM"] = "mail test"
    msg["Subject"] = "【mail test】"
    receivers = ['936534130@qq.com']
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()
    pass

if __name__ == "__main__":
    mail()

