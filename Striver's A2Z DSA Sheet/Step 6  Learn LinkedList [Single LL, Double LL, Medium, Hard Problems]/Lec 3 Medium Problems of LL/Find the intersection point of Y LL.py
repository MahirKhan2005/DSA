# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Visited set approach - TC - O(m+n), SC - O(m+n)
class Solution:
    def getIntersectionNode(self, headA, headB):
        i = headA
        j = headB
        hash = set()
        while i or j:
            if i:
                if i in hash:
                    return i
                hash.add(i)
                i = i.next
            if j:
                if j in hash:
                    return j
                hash.add(j)
                j = j.next
        return None

class Solution:
    def getIntersectionNode(self, headA, headB):
            if not headA or not headB:
                return None
            
            a,b = headA,headB
            while a is not b:
                a = a.next if a else headB
                b = b.next if b else headA
            return a
            

