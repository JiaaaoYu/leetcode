def bubble_sort(raw_list):
    n = len(raw_list)
    for i in range(n):
        for j in range(1, n - i):
            if raw_list[j-1] > raw_list[j]:
                raw_list[j-1], raw_list[j] = raw_list[j], raw_list[j-1]

    return raw_list

#测试
data_test=[10,23,1,53,654,54,16,646,65,3155,546,31]
sorted_list = bubble_sort(data_test)
print(sorted_list)