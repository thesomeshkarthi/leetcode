class MinStack:

    def __init__(self):
        self.stackList = []
        self.minValueList = []

    def push(self, val: int) -> None:
        (self.stackList).append(val)
        
        if len(self.minValueList) == 0:
            (self.minValueList).append(val)
        elif val <= self.minValueList[-1]:
            (self.minValueList).append(val)

    def pop(self) -> None:
        if self.stackList[-1] == self.minValueList[-1]:
            (self.minValueList).pop()

        (self.stackList).pop()
        
    def top(self) -> int:
        return self.stackList[-1]

    def getMin(self) -> int:
        return self.minValueList[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()