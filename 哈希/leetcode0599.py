class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {list1[i]:i for i in range(len(list1))}
        map2 = {list2[i]:i for i in range(len(list2))}
        inter = set(list1) & set(list2)
        sum_index = {i:map1[i] + map2[i] for i in inter}
        min_sum = min(sum_index.values())
        
        return [item for item in inter if sum_index[item] == min_sum]