class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.number = 1000
        self.buckets = [[] for _ in range(self.number)]
        

    def add(self, key: int) -> None:
        idx = key % self.number
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % self.number
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.number
        if key in self.buckets[idx]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)