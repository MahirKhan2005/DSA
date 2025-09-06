class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    
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
        
    def search(self,value):
        if self.head==None:
            print("Linked list is empty")
            return
        else:
            temp = self.head
            while temp:
                if temp.data==value:
                    return True
                temp = temp.next
        return False


ll = LinkedList()
ll.push_back(1)
ll.push_back(2)
ll.push_back(3)

ll.display()

print(ll.search(5))
