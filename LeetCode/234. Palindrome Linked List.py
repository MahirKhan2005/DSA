# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head):
        front=head
        prev=None
        while front:
            temp=front
            front=front.next
            temp.next=prev
            prev=temp
        return prev


    def isPalindrome(self, head):
        # Reaching the middle of the LL first
        fast=slow=head
        while fast and fast.next:
            fast = fast.next.next
            slow=slow.next

        # Head of the reversed second half
        second = self.reverseList(slow) 

        # Checking corresponding values from each halves
        firstHead = head
        secondHead = second
        ans = True # Default ans true
        while secondHead:
            if firstHead.val!=secondHead.val:
                ans = False # Ans false if any value mismatches
            firstHead=firstHead.next
            secondHead=secondHead.next

        # Re-reversing the reversed list
        secondHead = self.reverseList(second)

        return ans
        