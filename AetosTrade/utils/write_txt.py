#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
PATH = lambda path:os.path.join(os.path.dirname(os.getcwd()),path)
class WriteTxt:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = PATH('config_file/case_count.txt')
        else:
            self.file_path = file_path

    def write_data(self,data):
        with open(self.file_path,'a+') as fr:
            fr.write(data)
            fr.write('\n')

    def read_data(self):
        with open(self.file_path,'r+') as fr:
            lines = fr.readlines()
            return lines

    def clear_data(self):
        with open(self.file_path, 'w+') as fr:
            fr.truncate()

    def list_result(self):
        data = self.read_data()
        pass_list = []
        fail_list = []
        error_list = []
        for value in data:
            if 'pass' in value:
                pass_list.append(value)
            elif 'error' in value:
                error_list.append(value)
            else:
                fail_list.append(value)
        return pass_list,fail_list,error_list

if __name__ == '__main__':
    txt = WriteTxt()
    txt.write_data('pass')