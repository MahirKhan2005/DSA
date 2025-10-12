class Stack:
    def __init__(self,size):
        self.stack = [None]*size
        self.top = -1
        self.size = size
    def push(self,num):
        if self.top == self.size-1:
            print("Stack Overflow!")
        else:
            self.top+=1
            self.stack[self.top] = num
    def pop(self):
        if self.top==-1:
            print('Stack is empty')
        else:
            popped = self.stack[self.top]
            self.stack[self.top] = None
            self.top-=1
            return popped
    def peek(self):
        if self.top==-1:
            print('Stack is empty')
        else:
            print(f'{self.stack[self.top]} is on top')
            return self.stack[self.top]
    def display(self):
        if self.top==-1:
            print('Stack is empty')
        else:
            print(self.stack[:self.top+1])
    
s = Stack(10)
s.push(1)
s.push(2)
s.push(3)
s.display()
s.peek()
s.pop()
s.pop()
s.pop()
s.peek()