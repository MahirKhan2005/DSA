# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Version 1
class Solution:
    def deleteMiddle(self, head):
        fast = head.next.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# Version 2
class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        fast = slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head