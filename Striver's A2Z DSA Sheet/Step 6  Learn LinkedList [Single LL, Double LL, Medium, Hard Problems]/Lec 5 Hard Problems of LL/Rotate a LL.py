# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
    # Finding length first
        length = 0
        temp = head
        while temp:
            tail = temp
            length+=1
            temp = temp.next

        k%=length
        if k==0:
            return head

        # Finding newHead and newTail
        newTail = head
        for i in range(1,length-k):
            newTail = newTail.next
        newHead = newTail.next

        # Changing the links 
        newTail.next = None
        tail.next = head
        return newHead

        