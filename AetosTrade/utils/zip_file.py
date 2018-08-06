#!/usr/bin/env python
#-*- coding:utf-8 -*-
import zipfile
import os
class ZipFile:
    def zip_dir(self,dirname, zipfilename):
        file_list = []
        if os.path.isfile(dirname):
            file_list.append(dirname)
        else:
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    file_list.append(os.path.join(root, name))
        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in file_list:
            arc_name = tar[len(dirname):]
            zf.write(tar, arc_name)
        zf.close()