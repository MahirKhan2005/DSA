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

    def pop_front(self):
        if self.head==None:
            print("Linked list is empty")
            return
        else:
            self.head = self.head.next

    def pop_back(self):
        if self.head==None:
            print("Linked list is empty")
            return
        elif self.head.next==None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def delete(self,value):
        if self.head==None:
            print('Linked list is empty')
            return
        elif self.head.data==value:
            self.head = self.head.next
        else: 
            temp = self.head
            while temp.next and temp.next.data!=value:
                temp = temp.next
            if temp.next is None:
                print("Value not found")
            else:
                temp.next = temp.next.next
            
            

        
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

ll.delete(9)

ll.display()