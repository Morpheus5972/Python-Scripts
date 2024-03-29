import sys

class userStack:

    
    def __init__(self,size):
        self.stack_size = size
        self.stack = [0] * self.stack_size
        self.top = 0
        
    def push(self,element):
        
        if self.top < self.stack_size:
            self.stack[self.top] = element
            self.top += 1
        else:
            sys.exit("Stack Overflow")
        
    def pop(self):
        if self.top - 1 > -1:
            ele = self.stack[self.top - 1]
            self.top -= 1
            return ele
        else:
            sys.exit("Stack Underflow")
    
    def show(self):
        for i in range(self.top):
            print(self.stack[i])
        

s1 = userStack(5)
s1.push(10)
s1.push(20)
s1.push(50)
s1.push(40)
s1.push(30)
s1.show()
print("popped element :", s1.pop())
print("popped element :", s1.pop())
print("popped element :", s1.pop())
print("popped element :", s1.pop())
print("popped element :", s1.pop())
print("popped element :", s1.pop())
s1.show()