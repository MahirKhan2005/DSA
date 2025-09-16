# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        tail = dummy
        i,j = list1,list2
        while i and j:
            if i.val<j.val:
                tail.next = i
                i = i.next
            else: 
                tail.next = j
                j = j.next
            tail = tail.next
        if i:
            tail.next = i
        else:
            tail.next = j
        return dummy.next

        