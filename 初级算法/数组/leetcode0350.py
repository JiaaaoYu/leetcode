class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = collections.defaultdict(int)
        res = []
        for num in nums1:
            lookup[num] += 1
        
        for num in nums2:
            if lookup[num] != 0:
                res.append(num)
                lookup[num] -= 1
        
        return res