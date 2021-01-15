#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time : 2021/1/15 10:02 
# @Author : ZhaoQiang
# @File : unpack_zip_file.py 
# @Software: PyCharm
# @Description: 解压Zip文件
from zipfile import ZipFile


def unpack_zip_file(full_name, target_dir_path):
    with ZipFile(full_name, 'r') as zipObj:
        # 解压文件
        zipObj.extractall(path=target_dir_path)
