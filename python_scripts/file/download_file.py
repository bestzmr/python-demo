#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time : 2021/1/15 9:53 
# @Author : ZhaoQiang
# @File : download_file.py 
# @Software: PyCharm
# @Description: 下载文件
import requests


def download_file(url, filepath, header):
    # stream=True 开启懒下载，防止文件过大，放入内存时，内存会溢出，通过调用iter_content分块将文件放入内存
    response = requests.get(url, header=header, stream=True)
    # 若response返回响应状态不是200，会抛出错误，若为200，返回None
    response.raise_for_status()
    fp = open(filepath, 'wb')
    for chunk in response.iter_content(chunk_size=100000):
        if chunk:
            fp.write(chunk)
    fp.close()
