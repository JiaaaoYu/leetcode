class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, len(nums)):
                helper(j+1, tmp+[nums[j]])
        
        res = []
        helper(0, [])
        
        return res