class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        lookup = collections.defaultdict(int)
        for i in A:
            for j in B:
                lookup[-i-j] += 1
                
        return sum(lookup[c+d] for c in C for d in D)