# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        temp = head
        while temp:
            res = (res<<1) | (temp.val & 1)
            temp = temp.next
        return res
        