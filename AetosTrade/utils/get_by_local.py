#!/usr/bin/env python
#-*- coding:utf-8 -*-
from read_ini import ReadIni
class GetByLocal:
	def __init__(self,driver):
		self.driver = driver

	def get_element(self,key,section=None):
		read_ini = ReadIni()
		local = read_ini.get_value(key,section=section)
		if local != None:
			by = local.split('>')[0]
			local_by = local.split('>')[1]
			try:
				if by == 'id':
					return self.driver.find_element_by_id(local_by)
				elif by == 'className':
					return self.driver.find_element_by_class_name(local_by)
				elif by =='ids':
					return self.driver.find_elements_by_id(local_by)
				elif by == 'classNames':
					return self.driver.find_elements_by_class_name(local_by)
				else:
					return self.driver.find_element_by_xpath(local_by)
			except:
				return None
		else:
			return None


