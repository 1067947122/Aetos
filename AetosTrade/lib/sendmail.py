#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email import MIMEMultipart
from utils.read_ini import ReadIni
import os
class SendMail:
    def __init__(self, pass_list, fail_list,error_list):
        self.pass_list = pass_list
        self.fail_list = fail_list
        self.error_list = error_list
        self.reportname = self.new_report()
        self.read_ini = ReadIni()

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def new_report(self):
        if len(os.listdir('../reports')) == 0:
            return None
        else:
            dirs = os.listdir('../reports')
            dirs.sort()
            reportname = dirs[-1]
            print('The new report name: {0}'.format(reportname))
            return reportname

    def mail_result(self, ):
        pass_num = float(len(self.pass_list))
        fail_num = float(len(self.fail_list))
        error_num = float(len(self.error_list))
        count_num = pass_num + fail_num + error_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % ((fail_num +error_num ) / count_num * 100)

        content = "此次一共运行用例个数为{0}个,通过个数为{1}个,失败个数为{2},出现错误个数为{3},通过率为{4},失败率为{5}".format(
            count_num, pass_num, fail_num, error_num,pass_result, fail_result)
        return content

    def send_mail(self):
        content = self.mail_result()
        send = self.read_ini.get_value('send',section='email')
        receive = self.read_ini.get_value('receive',section='email')
        receive = receive.split(',')
        pwd = self.read_ini.get_value('pwd',section='email')
        server_163 = self.read_ini.get_value('server_163',section='email')
        if self.reportname == None:
            print(u'报告为空')
        else:
            new_file = os.path.join('../reports', self.reportname)
            with open(new_file, "rb") as fr:
                mail = fr.read()
            # 构造容器
            msg = MIMEMultipart.MIMEMultipart()
            msg['From'] = self._format_addr(u'王明的测试邮箱<%s>' % send)
            msg['To'] = ';'.join(receive)
            msg['Subject'] = Header(u'AetosTrade自动化测试报告', 'utf-8').encode()
            # 构造att1附件
            att1 = MIMEText(mail, _subtype='plain', _charset='utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment;filename = "{0}"'.format(self.reportname)
            msg.attach(att1)
            # 构造att2附件
            # if os.path.isfile("./screenshots.zip"):
            #     with open("./screenshots.zip", "rb").read() as file:
            #         att2 = MIMEText(file, 'base64', 'gb2312')
            #         att2["Content-Type"] = 'application/octet-stream'
            #         att2["Content-Disposition"] = 'attachment;filename = "screenshots.zip"'
            #         msg.attach(att2)



            # 构造发送内容
            con = MIMEText(content, _subtype='plain', _charset='utf-8')
            msg.attach(con)
            # 构造邮件服务器
            server = smtplib.SMTP(server_163)
            server.login(send, pwd)
            server.sendmail(send, receive, msg.as_string())
            server.quit()
            print("Send mail ok")


if __name__ == '__main__':
    sen = SendMail([2, 3, 45, 6], [1, 23, 5, 34],[0])
    sen.send_mail()












