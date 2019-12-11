class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 20001
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        for item in self.buckets[idx]:
            if item[0] == key:
                item[1] = value
                return
        self.buckets[idx].append([key, value])
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        for item in self.buckets[idx]:
            if item[0] == key:
                return item[1]
        
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        delete = None
        for item in self.buckets[idx]:
            if item[0] == key:
                delete = item
        
        if delete:
            self.buckets[idx].remove(delete)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)