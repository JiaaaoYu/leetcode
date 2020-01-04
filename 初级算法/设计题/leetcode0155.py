class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mins = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.mins) == 0 or x <= self.mins[-1]:
            self.mins.append(x)
        else:
            self.mins.append(self.mins[-1])
            

    def pop(self) -> None:
        if self.data:
            self.data.pop()
            self.mins.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()