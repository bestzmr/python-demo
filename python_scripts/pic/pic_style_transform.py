#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time : 2021/1/6 21:11
# @Author : ZhaoQiang
# @File : pic_style_transform.py
# @Software: PyCharm
# @Description: 图像风格转换


import requests, base64
import uuid


def get_acess_token():
    ak = 'WguFIGSGk86lqqA6WFjZlGf8'
    sk = 'Bt6U166M5srWUOU5GkEAhlnx5NKhGBML'
    # client_id 为官网获取的AK， client_secret 为官网获取的SK，去 百度智能管理中心创建获取
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + ak + '&client_secret=' + sk
    response = requests.get(host)
    return response.json()['access_token']


def make_picture(path):
    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans"
    # 二进制方式打开图片文件
    f = open(path, 'rb')
    img = base64.b64encode(f.read())
    '''
    option:String
    必选
    cartoon：卡通画风格
    pencil：铅笔风格
    color_pencil：彩色铅笔画风格
    warm：彩色糖块油画风格
    wave：神奈川冲浪里油画风格
    lavender：薰衣草油画风格
    mononoke：奇异油画风格
    scream：呐喊油画风格
    gothic：哥特油画风格
    '''
    params = {"image": img, "option": "gothic"}
    access_token = get_acess_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    res = response.json()

    if res:
        f = open(str(uuid.uuid1()) + '.png', 'wb')
        after_img = res['image']
        after_img = base64.b64decode(after_img)
        f.write(after_img)
        f.close()

    print('------------已完成---------------------')


if __name__ == '__main__':
    path = '20210106204122.jpg'
    make_picture(path)
