#!/usr/bin/env python
#-*- coding:utf-8 -*-
#swipe --- 滑动
#zoom --- 放大
#pinch ---缩小
#tap --- 点点
#scroll ----滚动
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

desired_caps = {}
desired_caps['platformName'] = 'Android' #平台名称
desired_caps['platformVersion'] = '6.0.1' #版本号
desired_caps['deviceName'] = 'Galaxy On7(2016)' #设备名称
desired_caps['appPackage'] = 'com.hhly.community.test' #包名
desired_caps['appActivity'] = 'com.hhly.community.ui.welcome.WelcomeActivity' #appActivity名称
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) #访问手机
time.sleep(1)

ele = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID , "t1")))

#允许权限
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(1)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(1)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(1)
driver.find_element_by_android_uiautomator()
#模拟滑动
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)
def swipeLeft(t):
    screen = getSize()
    driver.swipe(screen[0]*0.75, screen[1]*0.5, screen[0]*0.25, screen[1]*0.5, t)
def swipeUp(t):
    screen = getSize()
    driver.swipe(screen[0]*0.5, screen[1]*0.75, screen[0]*0.5, screen[1]*0.25, t)

if __name__ == "__main__":
    swipeLeft(1000)
    swipeLeft(1000)
    swipeLeft(1000)

#点击立即体验
driver.find_element_by_id("com.hhly.community.test:id/btn_enter").click()

#点击以后再说
driver.find_element_by_id("com.hhly.community.test:id/cancel_update").click()

#进入服务页面
driver.find_element_by_id("com.hhly.community.test:id/bottom_item3_tv").click()
time.sleep(1)

#进入赛事列表页
driver.find_element_by_xpath("//android.widget.TextView[@text='赛事']").click()
time.sleep(3)

# 进入某个赛事的购买页
driver.find_element_by_xpath("//android.widget.Button[@content-desc='篮球 ']").click()
time.sleep(3)

#返回赛事列表页
driver.find_element_by_class_name("android.widget.ImageButton").click()
time.sleep(3)

#筛选
driver.tap([(1000,1590)], 500)#点击筛选按钮，进入筛选页面
driver.find_element_by_xpath("//android.widget.Button[@content-desc='全部']").click()#全部赛事
driver.find_element_by_xpath("//android.widget.Button[@content-desc='确认']").click()
a = driver.find_element_by_name("足球").get_attribute()
print a

time.sleep(3)
#上滑加载数据
swipeUp(1000)
# time.sleep(2)
# swipeUp(1000)
# time.sleep(2)
# swipeUp(1000)
# time.sleep(2)
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

