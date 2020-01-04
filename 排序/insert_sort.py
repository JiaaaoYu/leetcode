# -*- coding:utf-8 -*-
def insert_sort(raw_list):
    n = len(raw_list)
    for i in range(1, n):
        tmp = raw_list[i]
        for j in range(i-1, -1, -1):
            if raw_list[j] <= tmp:
                break
            else:
                raw_list[j], raw_list[j+1] = tmp, raw_list[j]
    return raw_list

#测试
data_test = [10,23,1,53,654,54,16,646,65,3155,546,31]
sorted_list = insert_sort(data_test)
print(sorted_list)