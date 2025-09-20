# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""Classic"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1 or l2 or carry:
            total = 0
            if l1:
                total+=l1.val
                l1 = l1.next
            if l2:
                total+=l2.val
                l2 = l2.next
            total+=carry
            carry = total // 10
            temp.next = ListNode(total%10)
            temp = temp.next
        return dummy.next






"""Original Version"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        # Check which one is longest
        len1,len2 = 0,0
        curr1, curr2 = l1, l2
        while curr1:
            len1+=1
            curr1 = curr1.next
        while curr2:
            len2+=1
            curr2 = curr2.next
        if len1>len2:
            longest = l1
            short = l2
        else:
            longest = l2
            short = l1
        longHead = longest

        # Adding elements of short in longest 
        carry = 0
        while short and longest:
            if short.val+longest.val+carry>9:
                longest.val = longest.val+short.val+carry - 10
                carry = 1
            else:
                longest.val = longest.val + short.val + carry
                carry = 0
            short = short.next
            longest = longest.next
        # Adding further if there is any carry
        while longest:
            if carry:
                if longest.val+carry>9:
                    longest.val = 0
                    carry = 1
                else:
                    longest.val+=carry
                    carry = 0
            longest = longest.next
        # Adding a leading 1 if there is still a carry
        if carry:
            newNode = ListNode(1)
            temp = longHead
            while temp.next:
                temp = temp.next
            temp.next = newNode
            
        return longHead

