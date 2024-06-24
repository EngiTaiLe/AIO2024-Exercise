class MyQueue:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.queue = []
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True 
        else:
            return False 
    
    def is_full(self):
        if len(self.queue) == self.capacity:
            return True 
        else:
            return False 
        
    def dequeue(self):
        if self.is_empty():
            print("This queue is empty")
            return
        return self.queue.pop(0)

    def enqueue(self,value):
        if self.is_full():
            print("This queue is full")
            return 
        return self.queue.append(value)
    
    def front(self):
        if self.is_empty():
            print("This queue is empty")
            return 
        return self.queue[0]