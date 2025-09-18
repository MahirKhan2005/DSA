# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        oddHead = ListNode(-1)
        evenHead = ListNode(-2)
        oddptr = oddHead
        evenptr = evenHead
        ptr=head
        while ptr:
            # Adding odds in oddHead
            temp = ptr
            ptr = ptr.next
            oddptr.next = temp
            oddptr = oddptr.next
            temp.next = None
            # Adding evens in evenHead
            if ptr==None:
                break
            temp=ptr
            ptr = ptr.next
            evenptr.next = temp
            evenptr = evenptr.next
            temp.next = None
        
        # Tail of oddHead
        tail =  oddHead
        while tail.next:
            tail = tail.next
        # Joining the two
        oddHead = oddHead.next
        evenHead = evenHead.next
        tail.next = evenHead
        return oddHead
    
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head