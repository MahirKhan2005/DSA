# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addOne(self, head):
        # Firstly reversing the LL
        prev = None
        front = head
        while front:
            temp = front
            front = front.next
            temp.next = prev
            prev = temp
        # Adding 1 to it
        carry = 1
        newHead = prev
        while prev:
            last = prev  # Storing last node
            if carry:
                if prev.val==9:
                    prev.val = 0
                    carry = 1
                else:
                    prev.val+=carry
                    carry = 0
            prev = prev.next
        # If carry still remains
        if carry:
            last.next = ListNode(1)

        # Re-reversing the list
        prev = None
        front = newHead
        while front:
            temp = front
            front = front.next
            temp.next = prev
            prev = temp
        
        return prev
