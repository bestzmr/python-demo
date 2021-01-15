#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time : 2021/1/15 10:02 
# @Author : ZhaoQiang
# @File : zip_file_operation.py
# @Software: PyCharm
# @Description: 解压Zip文件、压缩文件
from zipfile import ZipFile


# 解压文件
def unpack_zip_file(full_name, target_dir_path):
    with ZipFile(full_name, 'r') as zipObj:
        # 解压文件
        zipObj.extractall(path=target_dir_path)


# 压缩文件
def pack_zip_file(filenames, target_zip_filename):
    my_zip = ZipFile(target_zip_filename)
    for filename in filenames:
        # 根据文件名filename将文件写入到目标压缩包中
        my_zip.write(filename)
