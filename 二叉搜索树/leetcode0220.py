class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        
        record = set() 
        for i in range(n):
            if t == 0:  # 如果t=0，那么看看窗口内是否有重复元素，有就返回True
                if nums[i] in record:
                    return True
            else:
                for j in record:  # 遍历窗口元素，判断是否有绝对值小于t的情况，有就返回True
                    if abs(j - nums[i]) <= t:
                        return True
            record.add(nums[i])  # 向集合添加元素
            
            if len(record) > k:
                record.remove(nums[i-k])  # 维护长度为k的窗口
        return False