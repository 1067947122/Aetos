#!/usr/bin/env python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
from utils.write_user_command import WriteUserCommand
import os,re
from utils.execute_cmd import DosCmd
APP_PATH = os.path.join(os.path.dirname(os.getcwd()),r'package\AetosTrade.apk')
class Driver:
    def __init__(self):
        self.cmd = DosCmd()

    def android_driver(self,i):

        print("this is android_driver:",i)
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        # platformVersion = self.cmd.excute_cmd_result('adb shell getprop ro.build.version.release')[0].strip() #获取Android版本
        # pack = self.cmd.excute_cmd_result('aapt dump badging ' + APP_PATH) #获取apppackage
        # appPackage = re.findall(r'\'com\w*.*?\'', pack[0])[0]
        print(devices,port)

        dic = {
            'platformName' : 'Android',
            'platformVersion': '5.0',
            'deviceName': '192.168.218.101:5555',
            'appPackage': 'com.aetos',
            'appActivity': 'com.aetos.ui.module.core.LoadingActivity',
            'app': APP_PATH,
            'noReset' : 'true',
            # 'noSign': 'true',
            # 'automationName':'uiautomator2'

        }
        driver = webdriver.Remote('http://127.0.0.1:' + '4723' + '/wd/hub', dic)
        driver.implicitly_wait(15)
        return driver

if __name__ == '__main__':
    driver = Driver().android_driver(0)
    print(driver)