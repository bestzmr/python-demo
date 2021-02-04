#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time : 2021/2/4 19:00 
# @Author : ZhaoQiang
# @File : var_utils.py 
# @Software: PyCharm
# @Description: 获取变量大小

import sys
import inspect


def get_size(obj, seen=None):  # 传入的obj为[1,2,3,4,5,6,7,8,9]
    size = sys.getsizeof(obj)  # 这里会调用系统的getsizeof算一遍大小
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    if hasattr(obj, '__dict__'):
        for cls in obj.__class__.__mro__:
            if '__dict__' in cls.__dict__:
                d = cls.__dict__['__dict__']
                if inspect.isgetsetdescriptor(d) or inspect.ismemberdescriptor(d):
                    size += get_size(obj.__dict__, seen)
                break
    if isinstance(obj, dict):
        size += sum((get_size(v, seen) for v in obj.values()))
        size += sum((get_size(k, seen) for k in obj.keys()))  # dict的key是不可变元素，这里不用重新计算
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum((get_size(i, seen) for i in obj))  # 这里列表里每个元素带进去算一遍，很明显有问题

    if hasattr(obj, '__slots__'):
        size += sum(get_size(getattr(obj, s), seen) for s in obj.__slots__ if hasattr(obj, s))

    return size