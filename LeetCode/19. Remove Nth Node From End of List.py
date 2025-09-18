# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        if not head.next:
            return head.next
        # Finding the length
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length+=1
        start = length - n
        # Removing the appropriate element
        if start==0:
            return head.next
        else:
            temp = head
            # Reaching the previous element of the removal element
            for i in range(1,start):
                temp = temp.next
            temp.next = temp.next.next
        return head

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head)
        fast=slow=dummy
        for i in range(n+1):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next