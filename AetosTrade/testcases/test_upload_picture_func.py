#!/usr/bin/env python
#-*- coding:utf-8 -*-
from lib.com_class import Login
import os,sys,time
from time import sleep
class Upload(Login):
    def test_upload_head_picture(self):
        """用户上传头像"""
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/main_rb_self").click()
        driver.find_element_by_id("com.aetos:id/self_user_icon").click()
        driver.find_element_by_id("com.aetos:id/userinfo_photo").click()
        driver.find_element_by_id("com.aetos:id/media_item_check").click()
        driver.find_element_by_id("com.aetos:id/choose_ok_btn").click()
        sleep(5)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "upload_picture_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))