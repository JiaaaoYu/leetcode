# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)

# #测试
# list=[10,23,1,53,654,54,16,646,65,3155,546,31]
# print(quick_sort(list))


def partition(li,left,right):
    item = li[left]
    while left < right:
        while left < right and li[right] >= item:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] < item:
            left += 1
        li[right] = li[left]
    li[left] = item  # left == right
    return left


def quicksort(li,left,right):
    if left < right:  # 递归终止条件
        mid = partition(li,left,right)
        quicksort(li,left,mid-1)
        quicksort(li,mid+1,right)

#测试
list=[10,23,1,53,654,54,16,646,65,3155,546,31]
quicksort(list, 0, len(list)-1)
print(list)