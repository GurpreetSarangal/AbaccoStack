class BStack:
    def __init__(self, max_capacity) -> None:
        self.max_capacity = max_capacity
        self.stack = []
    
    def push(self, item):
        if len(self.stack)>self.max_capacity:
            print("Stack is full")
        else:
            self.stack.append(item)
    
    def pop(self):
        if len(self.stack)==0:
            print("underflow")
            return
        else:
            return self.stack.pop()
    
    def isFull(self):
        return len(self.stack)>=self.max_capacity

    def peek(self):
        last_index = len(self.stack)-1
        return self.stack[last_index]


# test=BStack(3)
# test.push(10)
# test.push(2321)

# print(test.isFull())
# print(test.peek())
