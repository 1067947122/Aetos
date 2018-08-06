#!/usr/bin/env python
#-*- coding:utf-8 -*-
from utils.get_by_local import GetByLocal
import time
from base.base_driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # 获取登录页面所有的页面元素信息
    def __init__(self,driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    def get_username_element(self):
        '''
        获取用户名元素信息
        '''
        return self.get_by_local.get_element('username')

    def get_password_element(self):
        '''
        获取密码元素信息
        '''
        return self.get_by_local.get_element('password')

    def get_login_button_element(self):
        '''
        获取登陆按钮元素信息
        '''
        return self.get_by_local.get_element('login_button')

    def get_forget_password_element(self):
        '''
        忘记密码元素
        '''
        return self.get_by_local.get_element('forget_password')

    def get_remember_password_element(self):
        '''
        记住密码元素
        '''
        return self.get_by_local.get_element('remeber_pwd')

    def get_register_element(self):
        '''
        注册元素
        '''
        return self.get_by_local.get_element('register')

    def get_show_pwd_element(self):
        '''
        显示密码元素
        '''
        return self.get_by_local.get_element('show_pwd')

    def get_auto_login_element(self):
        '''
        自动登录元素
        '''
        return self.get_by_local.get_element('auto_login')

    def get_trade_account_element(self):
        '''
        获取交易账号元素
        '''
        return self.get_by_local.get_element('MT4','trade_account_login_element')

    def get_mt4_pwd_element(self):
        '''
        获取MT4登录页面密码元素
        '''
        return self.get_by_local.get_element('pwd','trade_account_login_element')

    def get_mt4_server_element(self):
        '''
        获取MT4登录页面server元素
        '''
        return self.get_by_local.get_element('server','trade_account_login_element')

    def get_back_element(self):
        '''
        获取其他地区登陆返回元素
        '''
        return self.get_by_local.get_element('back','other_area_login_element')

    def get_area_code_element(self):
        '''
        获取其他地区区号元素
        '''
        return self.get_by_local.get_element('area_code','other_area_login_element')

    def get_area_phone_element(self):
        '''
        获取其他地区手机号元素
        '''
        return self.get_by_local.get_element('phone','other_area_login_element')

    def get_area_pwd_element(self):
        '''
        获取其他地区密码元素
        '''
        return self.get_by_local.get_element('pwd','other_area_login_element')

    def get_select_mt4_server_element(self,server):
        '''
        获取点击server后的各服务器元素
        '''
        element = self.get_by_local.get_element('select_server','trade_account_login_element')
        for i in range(len(element)):
            text = element[i].text
            print(text)
            if text == server:
                return element[i]

    def get_mt4_login_btn_element(self):
        '''
        获取交易账号登陆元素
        '''
        return self.get_by_local.get_element('mt4_login_btn','trade_account_login_element')

    def get_other_area_btn_element(self):
        '''
        获取其它地区登陆元素
        '''
        return self.get_by_local.get_element('other_area_btn','other_area_login_element')

    def get_toast_element(self,message):
        '''
        获取toast_element
        '''
        time.sleep(2)
        toast_element = ('xpath','.//*[contains(@text,'+message+')]')
        try:
            element = WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(toast_element))
            print(element)
            return True
        except:
            return False

if __name__ == '__main__':
    driver = Driver()
    page = LoginPage(driver)


