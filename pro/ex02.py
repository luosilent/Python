#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 14:56
# @Author  : luoSilent
# @File    : ex02.py
# @Software: PyCharm

"""
输入年份 如果是闰年输出True 否则输出False
"""
year = int(input('请输入年份: '))

is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)

# print(is_leap)

if is_leap:
    print(year, "是闰年")
else:
    print(year, "不是闰年")
