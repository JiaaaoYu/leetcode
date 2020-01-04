# -*- coding:utf-8 -*-
def shell_sort(list):
    n = len(list)
    dist = n//2
    while dist > 0:
        for i in range(dist, n):
            tmp = list[i]
            j = i
            while j >= dist and tmp < list[j-dist]:
                list[j] = list[j-dist]
                j -= dist
            list[j] = tmp
        dist //= 2

    return list


#测试
list=[10,23,1,53,654,54,16,646,65,3155,546,31]
print(shell_sort(list))