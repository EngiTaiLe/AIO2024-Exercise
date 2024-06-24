class MyStack:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.stack = []
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False 
    
    def is_full(self):
        if len(self.stack) == self.capacity:
            return True 
        else:
            return False 
    
    def pop(self):
        if self.is_empty():
            print("This stack is empty")
            return 
        return self.stack.pop(-1) 
    
    def push(self,value):
        if self.is_full():
            print("This stack is full")
            return
        self.stack.append(value)
    
    def top(self):
        if self.is_empty():
            print("This stack is empty")
            return
        return self.stack[-1]