# -*- coding:utf-8 -*-
def select_sort(raw_list):
    n = len(raw_list)
    for i in range(n):
        for j in range(i, n):
            if raw_list[i] > raw_list[j]:
                raw_list[i], raw_list[j] = raw_list[j], raw_list[i]
    return raw_list

#测试
data_test=[10,23,1,53,654,54,16,646,65,3155,546,31]
sorted_list = select_sort(data_test)
print(sorted_list)

# 不稳定，o(n^2)