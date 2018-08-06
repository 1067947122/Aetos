#!/usr/bin/env python
#-*- coding:utf-8 -*-
from handle.login_handle import LoginHandle
from utils.read_ini import ReadIni
from utils.write_txt import WriteTxt
from base.base_driver import Driver
from page.login_page import LoginPage
class LoginBusiness:
	def __init__(self,driver):
		self.login_handle = LoginHandle(driver)
		self.driver = driver
		self.ini = ReadIni()
		self.txt = WriteTxt()
		self.login_page = LoginPage(driver)
		self.username = self.ini.get_value('username','login_value')
		self.password = self.ini.get_value('password','login_value')
		self.error_username = self.ini.get_value('error_username', 'login_value')
		self.error_pwd = self.ini.get_value('error_pwd', 'login_value')
		self.mt4 = self.ini.get_value('mt4id','login_value')
		self.error_mt4 = self.ini.get_value('error_mt4id','login_value')
		self.driver.implicitly_wait(15)

	def username_login_pass(self):
		'''
		用户名和密码都输入正确
		'''
		self.login_handle.send_username(self.username)
		self.login_handle.send_password(self.password)
		self.login_handle.click_login()

	def username_login_username_error(self):
		'''
		用户名输入错误，密码输入正确
		'''
		self.login_handle.send_username(self.error_username)
		self.login_handle.send_password(self.password)
		self.login_handle.click_login()


	def username_login_password_error(self):
		'''
		用户名输入正确，密码输入错误
		'''
		self.login_handle.send_username(self.username)
		self.login_handle.send_password(self.error_pwd)
		self.login_handle.click_login()

	def mt4_login_pass(self,server):
		'''
		交易账号输入正确，密码输入正确
		'''
		self.login_handle.click_mt4_btn()
		self.login_handle.send_trade_account(self.mt4)
		self.login_handle.send_mt4_pwd(self.password)
		self.login_handle.click_server()
		self.login_handle.click_select_mt4_server(server)
		self.login_handle.click_login()

	def mt4_login_mt4_error(self,server):
		'''
		交易账号输入错误，密码输入正确
		'''
		self.login_handle.click_mt4_btn()
		self.login_handle.send_trade_account(self.error_mt4)
		self.login_handle.send_mt4_pwd(self.password)
		self.login_handle.click_server()
		self.login_handle.click_select_mt4_server(server)
		self.login_handle.click_login()

	def mt4_login_pwd_error(self,server):
		'''
		交易账号输入正确，密码输入错误
		'''
		self.login_handle.click_mt4_btn()
		self.login_handle.send_trade_account(self.mt4)
		self.login_handle.send_mt4_pwd(self.error_pwd)
		self.login_handle.click_server()
		self.login_handle.click_select_mt4_server(server)
		self.login_handle.click_login()

if __name__ == '__main__':
	driver = Driver().android_driver(0)
	bu = LoginBusiness(driver)
