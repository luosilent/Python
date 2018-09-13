#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 16:49
# @Author  : luoSilent
# @File    : 03.py
# @Software: PyCharm

numSum1 = 0
for i in range(1, 101):
    numSum1 += i
print(numSum1)

numSum2 = 0
for x in range(1, 101):
    if x % 2 == 0:
        numSum2 += x
print(numSum2)

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
