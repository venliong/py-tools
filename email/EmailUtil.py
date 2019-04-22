#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText


class MEmail(object):
    def __init__(self, host=None, send_user=None, send_user_pwd=None):
        if host is None:
            self.host = "smtp.163.com"
        if send_user is None:
            self.sendUserName = "account"
        if send_user_pwd is None:
            self.sendUserPwd = "password"
        self.smtp = None

    def connect_email(self):
        s = smtplib.SMTP()
        s.connect(self.host)
        self.smtp = s

    def login_email(self):
        self.smtp.login(self.sendUserName, self.sendUserPwd)

    def send_mail_text(self, to_addr, subject, content):
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = self.sendUserName
        msg['To'] = to_addr
        self.smtp.sendmail(self.sendUserName, to_addr, msg.as_string())

    def quit_email(self):
        print(self.smtp.quit())


e = MEmail()
e.connect_email()
e.login_email()
e.send_mail_text('account', subject="helloPython", content="pythonxx")
e.quit_email()