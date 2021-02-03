#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time : 2021/2/3 16:07 
# @Author : ZhaoQiang
# @File : wx_util.py 
# @Software: PyCharm
# @Description: 微信中的工具

# 安装一下 Python 用到的模块
# pip install Appium-Python-Client
# 学习Appium,链接如下：
# https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg==&mid=2247487455&idx=1&sn=e6692fbfee0cbcd25083c988d10a29dd&scene=21#wechat_redirect
# 微信清理僵尸好友,链接如下：
# https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg%3D%3D&idx=1&mid=2247489564&scene=21&sn=2448215fbb222b57a039bc05c0b1f535#wechat_redirect
# 微信自动抢红包
# https://juejin.cn/post/6922340460119719943

from appium.webdriver import webdriver

desired_capabilities = {
    'platformName': 'Android', # 操作系统
    'deviceName': '2a254a02', # 设备 ID，使用 cmd 中 adb devices 命令得到
    'platformVersion': '10.0.10', # 设备版本号，在手机设置中查看
    'appPackage': 'com.tencent.mm', # app 包名
    'appActivity': 'com.tencent.mm.ui.LauncherUI', # app 启动时主 Activity
    'noReset': True # 是否保留 session 信息 避免重新登录
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
print('微信启动')