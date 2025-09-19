class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
    def display_forward(self):
        if not self.head:
            print('The list is empty')
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" <-> ")
                temp = temp.next
            print("None")
    def display_backward(self):
        if not self.head:
            print('The list is empty')
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            while temp:
                print(temp.data,end=" <-> ")
                temp = temp.prev
            print("None")
    def reverse(self):
        if not self.head or not self.head.next:
            return self.head
        current = self.head
        prev_node = None
        while current:
            current.prev, current.next = current.next, current.prev
            prev_node = current
            current = current.prev
        self.head = prev_node

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

dll.display_forward()

dll.reverse()
dll.display_forward()