class Queue:
    def __init__(self,size):
        self.queue = [None]*size
        self.size = size
        self.front = -1
        self.rear = -1
    def isEmpty(self):
        return self.rear==-1 or self.front>self.rear
    def isFull(self):
        return self.rear == self.size-1
    def enqueue(self,item):
        if self.isFull():
            print('Queue is full')
            return
        if self.isEmpty():
            self.front = 0
        self.rear+=1
        self.queue[self.rear] = item
        print(f'Enqueued: {item}')
    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        value = self.queue[self.front]
        self.front+=1
        print(f'Dequeued: {value}')
        if self.front>self.rear:
            self.rear = self.front = -1
        return value
    def display(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        print(f'Queue: {self.queue[self.front:self.rear+1]}')


q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()