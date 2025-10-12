class Queue:
    def __init__(self,size):
        self.queue = [None]*size
        self.start = -1
        self.end = -1