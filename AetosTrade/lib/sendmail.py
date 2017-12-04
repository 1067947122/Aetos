#!/usr/bin/env python
#-*- coding:utf-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from email import MIMEMultipart
from email import Encoders
from common import read_ini
import os,sys
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_email(new_file,reportname):
    send = read_ini()[9]
    receive = read_ini()[10]
    pwd = read_ini()[11]
    server_163 = read_ini()[12]
    f = open(new_file,"rb")
    mail = f.read()

    msg = MIMEMultipart.MIMEMultipart()  #构造附件
    att = MIMEText(mail, 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename = "{0}"'.format(reportname)
    msg.attach(att)

    # pic = open(os.path.join(os.path.abspath("./"),"screenshots"),"rb")
    # file = pic.read()
    # att2 =MIMEBase("application","octet-stream")
    # att2.set_payload(file)
    # Encoders.encode_base64(att2)
    # att2.add_header("Content-Disposition","attachment",filename ="{0}".format("picture"))
    # msg.attach(att2)

    #构造邮件
    msg['From'] = _format_addr(u'测试邮箱 <%s>' % send)
    msg['To'] = _format_addr(u'王明<%s>' % receive)
    msg['Subject'] = Header(u'AetosTrade自动化测试报告', 'utf-8').encode()

    #构造邮件服务器
    server = smtplib.SMTP(server_163)
    #server.set_debuglevel(1)
    server.login(send, pwd)
    server.sendmail(send, [receive], msg.as_string())
    server.quit()
    print "Sent mail ok"
    f.close()

def new_report(report):

    # lists = os.listdir(testreport)
    # lists.sort(key = lambda fn: os.path.getmtime(testreport + '\\' + fn))
    # new_file = os.path.join(testreport,lists[-1])
    # print(new_file)
    # return new_file
    dirs = os.listdir(report)
    dirs.sort()
    reportname = dirs[-1]
    print 'The new report name: {0}'.format(reportname)
    new_file = os.path.join(report, reportname)
    return new_file,reportname


