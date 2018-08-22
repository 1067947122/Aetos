#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
from base.base_driver import Driver
from utils.write_txt import WriteTxt
from business.fill_data_business import FillDataBusiness

class FillData(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().android_driver(0)
        self.txt = WriteTxt()
        self.driver.implicitly_wait(20)
        self.fill_data_bussiness = FillDataBusiness(self.driver)

    def tearDown(self):
        pass
        # driver = self.driver
        # driver.quit()

    def test_fill_data_success(self):
        '''
        :condition:用户已经注册demo成功
        :step:点击完善资料并开立真实账户，进入完善资料页面
        :except:用户能够完成资料且成功提交
        '''
        self.fill_data_bussiness.fill_data_pass()

if __name__ == '__main__':
    unittest.main()
