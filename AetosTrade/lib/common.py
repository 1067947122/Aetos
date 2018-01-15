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
import zipfile
from HTMLTestRunner import  HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction
import configparser
import logging
import logging.handlers

def login(driver):
    username = read_ini()[0]
    password = read_ini()[1]
    driver.implicitly_wait(10)
    driver.find_element_by_id("login_user_et_account").clear()
    driver.find_element_by_id("login_user_et_password").clear()
    driver.find_element_by_id("login_user_et_account").send_keys(username)
    driver.find_element_by_id("login_user_et_password").send_keys(password)
    driver.find_element_by_id("login_btn").click()

def read_ini():
    con = configparser.ConfigParser()
    con.read("./config.ini")
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

def zip_dir(dirname,zipfilename):
    file_list = []
    if os.path.isfile(dirname):
        file_list.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                file_list.append(os.path.join(root, name))
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in file_list:
        arc_name = tar[len(dirname):]
        zf.write(tar, arc_name)
    zf.close()



def log_output():
    LOG_DIR = 'log'
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
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
    return logger

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






