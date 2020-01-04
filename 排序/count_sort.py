def count_sort(numberlist, maxnumber):  # maxnumber为数组中的最大值
    # b = [0 for i in range(length)] # 设置输出序列，初始化为0
    c = [0 for i in range(maxnumber+ 1)]  # 设置技术序列，初始化为0
    for j in numberlist:
        c[j] = c[j] + 1

    res = []
    for idx, val in enumerate(c):
        if val > 0:
            res.extend([idx] * val)
    
    return res
    # for i in range(1, len(c)):
    #     c[i] = c[i] + c[i - 1]
    # for j in numberlist:
    #     b[c[j] - 1] = j
    #     c[j] = c[j] - 1
    # return b


#测试：
list=[10,23,1,53,654,54,16,646,65,3155,546,31]
print(count_sort(list, 3155))