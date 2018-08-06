#!/usr/bin/env python
#-*- coding:utf-8 -*-
from lib.sendmail import SendMail
import os,sys
sys.path.append(os.path.dirname(os.getcwd()))
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest
import time
from utils.server import Server
from HTMLTestRunner import  HTMLTestRunner
from utils.write_txt import WriteTxt
from testcases.test_login_func import LoginApp

class Runner:
    def run(self):
        txt = WriteTxt()
        server = Server()
        server.main()
        test_dir = os.path.join(os.path.dirname(os.getcwd()),'testcases')
        #构造suite容器
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTests(loader.loadTestsFromTestCase(LoginApp))
        with open("../reports/test_reports_%s.html" % time.strftime("%Y-%m-%d %H-%M-%S"),"wb") as file:
            runner = HTMLTestRunner(stream=file,title=u"AetosTrade自动化测试报告",
                                    description=u"用例执行情况:")
            # discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
            runner.run(suite)
        pass_list,fail_list,error_list = txt.list_result()
        print(pass_list, fail_list,error_list)
        send_mail = SendMail(pass_list, fail_list,error_list)
        send_mail.send_mail()
        txt.clear_data()



if __name__ == '__main__':
    runner = Runner()
    runner.run()
