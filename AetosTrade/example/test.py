#!/usr/bin/env python
# -*- coding:utf-8 -*
import chardet
a = '1'.decode().encode('gbk')
print(chardet.detect(a))

