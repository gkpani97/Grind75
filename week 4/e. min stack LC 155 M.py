class MinStack:

    def __init__(self):
        self.min_stack = []
    
    # min stack means its a normal stack, with no sorting taking place, but it 
    # should be able to return the minimum element at any point at 0(1)
    def push(self, val: int) -> None:
        # trick is to add a list/ tuple into the stack instead of an element alone
        # the 1st element of the list/ tuple is the element itself, 2nd is min value so far
        if self.min_stack:
            self.min_stack.append( [val, min(val, self.min_stack[-1][-1])] )
        else:
            self.min_stack.append( [val,val] )
                                        
    def pop(self) -> None:
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.min_stack[-1][0]
        

    def getMin(self) -> int:
        return self.min_stack[-1][-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
