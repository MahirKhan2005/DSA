class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    
    def push_front(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def push_back(self,data):
        newNode = Node(data)
        if self.head==None:
            self.head=newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("None")

    def length(self):
        temp = self.head
        count=0
        while temp:
            count+=1
            temp = temp.next
        return count

    def middleNode(self):
        length = self.length()
        midPos = length//2 + 1
        temp = self.head
        for i in range(1,midPos):
            temp = temp.next
        return temp.data





ll = LinkedList()
ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.push_back(7)
ll.push_back(9)
ll.push_back(0)
ll.push_back(6)

ll.display()

print(ll.middleNode())
