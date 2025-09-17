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
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("None")

    def reverseList(self):
        front = self.head
        prev = None
        while front:
            temp = front
            front = front.next
            temp.next = prev
            prev = temp
        self.head = prev
    
    # Recursive approach
    def reverseList(self,head):
        if head==None or head.next==None:
            return head
        newHead = self.reverseList(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newHead
            
            

ll = LinkedList()
ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.push_back(4)
ll.push_back(5)

ll.reverseList()
ll.display()