class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myList = []
        self.myDict = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.myDict:
            return False
        else:
            self.myDict[val] = len(self.myList)
            self.myList.append(val)
            
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.myDict:
            self.myDict[self.myList[-1]] = self.myDict[val]
            self.myList[self.myDict.pop(val)] = self.myList[-1]
            self.myList.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.myList)-1)
        return self.myList[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()