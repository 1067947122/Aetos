#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os,sys
import time
from time import sleep
from lib.com_class import Login
class News(Login):
    def test_keyword_search_news(self):
        """通过关键字查看新闻"""
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/main_rb_info").click()
        sleep(3)
        title = driver.find_element_by_id("com.aetos:id/bar_title").text
        print title
        self.assertEqual(title,u"新闻")
        driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.EditText\")").send_keys("USD")
        driver.find_element_by_id("com.aetos:id/fragment_news_list_btn_search").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "keyword_search_news_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

    # def test_click_search_news(self):
    #     """点击查看新闻内容"""
    #     driver = self.driver
    #     driver.implicitly_wait(10)
    #     driver.find_element_by_id("com.aetos:id/main_rb_info").click()
    #     driver.find_elements_by_id("com.aetos:id/news_item_org_tv_content")[0].click()
    #     driver.get_screenshot_as_file(
    #         os.path.join(os.path.abspath("./screenshots"),
    #                      "click_search_news_num1_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
    #     driver.find_element_by_id("com.aetos:id/back_bar_back").click()
    #     driver.find_elements_by_id("com.aetos:id/news_item_org_tv_content")[1].click()
    #     driver.get_screenshot_as_file(
    #         os.path.join(os.path.abspath("./screenshots"),
    #                      "click_search_news_num2_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
    #     driver.find_element_by_id("com.aetos:id/back_bar_back").click()
    #     driver.find_elements_by_id("com.aetos:id/news_item_org_tv_content")[2].click()
    #     driver.get_screenshot_as_file(
    #         os.path.join(os.path.abspath("./screenshots"),
    #                      "click_search_news_num3_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
    #     driver.find_element_by_id("com.aetos:id/back_bar_back").click()
