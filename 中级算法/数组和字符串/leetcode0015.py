class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        datas = sorted(nums)
        results = []
        i = 0
        for i in range(len(datas) - 2):
            if i == 0 or datas[i] != datas[i-1]:
                j, k = i+1, len(datas) - 1
                while j < k:
                    if datas[i] + datas[j] + datas[k] < 0:
                        j += 1
                    elif datas[i] + datas[j] + datas[k] > 0:
                        k -= 1
                    else:
                        results.append([datas[i], datas[j], datas[k]])
                        j += 1
                        k -= 1
                        while j < k and datas[j] == datas[j-1]:
                            j += 1
                        while j < k and datas[k] == datas[k+1]:
                            k -= 1
        
        return results