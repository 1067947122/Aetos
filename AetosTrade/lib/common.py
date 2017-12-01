#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os,sys
from HTMLTestRunner import  HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction
import configparser
import logging
import logging.handlers

def read_ini():
    con = configparser.ConfigParser()
    con.read("../config.ini")
    username = con.get("login","username")
    password = con.get("login","password")
    error_username = con.get("login","error_username")
    error_pwd = con.get("login","error_pwd")
    mt4id = con.get("login","mt4id")
    error_mt4id = con.get("login","error_mt4id")
    oversea = con.get("login","oversea")
    area_code = con.get("login","area_code")
    error_oversea = con.get("login","error_oversea")
    send = con.get("email","send")
    receive = con.get("email","receive")
    pwd = con.get("email","pwd")
    server_163 = con.get("email","server_163")
    user = [username,password,error_username,error_pwd,mt4id,error_mt4id,oversea,area_code,error_oversea,
                send,receive,pwd,server_163]
    return user


# def screenshot(driver):
#     driver.get_screenshot_as_file("../screenshots/shots_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S"))
# #模拟滑动
# def getSize(driver):
#     x = driver.get_window_size()['width']
#     y = driver.get_window_size()['height']
#     print x,y
#     return x,y
#
# def swipeLeft(driver,t):
#     screen = getSize(driver)
#     driver.swipe(screen[0]*0.75, screen[1]*0.5, screen[0]*0.25, screen[1]*0.5, t)
#
# def swipeUp(driver,t):
#     screen = getSize(driver)
#     driver.swipe(screen[0]*0.5, screen[1]*0.57, screen[0]*0.5, screen[1]*0.25, t)
#
# def swipeDown(driver,t):
#     w_size = getSize(driver)
#     x1 = int(w_size[0] * 0.5)    #获取x坐标，根据实际调整相乘参数
#     y1 = int(w_size[1] * 0.2)    #获取起始y坐标，根据实际调整相乘参数
#     y2 = int(w_size[1] * 0.8)    #获取终点y坐标，根据实际调整相乘参数
#     driver.swipe(x1, y1, x1, y2,t)
#
# def swipeRight(driver,t):
#     w_size = getSize(driver)
#     x1 = int(w_size[0] * 0.05)
def login(driver):
    username = read_ini()[0]
    password = read_ini()[1]
    driver.implicitly_wait(10)
    driver.find_element_by_id("login_user_et_account").clear()
    driver.find_element_by_id("login_user_et_password").clear()
    driver.find_element_by_id("login_user_et_account").send_keys(username)
    driver.find_element_by_id("login_user_et_password").send_keys(password)
    driver.find_element_by_id("login_btn").click()

def log_output():
    logger = logging.getLogger('process')
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.TimedRotatingFileHandler(os.path.join(os.path.abspath("./log"),"process_%s.log"% time.strftime("%Y-%m-%d %H-%M-%S")),'D')
    handler.setLevel(logging.DEBUG)
    process_formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    handler.setFormatter(process_formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    console_formatter = logging.Formatter('%(asctime)s:%(message)s')
    console.setFormatter(console_formatter)

    logger.addHandler(console)
    logger.addHandler(handler)

def is_toast_exist(driver,text,timeout=10,poll_frequency=0.5):
   '''is toast exist, return True or False
   :Agrs:
    - driver - 传driver
    - text   - 页面上看到的文本内容
    - timeout - 最大超时时间，默认30s
    - poll_frequency  - 间隔查询时间，默认0.5s查询一次
   :Usage:
    is_toast_exist(driver, "看到的内容")
   '''
   try:
       element = ("xpath", ".//*[contains(@text,'%s')]"%text)
       WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(element))
       print element
       return True
   except:
       return False

def is_id_exist(driver,ele):
    try:
        driver.find_element_by_id(ele)
        print True
    except:
        print False
#TouchAction
#TouchAction方法是appium自已定义的新方法
# * 短按 (press) * 释放 (release) * 移动到 (moveTo) * 点击 (tap) * 等待 (wait) * 长按 (longPress)  * 执行 (perform)
#以python为例
#
#
# TouchAction(driver).press(el0).moveTo(el1).release()
# #TouchAction 在python中是一个类它下面的方法有
#
# #长按
# long_press(self, el=None, x=None, y=None, duration=1000(ms))
# #短按
# press(self, el=None, x=None, y=None)
# #点击
# tap(self,el=None,x=None,y=None,count=1)
# #释放
# release(self)
# #移动到
# move_to(self,el=None,x=None,y=None)
# #等待
# wait(self,ms=0)
# #执行
# perform(self)
#
#
#
# #关于perform 官网给的伪代码中讲
# TouchAction().tap(el).perform()
# #与
# driver.perform(TouchAction().tap(el))
# #效果一致
#
#
# #MultiTouch
# #MultiTouch 多点触控 它只提供了两个方法 一个add 一个执行perform.官网例子为
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction
#
# action0 = TouchAction().tap(el1)
# action1 = TouchAction().tap(el2)
# MultiTouch().add(action0).add(action1).perform








