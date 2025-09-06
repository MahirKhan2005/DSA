class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def push_back(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    
    def push_front(self,data):
        newNode = Node(data)
        if self.head==None:
            self.head = newNode
            return 
        else:
            newNode.next = self.head
            self.head = newNode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.push_front(4)



ll.display()