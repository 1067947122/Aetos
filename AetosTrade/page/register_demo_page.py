#!/usr/bin/env python
#-*- coding:utf-8 -*-
from utils.get_by_local import GetByLocal
import time
from base.base_driver import Driver
class RegisterPage:
    # 获取注册页面所有的页面元素信息
    def __init__(self,driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    def get_register_au_btn_element(self):
        '''
        获取注册AU账户元素
        '''
        return self.get_by_local.get_element('register_au_btn','register_AU_demo_account')

    def get_back_element(self):
        '''
        获取返回元素信息
        '''
        return self.get_by_local.get_element('back','register_AU_demo_account')

    def get_close_element(self):
        '''
        获取关闭元素信息
        '''
        return self.get_by_local.get_element('close','register_AU_demo_account')

    def get_refresh_element(self):
        '''
        获取刷新元素信息
        '''
        return self.get_by_local.get_element('refresh','register_AU_demo_account')

    def get_area_code_element(self):
        '''
        获取手机区号元素信息
        '''
        return self.get_by_local.get_element('area_code','register_AU_demo_account')

    def get_phone_element(self):
        '''
        获取手机元素信息
        '''
        return self.get_by_local.get_element('phone','register_AU_demo_account')

    def get_verification_code_element(self):
        '''
        获取手机验证码元素信息
        '''
        return self.get_by_local.get_element('Verification_Code','register_AU_demo_account')

    def get_send_btn_element(self):
        '''
        获取发送按钮元素信息
        '''
        return self.get_by_local.get_element('send_btn','register_AU_demo_account')

    def get_next_step_element(self):
        '''
        获取下一步按钮元素信息
        '''
        return self.get_by_local.get_element('next_step','register_AU_demo_account')

    def get_mail_element(self):
        '''
        获取邮箱元素信息
        '''
        return self.get_by_local.get_element('mail','register_AU_demo_account')

    def get_call_element(self):
        '''
        获取称呼元素信息
        '''
        return self.get_by_local.get_element('call','register_AU_demo_account')

    def get_pwd_element(self):
        '''
        获取密码元素信息
        '''
        return self.get_by_local.get_element('pwd','register_AU_demo_account')

    def get_confirm_pwd_element(self):
        '''
        获取确认密码元素信息
        '''
        return self.get_by_local.get_element('confirm_pwd','register_AU_demo_account')

    def get_introducer_element(self):
        '''
        获取介绍人元素信息
        '''
        return self.get_by_local.get_element('introducer','register_AU_demo_account')

    def get_accept_term_element(self):
        '''
        获取接受条款元素信息
        '''
        return self.get_by_local.get_element('accept_term','register_AU_demo_account')

    def get_accept_ad_element(self):
        '''
        获取接受广告元素信息
        '''
        return self.get_by_local.get_element('accept_ad','register_AU_demo_account')

    def get_complete_element(self):
        '''
        获取接受完成元素信息
        '''
        return self.get_by_local.get_element('complete','register_AU_demo_account')

    def get_fill_data_element(self):
        '''
        获取完善资料并开立真实账户按钮元素
        '''
        return self.get_by_local.get_element('fill_data','register_AU_demo_account')

    def get_entre_trade_element(self):
        '''
        获取进入AETOSTrade元素
        '''
        return self.get_by_local.get_element('entre_trade','register_AU_demo_account')